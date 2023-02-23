from flow import FlowProject
import signac
import flow
# import environment_for_rahman
import environment_pbs

def workspace_command(cmd):
    """Simple command to always go to the workspace directory"""
    return " && ".join(
        [
            "cd {job.ws}",
            cmd if not isinstance(cmd, list) else " && ".join(cmd),
            "cd ..",
        ]
    )

sample_file = "sample.gro"
unwrapped_file = 'sample_unwrapped.xtc'
init_file = "system.gro"
for_lammps_data = "sample.data"
conp_file = "restart.final"
lammps_init_file =  "sample.data"
restart_file = 'file.restart.100000'

class Project(FlowProject):
    pass

@Project.label
def run_cpmed(job):
    return job.isfile(conp_file)

@Project.operation
@Project.pre.isfile(lammps_init_file)
@Project.post.isfile(restart_file)
@flow.cmd
def run_cpm(job):
    return _lammps_str(job)

def _lammps_str(job, 
                if_restart=0, 
                if_wat =0, 
                in_path = 'lammps_input/in.data_gcc', 
                exe='/global/cfs/cdirs/m1046/Xiaobo/installed_software/lammps_jan_3/build_gcc/lmp_mpi'):
    
    """Helper function, returns lammps command string for operation 
        Note: need to use cori_start.sh or cori_repeat.sh according to demand
    """
    # exe = '/global/cfs/cdirs/m1046/Xiaobo/installed_software/lammps_May272021_CPM_cray/build_new/lmp_mpi'
    case = job.statepoint()["case"] 
    voltage = job.statepoint()["voltage"] 
    lammps_input = signac.get_project().fn(in_path)
    temperature = 400
    print(case)
    print(job.id)
    if case == 'wat_litfsi':
        if_wat = 1
    
    print('if_restart is ', if_restart)
    
    cmd ='srun --exclusive --ntasks=32 {exe} -in {input} '\
        '-var voltage {voltage} '\
        '-var if_restart {if_restart} '\
        '-var if_wat {if_wat} '\
        '-var temperature {temperature}'
        
    return workspace_command(cmd.format(case = case, voltage=voltage, if_restart=if_restart, if_wat= if_wat, temperature = temperature, exe = exe, input = lammps_input))


@Project.label
def rerun_cpmed(job):
    return job.isfile(conp_file)

@Project.operation
@Project.pre.isfile(restart_file)
@Project.post.isfile(conp_file)
@flow.cmd
def rerun_cpm(job):
    return _lammps_str(job, if_restart=1)


if __name__ == "__main__":
    Project().main()

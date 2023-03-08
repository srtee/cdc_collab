from flow import FlowProject
import signac
import flow
import environment_for_bunya
# import environment_for_rahman
# import DefaultSlurmEnvironment

def workspace_command(cmd):
    """Simple command to always go to the workspace directory"""
    return " && ".join(
        [
            "cd {job.ws}",
            cmd if not isinstance(cmd, list) else " && ".join(cmd),
            "cd ..",
        ]
    )

init_file = "system.gro"
sample_file = "sample.gro"
unwrapped_file = 'sample_unwrapped.xtc'
conp_file = "file.restart.22000000"
lammps_init_file =  "sample.data"
restart_file = 'restart.1'

class Project(FlowProject):
    pass

@Project.label
def run_cpmed(job):
    return job.isfile(conp_file)

@Project.pre.isfile(lammps_init_file)
@Project.post.isfile(restart_file)
@Project.operation(cmd=True)
def run_cpm(job):
    return _lammps_str(job)

@Project.pre.isfile(restart_file) # no post-condition because "run upto" auto-stops a run that has gone too long
@Project.post.isfile('in_progress') # don't let rerun happen if run is in progress
@Project.operation(cmd=True)
def cont_cpm(job):
    return _lammps_str(job,if_restart=1)

def _lammps_str(job, 
                if_restart = 0, 
                if_wat = 0, 
                in_path = 'lammps_input/in.data_gcc', 
                exe='/home/uqstee4/lammps-conp2/build/lmp_conp2'):
    
    case = job.statepoint()["case"] 
    voltage = job.statepoint()["voltage"] 
    lammps_input = signac.get_project().fn(in_path)
    temperature = 400
    print(case)
    print(job.id)
    if case == 'wat_litfsi':
        if_wat = 1
    
    print('if_restart is ', if_restart)

    cmd = f'srun {exe} -in {lammps_input} -sf opt '\
          f'-var voltage {voltage} '\
          f'-var if_restart {if_restart} '\
          f'-var if_wat {if_wat} '\
          f'-var temperature {temperature} '\
          f'-var workdir {job.path}'
    return cmd

@Project.label
def rerun_cpmed(job):
    return job.isfile(conp_file)

if __name__ == "__main__":
    Project().main()

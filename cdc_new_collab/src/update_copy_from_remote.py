import os
import signac
import numpy as np
project = signac.get_project()

def copy_file(file_name, job_id, v, case, seed):
    #for job in project.find_jobs({'voltage': 0, 'case': case, 'seed': seed}):
    #    rahman_job_id = job
    #cluster_name = 'linx6@rahman.vuse.vanderbilt.edu'
    #rahman_job = f'/raid6/homes/linx6/project/self_project/CDC_corrected/cdc_new/workspace/{rahman_job_id}'
    #sourcedir = f'{cluster_name}:{rahman_job}'
    sourcedir = f'lammps_input/{case}'
    command_line = f'rsync -r {source_dir}/{file_name} workspace/{job_id}/'
    print(command_line)
    os.system(command_line)
    
voltages = [0]
cases = ['neat_emimtfsi', 'acn_emimtfsi', 'acn_litfsi', 'wat_litfsi']
seeds = [0,1,2,3]
i = 0
for seed in seeds:
    for case in cases:
        for v in voltages:
            for job in project.find_jobs({'voltage': v, 'case': case, 'seed': seed}):
                # copy_gro_file(case, 'system_lmp.gro', job.id)
                # copy_gro_file(case, 'system_lmp.top', job.id)
                # copy_file('sample.data', job.id, seed)
                # copy_file('conp.lammpstrj', job.id, seed)
                
                copy_file('sample.data', job.id, v, case, seed)
                # copy_file('system_lmp.gro', job.id, v, case, seed)
                print(f'Copy job {i} done (to job ID {job.id})')
                i += 1

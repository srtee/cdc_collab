import os
import signac
import numpy as np
project = signac.get_project()

# copy a file from equivalent 0V job to non-0V job
def copy_file(file_name, to_job_id, v, case, seed):
    job_id_0V = project.find_jobs({'voltage': 0, 'case': case, 'seed': seed})[-1].id
    command_line = f'rsync -r workspace/{job_id_0V}/{file_name} workspace/{to_job_id}/'
    print(command_line)
    os.system(command_line)
    
voltages = [1,2,3]
cases = ['neat_emimtfsi', 'acn_emimtfsi', 'acn_litfsi', 'wat_litfsi']
seeds = [0,1,2,3]
i = 0
for seed in seeds:
    for case in cases:
        for v in voltages:
            for job in project.find_jobs({'voltage': v, 'case': case, 'seed': seed}):
                copy_file('sample.data', job.id, v, case, seed)
                print(f'Copy job {i} done (to job ID {job.id}')
                i += 1

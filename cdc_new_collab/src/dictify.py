# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import signac
import matplotlib.pyplot as plt
import numpy as np
import mdtraj as md
project = signac.get_project()

#%% get finished jobs
# why can't I load labels from FlowProject??????

cases = ['neat_emimtfsi', 'acn_emimtfsi', 'acn_litfsi', 'wat_litfsi']
ncases = len(cases)

for c in cases:
    for job in project.find_jobs():
            if (job.statepoint()['case'] == c):
                print(job.id, job.statepoint()['case'], job.statepoint()['voltage'], job.statepoint()['seed'])

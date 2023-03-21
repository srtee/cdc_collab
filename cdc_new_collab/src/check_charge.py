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
        if (job.isfile('nrestart') and not job.isfile('in_progress')):
            if (job.statepoint()['case'] == c):
                print(job.statepoint())

#%% list of finished jobs

volts_and_seeds = [
  [[0, 0], [1, 1], [2, 0], [3, 1]], # neat_emimtfsi
  [[0, 3], [1, 0], [2, 3], [3, 0]], # acn_emimtfsi
  [[0, 2], [1, 2], [2, 1]], # acn_litfsi
  [[0, 0], [1, 0]]] #wat_tfsi

#%% density check

from CPManalysis.density_dist import calc_density_distribution

ncase = 0
c = cases[ncase]
fig, ax = plt.subplots(figsize=(8,3))
for vs in volts_and_seeds[ncase]:
    for job in project.find_jobs({'case': c, 'voltage': vs[0], 'seed': vs[1]}):
        with job:
            print(job.id)
            trj_file = "conp_0.xtc"
            gro_file = "system_lmp.gro"
            res_name = "emim"
            trj_total = md.load(trj_file, top=gro_file)
            new_bins, new_hist = calc_density_distribution(trj_total, last_n_frame=4000, res_name = res_name, binwidth = 0.1, axis = 2)
            ax.plot(new_bins, new_hist, label=f"V{vs[0]}")

ax.legend()
ax.set_xlabel('z (nm)')
ax.set_xlim(0, 24)
ax.set_ylabel(r'$\rho$ (nm$^{-3}$)')

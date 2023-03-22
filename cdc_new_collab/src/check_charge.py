# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import signac
import matplotlib.pyplot as plt
import numpy as np
import MDAnalysis as mda
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

#%% type infos

ntypes = [2, 3, 3, 3]

type_keyatoms = [
    [2, 10],
    [15, 2, 10],
    [8, 2, 3],
    [8, 2, 3],
    ]

type_names = [
    ['emim', 'tfsi'],
    ['acn', 'emim', 'tfsi'],
    ['acn', 'li', 'tfsi'],
    ['wat', 'li', 'tfsi']
    ]

#%% test density

from MDAnalysis.analysis.lineardensity import LinearDensity

ncase = 0
vs = volts_and_seeds[ncase][0]
for job in project.find_jobs({'case': cases[ncase], 'voltage': vs[0], 'seed': vs[1]}):
    with job:
        print(job.id)
        trj_file = "conp_0.xtc"
        gro_file = "sample.data"
        u = mda.Universe(gro_file, trj_file)
        emim = u.select_atoms("byres type 2")
        ldens = LinearDensity(emim,verbose=True)
        ldens.run()
        
#%% look at dict

for i, key in enumerate(ldens.results['z'].keys()):
    print(key,len(ldens.results['z'][key]) if i > 1 else 0)

#%% double check molecules


emim2 = u.select_atoms("type 3")
emim = u.select_atoms("byres type 3")
print(len(emim2))
print(len(emim))
print(len(emim)/len(emim2))


#%% density check

def mids(list):
    return 0.5*(list[1:]+list[:-1])

ncase = 0
c = cases[ncase]
ntype = 0
tname = type_names[ncase][ntype]
tkey = type_keyatoms[ncase][ntype]
fig, ax = plt.subplots(figsize=(8,3))
for vs in volts_and_seeds[ncase]:
    for job in project.find_jobs({'case': c, 'voltage': vs[0], 'seed': vs[1]}):
        with job:
            print(job.id)
            trj_file = "conp_0.xtc"
            gro_file = "sample.data"
            u = mda.Universe(gro_file, trj_file)
            sel = u.select_atoms(f"byres type {tkey}")
            ldens = LinearDensity(sel,verbose=True)
            ldens.run()
            mdens = ldens.results['z']['mass_density']
            mcents = mids(ldens.results['z']['hist_bin_edges'])
            ax.plot(mcents, mdens, label=f"V{vs[0]}")

ax.legend()
ax.set_xlabel('z (nm)')
ax.set_xlim(0, 24)
ax.set_ylabel(r'$\rho$ (nm$^{-3}$)')


#%%

print(len(sel))
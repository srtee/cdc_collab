#!/bin/bash
python src/project_cori.py submit -o rerun_cpm -f "voltage" 2 --bundle 8 --parallel --walltime 7
python src/project_cori.py submit -o rerun_cpm -f "voltage" 0 --bundle 8 --parallel --walltime 7
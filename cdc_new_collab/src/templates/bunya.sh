{% extends "base_script.sh" %}
{% block header %}
#!/bin/bash
#SBATCH --job-name="{{ id }}"
#SBATCH --partition=general
#SBATCH --distribution=block:block:block
{% block tasks %}
#SBATCH --account=a_bernhardt
#SBATCH --cpus-per-task=1

module load cmake openmpi aocc fftw.mpi openblas
{% endblock %}
{% endblock %}

{% extends "base_script.sh" %}
{% block header %}
#!/bin/bash
#SBATCH --job-name="{{ id }}"
#SBATCH --partition=general
#SBATCH --distribution=block:block:block
{% block tasks %}
#SBATCH --ntasks={{ np_global }}
module load cmake openmpi aocc fftw.mpi openblas
{% endblock %}
{% endblock %}

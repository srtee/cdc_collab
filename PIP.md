# Using pip and virtualenv on a HPC cluster

While conda is widely-used for managing environments on a local PC, it is also notoriously prone to breaking on HPCs in annoying and subtle ways.

Here's how I set up a virtual environment for these jobs on my HPC. Note that `virtualenvwrapper` (VEWrapper) makes robust virtual environments in the `~/.virtualenv` folder.

1. Load the HPC's Python module
2. Bootstrap `pip`
3. Install VEWrapper
4. Setup VEWrapper
5. Setup and go into `signac` venv
6. Update `pip` and install `signac`
7. Freeze requirements in project dir

with the commands:

```
module load hpc-python-module
python3 -m ensurepip --user
pip install virtualenvwrapper --user
source /path/to/virtualenvwrapper.sh # typically $HOME/.local/bin/
grep -Fxe 'virtualenvwrapper.sh' $HOME/.bashrc || {
  echo "source /path/to/virtualenvwrapper.sh" >> $HOME/.bashrc
} # idempotent appender
mkvirtualenv signac
workon signac
python3 -m pip install --upgrade pip
pip install signac signac-flow
cd /path/to/project/directory
pip freeze > requirements.txt
```

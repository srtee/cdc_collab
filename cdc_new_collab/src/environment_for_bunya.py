"""Configuration of the project enviroment. 
 
The environments defined in this module can be auto-detected. 
This helps to define environment specific behaviour in heterogenous 
environments. 
""" 
import flow 
 
__all__ = ['BunyaEnvironment']
 
class BunyaEnvironment(flow.environment.DefaultSlurmEnvironment): 
    hostname_pattern = r".*bunya.*"
    mpi_cmd = "srun"

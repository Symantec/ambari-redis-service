import sys, os, pwd, signal, time
from resource_management import *
from subprocess import call
from redis import redis

class redis_service(Script):
  def install(self, env):
    # Install packages listed in metainfo.xml
    self.install_packages(env)
    self.configure(env)
    #if any other install steps were needed they can be added here
  
  def configure(self, env):
    import params
    params.redis_slave=True
    env.set_params(params)
    redis()

  #To stop the service, use the linux service stop command and pipe output to log file
  def stop(self, env):
    import params
    env.set_params(params)
    stop_cmd = format("service redis stop")
    Execute(stop_cmd)

  #To start the service, use the linux service start command and pipe output to log file
  def start(self, env):
    import params
    env.set_params(params)
    start_cmd = format("service redis start")
    Execute(start_cmd)

  #To get status of the, use the linux service status command
  def status(self, env):
    import status_params
    env.set_params(status_params)
    check_process_status(status_params.redis_pid_file)
    
if __name__ == "__main__":
    redis_service().execute()
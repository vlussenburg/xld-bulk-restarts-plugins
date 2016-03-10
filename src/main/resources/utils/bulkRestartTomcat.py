#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS 
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

import time
import com.xebialabs.deployit.plugin.api.reflect.Type

def run_control_task(container, task_name):
  ctrlobj = controlService.prepare(task_name, str(container.id))
  taskid = controlService.createTask(ctrlobj)
  taskBlockService.start(taskid)
  taskobj = taskBlockService.getTask(taskid)._delegate
  print "Executing " + taskobj.description + ", task id " + taskid  

  return taskobj

def archive_or_cancel(task):
  try:
    taskBlockService.archive(task.id)
  except:
    print "Couldn't archive " + task.id + ", probably it failed"
    try:
      print "Canceling task " + task.id
      taskBlockService.cancel(task.id)
    except:
      print "Couldn't cancel " + task.id + ", probably something is really messed up"

def wait_for_tasks_to_finish(tasks):
  for task in tasks:
    while task.state.active:
      print "Waiting for task " + task.id + " to finish"
      time.sleep(5)
    
    archive_or_cancel(task)

containers = repositoryService.query(Type.valueOf("tomcat.Server"), None, thisCi.id, None, None, None, 0, -1)
print "Found Tomcat containers: " + str(containers)

tasks = []
for container in containers:
  tasks.append(run_control_task(container, "stop"))
wait_for_tasks_to_finish(tasks)


tasks = []
for container in containers:
  tasks.append(run_control_task(container, "start"))
wait_for_tasks_to_finish(tasks)
  

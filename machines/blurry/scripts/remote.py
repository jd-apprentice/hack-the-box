from clearml import Task, Logger
import os

def main():
    task = Task.init(project_name='Black Swan', task_name='Remote_execution PAYLOAD')
    task.execute_remotely(queue_name="testing")

    # do ls
    os.system("ls -la")
    
if __name__ == '__main__':
    main()
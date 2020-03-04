import numpy as np
from shutil import copy

def task_write(i_task,i_time):
    copy('Timed_tasks.txt','Timed_tasks.txt.bkp')
    with open('Timed_tasks.txt','r+') as file:
        lines = file.readlines()
        file.seek(0)
        task = i_task
        times = [i.replace(':', '.') for i in i_time.strip().split()]
        tot = round(abs((float(times[0].split('.')[0])+float(times[0][-3:])*100/60) - \
                    (float(times[1].split('.')[0])+float(times[1][-3:])*100/60)),2)

        for line in lines:
            if line.split()[0] == task:
                tot += float(line.split()[-1])
                line = line.replace(line,'{} {}\n'.format(task, tot))
                file.write(line)
            else: file.write(line)
        print("Added {} to '{}' time".format(tot,task))
        print("You've completed {} hours!".format(tot))

    return

if __name__ == '__main__':
    with open('records.txt','r') as f:
        for line in f:
            task_write(line.split()[0],' '.join(line.split()[1:][:]))
        print('Timed_task.txt has been updated')

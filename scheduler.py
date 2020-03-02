import numpy as np
import sys
from shutil import copy

if __name__ == '__main__':
    tasklist = []
    copy('Timed_tasks.txt','Timed_tasks.txt.bkp')
    with open('Timed_tasks.txt','r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines[1:]:
            tasklist.append(line.split()[0])
        task = input('What task {}: '.format(tasklist)).strip()
        if task.split()[0] == 'Reset':
            for line in lines:
                if line.split()[0] == task:
                    line = line.replace(line,'{} {}\n'.format(task.split()[1], 0.0))
                    file.write(line)
                else: file.write(line)
            print("Task {} time reset to 0.0".format(task.split()[1]))
            quit()
        times = [i.replace(':', '.') for i in input('What times: ').strip().split()]
        tot = round(abs((float(times[0].split('.')[0])+float(times[0][-3:])*100/60) - \
                    (float(times[1].split('.')[0])+float(times[1][-3:])*100/60)),2)

        if task in tasklist:
            for line in lines:
                if line.split()[0] == task:
                    tot += float(line.split()[-1])
                    line = line.replace(line,'{} {}\n'.format(task, tot))
                    file.write(line)
                else: file.write(line)
            print("Added {} to '{}' time".format(tot,task))
            print("You've completed {} hours!".format(tot))
        else:
            for line in lines:
                file.write(line)
            file.write('{} {}'.format(task, tot))
            print('Task {} appended to file'.format(task))

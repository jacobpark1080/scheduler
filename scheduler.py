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
        df = np.diff([int(i) for i in input('What times: ').strip().split()])
        tot = df[0]
        if task in tasklist:
            for line in lines:
                if line.split()[0] == task:
                    tot += float(line.split()[-1])
                    line = line.replace(line,'{} {}\n'.format(task, tot))
                    file.write(line)
                else: file.write(line)
            print("You've completed {} hours!".format(tot))
        else:
            for line in lines:
                file.write(line)
            file.write('{} {}'.format(task, tot))
            print('Task {} appended to file'.format(task))

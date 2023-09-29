import numpy as np

exit()
line = '    ' + '\n'
linenum = 64 #licz od 1
filename = 'pierwszak.py'
for i in range(1,7):
    with open(f'./POST{i}/{filename}', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data[linenum - 1] = line
    with open(f'./POST{i}/{filename}', 'w', encoding='utf-8') as file:
        file.writelines(data)

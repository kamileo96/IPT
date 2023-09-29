import numpy as np

with open('wyniki_final.txt', 'a+', encoding='utf-8') as file:
    
    for i in range(1,7):
        with open(f'./POST{i}/wyniki.txt', 'r', encoding='utf-8') as file2:
            data = file2.readlines()
        open(f'./POST{i}/wyniki.txt', 'w').close()
        file.writelines(data)

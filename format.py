import pandas as pd
import matplotlib.pyplot as plt

TESTS_COUNT=100

dictionary={
    'Orginal z5':[0,0,0],
    'Single-threaded z5':[0,0,0],
    '4 C++ Threads':[0,0,0],
    '4 OpenMP Threads':[0,0,0],
    '16 C++ Threads':[0,0,0],
    '16 OpenMP Threads':[0,0,0],
    '64 C++ Threads':[0,0,0],
    '64 OpenMP Threads':[0,0,0]
}


with open('results.txt','r') as file:
    lines = [line for line in file]

for i in range(0,len(lines)):
    if lines[i].startswith('Running orginal z5...'):
        dictionary['Orginal z5'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Orginal z5'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Orginal z5'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running optimized, single-threaded z5...'):
        dictionary['Single-threaded z5'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Single-threaded z5'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Single-threaded z5'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 4 C++ Threads...'):
        dictionary['4 C++ Threads'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['4 C++ Threads'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['4 C++ Threads'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 4 OpenMP Threads...'):
        dictionary['4 OpenMP Threads'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['4 OpenMP Threads'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['4 OpenMP Threads'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 16 C++ Threads...'):
        dictionary['16 C++ Threads'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['16 C++ Threads'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['16 C++ Threads'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 16 OpenMP Threads...'):
        dictionary['16 OpenMP Threads'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['16 OpenMP Threads'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['16 OpenMP Threads'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 64 C++ Threads...'):
        dictionary['64 C++ Threads'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['64 C++ Threads'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['64 C++ Threads'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 64 OpenMP Threads...'):
        dictionary['64 OpenMP Threads'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['64 OpenMP Threads'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['64 OpenMP Threads'][2]+=float(lines[i+10].split(' ')[1])
    
for key in list(dictionary.keys()):
    dictionary[key] = [round(dictionary[key][0]/TESTS_COUNT,3),round(dictionary[key][1]/TESTS_COUNT,3),round(dictionary[key][2]/TESTS_COUNT,3)]

for key in list(dictionary.keys()):
    print(key)
    print(dictionary[key])

df = pd.DataFrame.from_dict(dictionary, orient='index', columns=['small', 'medium', 'big'])

fig, ax = plt.subplots(figsize=(5, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, cellLoc='center', loc='center')

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.savefig('results_table.png', bbox_inches='tight', dpi=300)

print("Table saved as 'results_table.png'. You can now add this image to your PDF.")
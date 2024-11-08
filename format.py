TESTS_COUNT=100

dictionary={
    'Running orginal z5...':[0,0,0],
    'Running optimized, single-threaded z5...':[0,0,0],
    'Running multi-threaded z5 with 4 C++ Threads...':[0,0,0],
    'Running multi-threaded z5 with 4 OpenMP Threads...':[0,0,0],
    'Running multi-threaded z5 with 16 C++ Threads...':[0,0,0],
    'Running multi-threaded z5 with 16 OpenMP Threads...':[0,0,0],
    'Running multi-threaded z5 with 64 C++ Threads...':[0,0,0],
    'Running multi-threaded z5 with 64 OpenMP Threads...':[0,0,0]
}


with open('results.txt','r') as file:
    lines = [line for line in file]

for i in range(0,len(lines)):
    if lines[i].startswith('Running orginal z5...'):
        dictionary['Running orginal z5...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running orginal z5...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running orginal z5...'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running optimized, single-threaded z5...'):
        dictionary['Running optimized, single-threaded z5...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running optimized, single-threaded z5...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running optimized, single-threaded z5...'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 4 C++ Threads...'):
        dictionary['Running multi-threaded z5 with 4 C++ Threads...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running multi-threaded z5 with 4 C++ Threads...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running multi-threaded z5 with 4 C++ Threads...'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 4 OpenMP Threads...'):
        dictionary['Running multi-threaded z5 with 4 OpenMP Threads...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running multi-threaded z5 with 4 OpenMP Threads...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running multi-threaded z5 with 4 OpenMP Threads...'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 16 C++ Threads...'):
        dictionary['Running multi-threaded z5 with 16 C++ Threads...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running multi-threaded z5 with 16 C++ Threads...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running multi-threaded z5 with 16 C++ Threads...'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 16 OpenMP Threads...'):
        dictionary['Running multi-threaded z5 with 16 OpenMP Threads...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running multi-threaded z5 with 16 OpenMP Threads...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running multi-threaded z5 with 16 OpenMP Threads...'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 64 C++ Threads...'):
        dictionary['Running multi-threaded z5 with 64 C++ Threads...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running multi-threaded z5 with 64 C++ Threads...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running multi-threaded z5 with 64 C++ Threads...'][2]+=float(lines[i+10].split(' ')[1])
    elif lines[i].startswith('Running multi-threaded z5 with 64 OpenMP Threads...'):
        dictionary['Running multi-threaded z5 with 64 OpenMP Threads...'][0]+=float(lines[i+2].split(' ')[1])
        dictionary['Running multi-threaded z5 with 64 OpenMP Threads...'][1]+=float(lines[i+6].split(' ')[1])
        dictionary['Running multi-threaded z5 with 64 OpenMP Threads...'][2]+=float(lines[i+10].split(' ')[1])
    
for key in list(dictionary.keys()):
    dictionary[key] = [round(dictionary[key][0]/TESTS_COUNT,3),round(dictionary[key][1]/TESTS_COUNT,3),round(dictionary[key][2]/TESTS_COUNT,3)]

for key in list(dictionary.keys()):
    print(key)
    print(dictionary[key])


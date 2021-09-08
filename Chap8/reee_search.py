import re, os
    

dir = input('GIMMIE DIRECTORY: ')
reg = input('GIMMIE REEEEGEX: ')
searchRegex = re.compile(reg)

for file in os.listdir(dir):
    if not file.endswith('.txt'):
        continue
    print(os.path.join(dir, file))
    txtfile = open(os.path.join(dir, file), 'r')
    lines = txtfile.readlines()
    for line in lines:
        if not searchRegex.search(line) == None:
            print(f'\t{line}')
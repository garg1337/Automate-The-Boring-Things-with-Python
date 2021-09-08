import re, os

filename = input('Gief libs file pls: ')

libs = open(filename)
text = libs.read()
libs.close()

regex = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

for match in regex.findall(text):
    reg = re.compile(f'{match}')
    inp_text = input(f'Enter the substitute for {match}: ')
    text = reg.sub(inp_text, text, 1)

print(text)

ans = open(f'{os.path.basename(filename)}_ans', 'w')
ans.write(text)
ans.close()

def commacode(list):
    listLen = len(list)
    if listLen <= 0:
        return ''
    if listLen == 1:
        return list[0]
    listStr = ''        
    for i in range(listLen-1):
        listStr += list[i] + ', '
    listStr += 'and ' + list[-1] 
    return listStr

list = ['apples', 'bananas', 'tofu', 'cats']
list2 = ['apples']
list3 = []
print(commacode(list))
print(commacode(list2))
print(commacode(list3))
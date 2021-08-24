table1 = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]


table2 = [['PISSSSSSSSSSSSSSSSSS', 'oranges', 'SHIIIIIIIIIIIIIIIT', 'banana'],
['Alice', 'Bob', 'Carol', 'VISIONS OF FATTY'],
['dogs', 'cats', 'OORRRZEEAAAAAAAAAAA', 'goose']]

def formatTable(table):
    numRows = len(table)
    numCols = len(table[0])
    formattedTable = [[]] * numRows
    for i in range(0,numRows):
        longestLen = 0
        for j in range(0, numCols):
            longestLen = max(longestLen, len(table[i][j]))
        row = ['']*numCols
        for j in range(0, numCols):
            row[j] = table[i][j].rjust(longestLen)
        formattedTable[i] = row
    return formattedTable

def printTableColWise(table):
    numRows = len(table)
    numCols = len(table[0])
    for i in range(0,numCols):
        for j in range(0, numRows):
            print(table[j][i], end=' ')
        print()

printTableColWise(formatTable(table1))
printTableColWise(formatTable(table2))

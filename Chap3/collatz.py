def collatz(number):
    if number % 2 == 0:
        return number // 2
    return 3*number +1

while True:
    print('Gief int pls')
    try:
        number = int(input())
        break
    except:
        print('Das not an int ya git')

while True:
    number = collatz(number)
    print(number)
    if number == 1:
        print('Gj')
        break
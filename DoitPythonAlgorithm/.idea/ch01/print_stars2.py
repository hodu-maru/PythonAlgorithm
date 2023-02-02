
printStarNum = int(input('출력할 * 개수:'))
newLineNum = int(input('몇개마다 개행?:'))

for i in range(printStarNum // newLineNum):
    print('*' * newLineNum)

print('*' * (printStarNum % newLineNum))


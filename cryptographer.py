#SPACE - 000000
#A - 010101
#B - 110110
#C - 001101
#D - 101100
#E - 011110
#F - 111100
#G - 100110
#H - 000001
#I - 000100
#J - 010001
#K - 100001
#L - 101101
#M - 001100
#N - 000010
#O - 010000
#P - 010011
#Q - 000011
#R - 111101
#S - 100011
#T - 100111
#U - 010110
#V - 011111
#W - 010100
#X - 000101
#Y - 010111
#Z - 101010

a = 0

while a == 0:
    print(' ')
    print('1: Из букв в цифры')
    print('2: Из цифр в буквы')
    print(' ')

    type = int(input('Введите число: '))
    print(' ')

    if type == 1:
        code = input('Введите буквы: ')
        answer = []
        for i in range(len(code)):
            if code[i] == ' ':
                answer.append('000000')
            elif code[i] == 'A':
                answer.append('010101')
            elif code[i] == 'B':
                answer.append('110110')
            elif code[i] == 'C':
                answer.append('001101')
            elif code[i] == 'D':
                answer.append('101100')
            elif code[i] == 'E':
                answer.append('011110')
            elif code[i] == 'F':
                answer.append('111100')
            elif code[i] == 'G':
                answer.append('100110')
            elif code[i] == 'H':
                answer.append('000001')
            elif code[i] == 'I':
                answer.append('000100')
            elif code[i] == 'J':
                answer.append('010001')
            elif code[i] == 'L':
                answer.append('101101')
            elif code[i] == 'M':
                answer.append('001100')
            elif code[i] == 'N':
                answer.append('000010')
            elif code[i] == 'O':
                answer.append('010000')
            elif code[i] == 'P':
                answer.append('010011')
            elif code[i] == 'Q':
                answer.append('000011')
            elif code[i] == 'R':
                answer.append('111101')
            elif code[i] == 'S':
                answer.append('100011')
            elif code[i] == 'T':
                answer.append('100111')
            elif code[i] == 'U':
                answer.append('010110')
            elif code[i] == 'V':
                answer.append('011111')
            elif code[i] == 'W':
                answer.append('010100')
            elif code[i] == 'X':
                answer.append('000101')
            elif code[i] == 'Y':
                answer.append('010111')
            elif code[i] == 'Z':
                answer.append('101010')
            elif code[i] == 'K':
                answer.append('100001')
        print(' ')
        print('Ответ:', end=' ')
        for i in range(len(answer) - 1):
            print(answer[i], end=' ')
        print(answer[len(answer) - 1])
        print(' ')
    elif type == 2:
        print('!!ВВОДИТЬ С ПРОБЕЛАМИ!!')
        print(' ')
        code = []
        code = input('Введите цифры: ')
        code = code.split()
        answer = []
        for i in range(len(code)):
            if code[i] == '000000':
                answer.append(' ')
            elif code[i] == '010101':
                answer.append('A')
            elif code[i] == '110110':
                answer.append('B')
            elif code[i] == '001101':
                answer.append('C')
            elif code[i] == '101100':
                answer.append('D')
            elif code[i] == '011110':
                answer.append('E')
            elif code[i] == '111100':
                answer.append('F')
            elif code[i] == '100110':
                answer.append('G')
            elif code[i] == '000001':
                answer.append('H')
            elif code[i] == '000100':
                answer.append('I')
            elif code[i] == '010001':
                answer.append('J')
            elif code[i] == '100001':
                answer.append('K')
            elif code[i] == '101101':
                answer.append('L')
            elif code[i] == '001100':
                answer.append('M')
            elif code[i] == '000010':
                answer.append('N')
            elif code[i] == '010000':
                answer.append('O')
            elif code[i] == '010011':
                answer.append('P')
            elif code[i] == '000011':
                answer.append('Q')
            elif code[i] == '111101':
                answer.append('R')
            elif code[i] == '100011':
                answer.append('S')
            elif code[i] == '100111':
                answer.append('T')
            elif code[i] == '010110':
                answer.append('U')
            elif code[i] == '011111':
                answer.append('V')
            elif code[i] == '010100':
                answer.append('W')
            elif code[i] == '000101':
                answer.append('X')
            elif code[i] == '010111':
                answer.append('Y')
            elif code[i] == '101010':
                answer.append('Z')
        print(' ')
        print('Ответ:', end=' ')
        for i in range(len(answer)):
            print(answer[i], end='')
        print('')
        print(' ')
    else:
        print('!!ЧИСЛО ВВЕДЕНО НЕВЕРНО!!')
        print(' ')
    b = input('Введите что-нибудь чтобы закрыть или не вводите ничего: ')
    if b != '':
        a = 1
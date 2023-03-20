import re
import random
#Функции
###################################################
def TaskSelection():
    print("Выберите номер задачи:\n"
          "1 - Соединение слов в строку.\n"
          "2 - Соединение слов в строку (слово stop).\n"
          "3 - Редкие слова.\n"
          "4 - Математика для детей.")
    number = input()
    match number:
        case "1":
            ConnectingWordsToAString()
        case "2":
            ConnectingWordsToAStringStop()
        case "3":
            RareWords()
        case "4":
            MathForKids()
        case _:
            print("Введен неправильный номер.")
            TaskSelection()

###################################################
def ConnectingWordsToAString():
    while 1 == 1:
        Number = input('Введите количество слов. ')
        if Number.isdigit():
            Number = int(Number)
            break
        else:
            print('Вы ввели не число. Введите число!')
    counter = 1
    line = ''
    while counter <= Number:
        print('Введите', counter, 'слово.')
        Word = input()
        pattern = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern:
            counter = counter + 1
            line = line + Word + ' '
    print(line.rstrip())

###################################################

def ConnectingWordsToAStringStop():
    line = ''
    counter = 1
    while 1 == 1:
        print('Введите', counter, 'слово.')
        Word = input()
        if Word.lower() == 'stop':
            break
        pattern = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern is not None:
            counter = counter + 1
            line = line + Word + ' '
        else:
            print('Ошибка ввода!')
    print(line.rstrip())

###################################################

def RareWords():
    #while counter <= Number:
        print('Введите слово.')
        Word = input()
        pattern = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern:
            symbol = 'ф'
            if symbol in Word.lower():
                print("Ого! Это редкое слово!")
            else:
                print("Эх, это не очень редкое слово...")
        else:
            RareWords()

###################################################

def MathForKids():
    counterFalse = 0
    counterTrue = 0
    while counterFalse < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        str2 = str(num1) + ' + ' + str(num2) + ' = '
        while 0 < 1:
            Number = input(str2)
            if Number.isdigit():
                Number = int(Number)
                break
            else:
                print('Вы ввели не число. Введите число!')
        if (num1 + num2) == Number:
            counterTrue = counterTrue + 1
            print('Правильно!')
        else:
            counterFalse = counterFalse + 1
            print('Ответ неверный.')
    print('Игра окончена. Правильных ответов: ', str(counterTrue))

###################################################

#Основная программа
TaskSelection()
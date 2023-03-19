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
    print('Введите количество слов.')
    Number = input()
    pattern1 = re.fullmatch(r"[0-9]{1,}", Number)
    if pattern1:
        Number = int(Number)
    else:
        ConnectingWordsToAString()

    counter = 1
    str = ''
    while counter <= Number:
        print('Введите ', counter, ' слово.')
        Word = input()
        pattern2 = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern2:
            counter = counter + 1
            str = str + Word + ' '
    print(str.rstrip())
###################################################

def ConnectingWordsToAStringStop():
    print('Введите количество слов.')
    Number = input()
    pattern1 = re.fullmatch(r"[0-9]{1,}", Number)
    if pattern1:
        Number = int(Number)
    else:
        ConnectingWordsToAStringStop()

    counter = 1
    str = ''
    while counter <= Number:
        print('Введите ', counter, ' слово.')
        Word = input()
        if Word == 'stop':
            break
        pattern2 = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern2:
            counter = counter + 1
            str = str + Word + ' '
    print(str.rstrip())
###################################################

def RareWords():
    #while counter <= Number:
        print('Введите слово.')
        Word = input()
        pattern = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern:
            symbol = 'ф'
            if symbol in Word:
                print("Ого! Это редкое слово!")
            else:
                print("Эх, это не очень редкое слово...")
        else:
            RareWords()

###################################################

def MathForKids():
    counter = 0
    while counter <= 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        #str2 = str(num1) + ' + ' + str(num2) + ' = '
        str1 = str(55)
        str2 = str(44)
        print(num1)
        print(num2)
        print(str1)
        print(str2)
        Number = input(str2)
        if Number.isdigit():
            print('Введите ', counter, ' слово.')
        Word = input()
        pattern2 = re.fullmatch(r"[A-Za-zА-Яа-яЁё\-]{1,}", Word)
        if pattern2:
            counter = counter + 1
            str = str + Word + ' '
    print(str.rstrip())
###################################################

#Основная программа
TaskSelection()
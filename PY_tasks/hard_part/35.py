# Напишите программу, удаляющую из текста все слова содержащие "абв".
import re


def deleter(words):
    return re.sub(r'абв', '', words)


if __name__ == '__main__':
    test_text = input("Enter any text with random 'абв' in it:\n")
    print(deleter(test_text))

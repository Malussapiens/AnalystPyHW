# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
from os import system

# text = 'фбв! Абв, вфвыабв - абввыфвы, провыс'
system('cls')
print('Программа удаляет из текста все слова, содержащие ""абв""')
text = input('Введите текст: ')
words = text.split()
words = ' '.join(list(filter(lambda word: 'абв' not in word.lower(), words)))

print(words)
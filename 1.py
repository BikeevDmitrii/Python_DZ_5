# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# -*- coding: utf-8 -*-
import codecs
with codecs.open('1.txt', encoding='utf-8') as my_file:
    str_list = my_file.read()

def strs(str):
    for item in str_list:
        if 'абв' in item:
            str_list.remove(item)
    print(str_list)
res = list(filter(lambda item: 'абв' not in item, str_list.split()))
print(res)

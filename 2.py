# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Игрок 1
# Игрок 2
# 2021 конфета
# берут от 1 до 28 конфет
# Кто берет последнюю конфету, тот забирает все конфеты у противника


import random
print(('Выберите режим игры '))
print(('1- Игра на 2 игрока '))
print(('2- Игра с компьютером(random) '))
print(('3- Игра с компьютером(smart) '))
v = int(input('Выберите режим игры: '))

c = 121
h = 28
def proverka ():
    while True:
        n = int(input('Берет конфеты = '))
        if (n > 0) & (n <= h) : return n
        else:
            print('Вы ввели неверное значение. Попробуйте еще раз.')

if v == 1:
# Вариант 1 - игра на 2 человек
    
    while c > 0:
        print(f"Осталось конфет  = {c}")
        print ("      Игрок № 1")
        a = proverka()     
        c = c - a
        if c <= 0:
            print()
            print ('!!!!!!!!!!_____ПОБЕДА Игрок № 1_____!!!!!!!!!!' )
            break

        print(f"Осталось конфет = {c}")
        print ("      Игрок № 2")
        b = proverka()      
        c = c - b        
        if c <= 0:
            print()
            print ('!!!!!!!!!!_____ПОБЕДА Игрок № 2_____!!!!!!!!!!')
            break  
        count = 0    
    print("                  GAME END")


elif v == 2:
# Вариант 2 - игра с ботом (случайные числа)   
  
    while c > 0:
        print(f"Осталось конфет  = {c}")
        print ("      Игрок № 1")
        a = proverka()     
        c = c - a
        if c <= 0:
            print()
            print ('_______________ПОБЕДА Игрок № 1_______________' )
            break

        print(f"Осталось конфет = {c}")
        print ("      Игрок № 2")
        
        b = random.randint(1, h)
        print(f'Берет конфеты = {b} ')     
        c = c - b        
        if c <= 0:
            print()
            print ('_______________ПОБЕДА Игрок № 2_______________')
            break  
        count = 0    
    print("                  GAME END")


elif v == 3:
# Вариант 3 - игра с ботом (smart)

    while c > 0:
        print(f"Осталось конфет  = {c}")
        print ("      Игрок № 1")
        a = proverka()     
        c = c - a
        if c <= 0:
            print()
            print ('_______________ПОБЕДА Игрок № 1_______________' )
            break

        print(f"Осталось конфет = {c}")
        print ("      Игрок № 2")
        if (c > 29) &(c < 57):
            b = (c - 28) - 1
        # if (c == 57 ):
        #     b = (57-29)- (h-(57-29))
        elif (c <= 28):
            b = c
        elif (c > 56):
            b = random.randint(1, h)
        print(f'Берет конфеты = {b} ')     
        c = c - b        
        if c <= 0:
            print()
            print ('_______________ПОБЕДА Игрок № 2_______________')
            break  
print("                  GAME END")


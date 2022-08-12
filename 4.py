# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def sjatie(s):
	new_str = ""
	i = 0
	while i < len(s):
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1
		new_str += str(count) + s[i]
		i = i + 1
	return new_str

def rasjatie(t):
    new_str2 = '' 
    count = ''
    for char in t: 
        if char.isdigit(): 
            count += char
        else: 
            new_str2 += char * int(count)
            count = '' 
    return new_str2

path = '4.txt'
with open(path, 'r') as my_file:
    s = my_file.read()
print("Исходная информация:")
print(s)

with open('4_1.txt', 'w') as data:
    print("'Cжатая' информация:")
    print(sjatie(s))
    data.write(sjatie(s))


path = '4_1.txt'
with open(path, 'r') as my_file:
    t = my_file.read()

print("'Расжатая' информация:")
print(rasjatie(t))

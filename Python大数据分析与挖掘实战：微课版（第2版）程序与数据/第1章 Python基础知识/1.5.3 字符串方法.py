# -*- coding: utf-8 -*-
# S = str()  # 冗余代码，可删除

text_str = 'hello word!'
z1 = text_str.find('he', 0, len(text_str))
z2 = text_str.find('he', 1, len(text_str))
print(z1, z2)

text_replaced = text_str.replace('or', 'kl')
print(text_replaced)
print(text_str)

str_part1 = 'joh'
str_combined = str_part1 + ' ' + text_str
print(str_combined)

str1 = 'jo'
str2 = 'qb'
str3 = 'qb'
s1 = str1 != str2
s2 = str2 == str3
print(s1, s2)
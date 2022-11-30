import random
import time
import os
os.system('cls')
list = 'qwertyuiopasdfghjklzxcvbnm '
list = 'qüertyuiopöğasdfghjklıəzxcvbnmçşw .'
word = 'bu yaşamaq deyil mənasız şəkildə var olmaqdır.'
print_word = []
i = 0
wrong_count = 0
wronge_ch = 3
while i!=len(word):
    count = random.randint(0,len(list)-1)
    if wrong_count != wronge_ch:
        print_word.append(list[count])
        if list[count]!=word[i]:
            wrong_count = wrong_count + 1
            i = i - 1
            print(''.join(print_word)) #print('\033[0;0H',''.join(print_word))
            print_word.pop(len(print_word)-1)
        else:
            print(''.join(print_word)) #print('\033[0;0H',''.join(print_word))
            wrong_count = 0
    else:
        print_word.append(word[i])
        wrong_count = 0
        print(''.join(print_word)) #print('\033[0;0H',''.join(print_word))
    
    i = i + 1
    time.sleep(0.0001)   


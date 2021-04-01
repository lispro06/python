num = int(input())
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=' ')
print()


# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution(n):
    if (n & (n - 1)):
        return False
    else:
        return True
user_input = list(input() for _ in range(2))
ls = user_input[1].split()
list=[]
seq=0
print
for i in ls:
	seq = seq + 1
	if solution(int(i)) != True:
		list.append(seq)
print(len(list))
for i in list:
	print(i, end=' ')

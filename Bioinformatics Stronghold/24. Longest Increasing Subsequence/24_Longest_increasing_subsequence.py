'''
Problem:

Given: A positive integer n ≤ 10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

Sample Dataset
5
5 1 4 2 3

Sample Output
1 2 3
5 4 2

'''

f = open('rosalind_lgis.txt', 'r')

lines = f.read().splitlines()

n = int(lines[0])
num_list  = list(map(int, lines[1].split()))

def longIncrSub(string):
    lis_indx = [1]
    for i in range(1, n):
       lis_indx.append(1)
       for j in range(i):
           if string[i] > string[j] and lis_indx[i] <= lis_indx[j]:
               lis_indx[i] = 1 + lis_indx[j]
    lis = []
    last_ele = lis_indx.index(max(lis_indx))
    i = 0
    for k in range(last_ele, -1, -1):
        if lis_indx[k] == lis_indx[last_ele]-i:
            i += 1
            lis.append(string[k])       
         
    return reversed(lis)

def longDecrSub(string):
    lds_indx = [1]
    for i in range(1, n):
       lds_indx.append(1)
       for j in range(i):
           if string[i] < string[j] and lds_indx[i] <= lds_indx[j]:
               lds_indx[i] = 1 + lds_indx[j]
    lds = []
    last_ele = lds_indx.index(max(lds_indx))
    i = 0
    for k in range(last_ele, -1, -1):
        if lds_indx[k] == lds_indx[last_ele]-i:
            i += 1
            lds.append(string[k]) 

    return reversed(lds)

print(*longIncrSub(num_list))
print(*longDecrSub(num_list))
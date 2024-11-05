# task 1

# def print_pyramid(height):
#     current_number = 1
#     for row in range(1, height + 1):
        
#         print(" " * (height - row), end="")  
#         for _ in range(row):
#             print(f"{current_number} ", end="")
#             current_number += 1
#         print()  

# height = int(input())
# print_pyramid(height)


# task 2


# n = int(input())
# while n != 1:
#     print(n)
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1

# print(n)  

    


# task 3

# N = int(input())


# for a in range(1, N + 1):
#     sum_divisors = 0
#     for i in range(1, a // 2 + 1):
#         if a % i == 0:
#             sum_divisors += i
#     if sum_divisors == a:
#         print(a)


# task 4


# a = input()
# mydict = {}
# for i in a.lower():
#     mydict[i] = mydict.get(i, 0) + 1
# print(mydict)


# task 5


# a = input()
# mydict = {}
# mylist = list(a.split())
# for i in mylist:
#     mlist = []
#     for j in range(len(mylist)):
#         if i == mylist[j]:
#             mlist.append(j)
#     if i not in mydict.keys():
#         mydict[i] = mlist
# print(mydict)
    

# task 6

# mydict = {}
# old_dict = {'a':[1,2],
#             'b':[3,4]}
# for k,v in old_dict.items():
#     for i in v:
#         mydict[i]=k
# print(mydict)

# # task 7
# dict1 = {'a':1, 'b':2, 'c':3}
# dict2 = {'a':2, 'b':3, 'c':4}
# mydict = {}
# for k,v in dict1.items():
#     for m,n in dict2.items():
#         if m==k:
#             mydict[m] = v+n
# print(mydict)   

# task 8
# a = input()
# mydict = {}
# mylist = list(a.split())
# for i in mylist:
#     cnt = 0
#     for j in range(len(mylist)):
#         if i == mylist[j]:
#             cnt+=1
#     if i not in mydict.keys():
#         mydict[i] = cnt
# print(mydict)


# task 11
# def harshad_number(a):
#     m = str(a)
#     sum = 0
#     for i in m:
#         n = int(i)
#         sum += n
#     return a % sum == 0

# a = int(input())
# for i in range(1, a + 1):
#     if harshad_number(i):
#         print(i)

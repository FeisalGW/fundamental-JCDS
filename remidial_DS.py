##nomer1
# def find_sort(s):
#     y = s.split()
#     panjang_kata = []
    
#     for new in y:
#         panjang_kata.append(len(new))
#     panjang_kata.sort()
    
#     return print(panjang_kata[0])

# find_sort("many people get up early in the morning")
# find_sort("Every office would getting newest monitor")
# find_sort("Create new file after this morning")
    

#nomer2
# def persistence(x):
#     t_keseluruhan = x
#     jumlah = 0
    
#     while (t_keseluruhan >= 10):
#         z = t_keseluruhan
#         y = str(z)
#         total = 1

#         for a in range (len(y)):
#             total *= int(y[a])
#         jumlah += 1
#         t_keseluruhan = total

#     return print(jumlah)

# persistence(39)
# persistence(999)
# persistence(4)

##nomer 3
# def multiplication_table(x,y):
#     list1 = []
#     list2 = []
#     z = ''
#     for i1 in range (y):
#         list2.append(i1+1)
#     for i2 in range (x):
#         list1.append(list(map(lambda num: num * (i2+1), list2)))
#     for i3 in range (x):
#         for i4 in range (y):
#             z += ' {} '.format(str(list1[i3][i4]))
#         z += '\n'
    
#     return print(z)

# multiplication_table(3,3)
# multiplication_table(5,3)
# multiplication_table(3,5)

# ##nomer 4
# def alphabet_position(huruf):
#     dict = {'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8',
#     'i':'9','j':'10','k':'11','l':'12','m':'13','n':'14','o':'15','p':'16','q':'17',
#     'r':'18','s':'19','t':'20','u':'21','v':'22','w':'23','x':'24','y':'25','z':'26'
#     }
#     lists = []
#     kata = huruf.lower()
#     for item in list(kata):
#         for idx, val in dict.items():
#             if idx == item:
#                 lists.append(val)
    
#     return ' '.join(lists)
    
# print(alphabet_position("The sunset sets at twelveo'clock"))
# print(alphabet_position("It's never too late to try"))
# print(alphabet_position("Have you done your homework"))

##extra question
# def is_prime(nomor):
#     if nomor == 1:
#         prime = False
#     elif nomor == 2:
#         prime = True
#     elif nomor < 1:
#         prime = False    
#     else:
#         prime = True
#         for uji in range(2, int(nomor/2)+1):
#             if nomor % uji == 0:
#                 prime = False
#                 break
    
#     print(prime)

# is_prime(1)
# is_prime(2)
# is_prime(-1)
# is_prime(5099)





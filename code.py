#1
#print("Hello")
# 2
#print("Hello World")
#3 
#print ("Hello")
#print ("World")
#4
#print("'Hello'")
#5
#print('"Hello World"')
#6
#print(' "!@#$%^&*() \'')
#7
#print ("\"C:\\Download\\'hello'.py\"")
#8
#print("Hello'\\'nWolrld")
#print("print(\"Hello\\nWold\")")
#9
#c=input()
#print(c)
#10
#n=input()
#n=int(n)
#print(n)
#11
# f=input()
# f=float(f)
# print(f)
#12
# a=input()
# b=input()
# print(a)
# print(b)
#13
# a=input()
# b=input()
# print(b)
# print(a)
#14
# f=input()
# f=float(f)
# print(f)
# print(f)
# print(f)
#15
# a,b = input().split()
# print(a)
# print(b)
#16
# a, b=input().split()
# print(b,a)
#17
# n=input()
# print(n)
# print(n)
# print(n)
#18
# a ,b = input().split(':')
# print(a, b, sep=':')
#19
# y, m, d= input().split('.')
# print(d,m,y, sep='-')
#20
# a,b = input().split('-')
# print(a+b)
#21
# s= input()
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])
# print(s[4])
# #22
# s=input()
# #print (s[0:2:1], s[2:4:1], s[4:6:1])
# arr=[s[0:2],s[2:4],s[4:6]]
# for s  in arr:
#     print(s, end=' ')
#     print('\n')
#23
#a, b, c=input().split(':')
#print(b)
#24
# w1, w2 = input().split()
# s=w1+w2
# print(s)
#25
# a, b =input().split()
# c= int(a)+int(b)
# print(c)
#26
# a , b = input().split()
# c= float(a)+ float(b)
# print (c)
#27
# a=input()
# n=int(a)
# print('%x'%n)
# #28
# a=input()
# n=int(a)
# print('%X'%n)
#29
# a = input()
# n= int(a ,16)
# print ('%o' % n)
# #30
# print("영문알파벳입력하세요. (한자리)")
# n= ord(input())
# print(n)
#31
# c=int(input())
# print(chr(c))
#32
# a=int(input())
# print(-a)
#33
# a=int(input())
# print(chr(a+1))
# a = input()
# b = ord(a)+1
# c = chr(b)
# print(c)
#34
# a , b = input().split()
# c= int(a)-int(b)
# print(c)
#35 
# a , b = input().split()
# c = float(a)*float(b)
# print(c)
#36
# w , n = input().split()
# print(w*int(n))
#37
# n=input()
# s=input()
# print (int(n)*s)
#38
# a, b=input().split()
# c = int(a)**int(b)
# print(c)
#39 
# a , b =input().split()
# c = float(a)**float(b)
# print(c)
#40
# a ,b =input().split( )
# c = int(a)//int(b)
# print(c)
#41
# a , b = input().split()
# c = int(a) % int(b)
# print(c)
#42
# a , b= float (input().split())
# print(format(a, b,".2f"))
# 43
# a , b= input().split()
# a =float(a)
# b =float(b)
# c =a/b
# print("%.3f" % c)
#44
#a, b = input().split()
# c1 = int(a)+int(b)
# c2 =int(a)-int(b)
# c3 =int(a)*int(b)
# c4=int(a)//int(b)
# c5=int(a)%int(b)
# c6 =float(a)/float(b)
#깔끔한 정리
# a =int(a)
# b =int(b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print(round(a/b,2))
#45
# a , b, c = input().split()
# a = int(a)
# b = int(b)
# c = int (c)
# hap = a + b + c
# avg = hap % 3
# print(hap)
# print (format(avg, ".2f"))
#46 
# n = input()
# n = int(n)
# print (n << 1)
#47
# a , b = input().split()
# a = int (a)
# b = int (b)
# print (a<<b)
#48
# a ,  b = input().split()
# a =int(a)
# b = int(b)
# print (a<b)
#49
# a, b =input().split()
# a = int(a)
# b = int(b)
# print (a==b)
#50
# a , b = input().split()
# a = int(a)
# b = int(b)
# print (a<=b)
#51
# a ,b = input().split()
# a = int(a)
# b = int(b)
# print(a !=b)
#52
# n = int(input())
# print(bool(n))
#53
# a = bool(int(input()))
# print(not a)
#54
# a, b = input().split()
# print(bool(int(a)) and bool(int(b)))
#55
# a ,b = input().split()
# print(bool(int (a)) or bool(int(b)))
#56
# a , b = input().split()
# a =bool(int(a))
# b =bool(int(b))
# print((a and (not b)) or ((not a) and b))
#57 
# a, b = map (int ,  input().split())
# if (bool (a) ^ bool(b) ==True):
#     print("Fales")    
# else:
#         print("True")
#58
# a , b = map (int, input().split())
# a , b =bool(a), bool(b)
# if( a == False and b ==False):
#     print("True")
# else :
#     print("False")
#59
# a = int(input())
# print(~a)
#60
# a ,b = map (int, input().split())
# print (a&b)
#61
# a , b = map(int, input().split())
# print(a|b)
# a ,b = map (int, input().split())
# print(a^b)
#63
# a, b = map(int, input().split())
# c=(a if(a>=b)else b)
# print(int(c))
#64
# a, b, c = map(int, input().split())
# d =(a if a<b else b) if ((a if a<b else b)<c) else c
# print(int(d))
#65
# a, b, c = map(int, input().split())
# if a % 2 == 0:
#     print(a)
# if b % 2 ==0:
#     print(b)
# if c % 2 ==0:
#     print(c)
#66
# a , b, c = map(int, input().split())
# if a % 2 == 0 :
#     print("even")
# else : print("odd")
# if b % 2 == 0 :
#      print("even")
# else : print("odd") 
# if c % 2 == 0 :
#      print("even")
# else :  print("odd")     
#67
# a = int(input())
# if a < 0 :
#     if a % 2 == 0 : print ('A')
#     else : print('B')
# else : 
#     if a % 2 ==0 : print('C')
#     else : print('D')
#68
# jumsu = int(input())
# if jumsu >= 90 : print('A')
# else : 
#     if jumsu >=70 : print('B')
#     else : 
#         if jumsu >=40 : print('C')
#         else : print('D')
#69 
# 오답
# a, b, c, d= map (int, input().split())
# if a == a : print('A:best!!!!')
# else : 
#     if b ==b : print('B:good!!')
#     else : 
#         if  c==c: print('C:run!')
#         else : print('D:slowly~')
# 깔끔한 정리
# a = input ()
# if a == 'A' : print("best!!!!")
# elif a=='B': print('good!!')
# elif a == 'C' : print('run!!')
# elif a == 'D' : print('slowly~')
# else : print ('what?')
# 70
# a =int(input())
# if a//3==1:
#     print("spring")
# elif a//3==2:
#     print("summer")
# elif a//3==3:
#     print("fall")
# else : 
#     print("winter")
#71
#정리   
# while True:
#     a =input()
#     a =int(a)
#     if a ==0 :
#         break
#     else :
#         print(a)
#72 
# count = int(input())
# while count !=0 :
#     print (count)
#     count-=1
#73
# n =int(input())
# while n !=0:
#     n-=1
#     print(n)
#74
# c=ord(input())
# t =ord('a')
# while t<=c :
#     print(chr(t), end='\n' )
#     t  +=1
#75
# n = int(input())
# a=n 
# while n>=0:
#     print(a-n)
#     n-=1
#76
# n = int(input())
# for i in range (n+1):
#     print (i)
#77
# n =int(input())
# s =0
# for i in range (1, n+1):
#     if i%2==0 :
#         s=s+i
#         print (s)
#78
# while True :
#     x = input()
#     print(x)
#     if x =='q':
#         break
#79
# sum = 0
# i =0
# n = int (input())
# while True :
#     i+= 1
#     sum +=i
#     if(sum>n):
#         print(i)
#         break
#80
# a ,  b = map (int, input().split())
# for i in range(1, a+1):
#     for j in range (1, b+1):
#         print(i,j)
#81
# a = int(input(), 16)
# for i in range (1,16):
#     print('%X*%X=%X' %(a,i,a*i))
#82
# n = int (input())
# for i in range (1 , n+1) :
#     if i%10==3 or i%10==6 or i%10==9 :
#         print("X", end ='   \n')
#     else :  print(i, end = '   \n')
#83
# r, g, b = map (int, input().split())
# for i in range (0, r):
#     for j in range(0, g):
#         for k in range(0,  b):
#             print(i,j,k)
# print(r*g*b)
#84
# h, b,  c, s = map (int, input().split())
# m = (h* b * c * s) /8/1024/1024
# print('%.1f MB' %m)
#85
# w, h, b = map (int, input().split())
# print("%.2f MB" %(round(w*h*b/8/1024/2024,2)))
#86
# n = int(input())
# i = 0
# sum = 0
# while True:
#     sum+=i
#     i+=1
#     if(sum>=n):
#         break
#     print(sum)
#87
# n = int(input())
# for i in range(1, n+1):
#     if i%3==0:
#         continue
#     print(i,end='   ')
#88
# a ,b, n = map (int, input().split())
# total =a
# for i in range (0, n-1) :
#     total=total+b
# print(total)
#89
# a ,b, n = map (int, input().split())
# total =a
# for i in range (0, n-1) :
#     total=total*b
# print(total)
#90
# a, m, d, n = map (int, input().split())
# total=a
# for i in range (0,n-1):
#     total=total*m+d
# print(total)
#91 
# a, b, c = map( int, input().split())
# d=1
# while d%a !=0 or d%b !=0 or d%c !=0:
#         d+=1
#         print(d)

#92
# n = int (input())
# x = input().split()
# result =[ ]
# for i in range(n) :
#     x[i] = int(x[i])
# for i in range(24) :
#     result.append(0)
# for i in range(n) :
#     result[x[i]] += 1

# for i in range(1, 24) :
#     print (result[i], end=' ')

#93
# n= int(input())
# a = input().split()
# for i  in range(n) :
#     a[i] = int(a[i])

# for i in range(n-1, -1, -1):
#     print(a[i], end='  ')

#94 
# n = int(input())
# k = list(map(int, input().split()))
# a = k[0]
# for i in range(n):
#     if(a>k[i]):
#         a=k[i]
#     print(a)

#95

# d = []
# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)
# n = int(input())
# for i in range(n):
#     x , y = input().split()
#     d[int(x)][int(y)] =1 
# for i in range(1, 20) :
#     for j in range(1, 20):
#         print(d[i][j], end=' ')
#     print()

#96 예시 입력힘듬..

# p = []
# for i in range(20) :
#     p.append([])
#     for j in range(20) :
#             p[i].append(0)
# for i in range(19) :
#     a = input().split()
#     for j in range(19):
#         p[i+1][j+1] = int(a[j])
# n = int(input())
# for i in range(n) :
#     x , y = map(int, input().split())
#     for j in range(1, 20) :
#         if p [j][y] == 0:
#             p [j][y] =1 
#         else :
#             p [j][y] = 0

#         if p[x][y] == 0 :
#             p[x][y] = 1
#         else :
#             p[x][y] = 0

#     for i in range(1, 20):
#         for j in range(1,20):
#             print(p[i],[j], end=' ') 

#         print()           

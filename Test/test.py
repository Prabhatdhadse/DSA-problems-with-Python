# def p(n=1):
#     if n > 100:
#         return
#     print(n)
#     p(n + 1)

# p()


# print("DataScience"[ 3:])

# name = "python"

# if name == "java" or "c":
#     print("Login Done ")
# else:
#     print("Not Valid")


# print("ArtificialIntelligence"[::3])


# for i in range (1):
#     print("Prabhat")

# list = [2,3,4,5,6,7]

# print(list[2:5])


# my_array = [7, 12, 9, 4, 11, 8]
# minVal = my_array[0]

# for i in my_array:
#   if i < minVal:
#     minVal = i

# print('Lowest value:', minVal)

# x= 5
# y= 10
# z= x+y
# print(z)


# def checkOddEven(x):
#     # code here
#     if x % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# checkOddEven(4)


# n= 5873
# num = n
# while num > 0:
#     last_digit = num % 10
#     print(last_digit)
#     num = num // 10


# n= 5873
# num = n
# count= 0
# while num > 0:
#     count +=1
#     num = num // 10


# //palindorme//
# n = 1234
# num = n 
# result = 0
# while num > 0:
#     ld = num % 10
#     result = (result*10) + ld
#     num = num // 10
#     print(n == result)



# //angstrome number//
# n = 153
# num = n 
# total = 0
# nod = len(str(n))
# while num > 0:
#     ld = num % 10
#     total = total + (ld**nod)
#     num = num // 10
#     print(total ==n) 



# //prime number

# num = 20
# result = []
# for i in range (1,num+1):
#     if num % i == 0:
#         result.append(i)
# print(result)


# num = 10
# result = []
# for i in range(1,num//2+1):
#     if num % i ==0:
#         result.append(i)
# result.append(num)
# print(result)


# frequency map/dict

# nums = [1,5,6,4,7,1,5,4,8,6,2,8]
# freq_map = dict()
# for i in range(0,len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]] +=1
#     else:
#         freq_map[nums[i]] = 1 
#     print(freq_map)   



# frequency map/dict

# nums = [1,5,6,4,7,1,5,4,8,6,2,8]
# hash_map = dict()
# n = len(nums)
# for i in range(0,n):
#     hash_map[nums[i]] = hash_map.get(nums[i],0) + 1
# print(hash_map)


# hashing

# n = [1,2,6,7,5,4,2,1,7,8,9,10,5]
# m = [10,111,1,9,8,2,67]
# hash_list = [0]*11

# for num in n:
#     hash_list[num]+= 1

# for num in m:
#     if num<1 or num>10:
#         print(0)
#     else:
#         print(hash_list[num])



# Recursion using head

# def func(x,n):
#     if n == 0:
#         return
#     print(x)
#     func(x,n-1)
# func(15,4)


# printing 1 to n using head recursion

# def func(i,n):
#     if i>n:
#         return
#     print(i)
#     func(i+1, n)
# func(1,4)



# printing N to 1 using tail recursion

# def func(i,n):
#     if i>n:
#         return
#     func(i+1, n)
#     print(i)
    
# func(1,4)


# printing 1 to n using tail recursion
# def func(n):
#     if n==0:
#         return
#     func(n-1)
#     print(n)
# func(5)


# sum of 1 to n [parameterized]

# def func(sum,i,n):
#     if i>n:
#         print(sum)
#         return
#     func(sum+i,i+1,n)
# func(0,1,4)

# sum of 1 to N [functional]
# def func(N):
#     if N == 1:
#         return 1
#     return N+func(N-1)
# print(func(4))


# Factorial Recursion

# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     return num * factorial(num-1)
# print(factorial(4))



# Reverse array

# arr = [5,9,7,8,5,6,1,2,3]
# arr.reverse()
# arr[::-1]
# print(arr)


# Reverse array by recursion


# nums = [5,9,7,8,5,6,1,2,3]
# def func(nums,left,right):
#     if left >= right:
#         return
#     nums[left],nums[right] = nums[right],nums[left]
#     func(nums,left+1,right-1)

# def reverse_Array(nums,l,r):
#     func(nums,l,r)
#     return nums
# print(reverse_Array(nums, 0, len(nums)-1))


# Checking is palindrome or not

# S = 'ANBCDDCBNA'
# n = len(S)
# def func(S, left, right):
#     while left<right:
#         if S[left] != S[right]:
#             return False
#         left += 1
#         right -=1
#     return True
# print(func(S, 0, n-1))


#  short way to check is palindrome or not
# S = 'ANBCDDCBNA'
# print(S == S[::-1])

# palindrome check by recusrion

S = 'ANBCDDCBNA'
def palindrome(S,left,right):
    if left >= right:
        return True
    if S[left] != S[right]:
        return False
    return palindrome(S, left+1, right-1)
print(palindrome(S, 0, len(S)-1))
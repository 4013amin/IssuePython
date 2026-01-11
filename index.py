# def process_number():
#     number = int(input("Enter a number: "))
#     total_sum = 0

#     for i in range(1, number + 1):
#         if str(i).isdigit():
#             if i % 2 == 0:
#                 total_sum += i

#     return total_sum

# result = process_number()
# print("The sum of even numbers is:", result)


# def Sum_odd_number():
#     number = int(input("Enter a number :"))
#     count = 0
#     for i in range(1 , number + 1 , 2):
#         if i % 2 != 0:
#             count += i 
#     return count

# result = Sum_odd_number()
# print("This is Odd number is :" , result)

# def Calculate():
#     number = int(input("Enter a number :"))

#     if number % 2 == 0 :
#          print("این عدد زوج است ")
#     else :
#          print("این عدد فرد است")


# Calculate()

# def second_largest():
#     numberList = [10, 20, 4, 45, 99, 100, 50]

#     max_num = max(numberList)

#     filtered_list = [num for num in numberList if num != max_num]

#     second_max = max(filtered_list) if filtered_list else None

#     print("دومین عدد بزرگ:", second_max)

# second_largest()

# def calculate():
#     number = int(input("Enter a number : "))

#     if number % 2 == 0:
#         print("This number is زوج.")
#     else :
#         print("This is fard")

# calculate()

# def LuckyNumber():
#     number = input("Enter a number: ") 

#     zoj = []  
#     fard = []  

#     for digit in number: 
#         num = int(digit) 
#         if num % 2 == 0:
#             zoj.append(num)
#         else:
#             fard.append(num) 

#     if sum(zoj) == sum(fard) and len(zoj) == len(fard):
#         print("Lucky Number 🎉")
#     else:
#         print("Not a Lucky Number ❌")

# LuckyNumber()

# def SpecialNumber():
#     number = int(input("Enter a number: "))

#     sum_of_digits = sum(int(digit) for digit in str(number))
#     first = int(str(number)[0])
#     end = int(str(number)[-1])

#     result = first * end 
#     num_length = len(str(number))
#     sum_of_digits = sum(int(digit) for digit in str(number))
#     first = int(number[0])
#     end = int(number[-1])

#     result = first * end 
#     num_length = len(number)

#     if sum_of_digits == result and num_length % 2 == 0:
#         print("Special Number 🎉")
#     else:
#         print("Not a Special Number ❌")

# SpecialNumber()
# import math

# try:
#     n = int(input("یک عدد رو وارد کنید "))
# except ValueError:
#     print("عدد وارد نکردی ")

# if n < 2:
#     print("عدد اول نیست")
# else:
#     is_prime = True
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             is_prime = False
#             break

#     if is_prime: 
#         print("عدد اول است")
#     else:
#         print("عدد اول نیست")

# def Paladyom():
#     txt = input("یک متن رو وارد کنید :").lower()

#     if txt == txt[::-1]:
#         print("پالیندروم است")
#     else : 
#         print("پالادیوم نیست ")

# Paladyom()

# def multiple():

#     total = 0 
#     for i in range(1 , 1000):
#         if i % 3 == 0 or i % 5 == 0 :   
#             total += i
#     print(total)

# multiple()

# def sum_even_fibonacci(num):
#     a,b = 1,2
#     couner = 0

#     while a <= num:
#         if a % 2 == 0 :
#             couner += a 
#         a,b, = b,a +b 

#     return couner
# num = 4000000
# result = sum_even_fibonacci(num)
# print("مجموع اعداد زوج در دنباله فیبوناچی که از چهار میلیون بیشتر نیستند:", result)


# def largest_prime_factor(n):
#     divisor = 2  

#     while divisor * divisor <= n:  
#         if n % divisor == 0:  
#             n //= divisor  
#         else:
#             divisor += 1 

#     return n  

# number = 600851475143
# result = largest_prime_factor(number)
# print("بزرگ‌ترین مقسوم‌علیه اول عدد", number, "عبارت است از:", result)

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]

# max_palindrome = 0
# for i in range(100, 1000):
#     for j in range(i, 1000): 
#         product = i * j
#         if is_palindrome(product) and product > max_palindrome :
#             max_palindrome = product
#             factors = (i, j)

# print(f"Largest palindrome: {max_palindrome} = {factors[0]} × {factors[1]}")

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
#
# max_palindrome = 0
# for i in range(100, 1000):
#     for j in range(i, 1000):
#         product = i * j
#         if is_palindrome(product) and product > max_palindrome :
#             max_palindrome = product
#             factors = (i, j)
#
# print(f"Largest palindrome: {max_palindrome} = {factors[0]} × {factors[1]}")

# def index():
#     number = int(input("Enter a number: "))

#     for i in range(1, number + 1):
#         if i % 2 == 0:
#             print(i, "This is an even number.")
#         else:
#             print(i, "This is an odd number.")



# count = 0 

# for i in range( 1 , 101):
#     if i % 2 == 0 :
#         print( i , "zoj")
        
#     else :
#         print(i , "Fard")


# for i in range(1 , 20):
#     if i % 2 == 0:
#         if i == 18 :
#             print(i , "This number is 18")
#         print(i , "zoje")
#     else :
#         print(i , "Fard")
            
# numbers = []

# if numbers is not None:
#     numbers.append("Amin")
#     numbers.append(5)
#     numbers.clear()
#     print(numbers)

numbers = int(input("Enter a number"))

result = str(numbers)
resut_all = result + " Amin"

print(resut_all)
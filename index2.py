

# mtn = input("Enter a Txt : ")


# print(len(mtn))

# counter = 0

# vowels = "aeiouAEIOU"

# for i in mtn:
#     if i in vowels:
#         counter += 1
        

# print("Number of vowels:", counter)

# numbers = int(input("Enter a number : "))

# is_prime = True
# for i in range(2 , numbers -1) :
#     if numbers % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print("is a prime number")
# else:
#     print("is not prime Number")

# strings = input("Enter a txt : ")
# print(strings[::-1])
    
# list_number = [10 , 3 , 5 , 8  , 7 , 2]

# zoj = []
# fard = []

# for i  in list_number:
#     if  i % 2 == 0:
#         zoj.append(i)
#     else:
#         fard.append(i)
        
        
# print("This is zoj :" , zoj)
# print("This is Fard" , fard)

def calculate_factorial(num):
    result = 1 
    
    for i in range(num):
        
        result = result * (i + 1)
        print(i)
    return result
        

user = int(input("Enter a number : "))

answer = calculate_factorial(user)
print("Factorial is:", answer)
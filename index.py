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

def LuckyNumber():
    number = input("Enter a number: ") 

    zoj = []  
    fard = []  

    for digit in number: 
        num = int(digit) 
        if num % 2 == 0:
            zoj.append(num)
        else:
            fard.append(num) 

    if sum(zoj) == sum(fard) and len(zoj) == len(fard):
        print("Lucky Number 🎉")
    else:
        print("Not a Lucky Number ❌")

LuckyNumber()
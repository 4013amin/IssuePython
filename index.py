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


def Sum_odd_number():
    number = int(input("Enter a number :"))
    count = 0
    for i in range(1 , number + 1 , 2):
        if i % 2 != 0:
            count += i 
    return count

result = Sum_odd_number()
print("This is Odd number is :" , result)
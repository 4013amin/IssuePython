# numbers = list(map(int, input("Enter numbers separated by comma: ").split(',')))

# zoj = []
# fard = []

# for i in numbers:
#     if i % 2 == 0:
#         zoj.append(i)
#     else:
#         fard.append(i)

# print("اعداد زوج", zoj)
# print("اعداد فرد ", fard)

# result_zoj = sum(zoj)
# result_fard = sum(fard)

# print("مجموع اعداد زوج " , result_zoj)
# print("مجموع اعداد فرد " , result_fard)



# #جدا سازی اعداد تکراری 
# def Remove_duplicates(add):
#     add = input("Enter numbers separated by comma: ").split(',')
    
#     delete_dup = set(add)
#     return delete_dup

# print(Remove_duplicates(numbers))

#تبدیل عدد به متن 
numner = 1,2,3,4,5,6,7,8,9,10
txt = str(numner)
print(txt)
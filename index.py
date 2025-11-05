numbers = list(map(int, input("Enter numbers separated by comma: ").split(',')))

zoj = []
fard = []

for i in numbers:
    if i % 2 == 0:
        zoj.append(i)
    else:
        fard.append(i)

print("اعداد زوج", zoj)
print("اعداد فرد ", fard)

result_zoj = sum(zoj)
result_fard = sum(fard)

print("مجموع اعداد زوج " , result_zoj)
print("مجموع اعداد فرد " , result_fard)
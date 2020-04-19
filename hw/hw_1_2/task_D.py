"""
Задача D. Точная степень двойки

Дано натуральное число N. Выведите слово YES,
если число N является точной степенью двойки, или слово NO в противном случае.
Операцией возведения в степень пользоваться нельзя!

"""
number = int(input())

binary_representation = f"{number:b}"

# кол-во единиц в двоичном представлении
one_bit_count = sum([int(i) for i in binary_representation])

if one_bit_count == 1:
    print("YES")
else:
    print("NO")
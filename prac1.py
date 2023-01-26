first_num = float(input("Enter second number: "))
count = int(input("Eneter count operations"))

while (count != 0):
    count -= 1
    second_num = float(input("Enter second number again: "))
    operation = int(input("Choose operation: 1.+ 2.- 3.* 4./"))
    if operation == 1:
        first_num += second_num
    if operation == 2:
        first_num -= second_num
    if operation == 3:
        first_num *= second_num  
    if operation == 4:
        if second_num == 0:
            print('You cant divide by zero')
        else:
            first_num = first_num / second_num
    print(first_num)

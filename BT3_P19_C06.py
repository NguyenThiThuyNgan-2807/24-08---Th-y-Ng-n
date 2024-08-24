N = int(input("Số nguyên dương N = "))
if 9<N<100:
    a = N//10 
    b = N%10
    print("Tổng các chữ số của N: ", a+b)
else:
    print("Số nguyên không hợp lệ.")
num=float(input("biror sonni kiriting:"))
rounded_num=round(num,2)
print("yaxlitlangan son:", rounded_num)

num1=float(input("1-sonni kiriting:"))
num2=float(input("2-sonni kiriting:"))
num3=float(input("3-sonni kiriting:"))
largest=max(num1, num2, num3)
smallest=min(num1, num2, num3)
print("Eng katta son",largest)
print("Eng kichik son",smallest)

a=float(input("Necha km:"))
b=a*100_000
print("{} km={}sm".format(a,b))
a=float(input("selsiy haroratni kiriting:"))
b=a*1.4+32
print("{} °C = {} °F".format(a,b))

num=int(input("biror son kiriting:"))
if num%2==0:
    print("Bu son juft.")
else:
    print("Bu son toq.")
    
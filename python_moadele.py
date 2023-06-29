def moaadele(a,b,c):
    delta = (b**2)-4*a*c
    x_1= (-b + (delta**0.5))/2*a
    x_2= (-b - (delta**0.5))/2*a
    print("x1 is",int(x_1),'\n')
    print("x2 is",int(x_2),"\n")

print("Please Enter a , b and c")

a = int(
    input()
    )

b = int(
    input()
    )

c = int(
    input()
    )

delta = (b**2)-4*a*c

x_1= (-b + (delta**0.5))/2*a


x_2= (-b - (delta**0.5))/2*a


delta = (b**2)-4*a*c

result_1 = "{0} + {1} {2}".format(-b , "radical" , delta)

result_2 = "{0} - {1} {2}".format(-b , "radical" , delta)

result_list = str(result_1)
makhraj_length = len(result_list)/2 - 2
makhraj = 2*a

if delta < 0:
    print("rishe nadarad\n")
elif delta == 0:
    print("1 rishe darad\n")
    moaadele(a,b,c)
    print(result_1)
    print("-"*len(result_list))
    print(" "*int(makhraj_length), makhraj,'\n')
else:
    moaadele(a,b,c)

    print("agar aashari va gong bood adad =>> \n")


    print(result_1)
    print("-"*len(result_list))
    print(" "*int(makhraj_length), makhraj,'\n')
    print("and\n")
    print(result_2)
    print("-"*len(result_list))
    print(" "*int(makhraj_length), makhraj)


# This program creates loop to execute 100 times displaying "Fizz" for numbers divisible by 5, "Bizz" for numbers divisible by 8, "FizzBizz" for numbers divisible by both 5 and 8 as well as all the numbers(N).
# It is written from October 19, 2023 - November 1, 2023
# By Benjamin Osemene and Anmrew Ohwoka


# Program required inputs
Fizz= input("Enter the number divisible by 5:  ")
Bizz= input("Enter the number divisible by 8:  ")
FizzBizz= input("Enter the number divisible by 5 and 8:  ")



for N in range(1,101):
    if N % 5==0:
        print("Fizz" )
    elif N % 8==0:
        print("Bizz")
    elif ((N % 5==0) and (N % 8==0)):
        print("FizzBizz")
    else:
        print(N)



    

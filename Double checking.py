num = int(input("Enter number to check: "))  

if num > 50:  
    print("Number is greater than 50")  
    if num % 2 == 0:  
        print("And it is an even number")  
    else:  
        print("And it is an odd number")  
else:  
    print("The number is less than or equal to 50")  

def positive_factorial(num_desire_fact):
    # Factorial of n denoted n! = n(n-1)*****(n-1); (n-1) !=0 
    fac = 1
    if num_desire_fact > 0 and not num_desire_fact < 0: # Check for ensuring positive values 
        for num_desire_fact in range(0, num_desire_fact+1):
            fac*= (num_desire_fact+1)
        return fac
    elif num_desire_fact == 0: # 0! = 1
        return 1
    else:
        return ValueError #when input number is negatively, output is does not exit

if __name__ == "__main__":
    num_desire_fact = int(input("Please type the number that desires to evaluate its factorial: "))
    print(positive_factorial(num_desire_fact))

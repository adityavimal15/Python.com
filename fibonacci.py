def fibonacci_series(n):
    a,b=0,1
    if n<=0:
        print("Please enter a positive number.")
    elif n==1:
        print(a)
    else:
        print("Fibonacci Series:")
        for _ in range(n):
            print(a,end="")
            a,b=b, a+b
num_of_terms=int(input("Enter the number of terms:"))
fibonacci_series(num_of_terms)
def print_pyramid(n):
    for i in range(1,n+1):
        print(' '*(n-i),end=' ')
        print('* '*i)
num_of_rows= int(input("Enter the number of rows:"))
print_pyramid(num_of_rows)
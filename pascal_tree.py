def print_pascal_triangle(n):
    for i in range(n):
        row=[1]*(i+1)
        for j in range(1,i):
            row[j]=triangle[i-1][j-1]+triangle[i-1][j]
        triangle.append(row)
        print(' '*(n-i),' '.join(map(str,row)))
num_of_rows=int(input("Enter the number of rows:"))
triangle=[]
print_pascal_triangle(num_of_rows)    
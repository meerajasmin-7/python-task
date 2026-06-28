n=4
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()

    n=5
for i in range(1,n+1):
    for j in range(1,i+1):
      print("* ",end="")
    print()

    n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
      print("* ",end="")
    print()

    n=4
m=8
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()

    n=8
m=4
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()

    n=3
for i in range(n):
    for j in range(n):
        print(i,j,end="  ")
    print()

    n=3
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()

    n=3
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

    n=3
val=1
for i in range(n):
    for j in range(n):
        print(val,end=" ")
        val+=1
    print()

    n=3
for i in range(n):
    val=1
    for j in range(n):
        print(val,end=" ")
        val+=1
    print()

n=4
val=1
for i in range(1,n+1):
    for j in range(i):
        print(val,end=" ")
        val+=1
    print()

    n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

    n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print((i+j)%2,end=" ")
    print()

for ch in range(26):
    print(chr(ch+65))

for ch in range(26):
    print(chr(ch+97))

    n=5
for i in range(n):
    val=65
    for j in range(1,i+1):
        print(chr(val),end=" ")
        val+=1
    print()

    n=5
for i in range(n,0,-1):
    val=65
    for j in range(1,i+1):
        print(chr(val),end=" ")
        val+=1
    print()

    n=3
val=65
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
    print()

    n=3
for i in range(n):
    val=65
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
    print()

    n=4
m=4
val=97
for i in range(n):
    for j in range(n):
        print(chr(val),end=" ")
        val+=1
    print()

x=5
for i in range(x):
    for j in range(x):
        print("*",end=" ")
    print()
    x=5
for i in range(x):
    for j in range(x):
        if (i==0 or j==0):
           print("*",end=" ")
    print()

    # empty square

x=5
for i in range(x):
    for j in range(x):
        if (i==0 or j==0 or i==x-1 or j==x-1):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    # empty rectangle

n=4
m=8
for i in range(n):
    for j in range(m):
        if (i==0 or j==0 or i==n-1 or j==m-1):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    n = 5
for i in range(n):
    for j in range(i + 1):
        if j==0 or i==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n = 5
for i in range(n-1,-1,-1):
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n = 5
for i in range(n):
    for j in range(i + 1):
        if j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(i+1):
        if j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    count=0
n = int(input())
for i in range(n-1,-1,-1):
    for j in range(i+1):
            print("*", end=" ")
            count+=1
    print()
print(count)

n=5
for i in range(n):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n-i):
            print(" ", end=" ")
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n=5
for i in range(n-1,-1,-1):
    for j in range(n-i):
            print(" ", end=" ")
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n-i):
            print(" ", end=" ")
    for j in range(i+1):
        if j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(n-i):
            print(" ", end=" ")
    for j in range(i+1):
        if j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
        if j==0 or i==n-1 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
        if j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
        if j==0 or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
            print("*", end=" ")
    print()

    n=5
for i in range(n-1,-1,-1):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
            print("*", end=" ")
    print()

    n=5
for i in range(n):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
            print("*", end=" ")
    print()
for i in range(n,-1,-1):
    for j in range(n-i):
            print(" ", end="")
    for j in range(i+1):
            print("*", end=" ")
    print()

    n=4
m=3
for i in range(n):
    for j in range(m):
        print("*",end=" ")
    print()

    n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

    n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

    n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

n=6
for i in range(n):
    val=65
    for j in range(1,i+1):
        print(chr(val),end=" ")
        val+=1
    print()

    n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

    n=5
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

    n=5
val=1
for i in range(1,n+1):
    for j in range(i):
        print(val,end=" ")
        val+=1
    print()


    n=5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
       

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

    n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()

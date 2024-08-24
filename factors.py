def factors(n):
    print("The factors",n,"are: ")

    for i in range(1,n+1):
        if n%i==0:
            print(i)

n=int(input("Enter you number to find factors: "))

factors(n)


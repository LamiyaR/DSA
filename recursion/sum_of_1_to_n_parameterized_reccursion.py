def func(sum,i,n):
    if i>n:
        print (sum)
        return 1
    func(sum+i, i+1, n)

x = func(0,1,4)
print(x)
    
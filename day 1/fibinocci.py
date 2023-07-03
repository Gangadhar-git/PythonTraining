#series
def fibinocci(n):
    sum=0
    res=1
    l=[0,1]
    for i in range(2,n):
        r=sum+res
        l.append(r)
        sum=res
        res=r
    return l
n=int(input())
print(fibinocci(n))
## nth term

def fib(a):
    if a<0:
        return False
    elif a==1:
        return 0
    elif a==2:
        return 1

    return fib(a-1)+fib((a-2))
a=int(input())
print(fib(a))




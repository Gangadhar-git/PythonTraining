def sum_dig(n):
      l=[]
      sum=0
      while(n>0):
          rem=n%10
          l.append(rem)
          n=n//10
          sum=sum+rem
          l=l[::-1]
      for i in range(len(l)):
          print(l[i])

      return sum
n=int(input())
print(sum_dig(n))
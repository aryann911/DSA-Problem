class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            temp=n
            mul=1
            while mul !=0 and temp>0:
                mul*=temp%10
                temp//=10
            if mul%t==0:
                return n
                
            n+=1



        
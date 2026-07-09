import sys
# sys.stdin=open("input.txt", "r")

N,K = map(int,input().split())

a = list(map(int, input().split()))

result = set()

for i in range(N) :
    for j in range(i+1,N):
        for k in range(j+1,N):
            result.add(a[i]+a[j]+a[k])
            
res = sorted(result,reverse = True)

print(res[K-1])
    


from sys import stdin
input = stdin.readline

t = int(input())
answer = []
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    
    if n>2*k:
        ans = "NO"
    else:
        b = [0]*100
        ans = "YES"
        for i in range(n):
            b[a[i]-1]+=1
        for i in range(100):
            if b[i]>2:
                ans = "NO"
                break

    answer.append("Case #" + str(_+1) + ": " + str(ans) + "\n")

file1 = open('outputA.txt', 'w')
file1.writelines(answer)
file1.close()
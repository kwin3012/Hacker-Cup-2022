from sys import stdin
input = stdin.readline

f = open("input.txt", "r")
t = int(f.readline())

# t = int(input())
mod = 10**9 + 7  

answer = []

a = [[(abs(i-j)**2)%mod for i in range(3001)] for j in range(3001)]
for _ in range(t):
    # n = int(input())
    n = int(f.readline())
    a1 = [0]*3001
    a2 = [0]*3001
    b1 = [0]*3001
    b2 = [0]*3001
    
    for i in range(n):
        x,y = map(int,f.readline().split())
        b1[x]+=1
        b2[y]+=1

    
    for i in range(3001):# for all 1-d points calculate the distance of all trees from it.
        c1 = 0
        c2 = 0
        for j in range(3001):
            c1 += (a[i][j]*b1[j])%mod
            c2 += (a[i][j]*b2[j])%mod
        a1[i] = c1
        a2[i] = c2   
    
    q = int(f.readline())
    ans = 0
    for i in range(q):
        x,y = map(int,f.readline().split())
        ans += (a1[x] + a2[y])%mod
    
    ans = ans%mod
    answer.append("Case #" + str(_+1) + ": " + str(ans) + "\n")
        

file1 = open('outputB1.txt', 'w')
file1.writelines(answer)
file1.close()

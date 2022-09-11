from sys import stdin
input = stdin.readline

k = open("watering_well_chapter_2_input.txt", "r") 
mod = 10**9 + 7

answer = []
t = int(k.readline())
for _ in range(t):
    n = int(k.readline())
    a1 = []
    a2 = []
    for i in range(n):
        x,y = map(int,k.readline().split())
        a1.append(x)
        a2.append(y)
        
    s3 = sum(a1)%mod
    s4 = sum(a2)%mod
    s1 = 0
    s2 = 0
    for i in range(n):
        s1 += (a1[i]**2)%mod
        s2 += (a2[i]**2)%mod
    
    ans = 0 
    q = int(k.readline())
    for i in range(q):
        x,y = map(int,k.readline().split())
        ans +=  ((s1 + n*x**2 - 2*x*s3) + (s2 + n*y**2 - 2*y*s4))%mod
        
    ans = ans%mod
    answer.append("Case #" + str(_+1) + ": " + str(ans) + "\n")


f1 = open('outputB2.txt', 'w')
f1.writelines(answer)
f1.close()

        
        
    
    
    
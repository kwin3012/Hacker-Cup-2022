from sys import stdin
input = stdin.readline

t = int(input())
answer = []
for _ in range(t):
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        b = input().strip()
        a.append(b)
    
    ans = "Impossible"
    c = []
    if n==1:
        if a[0].count("^") == 0:
            ans = "Possible"
            c = a
    elif m==1:
        count = 0
        for i in range(n):
            if a[i][0] == "^":
                count += 1
        if count == 0:
            ans = "Possible"
            c = a
    else:
        ans = "Possible"
        for i in range(n):
            c.append("^"*m)
         
    answer.append("Case #" + str(_+1) + ": " + str(ans) + "\n")
    if ans == "Possible":
        for i in range(n):
            answer.append(str(c[i]) + "\n")

file1 = open('outputB.txt', 'w')
file1.writelines(answer)
file1.close()
    
    
        
        
                
        
    
    
    
   
        
    
    

from sys import stdin
input = stdin.readline
    
f = open("consecutive_cuts_chapter_1_input.txt", "r")
t = int(f.readline())
answer = []

for _ in range(t):
    n,k = map(int,f.readline().split())
    a = list(map(int,f.readline().split()))
    b = list(map(int,f.readline().split()))
    
    ind = -1
    for i in range(n):
        if b[i] == a[0]:
            ind = i
            break 
    
    count = 0
    for i in range(n):
        if a[i] == b[(ind+i)%n]:
            count+=1
    p = 0
    if count == n:
        if n == 2:
            if ind:
                if k%2==1:
                    p = 1
            else:
                if k%2==0:
                    p = 1
        else:
            if ind:
                if k:
                    p = 1
            else:
                if k != 1:
                    p = 1
                
    if p:
        ans = "YES"
    else:
        ans = "NO"

    answer.append("Case #" + str(_+1) + ": " + ans + "\n")
        

f1 = open('outputA1.txt', 'w')
f1.writelines(answer)
f1.close()

        
        
            
        
    
            
        
        
        
    
    
    
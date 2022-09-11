# The submission got wrong answer verdict.

from sys import stdin
input = stdin.readline
    
mod = 10**9 + 7
f = open("consecutive_cuts_chapter_2_input.txt", "r")
t = int(f.readline())
answer = []
for _ in range(t):
    n,k1 = map(int,f.readline().split())
    a = list(map(int,f.readline().split()))
    b = list(map(int,f.readline().split()))
    
    d1 = {}
    d2 = {}
    for i in range(n):
        if a[i] not in d1:
            d1[a[i]] = [i]
        else:
            d1[a[i]].append(i)
        
        if b[i] not in d2:
            d2[b[i]] = [i]
        else:
            d2[b[i]].append(i)
    
    cc = 0
    for k in d1.keys():
        v1 = []
        v2 = []
        for i in range(1,len(d1[k])):
            v1.append(d1[k][i]-d1[k][i-1]-1)
        v1.append(n-1-d1[k][-1] + d1[k][0])
        
        for i in range(1,len(d2[k])):
            v2.append(d2[k][i]-d2[k][i-1]-1)
        v2.append(n-1-d2[k][-1] + d2[k][0])
        
        v1.sort()
        v2.sort()
        
        c = 0
        for i in range(len(d1[k])):
            if v1[i] == v2[i]:
                c+=1
        
        if c == len(d1[k]):
            cc+=1
        else:
            break
    
    if cc == len(d1.keys()):
        possible = 1
        
    e = 0
    for k in d1.keys():
        if len(d1[k]) == 1:
            ind1 = d1[k][0]
            ind2 = d2[k][0]
            break
            
    for i in range(n):
        if a[(ind1+i)%n] == b[(ind2+i)%n]:
            e+=1
    
    if e == n:
        possible = 1
    else:
        possible = 0
            
    ind = 1
    count = 0
    for i in range(n):
        if a[i] == b[i]:
            count+=1
    if count == n:
        ind = 0
        
    p = 0
    if possible:
        if n == 2:
            if a[0] == a[1]:
                 p = 1
            else:
                if ind:
                    if k1%2==1:
                        p = 1
                else:
                    if k1%2==0:
                        p = 1
        else:
            if ind:
                if k1:
                    p = 1
            else:
                if k1 != 1:
                    p = 1
                
    if p:
        ans = "YES"
    else:
        ans = "NO"
        
    answer.append("Case #" + str(_+1) + ": " + ans + "\n")
        
f1 = open('outputA2.txt', 'w')
f1.writelines(answer)
f1.close()

            
        
        
            
        
    
            
        
        
        
    
    
    
from sys import stdin
input = stdin.readline

def helper(p,q,x,y):
    c = [0]*26
    d = [0]*26
    for i in range(26):
        c[i] = b[i][q] - b[i][p-1] 
    for i in range(26):
        d[i] = b[i][y] - b[i][x-1] 

    count = 0
    for i in range(26):
        if c[i] != d[i]:
            count+=1
            
    if count == 1:
        return 1
    
    return 0

f = open("perfectly_balanced_chapter_1_input.txt", "r")
t = int(f.readline())
answer = []
for _ in range(t):
    s = f.readline().strip()
    n = len(s)
    b = [ [0 for i in range(n+1)] for j in range(26)]
    
    for i in range(n):
        o = ord(s[i])-97
        b[o][i+1] = b[o][i] + 1
        for j in range(26):
            if o != j:
                b[j][i+1] = b[j][i]
        
    ans = 0
    q = int(f.readline())
    for i in range(q):
        l,r = map(int,f.readline().split())
        if (l-r+1)%2 == 1:
            e = r-l
            c = helper(l,l+e//2-1,l+e//2,r)
            d = helper(l,l+e//2,l+e//2 + 1,r)
            if c|d:
                ans+=1

    answer.append("Case #" + str(_+1) + ": " + str(ans) + "\n")
        

f1 = open('outputA1.txt', 'w')
f1.writelines(answer)
f1.close()

        
        
            
        
    
            
        
        
        
    
    
    
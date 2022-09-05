from sys import stdin
input = stdin.readline

t = int(input())
answer = []
for _ in range(t):
    s = input().strip()
    n = len(s)
    d = {
            "A":True,
            "E":True,
            "I":True,
            "O":True,
            "U":True,
        }
    
    v = 0
    e = {}
    f = {}
    for i in range(n):
        if d.get(s[i]) is not None:
            v+=1
            if s[i] not in e:
                e[s[i]]=0
            e[s[i]]+=1
        else:
            if s[i] not in f:
                f[s[i]]=0
            f[s[i]]+=1
    vv = 0
    cc = 0
    if len(e.values())>0:
        vv = max(e.values())
    if len(f.values())>0:
        cc = max(f.values())
    
    a1 = (v-vv)*2 + n-v
    a2 = (n-v-cc)*2 + v
    
    ans = min(a1,a2)
    answer.append("Case #" + str(_+1) + ": " + str(ans) + "\n")

file1 = open('myfile.txt', 'w')
file1.writelines(answer)
file1.close()

# with open("sample_output5.txt", "a") as file:
#     file.write("Case #" + str(_+1) + ": " + str(ans) + "\n")
# file.close()
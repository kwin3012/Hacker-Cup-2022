from sys import stdin
input = stdin.readline

from queue import Queue

t = int(input())
answer = []
for _ in range(t):
    s = input().strip()
    n = len(s)
    k = int(input())
    d = {}
    for i in range(k):
        ab = input().strip()
        ai = ab[0]
        bi = ab[1]
        if ai not in d:
            d[ai] = []
        d[ai].append(bi)

    dis = [[-1 for i in range(26)] for j in range(26)]
    for i in range(26):
        dis[i][i] = 0

    for i in range(65,91):
        root = chr(i)
        if d.get(root) is not None:
            q = Queue()
            vis = [0 for i in range(26)]
            q.put([root,0])
            vis[i-65] = 1
            while(q.empty() is not True):
                li = q.get()
                node = li[0]
                level = li[1]

                if d.get(node) is not None:
                    for ele in d[node]:
                        if ele != node:
                            if vis[ord(ele)-65] == 0:
                                vis[ord(ele)-65] = 1
                                q.put([ele,level+1])
                                if dis[i-65][ord(ele)-65] == -1:
                                    dis[i-65][ord(ele)-65] = level+1

    
    ans = 10**20
    for i in range(65,91):
        p = 1
        curr = 0
        for j in range(n):
            if dis[ord(s[j])-65][i-65] == -1:
                p = 0
                break
            else:
                curr += dis[ord(s[j])-65][i-65]
        if p:
            ans = min(ans,curr)
    
    if ans == 10**20:
        ans = -1

    answer.append("Case #" + str(_+1) + ": " + str(ans) + "\n")

file1 = open('output2.txt', 'w')
file1.writelines(answer)
file1.close()

# with open("sample_output5.txt", "a") as file:
#     file.write("Case #" + str(_+1) + ": " + str(ans) + "\n")
# file.close()
def check(arr,k):
    count = 0
    for i in arr:
        if (i>k):
            count+=1
    return count

t = int(input())
h = []
li = []

for i in range(t):
    p,k = map(int,input().split())
    h.append(k)
    people = list(map(int,input().split()))
    li.append(people)

for i in range(t):
    print(check(li[i],h[i]))


n, m, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]


cnt = int(m/(k+1))*k
cnt += m%(k+1)

res = 0
res += cnt*first
res += (m-cnt)*second

print(res)
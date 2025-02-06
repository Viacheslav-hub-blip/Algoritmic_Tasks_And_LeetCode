n  = int(input())
a  = [int(x) for x in input().split()]
q  = int(input())

requests = []
for i in range(q):
    request = [int(x) for x in input().split()]
    requests.append(request)

print(requests)

prefix_sum  = [0]

for i in range(1, n+1):
    prefix_sum.append(prefix_sum[i-1] + a[i-1])
print(prefix_sum)

requests_res  = []

for request in requests:
    requests_res.append(prefix_sum[request[1]] - prefix_sum[request[0]])

print(requests_res)

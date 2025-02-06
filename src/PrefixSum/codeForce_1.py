n  = int(input())
a  = [int(x) for x in input().split()]

prefix_sum = [0]

for i in range(1, n+1):
    prefix_sum.append(prefix_sum[i-1] + a[i-1])

print(" ".join([str(x) for x in prefix_sum]))
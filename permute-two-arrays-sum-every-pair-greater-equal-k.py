def helper(a, b, n, k):
    a=sorted(a,reverse=True)
    b=sorted(b)
    for i in range(n):
        if (a[i] + b[i] < k):
            return False
    return True

a = [2, 1, 3]
b = [7, 8, 9]
k = 10
n = len(a)

if(helper(a, b, n, k)):
    print("Yes")
else:
    print("No")
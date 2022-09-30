import time

def sum_of_n(n: int):
    if n > int(10**25):
        return 0

    if n % 2 == 0:
        return int((n+1)*n//2)

    else:
        return int((n+1)//2*n + (n+1)//2)



a = int(input())

print("Input  {0}".format(a))
start = time.time()
print("Output {0}".format(sum_of_n(a)))


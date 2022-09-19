## Add code below with answer clearly stated
def fect(n):
    if n==1:
        return 1
    else:
        return n*(fect(n-1))

print(sum([int(x) for x in str(fect(100))]))       
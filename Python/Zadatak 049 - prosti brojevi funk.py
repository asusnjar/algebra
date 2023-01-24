n = int(input ('Koliko brojeva: '))

def prosti(n):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return n
    return n

print (prosti(n))
n = int(input("Enter a number: "))
res = ""

if n > 999:
    part = str(n % 1000) 
    if len(part) < 3 and n > 0: 
        part = "0" * (3 - len(part)) + part
    res = part + "," + res 
    n = n // 1000

while n > 0:
    part = str(n % 100)
    if len(part) < 2 and n > 0: 
        part = "0" * (2 - len(part)) + part
    res = part + "," + res
    n = n // 1000

print(res.rstrip(","))  
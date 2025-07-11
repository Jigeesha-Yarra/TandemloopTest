def generate_series(a,series):
    if a%2 == 0:
        a -= 1 
    current = 1
    while current <= a:
        series.append(current)
        a += 1
        current += 2 
    return series

a = int(input("Enter input: "))
result = generate_series(a,[])
print(', '.join(map(str, result)))

def print_series(a,series):
    c = 0
    i = 1
    while c < a:
        series.append(i)
        i += 2
        c += 1
    return series 

a = int(input("Enter input: "))
result = print_series(a,[])
print(', '.join(map(str,result))) 
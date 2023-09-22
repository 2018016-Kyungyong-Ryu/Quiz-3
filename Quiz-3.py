score = [90, 45, 64, 9, 17, 29]
results = []
for i in score:
    if i>=71:
        results.append('A')
    elif 71> i >=41:
        results.append('B')
    elif 41> i >=11:
        results.append('C')
    else:
        results.append('D')
print(results)

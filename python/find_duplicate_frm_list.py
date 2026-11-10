test_cases = [
    "TC101", "TC102", "TC103",
    "TC101", "TC104", "TC102",
    "TC105", "TC101"
]

results = []

for i in range(len(test_cases)):
    for j in range(i+1, len(test_cases)):

        if test_cases[i] == test_cases[j]:

            if test_cases[i] not in results:
                results.append(test_cases[j])

print(results)
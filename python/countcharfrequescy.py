message = "automation"
dic = {}
# count = 1
for i in range(len(message)):

    if message[i] not in dic:
        count = 1

        for j in range(i + 1, len(message)):
            if message[i] == message[j]:
                count += 1

        dic[message[i]] = count

print(dic)
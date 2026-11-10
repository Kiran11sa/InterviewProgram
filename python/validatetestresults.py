results = [
    {"test_id": "TC101", "status": "PASS"},
    {"test_id": "TC102", "status": "FAIL"},
    {"test_id": "TC103", "status": "PASS"},
    {"test_id": "TC104", "status": "SKIP"},
    {"test_id": "TC105", "status": "FAIL"},
    {"test_id": "TC106", "status": "PASS"}
]
dic = {'PASS':0,'FAIL':0,'SKIP':0}
# fail = 0
for i in results:
  status = i['status']
  dic[status] += 1
  # print(i)
  # print((i['status']).count('FAIL'))
  # if i['status'] == 'FAIL':
  #   fail += 1
  #   if i['status'] not in dic:
  #     dic[i['status']] = fail
print(dic)
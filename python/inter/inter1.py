import pandas as pd
# reading csv
df = pd.read_csv('inter.csv')
# print("##############",df)
for index,row in df.iterrows():
    print(row['name'],row['age'],row['company'])
# writing into csv
data = {
    'name':['bala'],
    'age':['35'],
    'company':['abc']
}
df = pd.DataFrame(data)
df.to_csv('inter.csv',mode='a',header=False,index=False)
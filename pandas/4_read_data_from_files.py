import pandas as pd 

result = pd.read_csv('marks.csv').squeeze()
print(result)
key = print("Press enter to continue")
result = pd.read_excel('marks.xlsx').squeeze()
print(result)
key = print("Press enter to continue")

result = pd.read_json('marks.json').squeeze()
print(result)
key = print("Press enter to continue")

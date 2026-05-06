import pandas as pd 
import numpy as np 

list = [1,2,3,4,5]

#create series 
s1 = pd.Series(list)
print(s1)

s1 = pd.Series(list,index=['ram','shiv','krishna','hanuman','ganesh'])
print(s1)

state_ranks = {'Alaska': 1, 'Texas': 2, 'California': 3, 'Montana': 4, 'New Mexico': 5, 'Arizona': 6, 'Nevada': 7, 'Colorado': 8, 'Oregon': 9, 'Wyoming': 10, 'Michigan': 11, 'Minnesota': 12, 'Utah': 13, 'Idaho': 14, 'Kansas': 15, 'Nebraska': 16, 'South Dakota': 17, 'Washington': 18, 'North Dakota': 19, 'Oklahoma': 20, 'Missouri': 21, 'Florida': 22, 'Wisconsin': 23, 'Georgia': 24, 'Illinois': 25, 'Iowa': 26, 'New York': 27, 'North Carolina': 28, 'Arkansas': 29, 'Alabama': 30, 'Louisiana': 31, 'Mississippi': 32, 'Pennsylvania': 33, 'Ohio': 34, 'Virginia': 35, 'Tennessee': 36, 'Kentucky': 37, 'Indiana': 38, 'Maine': 39, 'South Carolina': 40, 'West Virginia': 41, 'Maryland': 42, 'Hawaii': 43, 'Massachusetts': 44, 'Vermont': 45, 'New Hampshire': 46, 'New Jersey': 47, 'Connecticut': 48, 'Delaware': 49, 'Rhode Island': 50}

#create series
s3 = pd.Series(state_ranks)
print(s3)


array1 = np.array([10,20,30.45,40,50.25])
#create series
s4 = pd.Series(array1,index=['ram','shyam','mohan','geeta','sita'],name='salary')
print(s4)
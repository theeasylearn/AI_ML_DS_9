import pandas as pd 

# Create Series using Dictionary 
punjab_batters_scores = {
    "Priyansh Arya": 1,
    "Prabhsimran Singh": 3,
    "Cooper Connolly": 107,
    "Shreyas Iyer": 5,
    "Marcus Stoinis": 28,
    "Suryansh Shedge": 25,
    "Shashank Singh": 4,
    "Marco Jansen": 19,
    "Vijaykumar Vyshak": -1  # Fixed the negative value
}

s1 = pd.Series(punjab_batters_scores)
print(s1)
print(s1.abs())
print(s1.idxmax(),s1.max())
print(s1.idxmin(),s1.min())
print(s1.sort_values())
print(s1.sort_index())
print("no of values",len(s1))
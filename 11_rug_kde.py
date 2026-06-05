import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd 
import numpy as np 

# Load dataset 
sachin = pd.read_csv('sachin.csv')

plt.figure(figsize=(18, 6))

# Fix: Manually add a small amount of uniform noise to 'Age' 
# This prevents lines from drawing exactly on top of each other
jittered_age = sachin['Age'] + np.random.uniform(-0.25, 0.25, size=len(sachin))

sns.rugplot(x=jittered_age, height=0.3, alpha=0.6, linewidth=1.5)
sns.kdeplot(x=jittered_age,data=sachin,alpha=0.5,color='yellow',fill=True)

plt.xlabel('Age')
plt.title('Sachin Century Data (with Manual Jitter)')
plt.xlim(15, 40)
plt.xticks(ticks=np.arange(15, 40))
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
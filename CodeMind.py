import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#This is the example of the barplot
categories = ['A','B','C','D','E','F']
values = np.random.randint(25,85,6)

plt.bar(categories, values, color='Purple')
plt.title("Bar Plot Example")
plt.xlabel("categories")
plt.ylabel("values")
plt.show()

data = {'Name': ['Omar','Fakhar','Babar','Rizwan','Shaheen','Naseem'],
        'Age': np.random.randint(25,35,6),
        'Salary': np.random.randint(40000,80000,6),
        'Performance Score': np.random.uniform(1.0,5.0,6),
        }
df = pd.DataFrame(data)
df.head()

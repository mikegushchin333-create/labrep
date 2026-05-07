import pandas
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris(as_frame=True)
df = iris.frame
df['species'] = iris.target_names[iris.target]
color={'setosa':'red', 'versicolor':'blue', 'virginica':'green'}
plt.figure(figsize=(8,6))
plt.style.use('seaborn-v0_8-whitegrid')
for species, color in color.items():
    subset = df[df['species']== species] 
    plt.scatter(subset['sepal width (cm)'],
                subset['sepal length (cm)'],
                color=color,
                s=80,
                alpha = 0.8,
                label=species)
plt.xlabel('sepal length (cm)', fontsize = 10)
plt.ylabel('sepal width (cm)', fontsize = 10)
plt.title('blabla', fontsize = 15)
plt.grid(True, linestyle = '--', alpha = 0.5)
plt.show()
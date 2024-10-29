import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example data, replace this list with your actual data
data = {'p1_p2': [1.2, 2.1, 3.3, 2.2, 1.7, 2.8, 3.0, 1.9, 2.5, 2.7]}
df = pd.DataFrame(data)

# Plot the density
plt.figure(figsize=(10, 6))
sns.kdeplot(df['p1_p2'], shade=True)
plt.title('Density Plot of p1_p2')
plt.xlabel('p1_p2')
plt.ylabel('Density')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Plotting a boxplot of Dx_QTc grouped by Large_genogroup
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='Large_genogroup', y='Dx_QTc')
plt.title('Distribution of Dx_QTc by Large Genogroup')
plt.xlabel('Large Genogroup')
plt.ylabel('Dx_QTc')
plt.xticks(rotation=45)
plt.show()


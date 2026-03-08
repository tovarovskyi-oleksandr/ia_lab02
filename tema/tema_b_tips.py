import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Încărcarea dataset-ului demo din Seaborn [cite: 314, 477]
tips = sns.load_dataset('tips')

# 2. Explorarea datelor cu Pandas [cite: 483, 493]
print("=== Primele 5 înregistrări ===")
print(tips.head())

print("\n=== Informații generale despre dataset ===")
tips.info()

print("\n=== Statistici descriptive (coloane numerice) ===")
print(tips.describe())

# 3. Analiza agregată (Media notei de plată și a bacșișului pe zi) [cite: 264]
print("\n=== Media consumului și a bacșișului pe zi ===")
media_per_zi = tips.groupby('day', observed=True)[['total_bill', 'tip']].mean()
print(media_per_zi)

# 4. Vizualizarea datelor cu Seaborn [cite: 300]
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle('Analiza Exploratorie Dataset Tips', fontsize=16, fontweight='bold')

# Subplot 1: Relația dintre total_bill și tip, colorată după sex [cite: 273, 107]
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', ax=axes[0])
axes[0].set_title('Relația Nota de plată vs Bacșiș (per Sex)')
axes[0].set_xlabel('Total Bill ($)')
axes[0].set_ylabel('Tip ($)')

# Subplot 2: Distribuția bacșișului în funcție de zi (Boxplot) [cite: 126]
sns.boxplot(data=tips, x='day', y='tip', order=['Thur', 'Fri', 'Sat', 'Sun'], palette='Set2', ax=axes[1])
axes[1].set_title('Distribuția Bacșișului per Zi')
axes[1].set_xlabel('Ziua Săptămânii')
axes[1].set_ylabel('Bacșiș ($)')

# Salvarea și afișarea rezultatelor [cite: 161]
plt.tight_layout()
plt.savefig('tema_b_analiza_tips.png', dpi=150)
plt.show()

# 5. Interpretare scurtă (Bonus)
print("\nInterpretare: Se observă o corelație pozitivă între valoarea notei de plată și bacșiș.")
print("Zilele de sâmbătă și duminică tind să aibă valori mai mari pentru nota de plată.")
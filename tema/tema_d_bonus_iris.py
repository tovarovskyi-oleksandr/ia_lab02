import seaborn as sns
import matplotlib.pyplot as plt

# Pregătirea datelor conform laboratorului
# Seaborn include dataset-uri clasice precum Iris
iris = sns.load_dataset('iris')

# --- 1. Generare Pairplot ---
# Pairplot-ul este un instrument esențial în EDA pentru identificarea relațiilor
# Se cere hue='species' și diag_kind='kde'
pair_plot = sns.pairplot(iris, hue='species', diag_kind='kde')
plt.suptitle('Pairplot — dataset Iris', y=1.02) # Titlu cerut

# Salvarea figurii (trebuie apelată înainte de plt.show pentru a nu fi goală)
pair_plot.savefig('iris_pairplot_complet.png', bbox_inches='tight')

# --- 2. Figura separată cu 4 Violinplots (1x4) ---
# Violinplot combină boxplot cu estimarea densității KDE
# Se cere o figură separată cu 4 subploturi pentru fiecare variabilă numerică
fig, axes = plt.subplots(1, 4, figsize=(18, 5))
fig.suptitle('Raport comparativ Iris - Violin Plots', fontsize=16)

features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

for i, feature in enumerate(features):
    # Se cere hue='species' și split=False
    sns.violinplot(data=iris, x='species', y=feature, hue='species', split=False, ax=axes[i])
    axes[i].set_title(feature.replace('_', ' ').title())

# --- 3. Titlu general și salvare ---
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('iris_violinplots.png')

plt.show()
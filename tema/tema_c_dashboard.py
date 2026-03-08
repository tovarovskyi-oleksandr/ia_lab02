# =============================================================
# Dashboard vizualizare - Dataset Tips
# =============================================================

import matplotlib.pyplot as plt
import seaborn as sns

# Tema seaborn
sns.set_theme(style="whitegrid")

# Încărcare dataset
tips = sns.load_dataset("tips")

# Creare figură cu 2x2 subploturi
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle("Dashboard vizualizare — Dataset Tips", fontsize=16, fontweight="bold")

# =============================================================
# 1. Scatter (Matplotlib): total_bill vs tip colorat după sex
# =============================================================

culori = {"Male": "steelblue", "Female": "coral"}

for sex, culoare in culori.items():
    subset = tips[tips["sex"] == sex]
    axes[0, 0].scatter(
        subset["total_bill"],
        subset["tip"],
        label=sex,
        color=culoare,
        alpha=0.7
    )

axes[0, 0].set_title("Total bill vs Tip (colorat după sex)")
axes[0, 0].set_xlabel("Total bill ($)")
axes[0, 0].set_ylabel("Tip ($)")
axes[0, 0].legend()

# =============================================================
# 2. Boxplot (Seaborn): distribuția total_bill per day
# =============================================================

sns.boxplot(
    data=tips,
    x="day",
    y="total_bill",
    order=["Thur", "Fri", "Sat", "Sun"],
    ax=axes[0, 1]
)

axes[0, 1].set_title("Distribuția total_bill per zi")
axes[0, 1].set_xlabel("Zi")
axes[0, 1].set_ylabel("Total bill ($)")

# =============================================================
# 3. Histogramă (Seaborn): distribuția tip cu hue='time'
# =============================================================

sns.histplot(
    data=tips,
    x="tip",
    hue="time",
    kde=True,
    bins=20,
    ax=axes[1, 0]
)

axes[1, 0].set_title("Distribuția bacșișurilor (Lunch vs Dinner)")
axes[1, 0].set_xlabel("Tip ($)")
axes[1, 0].set_ylabel("Frecvență")

# =============================================================
# 4. Barplot (Seaborn): bacșiș mediu per day cu interval CI
# =============================================================

sns.barplot(
    data=tips,
    x="day",
    y="tip",
    order=["Thur", "Fri", "Sat", "Sun"],
    errorbar="ci",
    ax=axes[1, 1]
)

axes[1, 1].set_title("Bacșiș mediu per zi")
axes[1, 1].set_xlabel("Zi")
axes[1, 1].set_ylabel("Tip mediu ($)")

# =============================================================
# Layout + salvare imagine
# =============================================================

plt.tight_layout()
plt.savefig("dashboard_tips.png", dpi=150, bbox_inches="tight")
plt.show()

print("Figura a fost salvată ca 'dashboard_tips.png'")

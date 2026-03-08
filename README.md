# Laborator 02 - Numpy & Pandas

## Structura proiectului

Proiectul este organizat in doua sectiuni principale:

1. **Exercitii individuale (cerinte)**
   - `cerinta_3_1_numpy.py` - Probleme introductive cu Numpy: creare si manipulare de array-uri, operatii aritmetice si statistice.
   - `cerinta_3_2_numpy.py` - Utilizarea functiilor avansate Numpy, cum ar fi broadcasting si indexare complexa.
   - `cerinta_3_3_numpy.py` - Generare de date aleatoare, transformari si evaluarea performantei.
   - `cerinta_3_4_numpy.py` - Aplicatii liniare: matrici, determinanti, sisteme de ecuatii.
   - `cerinta_3_5_numpy.py` - Analiza seriei temporale sau alte seturi de date sintetice.
   - `cerinta_3_6_numpy.py` - Probleme mixte si exercitii finale pentru consolidare.

2. **Tema laboratorului** (directorul `tema/`):
   - `tema_a_numpy.py` - Prima parte: se bazeaza pe cunostintele din exercitiile cu Numpy, implementand un algoritm sau prelucrare de date specifice.
   - `tema_b_tips.py` - A doua parte: poate contine sfaturi si trucuri ("tips") pentru rezolvarea unor probleme frecvente cu Pandas.
   - `tema_c_dashboard.py` - Script care genereaza un dashboard simplu, eventual cu ajutorul bibliotecii `matplotlib` sau `seaborn` pentru vizualizare.
   - `tema_d_bonus_iris.py` - Script optional folosind celebrul set de date Iris pentru clasificare sau analiza.
   - `tema_e_colab.ipynb` - Notebook Google Colab pregatit pentru vizualizare interactiva, utile la prezentarea temei.

- `requirements.txt`: specifica pachetele Python necesare pentru rulare, de regulă `numpy`, `pandas` si eventual biblioteci de vizualizare.

Aceasta structura permite rularea independenta a fisierelor la nevoie si extinderea ulterioara a proiectului cu alte exercitii sau teme.

## Instructiuni de utilizare

1. Cloneaza repository:
   ```bash
   git clone <url-repo>
   cd ia-lab02-numpy-pandas
   ```
2. Creeaza un mediu virtual si instaleaza dependentele:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Ruleaza exercitiile sau scripturile temei:
   ```bash
   python3 cerinta_3_1_numpy.py
   ```
   si altele similare.


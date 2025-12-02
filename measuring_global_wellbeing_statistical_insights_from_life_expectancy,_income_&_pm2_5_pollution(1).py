# -*- coding: utf-8 -*-
"""Measuring Global Wellbeing: Statistical Insights from Life Expectancy, Income & PM2.5 Pollution


!pip install pandas numpy seaborn matplotlib plotly scikit-learn kaggle

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings("ignore")

plt.style.use("seaborn-v0_8")

import pandas as pd

gap_url = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"
gap = pd.read_csv(gap_url)

gap.head()

# keep most recent data per country
gap_recent = gap.sort_values("year").groupby("country").tail(1).reset_index(drop=True)

# create a happiness proxy based on development indicators
gap_recent["happiness_proxy"] = (
    gap_recent["lifeExp"] +
    (gap_recent["gdpPercap"].apply(lambda x: np.log(x+1)))
) / 2

gap_recent.head()

import requests
import pandas as pd

# PM2.5 indicator from the World Bank
pm25_api = "https://api.worldbank.org/v2/country/all/indicator/EN.ATM.PM25.MC.M3?format=json&per_page=20000"
pm_json = requests.get(pm25_api).json()

pm_list = []
for entry in pm_json[1]:
    if entry["value"] is not None:
        pm_list.append([
            entry["country"]["value"],
            entry["date"],
            entry["value"]
        ])

pm25 = pd.DataFrame(pm_list, columns=["country", "year", "pm25"])
pm25 = pm25.sort_values("year").groupby("country").tail(1).reset_index(drop=True)

pm25.head()

# Basic summary statistics

df_stats = gap_recent[["lifeExp", "gdpPercap", "happiness_proxy"]].describe()
df_stats

stats = gap_recent[["lifeExp", "gdpPercap", "happiness_proxy"]].describe().T
stats["cv"] = stats["std"] / stats["mean"]
stats

import seaborn as sns
import matplotlib.pyplot as plt

sns.pairplot(
    gap_recent[["lifeExp", "gdpPercap", "happiness_proxy"]],
    diag_kind="kde",
    plot_kws={"alpha": 0.7}
)
plt.suptitle("Pairwise Relationships Between Key Indicators", y=1.02)
plt.show()

import numpy as np

corr = gap_recent[["lifeExp", "gdpPercap", "happiness_proxy"]].corr()

mask = np.triu(np.ones_like(corr, dtype=bool))

plt.figure(figsize=(7,5))
sns.heatmap(
    corr,
    annot=True,
    cmap="viridis",
    linewidths=0.5,
    mask=mask,
    fmt=".2f"
)
plt.title("Correlation Matrix (Masked Upper Triangle)")
plt.show()

plt.figure(figsize=(14,4))

for i, col in enumerate(["lifeExp", "gdpPercap", "happiness_proxy"]):
    plt.subplot(1, 3, i+1)
    sns.histplot(gap_recent[col], kde=True)
    plt.title(f"Distribution: {col}")

plt.tight_layout()
plt.show()

"""# Key Insights

Life expectancy and GDP per capita show a strong positive correlation (~0.68), consistent with global development theory.

The happiness proxy strongly correlates with both life expectancy (1.00) and GDP per capita (~0.71), confirming that longevity and economic prosperity jointly drive wellbeing.

GDP has the highest coefficient of variation (CV), indicating extreme inequality across countries.

Life expectancy has the lowest CV, showing global convergence driven by medical advancements.

Distributions show GDP is right-skewed, while life expectancy and happiness proxy are more symmetric.
"""

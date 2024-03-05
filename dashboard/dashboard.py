import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def basedOnYear(df):
    data = df[(df['season'] == 2) & (df['holiday'] == 1)]
    return data

def basedOnDays(df):
    data = df[(df['workingday'] == 1) & (df['casual'] > 0)]
    return data

all_df = pd.read_csv("main_data.csv")
datetime_column = ["dteday"]
all_df.sort_values(by="dteday", inplace=True)
all_df.reset_index(inplace=True)

df_based_year = basedOnYear(all_df)
df_based_days = basedOnDays(all_df)

st.header('Bike Dataset')
colors = ['#90CAF9', '#FF7043', '#66BB6A', '#FFD54F']

fig, ax = plt.subplots(figsize=(30, 20))
sns.barplot(
    df_based_year,
    x='yr',
    y='cnt',
    palette=colors
)
ax.tick_params(axis='y', labelsize=40)
ax.tick_params(axis='x', labelsize=45)
ax.set_xlabel('Tahun', fontsize=45)
ax.set_ylabel('jumlah sewa sepeda', fontsize=45)
ax.set_title('Jumlah sewa sepeda per tahun selama musim panas', fontsize=45)
st.pyplot(fig)

sns.barplot(
    df_based_days,
    x='weekday',
    y='casual',
    palette=colors
)
ax.tick_params(axis='y', labelsize=40)
ax.tick_params(axis='x', labelsize=45)
ax.set_xlabel('Hari kerja', fontsize=45)
ax.set_ylabel('jumlah sewa sepeda', fontsize=45)
ax.set_title('Jumlah sewa sepeda bagi pengguna casual saat hari kerja', fontsize=45)
st.pyplot(fig)
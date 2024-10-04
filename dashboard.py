import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='darkgrid')

day_df = pd.read_csv("day.csv")
hour_df = pd.read_csv("hour.csv")

st.title("Bike Sharing Dashboard")

grouped_data = hour_df.groupby(by="season").agg({
    "cnt": "mean"
})

sns.barplot(x='season', y='cnt', data=grouped_data)
plt.xlabel('Cuaca')  
plt.ylabel('Rata-rata penyewaan sepeda') 
st.pyplot(plt)

st.write("Pada visualisasi tersebut, saya dapat melihat bahwa musim 3(fall) cenderung memiliki jumlah penyewaan yang tinggi, diikuti oleh musim 2,4, dan 1")

season_colors = {1: '#e6194B', 2: '#3cb44b', 3: '#ffe119', 4: '#4363d8'}
season_labels = {1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'}

plt.figure(figsize=(12, 6))
for season in [1, 2, 3, 4]:
    sns.regplot(
        x='hum', 
        y='cnt', 
        data=day_df[day_df['season'] == season],
        scatter_kws={'color': season_colors[season], 'label': season_labels[season]},
        line_kws={'color': season_colors[season]},
        label = season_labels[season]
    )

plt.title('Bike Rentals vs Humidity')
plt.xlabel('Humidity (Normalized)')
plt.ylabel('Total Rentals')
plt.legend(title="Season", loc='lower right', fontsize=8)  
st.pyplot(plt)

st.write("Pada musim panas, gugur, dan dingin tingkat kelembapan berbanding terbalik dengan jumlah peminjam sepeda dan pada musim semi cenderung tidak berpengaruh")

season_colors = {1: '#e6194B', 2: '#3cb44b', 3: '#ffe119', 4: '#4363d8'}
season_labels = {1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'}

plt.figure(figsize=(12, 6))
for season in [1, 2, 3, 4]:
    sns.regplot(
        x='temp',  
        y='cnt', 
        data=day_df[day_df['season'] == season],
        scatter_kws={'color': season_colors[season], 'label': season_labels[season]},
        line_kws={'color': season_colors[season]},
        label = season_labels[season]
    )

plt.title('Bike Rentals vs Temperature')
plt.xlabel('Temperature (Normalized)')
plt.ylabel('Total Rentals')
plt.legend(title="Season", loc='lower right', fontsize=8)
st.pyplot(plt)

st.write("Pada musim panas, dingin, dan semi tingkat temperatur berbanding lurus dengan jumlah peminjam sepeda dan pada musim gugur cenderung berbanding terbalik dengan jumlah peminjam sepeda")

season_colors = {1: '#e6194B', 2: '#3cb44b', 3: '#ffe119', 4: '#4363d8'}
season_labels = {1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'}

plt.figure(figsize=(12, 6))
for season in [1, 2, 3, 4]:
    sns.regplot(
        x='atemp',
        y='cnt', 
        data=day_df[day_df['season'] == season],
        scatter_kws={'color': season_colors[season], 'label': season_labels[season]},
        line_kws={'color': season_colors[season]},
        label = season_labels[season]
    )

plt.title('Bike Rentals vs Feeling Temperature')
plt.xlabel('Feeling Temperature (Normalized)')
plt.ylabel('Total Rentals')
plt.legend(title="Season", loc='lower right', fontsize=8)
st.pyplot(plt)

st.write("Pada musim panas, dingin, dan semi tingkat feeling temperatur berbanding lurus dengan jumlah peminjam sepeda dan pada musim gugur cenderung berbanding terbalik dengan jumlah peminjam sepeda")

season_colors = {1: '#e6194B', 2: '#3cb44b', 3: '#ffe119', 4: '#4363d8'}
season_labels = {1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'}

plt.figure(figsize=(12, 6))
for season in [1, 2, 3, 4]:
    sns.regplot(
        x='windspeed',  
        y='cnt', 
        data=day_df[day_df['season'] == season],
        scatter_kws={'color': season_colors[season], 'label': season_labels[season]},
        line_kws={'color': season_colors[season]},
        label = season_labels[season]
    )

plt.title('Bike Rentals vs Windspeed')
plt.xlabel('Windspeed (Normalized)')
plt.ylabel('Total Rentals')
plt.legend(title="Season", loc='lower right', fontsize=8)
st.pyplot(plt)

st.write("Pada musim, panas, dingin, semi, dan gugur tingkat kecepatan angin berbanding terbalik dengan jumlah peminjam sepeda")

peak_weathersit_data = day_df[day_df['weathersit'] == 3]
correlation_matrix = peak_weathersit_data[['cnt','temp','atemp','hum','windspeed']].corr()
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.regplot(x = 'temp', y = 'cnt', data=peak_weathersit_data, line_kws={"color":"orange"})
plt.title('Bike Rentals vs Temperature in Peak Weathersit')
plt.xlabel('Temperature (Normalized)')
plt.ylabel('Total Rentals')
st.pyplot(plt)

st.write("Semakin suhunya meningkat, grafiknya akan semakin naik yang mana itu membuktikan bahwa saat cuaca (Clear, Few clouds, Partly cloudy) semakin banyak orang yang menyewa sepeda")
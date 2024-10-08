# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mTGa7tsdbOZTx786ghwlJemtk1kuCYsa
"""

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('Europe Hotel Booking Satisfaction Score.csv')
df

df.info()

df.describe()

# Analysis 1: Factors that affect cutomers satisfaction
factors = ['Hotel wifi service', 'Departure/Arrival  convenience',
           'Ease of Online booking', 'Hotel location', 'Food and drink',
           'Stay comfort', 'Common Room entertainment',
           'Checkin/Checkout service', 'Other service', 'Cleanliness']
factor_means = df[factors].mean().sort_values(ascending=False)

#Defining the colors of the bar chart
warna = ['#4F3139', '#66424D', '#8F6370', '#B99AA3', '#E0D6D9', '#3E262D',
         '#2E1C21', '#1E1115', '#314F45', '#4F313F']

# Visualisasi Factors that affect cutomers satisfaction
plt.figure(figsize=(10, 6))
sn.barplot(x=factor_means.index, y=factor_means.values, palette=warna)
plt.title('Average level of satisfaction')
plt.xticks(rotation=45)
plt.ylabel('Level of satisfaction')
plt.xlabel(" ")
plt.grid(axis='y')
plt.show()

gender_counts = df['Gender'].value_counts()

#Defining the colors
warna1 = ['#4F3139', '#B99AA3']

# Making chart pie
plt.pie(gender_counts, labels = gender_counts.index,
        colors = warna1, autopct='%1.1f%%')
plt.title('Customer gender comparison')
plt.show()

# Calculating the total satisfaction
df['Total Satisfaction'] = df[['Hotel wifi service',
                               'Departure/Arrival  convenience',
                               'Ease of Online booking', 'Hotel location',
                               'Food and drink', 'Stay comfort',
                               'Common Room entertainment', 'Checkin/Checkout service',
                               'Other service', 'Cleanliness']].mean(axis=1)

# Making scatter plot
sn.scatterplot(x='Age', y='Total Satisfaction', data=df, color = '#8F6370')
plt.xlabel('Age')
plt.ylabel('Total Satisfaction')
plt.title('Scatter Plot: Age vs. Total Satisfaction')
plt.show()

Type_Of_Booking_counts = df['Type Of Booking'].value_counts()

# Making chart pie
plt.pie(Type_Of_Booking_counts, labels = Type_Of_Booking_counts.index,
        colors = warna2, autopct='%1.1f%%')
plt.title('Type Of Booking comparison')
plt.show()

purpose_of_travel_counts = df['purpose_of_travel'].value_counts()

# Defining colors
warna2 = ['#4F3139', '#66424D', '#8F6370', '#B99AA3', '#E0D6D9']

# Making chart pie
plt.pie(purpose_of_travel_counts, labels = purpose_of_travel_counts.index,
        colors = warna2, autopct='%1.1f%%')
plt.title('purpose of travel comparison')
plt.show()

Type_of_Travel_counts = df['Type of Travel'].value_counts()

# Making chart pie
plt.pie(Type_of_Travel_counts, labels = Type_of_Travel_counts.index,
        colors = warna1, autopct='%1.1f%%')
plt.title('Type of Travel comparison')
plt.show()

# Menghitung jumlah pelanggan berdasarkan gender dan kepuasan
gender_satisfaction_counts = df.groupby(['Gender', 'satisfaction']).size().unstack()
print(gender_satisfaction_counts)
# Membuat bar chart
gender_satisfaction_counts.plot(kind='bar', stacked=True, color = warna1)
plt.xlabel('Gender')
plt.ylabel('Jumlah Pelanggan')
plt.title('Perbandingan Kepuasan antara Pelanggan Pria dan Wanita')
plt.legend(title='Satisfaction', loc='upper right')
plt.grid(axis='y')
plt.show()
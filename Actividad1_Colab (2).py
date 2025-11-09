# Actividad 1 - Data Visualization (Google Colab)
# Autor: Sneider Pérez

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('university_student_data (1).csv')
print("Columnas disponibles:", df.columns.tolist())
print(df.head())

# Gráfica 1: Retention Rate Over Time
retention = df.groupby('Year')['Retention Rate (%)'].mean().reset_index()
plt.figure(figsize=(8,4))
plt.plot(retention['Year'], retention['Retention Rate (%)'], marker='o')
plt.title('Retention Rate Over Time')
plt.xlabel('Year')
plt.ylabel('Retention Rate (%)')
plt.grid(True)
plt.show()

# Gráfica 2: Satisfaction by Year
satisfaction = df.groupby('Year')['Student Satisfaction (%)'].mean().reset_index()
plt.figure(figsize=(8,4))
plt.bar(satisfaction['Year'].astype(str), satisfaction['Student Satisfaction (%)'])
plt.title('Average Satisfaction by Year')
plt.xlabel('Year')
plt.ylabel('Student Satisfaction (%)')
plt.show()

# Gráfica 3: Retention by Term
term = df.groupby('Term')['Retention Rate (%)'].mean().reset_index()
plt.figure(figsize=(6,4))
plt.bar(term['Term'].astype(str), term['Retention Rate (%)'])
plt.title('Retention by Term')
plt.xlabel('Term')
plt.ylabel('Retention Rate (%)')
plt.show()

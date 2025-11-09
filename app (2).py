# app.py - versión corregida
# Autor: Sneider Pérez

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="University Dashboard - Sneider Pérez", layout="wide")
st.title("🎓 University Data Dashboard")
st.markdown("### Autor: Sneider Pérez")
st.write("Análisis interactivo de retención, satisfacción y matrícula estudiantil.")

df = pd.read_csv('university_student_data_(1).csv')

# Filtros laterales
year_filter = st.sidebar.multiselect("Selecciona el año:", sorted(df['Year'].unique()))
term_filter = st.sidebar.multiselect("Selecciona el periodo (Term):", sorted(df['Term'].unique()))

filtered_df = df.copy()
if year_filter:
    filtered_df = filtered_df[filtered_df['Year'].isin(year_filter)]
if term_filter:
    filtered_df = filtered_df[filtered_df['Term'].isin(term_filter)]

# Métricas principales
st.subheader("📊 Indicadores Clave")
col1, col2, col3 = st.columns(3)
col1.metric("Average Retention", f"{filtered_df['Retention Rate (%)'].mean():.2f}%")
col2.metric("Average Satisfaction", f"{filtered_df['Student Satisfaction (%)'].mean():.2f}%")
col3.metric("Total Enrolled", int(filtered_df['Enrolled'].sum()))

# Gráficas
st.subheader("📈 Retention Rate Over Time")
retention = filtered_df.groupby('Year')['Retention Rate (%)'].mean().reset_index()
st.line_chart(retention.set_index('Year')['Retention Rate (%)'])

st.subheader("😊 Average Satisfaction by Year")
satisfaction = filtered_df.groupby('Year')['Student Satisfaction (%)'].mean().reset_index()
st.bar_chart(satisfaction.set_index('Year')['Student Satisfaction (%)'])

st.subheader("🗓️ Retention by Term")
term = filtered_df.groupby('Term')['Retention Rate (%)'].mean().reset_index()
st.bar_chart(term.set_index('Term')['Retention Rate (%)'])

st.markdown("---")
st.markdown("**Nota:** Datos visualizados directamente del archivo CSV proporcionado por la Universidad de la Costa.")

# -*- coding: utf-8 -*-
"""Fake news Random Forest

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AhoABT-erzfj1zlMaJ1NWl5tHP0_vi9W
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt

url = "/content/fake_and_real_news.csv"


data = pd.read_csv(url)
print(data.head())

# Paso 3: Separar las características y la variable objetivo
X = data['Text']
y = data['label']

vectorizer = CountVectorizer()
X_transformed = vectorizer.fit_transform(X)

# Convertir las etiquetas en números
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Paso 4: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y_encoded, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Clases en y_test:", set(y_test))
print("Clases en y_pred:", set(y_pred))

report = classification_report(y_test, y_pred, target_names=['Fake', 'No Fake'])
print(report.replace("precision", "Precisión")
              .replace("recall", "Sensibilidad")
              .replace("f1-score", "Puntuación F1")
              .replace("support", "Soporte")
              .replace("accuracy", "Exactitud"))

conf_matrix = confusion_matrix(y_test, y_pred)

# Visualizar la matriz de confusión
plt.figure(figsize=(10, 7))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=model.classes_, yticklabels=model.classes_)
plt.ylabel('Actual')
plt.xlabel('Predicho')
plt.title('Matriz de Confusión')
plt.show()

# Paso 1: Crear el nuevo dato
nuevo_texto = ["Este es un ejemplo de un texto que quiero clasificar."]

# Paso 2: Vectorizar el nuevo texto
nuevo_texto_transformed = vectorizer.transform(nuevo_texto)

# Paso 3: Hacer la predicción
prediccion = model.predict(nuevo_texto_transformed)

# Paso 4: Decodificar la predicción
etiqueta_predicha = label_encoder.inverse_transform(prediccion)

print("El nuevo texto es clasificado como:", etiqueta_predicha[0])
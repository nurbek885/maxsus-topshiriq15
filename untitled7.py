# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nMtXjIQS_VEgAxqb2k4PS-RkGlYGpgwV
"""

import numpy as np
import matplotlib.pyplot as plt

# Sinus funksiyasi uchun ma'lumotlar
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Scatter grafik uchun ma'lumotlar
x_scatter = np.random.uniform(0, 10, 50)
y_scatter = np.random.uniform(0, 10, 50)

# Grafika o'lchamlari
fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Sinus funksiyasi grafigi
axs[0].plot(x, y, color='blue', label='Sinus(x)')
axs[0].set_title("Sinus Funksiyasining Grafiki")
axs[0].set_xlabel("X qiymatlari")
axs[0].set_ylabel("Y qiymatlari")
axs[0].grid(True)
axs[0].legend()

# Scatter grafika
axs[1].scatter(x_scatter, y_scatter, color='purple', label='Nuqtalar')
axs[1].set_title("Tasodifiy Nuqtalar Scatter Grafiki")
axs[1].set_xlabel("X qiymatlari")
axs[1].set_ylabel("Y qiymatlari")
axs[1].legend()

# Grafika ko'rsatish
plt.tight_layout()
plt.show()

from google.colab.patches import cv2_imshow
import cv2

# Fayllarni ro'yxatga olish
fayllar = ['picture.jpg', 'rasm.jpg', 'surat.jpg']

oq_qora_rasmlar = []  # Oq-qora rasmlar saqlanadigan ro'yxat

for fayl in fayllar:
    # Tasvirni o'qish
    rasm = cv2.imread(fayl)
    if rasm is None:
        print(f"Fayl topilmadi: {fayl}")
        continue

    # Oq-qora rangga o'zgartirish
    oq_qora = cv2.cvtColor(rasm, cv2.COLOR_BGR2GRAY)
    oq_qora_rasmlar.append(oq_qora)

# Barcha oq-qora rasmlarni birdaniga ko'rsatish
for idx, oq_qora_rasm in enumerate(oq_qora_rasmlar, start=1):
    print(f"Oq-qora {idx}-rasm:")
    cv2_imshow(oq_qora_rasm)

import pandas as pd

# Read the CSV file
file_path = "/content/WHO COVID-19 cases (1).csv"  # Replace with the actual file path
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Apply a filter (e.g., filter rows where 'Region' is 'Europe')
filtered_data = data[data['Continent'] == 'Europe']  # Replace 'Region' with your actual column name

# Display the filtered data
print(filtered_data)

# Optionally, save the filtered data to a new CSV file
filtered_data.to_csv("filtered_data.csv", index=False)
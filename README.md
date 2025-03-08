# 🔗🚲Analysis of the Bike Sharing Dataset

## Struktur Proyek:
```
submission/
│-- dashboard/
│   │-- bike-dataset.jpg
│   │-- dashboard.py
│   │-- main_data.csv
│   │-- user.jpg
│-- data/
│   │-- day.csv
│   │-- hour.csv
│-- README.md
│-- Readme.txt
│-- Submission_GilangEgaBagaswara_Bike_Dataset.ipynb
│-- requirements.txt
│-- url.txt

```
## 🔧 Prasyarat
Pastikan Anda telah menginstal Python 3.7+. Anda dapat memeriksa versi Python dengan menjalankan perintah berikut:
```
python --version
```
## ⚙️ Instalasi & Persiapan
1️. Clone the Repository.
```
git clone <repository_url>
cd submission/dashboard
```
2. Buat dan Aktifkan Virtual Environment (Rekomendasi).
```
python -m venv venv
venv\Scripts\activate
```
3. Instal Dependensi.
```
pip install streamlit pandas matplotlib seaborn
```
## 🚀 Menjalankan Dashboard
Untuk menjalankan aplikasi Streamlit, jalankan perintah berikut:
```
streamlit run dashboard.py
```
Setelah dijalankan, Anda akan melihat output seperti ini:

Anda sekarang dapat melihat aplikasi Streamlit Anda di browser.
```
Local URL: http://localhost:8501
Network URL: http://192.168.xx.xx:8501

```
## 📝 Deskripsi Proyek
```
Proyek ini bertujuan untuk menganalisis dataset Bike Sharing yang mencakup data penggunaan sepeda sewaan dari tahun 2011 hingga 2012. Dataset ini menyediakan informasi rinci seperti:
Jumlah penyewaan sepeda per jam dan harian.
Kondisi cuaca (suhu, kelembapan, kecepatan angin).
Hari libur dan musim.
```
Dengan menggunakan dashboard ini, Anda dapat memvisualisasikan tren dan pola penggunaan sepeda, serta memahami faktor-faktor yang memengaruhi penyewaan sepeda.


## 🎯 Tujuan Proyek
```
Analisis Data         : Memahami pola penggunaan sepeda berdasarkan waktu, cuaca, dan hari libur.
Visualisasi           : Menyajikan data dalam bentuk grafik yang interaktif dan mudah dipahami.
Pengambilan Keputusan : Memberikan wawasan untuk meningkatkan manajemen sistem bike sharing.
```

## 📂 Struktur File
```
dashboard.py                : File utama untuk menjalankan aplikasi Streamlit.
main_data.csv               : Dataset utama yang digunakan untuk analisis.
bike-dataset.jpg & user.jpg : Gambar yang digunakan dalam dashboard.
day.csv & hour.csv          : Dataset tambahan untuk analisis lebih lanjut.
``` 

## 🙏 Terima Kasih


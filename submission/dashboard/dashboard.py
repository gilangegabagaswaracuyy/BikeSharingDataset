import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
import os

# Set theme
sns.set_theme(style='dark')

# Define the base directory (sesuaikan dengan struktur folder Anda)
base_dir = os.getcwd()  # Direktori kerja saat ini
dashboard_dir = os.path.join(base_dir, "submission", "dashboard")  # Path ke folder dashboard

# Path ke file CSV dan gambar
csv_path = os.path.join(dashboard_dir, "main_data.csv")
user_image_path = os.path.join(dashboard_dir, "user.jpg")
bike_image_path = os.path.join(dashboard_dir, "bike-dataset.jpg")

# Check if main_data.csv exists
if not os.path.exists(csv_path):
    st.error(f"File 'main_data.csv' tidak ditemukan di direktori: {dashboard_dir}. Pastikan file ada di direktori yang benar.")
else:
    # Load dataset
    all_df = pd.read_csv(csv_path)

    # Sorting & Changing Data Type
    all_df['dteday'] = pd.to_datetime(all_df['dteday'])
    all_df.sort_values(by='dteday', inplace=True)
    all_df.reset_index(drop=True, inplace=True)

    # Helper Functions
    def create_daily_users_df(df):
        return df.groupby('dteday').agg({
            'registered': 'sum',
            'casual': 'sum',
            'total': 'sum'
        }).reset_index()

    def create_casreg_pie(df):
        return df[['casual', 'registered']].sum()

    def create_grouped_df(df, group_col):
        return df.groupby(by=group_col).agg({
            'registered': 'sum',
            'casual': 'sum',
            'total': 'sum'
        }).sort_values(by='total', ascending=False)

    # Custom CSS for styling
    st.markdown("""
       <style>
            .profile-header {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 15px;
                padding-bottom: 8px;
                border-bottom: 2px solid #555;
                color: white;
                text-align: center;
                width: 100%;
            }
            .info {
                text-align: left;
                font-size: 16px;
                margin-top: 10px;
                color: white;
            }
            .info div {
                margin-bottom: 8px;
            }
            .info span {
                font-weight: bold;
                color: white;
            }
            .sidebar-img {
                border-radius: 10px;
                display: block;
                margin: auto;
                width: 100%;
                max-width: 200px;
            }
            .social-container {
                display: flex;
                justify-content: center;
                gap: 15px;
                margin-top: 15px;
            }
            .social-box {
                width: 70px;
                height: 70px;
                background-color: #f3f3f3;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;
                border-radius: 10px;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            }
            .social-box img {
                width: 40px;
                height: 40px;
            }
            .social-box a {
                display: flex;
                align-items: center;
                justify-content: center;
                width: 100%;
                height: 100%;
            }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar for Dashboard
    with st.sidebar:
        st.markdown('<div class="profile-header">PROFILE INFORMATION</div>', unsafe_allow_html=True)
        
        # Profile Picture
        if not os.path.exists(user_image_path):
            st.error(f"File 'user.jpg' tidak ditemukan di direktori: {dashboard_dir}. Pastikan file ada di direktori yang benar.")
        else:
            try:
                st.sidebar.image(user_image_path, caption="Profile Picture", use_container_width=True)
            except Exception as e:
                st.error(f"Error loading image: {e}")

        # Profile Details
        st.markdown("""
            <div class="info">
                <div>Nama<span>:</span> Gilang Ega Bagaswara</div>
                <div>Email<span>:</span> <a href="mailto:gilangegabagaswara@gmail.com" style="color:white; text-decoration:none;">gilangegabagaswara@gmail.com</a></div>
                <div>Id<span>:</span>gilangegabagaswara</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border: 1px solid #555; margin: 10px 0;'>", unsafe_allow_html=True)

        # Date Range
        min_date, max_date = all_df['dteday'].min(), all_df['dteday'].max()
        start_date, end_date = st.date_input("Pilih Rentang Waktu", min_value=min_date, max_value=max_date, value=[min_date, max_date])
        
        # Weather filter
        selected_weather = st.selectbox("Pilih kondisi cuaca:", ['All'] + list(all_df['weathersit'].unique()))
        
        # Filter dataset
        main_df = all_df[(all_df['dteday'] >= pd.Timestamp(start_date)) & (all_df['dteday'] <= pd.Timestamp(end_date))]
        if selected_weather != 'All':
            main_df = main_df[main_df['weathersit'] == selected_weather]

        st.markdown("<hr style='border: 1px solid #555; margin: 10px 0;'>", unsafe_allow_html=True)
        
        # Social Media
        st.markdown("""
        <div class="social-container">
            <div class="social-box">
                <a href="https://www.linkedin.com/in/gilang-ega-bagaswara/" target="_blank">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn">
                </a>
            </div>
            <div class="social-box">
                <a href="https://github.com/gilangegabagaswaracuyy" target="_blank">
                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub">
                </a>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Calculate total rentals
    total_rentals = main_df['total'].sum()

    # Main title
    st.markdown("""
        <h2 style="text-align: center; color: white;">📊 Analysis Bike Sharing Dataset 🚲</h2>
    """, unsafe_allow_html=True)

    # Display profile image
    if not os.path.exists(bike_image_path):
        st.error(f"File 'bike-dataset.jpg' tidak ditemukan di direktori: {dashboard_dir}. Pastikan file ada di direktori yang benar.")
    else:
        try:
            st.image(Image.open(bike_image_path), use_container_width=True, caption="Bike Sharing Dataset")
        except Exception as e:
            st.error(f"Error loading image: {e}")

    # Show total rentals metric
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; justify-content: center;">
            <h3 style="margin-right: 10px;">Total Penyewaan:</h3>
            <h3 style="color: white; margin: 0;">{total_rentals}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Visualize Question 1: Impact of Temperature, Humidity, and Windspeed
    plt.figure(figsize=(12, 6))

    # Scatter plot for temperature
    plt.subplot(1, 3, 1)
    sns.scatterplot(data=main_df, x='temp', y='total', hue='weathersit', palette='viridis', alpha=0.6)
    plt.title('Pengaruh Suhu ')
    plt.xlabel('Suhu')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.grid()

    # Scatter plot for humidity
    plt.subplot(1, 3, 2)
    sns.scatterplot(data=main_df, x='hum', y='total', hue='weathersit', palette='viridis', alpha=0.6)
    plt.title('Pengaruh Kelembapan')
    plt.xlabel('Kelembapan')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.grid()

    # Scatter plot for windspeed
    plt.subplot(1, 3, 3)
    sns.scatterplot(data=main_df, x='windspeed', y='total', hue='weathersit', palette='viridis', alpha=0.6)
    plt.title('Pengaruh Kecepatan Angin ')
    plt.xlabel('Kecepatan Angin')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.grid()

    st.pyplot(plt)

    # Visualize Holiday Rentals
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=main_df, x='holiday', y='total', hue='holiday', palette='pastel', legend=False)
    plt.title('Distribusi Jumlah Penyewaan Sepeda pada Hari Libur vs Bukan Hari Libur')
    plt.xlabel('Hari Libur')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.xticks(ticks=[0, 1], labels=['Bukan Hari Libur', 'Hari Libur'])
    plt.grid()

    st.pyplot(plt)

    # Footer Welcome Message
    st.markdown("""
        <div style="text-align: center; background-color: #808080; padding: 10px; border-radius: 10px; color: white;">
            <h3>🚲📊 Welcome to Bike Sharing Dashboard! 📈📍</h3>
        </div>
    """, unsafe_allow_html=True)

    # Define tabs for additional content
    tab1, tab2 = st.tabs(["The Rationale Behind the Dashboard", "Overview of the Bike Sharing Dataset"])

    with tab1:
        st.markdown("""
            <style>
                .justify-text {
                    text-align: justify;
                    text-justify: inter-word;
                    font-size: 20px;
                    line-height: 1.6;
                    color: white; /* Text color */
                }
                .centered-header {
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    color: white; /* Header color */
                }
            </style>
        """, unsafe_allow_html=True)

        # Content in Indonesian
        st.markdown("""
            <p class="justify-text">
            Tujuan dari pengembangan dashboard proyek akhir untuk analisis dataset sepeda ini adalah untuk memenuhi persyaratan proyek akhir dalam program pembelajaran Analisis Data dari Dicoding.  
            Dashboard ini berfungsi sebagai platform komprehensif untuk menyajikan wawasan utama, tren, dan pola yang diperoleh dari dataset, memastikan pendekatan yang terstruktur dan berbasis data dalam pengambilan keputusan analitis.  
            Dengan memanfaatkan berbagai teknik visualisasi data, dashboard ini secara efektif mengkomunikasikan temuan, memungkinkan pemahaman yang lebih mendalam dan interpretasi dataset yang lebih akurat.  
            Selain itu, proyek ini bertujuan untuk meningkatkan keterampilan dalam pemrosesan data, visualisasi, dan interpretasi, memperkuat kemampuan analitis yang penting dalam pemecahan masalah berbasis data di dunia nyata.
            </p>
        """, unsafe_allow_html=True)

    with tab2:
        # CSS for justified text
        st.markdown("""
            <style>
                .justify-text {
                    text-align: justify;
                    text-justify: inter-word;
                    font-size: 16px;
                    line-height: 1.6;
                    color: white; /* Text color */
                }
                .centered-header {
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    color: white; /* Header color */
                }
            </style>
        """, unsafe_allow_html=True)

        # Content in Indonesian
        st.markdown("""
            <p class="justify-text">
            Dataset ini menyediakan catatan rinci tentang jumlah penggunaan sepeda sewaan, baik secara per jam maupun harian, dalam sistem Capital Bike Share.  
            Data ini mencakup periode dari tahun 2011 hingga 2012 dan menyertakan informasi kontekstual yang relevan, seperti kondisi cuaca dan variasi musiman,  
            yang dapat memengaruhi pola penyewaan sepeda.
            </p>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown(
        "<p style='text-align: center; color: white;'>© 2025 Gilang Ega Bagaswara. All Rights Reserved.</p>", 
        unsafe_allow_html=True
    )

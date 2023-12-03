import streamlit as st
from streamlit_option_menu import option_menu

# Navigasi Side Bar 
with st.sidebar :
    selected = option_menu ("Aritmatika",
        ["Kalkulator", 
        "Luas Bangun Datar"],                        
    default_index = 0)


# Halaman Kalkulator 
if (selected == "Kalkulator") :
    st.title("Kalkulator Sederhana ")

    angka1 = st.number_input("Masukkan Angka Pertama", step=1)
    angka2 = st.number_input("Masukkan Angka Kedua", step=1)

    operasi = st.selectbox("Pilih Operasi", ["Tambah", "Kurang", "Kali", "Bagi"])

    hasil = 0

    if operasi == "Tambah":
        hasil = angka1 + angka2
    elif operasi == "Kurang":
        hasil = angka1 - angka2
    elif operasi == "Kali":
        hasil = angka1 * angka2
    elif operasi == "Bagi":
        if angka2 != 0:
            hasil = angka1 / angka2
        else:
            st.error("Pembagian dengan nol tidak diizinkan")

    st.success(f"Hasilnya adalah    = {hasil}")
    
if (selected == "Luas Bangun Datar") :
    st.title ("Luas Bangun Datar")
    
    opsi = st.selectbox ("Pilih Bangunnya", ["Persegi Panjang", "Segitiga", "Jajar Genjang", "Persegi"])
    hasil = 0
    
    if opsi == "Persegi Panjang" :
        panjang = st.number_input ("Masukkan Nilai Panjang", 0)
        lebar = st.number_input ("Masukkan Nilai Lebar", 0)
        hitung = st.button ("Hitung Luas Persegi Panjang")
        
        luas = panjang * lebar
        st.success(f"Hasilnya adalah    = {luas}")
        
    if opsi == "Segitiga" :
        alas = st.number_input ("Masukkan Nilai Alas", 0)
        tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
        hitung = st.button ("Hitung Luas Segitiga")
        
        luas = 0.5 * alas * tinggi
        st.success(f"Hasilnya adalah    = {luas}")
        
    if opsi == "Jajar Genjang" :
        alas = st.number_input ("Masukkan Nilai Alas", 0)
        tinggi = st.number_input ("Masukkan Nilai Tinggi", 0)
        hitung = st.button ("Hitung Luas Jajar Genjang")
        
        luas = alas * tinggi
        st.success(f"Hasilnya adalah    = {luas}")
        
    if opsi == "Persegi" :
        sisi = st.number_input ("Masukkan Nilai Sisi", 0)
        hitung = st.button ("Hitung Luas Persegi")
        
        luas = sisi * sisi
        st.success(f"Hasilnya adalah    = {luas}")
    

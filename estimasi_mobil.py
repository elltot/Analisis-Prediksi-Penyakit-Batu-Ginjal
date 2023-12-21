import pickle
import streamlit as st 

model = pickle.load(open('estimasi_mobil.sav', 'rb'))

st.title ('Estimasi harga Mobil Second')

year = st.number_input ('Input Tahun Mobil')
mileage = st.number_input ('Input Km Mobil')
tax = st.number_input ('Input Pajak Mobil')
mpg = st.number_input ('Input Konsumsi BBM Mobil')
engineSize = st.number_input ('Input Engine Size')

predict = ''

if st.button ('Estimasi Harga') :
    predict = model.predict (
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi Harga Mobil Second dalam Ponds : ', predict)
    st.write ('Estimasi Harga Mobil Bekas dalam IDR : ', predict * 15000)
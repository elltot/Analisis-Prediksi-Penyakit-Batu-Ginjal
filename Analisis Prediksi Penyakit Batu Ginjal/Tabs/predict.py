import streamlit as st 

from web_function import predict

def app(df, x, y) :
    
    st.title("Halaman Prediksi")
    
    col1,col2,col3 = st.columns(3)
    with col1 :
        bp = st.text_input ("Input Nilai Bp")
    with col1 :
        sg = st.text_input ("Input Nilai Sg")
    with col1 :
        al = st.text_input ("Input Nilai Al")
    with col1 :
        su = st.text_input ("Input Nilai Su")
    with col1 :
        rbc = st.text_input ("Input Nilai Rbc")
    with col1 : 
        pc = st.text_input ("Input Nilai Pc")
    with col1 :
        pcc = st.text_input ("Input Nilai Pcc")
    with col1 :
        ba = st.text_input ("Input Nilai Ba")
    with col2 :
        bgr = st.text_input ("Input Nilai Bgr")
    with col2 :
        bu = st.text_input ("Input Nilai Bu")
    with col2 :
        sc = st.text_input ("Input Nilai Sc")
    with col2 :
        sod = st.text_input ("Input Nilai Sod")
    with col2 :
        pot = st.text_input ("Input Nilai Pot")
    with col2 :
        hemo = st.text_input ("Input Nilai Hemo")
    with col2 :
        pcv = st.text_input ("Input Nilai Pvc")
    with col2 :
        wc = st.text_input ("Input Nilai Wc")
    with col3 :
        rc = st.text_input ("Input Nilai Rc")
    with col3 :
        htn = st.text_input ("Input Nilai Htn")
    with col3 :
        dm = st.text_input ("Input Nilai Dm")
    with col3 :
        cad = st.text_input ("Input Nilai Cad")
    with col3 :
        appet = st.text_input ("Input Nilai Appet")
    with col3 :
        pe = st.text_input ("Input Nilai Pe")
    with col3 :
        ane = st.text_input ("Input Nilai Ane")
        
    features = [bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]
    
    ## Tombol Prediksi
    if st.button ("Prediksi") :
        prediction, score = predict (x,y, features)
        score = score
        st.info("Prediksi Sukses")
        
        if (prediction == 1) :
            st.warning ("Orang tersebut rentan terkena penyakit Ginjal !")
            
        else :
            st.success ("Orang tersebut relatif aman dari penyakit Ginjal !")

        st.write ("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")
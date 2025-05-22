import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Status Mahasiswa",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS 
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid #E5E7EB;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #1E3A8A;
        padding-bottom: 0.5rem;
        border-bottom: 1px solid #E5E7EB;
        margin-bottom: 1rem;
    }
    .card {
        background-color: #F3F4F6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .prediction-card {
        background-color: #EFF6FF;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
        margin-bottom: 1rem;
        border-left: 4px solid #2563EB;
    }
</style>
""", unsafe_allow_html=True)

# Function untuk load model
@st.cache_resource
def load_model_components():
    try:
        model = joblib.load('./komponen/student_performance_model.pkl')
        scaler = joblib.load('./komponen/scaler_edutech.pkl')
        le = joblib.load('./komponen/encoder_edutech.pkl')
        feature_list = joblib.load('./komponen/fitur_edutech.pkl')
        kelas_mapping = joblib.load('./komponen/kelas_mapping_edutech.pkl')
        return model, scaler, le, feature_list, kelas_mapping
    except Exception as e:
        st.error(f"Error loading model files: {e}")
        return None, None, None, None, None

# Load model dan komponen
model, scaler, le, feature_list, kelas_mapping = load_model_components()

if model is None:
    st.error("Model tidak dapat dimuat. Pastikan semua file pickle tersedia.")
    st.stop()

# Tampilkan judul aplikasi
st.markdown('<div class="main-header">Prediksi Status Mahasiswa</div>', unsafe_allow_html=True)
st.markdown("Prediksi status kelulusan mahasiswa berdasarkan data akademik dan demografis.")

# Buat dictionary untuk menyimpan input data
input_data = {}

# Ini adalah data default untuk kolom yang tidak diminta input dari user
default_values = {
    'Application_mode': 1,
    'Application_order': 1,
    'Previous_qualification': 1,
    'Previous_qualification_grade': 13,
    'Nationality': 1,
    'Nacionality': 1,
    'Mothers_qualification': 12,
    'Fathers_qualification': 12,
    'Mothers_occupation': 5,
    'Fathers_occupation': 5,
    'Displaced': 0,
    'Tuition_fees_up_to_date': 1,
    'Scholarship_holder': 0,
    'International': 0,
    'Curricular_units_1st_sem_evaluations': 6,
    'Curricular_units_2nd_sem_evaluations': 6,
    'Unemployment_rate': 10.8,
    'Inflation_rate': 1.4,
    'GDP': 1.74,
    'Daytime_evening_attendance': 0,
    'Curricular_units_1st_sem_credited': 0
}

# Set semua kolom default sebagai nilai awal
for col in default_values:
    input_data[col] = default_values[col]

# Sidebar untuk fitur demografis dan umum
with st.sidebar:
    st.markdown('<div class="sub-header">Data Demografis & Umum</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Usia saat pendaftaran
    input_data['Age_at_enrollment'] = st.slider(
        "Usia saat pendaftaran", 
        min_value=17, 
        max_value=70, 
        value=20,
        help="Usia mahasiswa saat pertama kali mendaftar"
    )
    
    # Jenis Kelamin
    gender = st.radio(
        "Jenis Kelamin",
        options=["Laki-laki", "Perempuan"],
        horizontal=True
    )
    input_data['Gender'] = 1 if gender == "Laki-laki" else 0
    
    # Status Pernikahan
    status_pernikahan = st.selectbox(
        "Status Pernikahan",
        options=[1, 2, 3, 4, 5, 6],
        format_func=lambda x: {1: "Lajang", 2: "Menikah", 3: "Janda/Duda", 4: "Bercerai", 
                              5: "Berpasangan", 6: "Lainnya"}[x],
        index=0
    )
    input_data['Marital_status'] = status_pernikahan
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Kebutuhan pendidikan khusus
    edu_needs = st.radio(
        "Kebutuhan Pendidikan Khusus",
        options=["Tidak", "Ya"],
        horizontal=True
    )
    input_data['Educational_special_needs'] = 1 if edu_needs == "Ya" else 0
    
    # Status hutang
    debtor = st.radio(
        "Status Hutang Biaya Kuliah",
        options=["Tidak Ada Hutang", "Ada Hutang"],
        horizontal=True
    )
    input_data['Debtor'] = 1 if debtor == "Ada Hutang" else 0
    
    # Pemegang beasiswa
    scholarship = st.radio(
        "Pemegang Beasiswa",
        options=["Tidak", "Ya"],
        horizontal=True
    )
    input_data['Scholarship_holder'] = 1 if scholarship == "Ya" else 0
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    # Jurusan/Program Studi
    course = st.selectbox(
        "Program Studi",
        options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        format_func=lambda x: f"Jurusan {x}",
        index=0
    )
    input_data['Course'] = course
    
    # Waktu Perkuliahan
    daytime = st.radio(
        "Waktu Perkuliahan",
        options=["Siang", "Malam"],
        horizontal=True
    )
    input_data['Daytime_evening'] = 0 if daytime == "Siang" else 1
    
    # Nilai masuk
    input_data['Admission_grade'] = st.slider(
        "Nilai Masuk", 
        min_value=0, 
        max_value=200, 
        value=120,
        help="Nilai ujian masuk perguruan tinggi"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)

# Tabs untuk data akademik
tab1, tab2 = st.tabs(["Data Akademik Semester 1", "Data Akademik Semester 2"])

# Tab 1: Data Akademik Semester 1
with tab1:
    st.markdown('<div class="sub-header">Data Akademik Semester 1</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Unit Terdaftar Semester 1
        input_data['Curricular_units_1st_sem_enrolled'] = st.slider(
            "Unit Terdaftar", 
            min_value=0, 
            max_value=10, 
            value=6,
            help="Jumlah unit kurikulum yang terdaftar di semester 1"
        )
        
        # Unit Lulus Semester 1
        input_data['Curricular_units_1st_sem_approved'] = st.slider(
            "Unit Lulus", 
            min_value=0, 
            max_value=10, 
            value=5,
            help="Jumlah unit kurikulum yang lulus di semester 1"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Nilai Rata-rata Semester 1
        input_data['Curricular_units_1st_sem_grade'] = st.slider(
            "Nilai Rata-rata", 
            min_value=0, 
            max_value=20, 
            value=13,
            help="Nilai rata-rata untuk unit kurikulum semester 1"
        )
        
        # Unit Tanpa Evaluasi Semester 1
        input_data['Curricular_units_1st_sem_without_evaluations'] = st.slider(
            "Unit Tanpa Evaluasi", 
            min_value=0, 
            max_value=10, 
            value=0,
            help="Jumlah unit kurikulum tanpa evaluasi di semester 1"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)

# Tab 2: Data Akademik Semester 2
with tab2:
    st.markdown('<div class="sub-header">Data Akademik Semester 2</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Unit Terdaftar Semester 2
        input_data['Curricular_units_2nd_sem_enrolled'] = st.slider(
            "Unit Terdaftar", 
            min_value=0, 
            max_value=10, 
            value=6,
            help="Jumlah unit kurikulum yang terdaftar di semester 2"
        )
        
        # Unit Lulus Semester 2
        input_data['Curricular_units_2nd_sem_approved'] = st.slider(
            "Unit Lulus", 
            min_value=0, 
            max_value=10, 
            value=5,
            help="Jumlah unit kurikulum yang lulus di semester 2"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Nilai Rata-rata Semester 2
        input_data['Curricular_units_2nd_sem_grade'] = st.slider(
            "Nilai Rata-rata", 
            min_value=0, 
            max_value=20, 
            value=13,
            help="Nilai rata-rata untuk unit kurikulum semester 2"
        )
        
        # Unit Tanpa Evaluasi Semester 2
        input_data['Curricular_units_2nd_sem_without_evaluations'] = st.slider(
            "Unit Tanpa Evaluasi", 
            min_value=0, 
            max_value=10, 
            value=0,
            help="Jumlah unit kurikulum tanpa evaluasi di semester 2"
        )
        
        st.markdown('</div>', unsafe_allow_html=True)

# Tombol untuk prediksi (di tengah)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("📊 Prediksi Status Mahasiswa", use_container_width=True)

# Proses prediksi
if predict_button:
    # Buat dataframe dari input data
    input_df = pd.DataFrame([input_data])
    
    # Feature Engineering - sama persis dengan training
    # Tambahkan semua fitur turunan yang dibuat di proses training
    
    # Fitur performa akademik
    input_df['total_unit_sem1'] = input_df['Curricular_units_1st_sem_enrolled']
    input_df['total_unit_sem2'] = input_df['Curricular_units_2nd_sem_enrolled']

    # Tingkat keberhasilan semester 1
    input_df['tingkat_lulus_sem1'] = np.where(
        input_df['Curricular_units_1st_sem_enrolled'] > 0,
        input_df['Curricular_units_1st_sem_approved'] / input_df['Curricular_units_1st_sem_enrolled'],
        0
    )

    # Tingkat keberhasilan semester 2
    input_df['tingkat_lulus_sem2'] = np.where(
        input_df['Curricular_units_2nd_sem_enrolled'] > 0,
        input_df['Curricular_units_2nd_sem_approved'] / input_df['Curricular_units_2nd_sem_enrolled'],
        0
    )

    # Performa akademik keseluruhan
    input_df['rata_rata_nilai'] = (input_df['Curricular_units_1st_sem_grade'] + input_df['Curricular_units_2nd_sem_grade']) / 2

    # Tingkat pendidikan keluarga (rata_Rata kualifikasi orang tua)
    input_df['rata_kualifikasi_ortu'] = (input_df['Mothers_qualification'] + input_df['Fathers_qualification']) / 2

    # Rasio unit yang diambil vs yang lulus
    input_df['rasio_lulus_total'] = np.where(
        (input_df['Curricular_units_1st_sem_enrolled'] + input_df['Curricular_units_2nd_sem_enrolled']) > 0,
        (input_df['Curricular_units_1st_sem_approved'] + input_df['Curricular_units_2nd_sem_approved']) /
        (input_df['Curricular_units_1st_sem_enrolled'] + input_df['Curricular_units_2nd_sem_enrolled']),
        0
    )

    # Unit tanpa evaluasi (indikator kemungkinan bermasalah)
    input_df['total_tanpa_evaluasi'] = (input_df['Curricular_units_1st_sem_without_evaluations'] + 
                                     input_df['Curricular_units_2nd_sem_without_evaluations'])
    
    try:
        # Pilih hanya fitur yang diperlukan model
        X_input = pd.DataFrame()
        for feature in feature_list:
            if feature in input_df.columns:
                X_input[feature] = input_df[feature]
            else:
                st.error(f"Kolom '{feature}' tidak ditemukan di input data!")
        
        # Scale fitur
        X_input_scaled = scaler.transform(X_input)
        
        # Prediksi
        y_pred = model.predict(X_input_scaled)
        y_prob = model.predict_proba(X_input_scaled)
        
        # Reverse mapping ke label asli
        kelas_mapping_reverse = {v: k for k, v in kelas_mapping.items()}
        status_prediksi = kelas_mapping_reverse[y_pred[0]]
        
        # Tampilkan hasil dalam kotak hasil prediksi yang menarik
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
        
        # Status prediksi
        st.markdown(f"<h2 style='text-align: center; color: #1E40AF;'>Status Prediksi: {status_prediksi}</h2>", 
                  unsafe_allow_html=True)
        
        # Tampilkan probabilitas
        st.markdown("<h3>Probabilitas per Kelas</h3>", unsafe_allow_html=True)
        prob_df = pd.DataFrame({
            'Status': [kelas_mapping_reverse[i] for i in range(len(y_prob[0]))],
            'Probabilitas': y_prob[0]
        })
        
        # Format probabilitas sebagai persentase
        prob_df['Probabilitas'] = prob_df['Probabilitas'] * 100
        
        # Tampilkan chart
        st.bar_chart(prob_df.set_index('Status'))
        
        # Tampilkan tabel probabilitas
        st.table(prob_df.style.format({'Probabilitas': '{:.2f}%'}))
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        
    except Exception as e:
        st.error(f"Error saat melakukan prediksi: {e}")
        st.write("Traceback:")
        st.code(str(e))
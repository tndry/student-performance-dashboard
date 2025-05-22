# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis

1. **Tingkat Dropout yang Tinggi**: Institusi menghadapi tantangan dengan tingkat dropout mahasiswa yang cukup tinggi, yang berdampak pada reputasi institusi dan keberlanjutan keuangan
2. **Identifikasi Faktor Risiko** : Manajemen kesulitan mengidentifikasi mahasiswa yang berisiko tinggi untuk dropout sebelum terlalu terlambat untuk melakukan intervensi
3. **Alokasi Sumber Daya yang tidak efisien**: Kurangnya pemahaman tentang faktor pendorong keberhasilan akademik menyebabkan alokasi sumber daya yang tidak optimal untuk program bantuan mahasiswa
4. **Efektivitas Program Beasiswa**: Perlu evaluasi dampak program beasiswa terhadap retensi dan keberhasilan mahasiswa untuk pengambilan keputusan pendanaan yang lebih baik.

### Cakupan Proyek

1. **Data Preparation & EDA**: Melakukan data understanding untuk mengetahui faktor-faktor apa saja yang menyebabkan tingkat dropout yang tinggi dan cleaning data untuk mentayiapkan data yang digunakan dalam pembuatan model.

2. **Business Dashboard**: Pengembangan dashboard analitik komprehensif menggunakan metabase untuk memberikan wawasan tentang faktor-faktor yang mempengaruhi status mahasiswa dan kinerja akademik mereka
3. **Machine Learning Prototype** : Pengembagan model prediktif menggunakan Streamlit untuk mengidentifikasi mahasiswa dnegan risiko dropout tinggi berdasarkan karakterisitik demografis, latar belakang, dan kinerja akademik.

### Persiapan

Sumber data: Dataset yang digunakan merupakan dataset akademik yang tersedia pada [link](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv) berikut. Dataset terdiri dari 35 feature, termasuk faktor demografis, latar belakang keluarga, performa akademik, dan status akhir mahasiswa.

Setup environment:

**Menggunakan `virtualenv`**

1. **Install virtualenv**

```Python
pip install virtualenv

```

2. **Buat environment baru**

```
virtualenv myenv
```

3. **Aktifkan environment**

- Windows

```
myenv\Scripts\activate
```

- Mac

```
source myenv/bin/activate
```

4. **Install Dependencies**

```
pip install -r requirements.txt
```

5. **Jalankan kode anda di environment yang sudah di setup**

**Menggunakan `conda`**

1. **Buat environment baru**

```
conda create --name myenv python=3.9
```

2. **Aktifkan environment**

```
conda activate myenv
```

3. **Install Dependencies**

```
pip install -r requirements.txt
```

## Kredensial Login Metabase

- Email : root@mail.com
- Password : QELwz_D4g5WKeT (temporary password)

> **Catatan Penting**: Karena keterbatasan teknis Metabase, tidak memungkinkan untuk menetapkan password "root123" secara langsung. Mohon gunakan temporary password di atas untuk login ke dashboard. Setelah login dengan password sementara ini, password dapat diubah menjadi "root123" jika diperlukan.

## Kredensial Database Supabase

- Username: postgres.adllwemrfrsydzniwzvs
- Password: XrxI3Hxrc0JuyB
- Host: aws-0-ap-southeast-1.pooler.supabase.com
- Port: 5432
- Database: postgres

## Business Dashboard

![dasboard](./tandry%20simamora-dashboard.png)

Dashboard yang ditampilkan diatas merupakan **Student Performance Dashboard** -- sebuah dashboard yang dirancang untuk memantau dan menganalisis tingkat dropoout mahasiswa. Berikut penjelasan detail dari setiap bagian visualisasi

## Key Metrics

- **Total Mahasiswa**: 4424 orang
- **Total Mahasiswa Graduate**: 2209 orang
- **Total Mahasiswa Dropout**: 1421 orang
- **Total Mahasiswa Enrolled**: 794 orang

### 1. Distribusi Mahasiswa (Donut Chart)

- 49.9% mahasiswa berstatus Graduate (warna biru)
- 32.1% mahasis berstatus dropout (warna merah)
- 17.9% mahasiswa berstatus enrolled (warna hijau)

📌 **Insights**: Tingkat dropout yang sangat tinggi merupakan hal yang dapat menjadi perhatian bagi kampus.

### 2. Educational Special Needs(Donut Chart)

- Terdapat total 1.15% mahasiswa yang memiliki kebutuhan khusus

### 3. Korelasi Faktor Demografi dengan Status:

Analisis tentang bagaimaan variabel demografis seperti gender, usia, dan status pernikahan berhubungan dengan status akhir mahasiswa

### 4. Pengaruh Latar Belakang Keluarga

Visualisasi yang menunjukkan korelasi antara tingkat pendidikan dan pekerjaan orang tua dengan keberhasilan akademik mahasiswa

### 5. Dampak Faktor Ekonomi

Analisis tentang bagaimana tingkat pengangguran, inflasi, dan GDP berkorelasi dengan status mahasiswa

### 6. Profil Mahasiswa Berdasarkan Status

Karakteristik rata-rata mahasiswa dalam setiap kategori status untuk memberikan pemahaman yang lebih dalam tentang perbedaan antara kelompok.

## Menjalankan Sistem Machine Learning

Sistem machine learning dalam proyek ini dikembangkan sebagai prototype untuk memprediksi risiko dropout mahasiswa berdasarkan karakteristik demografis, latar belakang keluarga, dan kinerja akademik. Model ini bertujuan untuk membantu institusi mengidentifikasi mahasiswa yang berisiko tinggi secara dini sehingga intervensi yang tepat dapat dilakukan

### Cara menjalankan Prototype:

```
streamlit run main.py
```

Aplikasi streamlit akan berjalan di browser pada alamat https://student-performance-prototype.streamlit.app/

## Conclusion

Berdasarkan analisis yang dilakukan melalui Business Dashboard dan model ML, diidentifikasi beberapa temuan utama:

1. Terdapat total 4424 mahasiswa dnegan 32.1% diantaranya merupakan mahasiswa dropout, ini menunjukkan bahwa hampir 1/3 mahasiswa mengalami dropout, angka yang cukup signifikan dan perlu ditindaklanjuti.

2. Mahasiswa berkebutuhan khusus hanya 1.15% dari total mahasiswa, menunjukkan kelompok ini masih kecil.

3. Mahasiswa dari kelompok pendapatan rendah memiliki proporsi dropout yang tinggi dibanding kelompok pendapatan tinggi. Hal ini menunjukkan bahwa faktor ekonomi sangat berpengaruh terhadap keberlangsungan studi mahasiswa

4. Mayoritas mahasiswa berusia dibawah 30 tahun saat melakukan pendaftaran

5. Program Manajemen memiliki jumlah dropout tertinggi, perlu dilkaukan evaluasi lebih lanjut terhadap kurikulum, beban belajar, atau dukungan akademik di program tersebut.

6. Dropout banyak terjadi di usia mahasiswa yang lebih tua > 30 tahun

7. Perempuan memiliki tingkat dropout yang lebih tinggi dibanding laki-laki

8. Mahasiswa yang dropout cenderung memiliki rata-rata lebih rendah dibanding yang lulus atau masih aktif, hal ini menunjukkan pentingnya dukungan di semester awal.

### Rekomendasi Action Items

**- Implementasi Program Mentoring Semester Pertama**:

Kembangkan program mentoring intensif yang difokuskan pada mahasiswa semester pertama untuk meningkatkan retensi dan keberhasilan di akademik awal

**- Perluasan Program Beasiswa Berbasis Kebutuhan**:

Tingkatkan alokasi beasiswa utk mahasiswa dari latar belakang sosioekonomi yang kurang menguntungkan untuk meningkatkan akses dan keberhasilan

**- Program Dukungan Khusus untuk mahasiswa yang lebih tua**

Kembangkan layanan dukungan yang disesuaikan untuk mahasiswa yang lebih tua > 30 tahun yang mungkin menghadapi tantangan unik dalam pendidikan tinggi

**- Review Kurikulum untuk mata kuliah dengan tingkat dropout tinggi**

Identifikasi dan evaluasi mata kuliah dengan tingkat ketidaklulusan tinggi untuk perbaikan pedagogis atau dukungan tambahan.

# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan di seluruh penjuru negeri. Meskipun telah berkembang menjadi perusahaan besar, mereka menghadapi tantangan serius dalam hal pengelolaan SDM, yang menyebabkan tingginya angka attrition (tingkat keluar masuk karyawan) yang mencapai lebih dari 10%.

HR Department ingin mengetahui faktor-faktor utama yang menyebabkan karyawan keluar dari perusahaan dan bagaimana perusahaan dapat mengambil keputusan berbasis data untuk menurunkan angka tersebut.

---

## Permasalahan Bisnis
- Tingginya tingkat attrition (>10%) di perusahaan.
- Kurangnya pemahaman mengenai faktor-faktor yang menyebabkan karyawan keluar.
- Tidak adanya sistem pemantauan visual yang mudah dipahami untuk membantu HR dalam mengambil tindakan proaktif.

---

## Cakupan Proyek
- Melakukan eksplorasi dan pembersihan dataset karyawan.
- Mengidentifikasi faktor-faktor utama yang mempengaruhi keputusan karyawan untuk keluar.
- Membuat dashboard interaktif menggunakan Tableau untuk membantu tim HR memonitor attrition.
- Memberikan rekomendasi action items berbasis data.
- Membuat model machine learning untuk memprediksi karyawan yang ingin resign.

---

## Persiapan  
**Sumber data:**  
- File: `employee_data.csv`  
- Data ini berisi berbagai variabel demografis dan pekerjaan seperti usia, departemen, jarak dari rumah, status pernikahan, gaji bulanan, kepuasan kerja, dll.

**Setup environment:**  
- Machine learning dibuat menggunakan code editor Google Colab dan Bahasa Python 3.
- Mengimport library yang dibutuhkan untuk project.
- Visualisasi dan dashboard dibangun menggunakan **Tableau Desktop**.

**Tahapan Inspeksi Data:**
1. Melihat Dimensi dan Informasi Umum Dataset
2. Melihat Beberapa Sampel Data
3. Mengecek Missing Values
4. Mengecek Distribusi Target (Attrition)
5. Visualisasi Distribusi Attrition 

**Tahapan Cleansing Data:**
1. **Memfilter nilai null values** di kolom `Attrition` untuk menjaga keakuratan analisis.
2. **Mengubah nilai numerik** di kolom `Attrition` menjadi label kategori:
   - `1` menjadi `"Leave"`  
   - `0` menjadi `"Stay"`
3. **Mengganti value di kolom `WorkLifeBalance`** agar lebih informatif di Tableau:
   - `1` → `"Low"`  
   - `2` → `"Good"`  
   - `3` → `"Excellent"`  
   - `4` → `"Outstanding"`
4. **Mengganti value di kolom `JobInvolvement`** agar lebih informatif di Tableau:
   - `1` → `"Low"`  
   - `2` → `"Medium"`  
   - `3` → `"High"`  
   - `4` → `"Very High"`
5. **Membuat bin untuk kolom `Age`** di Tableau agar bisa dikelompokkan berdasarkan rentang usia, sehingga memudahkan analisis attrition berdasarkan kelompok umur.

**Tahapan Feature Engineering:**
1. Ubah data string ke numerik menggunakan Label Encoder.
2. Menghapus kolom 'EmployeeCount', 'EmployeeNumber', dan 'Over18' karena tidak terpakai.
3. Oversampling menggunakan Teknik SMOTE untuk oversampling data kelas minoritas.
4. Split dataset ke 80% train dan 20% test.

**Model Development dan Evaluation**
1. Membuat model menggunakan model random forest. Random forest dipilih karena dataset terdapat feature numerikan dan kategorikal sehingga paling sesuai.
2. Evaluasi model menggunakan confusion matrix dan akurasi.
3. Interpretasi hasil model menggunakan feature importance untuk analisa faktor apa yang penting dalam memprediksi karyawan yang ingin resign.

**Deployment**
Untuk mendeploy model, model disimpan dahulu ke format pkl dan didownload.

---

## Business Dashboard
Dashboard "Attrition Rate" di Tableau memberikan gambaran visual mengenai perbandingan antara karyawan yang keluar (LEAVE) dan tetap (STAY), dengan analisis lebih lanjut berdasarkan:

- **Total Working Years**: Karyawan yang sudah lama bekerja memiliki kecenderungan lebih loyal.
- **Job Involvement**: Karyawan yang memiliki keterlibatan rendah terhadap pekerjaan memiliki persentasi resign tinggi (40%).
- **Department**: Sales memiliki attrition tertinggi (20.69%).
- **Life Balance**: Skor Life Balance yang rendah cenderung memiliki attrition lebih tinggi.
- **Distance From Home**: Karyawan yang keluar cenderung tinggal lebih jauh dari kantor.
- **Business Travel**: Karyawan yang sering melakukan perjalanan bisnis memiliki tingkat keluar lebih tinggi (24.88%).
- **Overtime**: Karyawan dengan jam lembur tinggi lebih rentan untuk keluar (31.92%).
- **Job Satisfaction**: Nilai kepuasan kerja lebih rendah pada karyawan yang keluar.
- **Marital Status**: Karyawan lajang menunjukkan angka attrition tertinggi (26.7%).
- **Monthly Income**: Gaji rata-rata karyawan yang keluar lebih rendah dari yang bertahan.
- **Usia**: Karyawan muda (<35 tahun) memiliki attrition rate lebih tinggi dibanding kelompok usia lainnya.

Link dashboard:
https://public.tableau.com/views/Dashboard_17447045199160/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

---

## Conclusion
Melalui visualisasi dan analisis data yang telah dilakukan, ditemukan bahwa attrition karyawan dipengaruhi oleh sejumlah faktor seperti umur, departemen, jarak dari rumah, frekuensi lembur, dan kepuasan kerja. Dashboard yang dibangun memberikan insight yang mudah dipahami secara visual dan dapat digunakan bagi divisi HR sebagai alat bantu dalam mengambil keputusan strategis berbasis data.

---

## Rekomendasi Action Items
Berikut adalah beberapa langkah yang dapat dilakukan perusahaan untuk menurunkan angka attrition:

1. **Program Retensi untuk Karyawan Muda (<35 tahun):**  
   Buat program pengembangan karier, mentorship, dan keterlibatan karyawan untuk kelompok usia muda.

2. **Optimasi Beban Kerja dan Kompensasi:**  
   Tinjau ulang kebijakan lembur dan frekuensi perjalanan bisnis terutama di departemen dengan attrition tinggi seperti Sales.

3. **Tingkatkan Work-Life Balance:**  
   Terapkan jam kerja fleksibel atau kebijakan hybrid, terutama bagi karyawan yang tinggal jauh dari kantor.

4. **Program Engagement dan Kepuasan Kerja:**  
   Adakan survei rutin tentang kepuasan kerja dan gunakan hasilnya untuk merancang kebijakan yang lebih memuaskan karyawan.

5. Dorong partisipasi dalam pengambilan keputusan tim atau proyek, agar merasa lebih memiliki pekerjaan. Adakan program recognition & reward untuk karyawan yang aktif dan berdedikasi.

6. **Exit Interview Terstruktur:**  
   Lakukan exit interview secara konsisten untuk memahami alasan utama karyawan keluar dan gunakan data tersebut untuk perbaikan berkelanjutan.

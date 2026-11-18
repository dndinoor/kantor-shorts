# 07 - Publish: Cara Kerja Kopling Motor

Slug: kopling-motor | Berkas: `final.mp4` (1080x1920, 51,2 dtk, h264 + AAC) | Status: PAKET SIAP, BELUM DIUNGGAH

## Opsi judul (maks 60 karakter)
1. **Kenapa Tuas Kopling Motor Cuma Gerak Beberapa Milimeter?** (56 karakter) - disarankan, sesuai hook video
2. Cara Kerja Kopling Motor: Isinya Ternyata Begini #Shorts (56 karakter)
3. Jangan Setengah Kopling! Ini yang Terjadi di Dalam (50 karakter) - sudut kesalahan umum
4. Isi Kopling Motor: Pelat Dijepit Lalu Dilepas #Shorts (54 karakter)

Catatan: #Shorts di judul opsional. Cukup ada di deskripsi bila ingin judul bersih.

## Deskripsi (siap tempel)
```
Tuas kopling ditarik jauh, tapi di dalam cuma bergeser beberapa milimeter. Di video ini kita bedah kopling basah motor: pelat gesek dan pelat baja yang dijepit pegas, lalu dilepas saat tuas ditarik.

Bonus: kenapa kebiasaan setengah kopling di tanjakan atau macet bikin selip, panas, dan kampas cepat aus. Pakai rem, dan pindah ke netral saat berhenti lama.

Catatan: animasi adalah ilustrasi sederhana buatan sendiri. Ukuran celah digambar berlebihan agar terlihat dan bukan ukuran sebenarnya. Konstruksi kopling bisa berbeda antar motor.

Follow untuk bedah isi motor lainnya.

#Shorts #KoplingMotor #CaraKerjaKopling #TipsMotor #BedahMotor
```

## Tag (12)
kopling motor, cara kerja kopling motor, kopling basah, kopling manual motor, setengah kopling, kampas kopling aus, kampas kopling selip, tuas kopling, pelat kopling, tips motor, edukasi otomotif, shorts

## Hashtag
#Shorts #KoplingMotor #CaraKerjaKopling #TipsMotor #BedahMotor

## Saran thumbnail / frame awal
- Shorts tidak selalu memakai thumbnail kustom di aplikasi; yang paling berpengaruh adalah frame pertama dan frame yang dipilih di YouTube Studio.
- Pilihan utama: frame sekitar detik 3-4 (hook), penampang tumpukan pelat dengan celah kuning disorot dan teks "Tarik tuas kopling... di dalam cuma gerak SEGINI." (kata SEGINI kuning). Kontras tinggi, teks di area aman (y 240-420).
- Alternatif: frame adegan 4 (sekitar detik 28-30) dengan "TERPUTUS" merah dan celah kuning terbuka.
- Hindari frame yang ada teks di bawah y=1440 atau di kanan x=920 (tertutup UI Shorts).
- Bila mengunggah thumbnail kustom, ekspor dari frame di atas tanpa menambah logo atau elemen berhak cipta.

## Checklist pra-upload

### Teknis
- [x] Durasi <= 60 dtk: 51,2 dtk (hasil ffprobe di 06-musik.md)
- [x] Rasio 9:16: 1080x1920
- [x] Codec: h264 + AAC, decode tanpa error
- [ ] Audio jelas: musik -24 dB dengan ducking, tetapi **belum didengarkan manusia**. User dengarkan sekali; bila musik atau SFX terlalu ramai, turunkan gain.
- [ ] Teks aman dari UI Shorts: cek 1 frame per adegan dengan overlay kotak aman (x 60-920, y 220-1440), sesuai 04-visual.md poin 12
- [ ] Sinkron teks dan voiceover: durasi final 51,2 dtk sedangkan rencana visual 48 dtk. Pastikan teks dan adegan masih pas dengan suara.

### Hak cipta dan lisensi
- [x] Musik dan SFX: dibuat sendiri secara prosedural (`05-asset/render/gen_musik.py`), tanpa sampel atau lagu pihak ketiga. Aman tanpa atribusi.
- [x] Visual: animasi buatan sendiri, tanpa logo, merek, atau motor bermerek. Font Poppins/Montserrat/DejaVu berlisensi OFL/bebas.
- [ ] Cek ulang tidak ada siluet motor atau ikon yang menyerupai model atau merek tertentu (04-visual.md poin 11).
- [ ] Voiceover: saat ini suara sintetis robotik (espeak-ng). Tidak ada masalah hak cipta, tetapi **sangat disarankan diganti rekaman suara manusia** agar retensi dan kesan kualitas lebih baik. Bila diganti, sinkronkan ulang teks dan adegan, lalu rakit ulang final.mp4.
- [ ] Saat upload, isi pengungkapan konten sintetis/diubah (altered or synthetic content) sesuai kebijakan YouTube bila berlaku. Suara sintetis perlu dipertimbangkan di sini; user yang memutuskan jawabannya.

### Akurasi fakta
- [ ] **Sumber utama riset belum dibaca langsung.** Pengambilan halaman penuh gagal (detik, gridoto, motorcyclistonline, rideapart tidak bisa di-resolve). Fakta hanya berdasar ringkasan hasil pencarian web. Idealnya user atau agen membuka sumber di 01-riset.md dan memastikan fakta 1-4 dan 6 sebelum upload.
- [x] Klaim yang berisiko sudah dibuang: tanpa "18% selip", tanpa angka mm di layar, tanpa bahan pelat, tanpa tipe pegas, JASO tidak dibahas.
- [x] Angka "1-2 mm" hanya ditulis "beberapa milimeter" (sumber berbahasa Inggris, sifatnya perkiraan).
- [x] Disclaimer ilustrasi: ukuran celah di animasi digambar berlebihan, hanya ilustrasi. Sudah ada di deskripsi di atas. Pertimbangkan juga menambah teks kecil di video bila ada revisi.
- [ ] Saran "setengah kopling" berbasis pengalaman mekanik dan media otomotif, bukan riset formal. Nada di video sudah berupa saran umum; jangan dijadikan klaim teknis mutlak di komentar atau balasan.

### Pengaturan di YouTube Studio
- [ ] Audiens: pilih **"Tidak, video ini bukan dibuat untuk anak-anak"** (sesuai keputusan user). Bila dipilih "made for kids", komentar dan fitur lain dibatasi.
- [ ] Kategori: Otomotif (Autos and Vehicles); alternatif Edukasi.
- [ ] Bahasa video: Indonesia. Lokasi opsional.
- [ ] Visibilitas: sebaiknya pilih Pribadi atau Tidak Terdaftar dulu untuk uji tonton di ponsel, lalu Publik setelah user setuju.
- [ ] Tambahkan #Shorts di deskripsi (sudah ada). Judul pilih salah satu opsi di atas.
- [ ] Cek peringatan hak cipta (Copyright check) selesai tanpa klaim sebelum menjadikan Publik.
- [ ] Komentar dan monetisasi: sesuai preferensi user.

## Ringkasan risiko yang perlu diputuskan user
1. Voiceover robotik: ganti rekaman manusia atau unggah apa adanya.
2. Fakta belum dicek ke halaman sumber asli: cek manual atau terima risikonya.
3. Audio belum didengar manusia: dengarkan sekali.
4. Jawaban pengungkapan konten sintetis di YouTube Studio.

Paket siap. Menunggu izin user sebelum upload.

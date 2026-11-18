# Paket Publish - yecvt-nmax

Status: PAKET SIAP, BELUM DIUNGGAH. Tidak ada upload yang dilakukan oleh agen mana pun.
Berkas video: `output/yecvt-nmax/final.mp4` (menurut 05-asset/DAFTAR.md: 1080x1920, 30 fps, 38 dtk, SFX + musik latar, tanpa voiceover).

## 1. Opsi judul (maks 70 karakter)

1. `NMAX Turbo Bukan Turbo! Ini Matic Tanpa Roller (YECVT)` (54 karakter) - rekomendasi, paling dekat dengan hook video.
2. `Matic Tanpa Roller? Begini Cara Kerja YECVT di NMAX Turbo` (57 karakter)
3. `Kenapa NMAX Turbo Nggak Pakai Turbo? Jawabannya YECVT` (53 karakter)

Catatan: tidak memakai kata "pertama", "tercanggih", atau klaim performa. Jumlah karakter dihitung manual, cek ulang saat mengetik di YouTube Studio.

## 2. Deskripsi

```
NMAX Turbo ternyata bukan pakai turbocharger. Namanya merujuk ke fitur YECVT, CVT yang dikontrol elektronik. Di matic biasa, roller di pulley primer bergeser karena gaya sentrifugal. Di YECVT, fungsi roller digantikan dinamo listrik yang diatur TCU.

Animasi di video adalah penyederhanaan edukatif, bukan gambar teknis akurat.

Menurutmu matic tanpa roller ini worth it? Tulis di komentar. Follow untuk bedah teknologi motor lainnya.

Musik latar dan efek suara dibuat sendiri. Visual animasi buatan sendiri, tanpa logo atau foto resmi.

#Shorts #YECVT #NMAXTurbo #Yamaha #MotorMatic #CVT #OtomotifIndonesia
```

Pemeriksaan klaim: tidak ada angka rpm, harga motor/part, atau jumlah sensor. Tidak membahas Y-Shift, mode T/S, mode darurat, garansi, atau "pertama di dunia". Isinya hanya fakta 1, 2, 3, 7 dari riset. Kata "Yamaha" muncul sebagai nama merek dalam hashtag. Tidak ada klaim afiliasi atau endorsement.

## 3. Tag (kolom tag di YouTube Studio)

yecvt, nmax turbo, yamaha nmax turbo, cara kerja yecvt, cvt elektronik, matic tanpa roller, nmax bukan turbo, pulley cvt, roller cvt, tcu motor, teknologi motor, otomotif indonesia, shorts

Hashtag di deskripsi (maks 3 tampil di atas judul; YouTube memakai tiga hashtag pertama): #Shorts #YECVT #NMAXTurbo

## 4. Thumbnail / cover

- Shorts tidak mengandalkan thumbnail kustom. Pilih frame cover dari video di YouTube Studio, atau unggah gambar bila tersedia untuk akunmu.
- Frame yang disarankan: sekitar detik 2-3 (adegan 1) saat "TURBO" sudah dicoret merah dan "BUKAN TURBOCHARGER" terbaca. Kontras tinggi dan teksnya besar.
- Pastikan teks tidak tertutup UI Shorts: zona aman x 60-930, y 250-1440.
- Cadangan: frame awal adegan 4 (label "YECVT" oranye, roller memudar), yang menonjolkan perbandingan.
- Tidak memakai foto motor resmi, logo, atau karakter.
- Catatan: font di video adalah DejaVu Sans Bold (pengganti Montserrat/Poppins, yang tidak tersedia). Tampilan kemungkinan kurang rapi dibanding style guide. Periksa apakah teks hook masih muat dalam lebar aman.

## 5. Pengaturan upload

| Pengaturan | Nilai |
|---|---|
| Kategori | Autos & Vehicles (Otomotif) |
| Audiens | Bukan made for kids (pilih "Tidak, ini bukan konten untuk anak-anak") |
| Pembatasan usia | Tidak |
| Bahasa video | Bahasa Indonesia |
| Komentar | Aktif (CTA mengajak komentar) |
| Visibilitas | Disarankan unggah sebagai Pribadi/Tidak publik dulu untuk pratinjau, lalu publik setelah checklist selesai |
| Konten sintetis/dimodifikasi | Isi pengungkapan sesuai pertanyaan di Studio. Visual berupa animasi diagram buatan skrip, bukan rekayasa realistis orang atau peristiwa nyata. User yang memutuskan jawabannya. |
| Konten berbayar/sponsor | Tidak ada |
| Playlist | Opsional (mis. "Bedah Teknologi Motor") |

## 6. Catatan hak cipta

- Musik: dibuat sendiri secara prosedural (Python + numpy, sintesis gelombang sinus), tanpa sampel atau lagu pihak lain. Lihat 06-musik.md. Tidak ada atribusi wajib.
- SFX ("tek" dan whoosh): disintesis sendiri dengan ffmpeg.
- Visual: digambar sendiri dengan Python PIL, tanpa logo Yamaha, tanpa foto resmi, tanpa karakter. Siluet motor generik. Kata "NMAX" hanya muncul di subtitle/judul sebagai penyebutan nama produk.
- Font: DejaVu Sans Bold (lisensi bebas). Perlu dipastikan lisensinya jika ingin dicantumkan, tetapi tidak membutuhkan atribusi di deskripsi.
- Risiko tersisa: sistem Content ID bisa saja salah menandai musik sintetis. Jika terjadi, ajukan sanggahan dengan menyebut bahwa karya dibuat sendiri.

## 7. Checklist pra-upload

Teknis
- [ ] Durasi <= 60 dtk (menurut DAFTAR.md 38 dtk). Cek ulang dengan ffprobe atau pemutar video.
- [ ] Rasio 9:16 (1080x1920). Cek ulang pada file `final.mp4`.
- [ ] Teks dan subtitle tidak tertutup UI Shorts (zona aman terpenuhi). Cek pratinjau di ponsel.
- [ ] Subtitle terbaca di layar HP (DejaVu Sans Bold 54 px, maks 2 baris). Tidak ada teks terpotong atau tumpang tindih, terutama adegan 1 ("TURBOCHARGER" harus muat) dan adegan 5 (padat).
- [ ] Font pengganti: Montserrat/Poppins tidak tersedia, video memakai DejaVu Sans Bold. Putuskan apakah tampilannya bisa diterima atau perlu dirender ulang dengan font sesuai style guide.

Audio
- [ ] **Video tanpa voiceover (hanya subtitle).** Pastikan user menerima hal ini. Konsep awal dan naskah memakai voiceover, sehingga penonton harus membaca subtitle dengan cepat. Adegan padat (terutama 3, 5, 6) berisiko terlalu cepat dibaca. Pertimbangkan menambah voiceover (vo-01..06.wav belum ada) lalu rakit ulang.
- [ ] **Musik belum didengarkan manusia.** Dengarkan dari awal sampai akhir: volume, kualitas, dan apakah mengganggu. Cek juga bahwa SFX tidak tertutup dan tidak ada audio pecah (clipping).
- [ ] Audio jelas dan tidak terlalu keras/pelan terhadap kebiasaan Shorts lain.

Fakta
- [ ] **Fakta 1, 2, 3, dan 7 belum dicek ke sumber asli.** Riset tidak bisa membuka halaman sumber (Detik Oto, Autofun, Yamaha JP, RideApart, Zigwheels diblokir daftar domain sesi) dan hanya memakai ringkasan hasil pencarian. Buka sumber di 01-riset.md dan pastikan:
  - Fakta 1: YECVT = CVT berkontrol elektronik, pulley primer digerakkan motor listrik.
  - Fakta 2: CVT biasa memakai roller dan gaya sentrifugal; di YECVT fungsi roller digantikan motor.
  - Fakta 3: dinamo diatur TCU, yang membaca sensor kecepatan pulley primer dan sekunder, bukaan gas, kecepatan, dan putaran mesin.
  - Fakta 7: "Turbo" bukan turbocharger, nama merujuk ke fitur YECVT/Y-Shift.
- [ ] Perhatikan nuansa fakta 7: sumber menyebut nama merujuk ke fitur YECVT/Y-Shift, sedangkan video hanya menyebut YECVT. Pastikan tidak menyesatkan, atau tambahkan Y-Shift hanya setelah diverifikasi.
- [ ] Diagram mekanis (roller bergeser keluar, dinamo mendorong pulley lewat ulir/batang) adalah penyederhanaan edukatif. Mekanisme dinamo di adegan 4 (batang/ulir oranye) tidak ada di riset, jadi tinjau apakah visual itu menyiratkan detail yang belum terbukti. Jika ragu, sederhanakan visualnya atau tambahkan keterangan di deskripsi (sudah ada).
- [ ] Tidak ada angka rpm, harga, jumlah sensor, atau klaim "pertama/tercanggih" di video, judul, deskripsi, maupun tag. Periksa ulang final.mp4.

Hak cipta dan kebijakan
- [ ] Tidak ada logo, foto resmi, atau karakter di video.
- [ ] Musik dan SFX buatan sendiri (lihat bagian 6).
- [ ] Pengaturan "bukan made for kids" dan kategori sudah sesuai.

Persetujuan
- [ ] User sudah memeriksa semua poin di atas.
- [ ] User sudah menulis persetujuan eksplisit ("setuju upload") atau mengunggah sendiri secara manual.

## Pesan akhir

Paket siap. Menunggu izin user sebelum upload.

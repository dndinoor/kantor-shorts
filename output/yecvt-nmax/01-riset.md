# Riset: Cara kerja YECVT pada Yamaha NMAX

Tanggal riset: 2026-11-18

CATATAN METODE: Pengambilan halaman langsung (WebFetch) gagal karena domain global.yamaha-motor.com, oto.detik.com, dan www.autofun.co.id tidak ada di daftar domain yang diizinkan sesi ini. Semua fakta di bawah berasal dari ringkasan hasil pencarian web, bukan dari membaca halaman penuh. Sebelum naik ke tahap Script, sebaiknya fakta bertanda (*) dicek ulang ke halaman aslinya.

## Ide terpilih
"Motor matic ini tidak punya roller: pulley-nya digerakkan dinamo listrik yang diatur komputer (YECVT di NMAX Turbo)."

## Alasan
- Potensi tonton: kata "Turbo" memancing rasa penasaran, dan klarifikasinya ("bukan turbocharger") adalah hook yang kuat.
- Unik: perbandingan roller (gaya sentrifugal) vs dinamo (diatur elektrik) mudah divisualkan dengan animasi 2D.
- Produksi mudah: cukup animasi diagram pulley, teks, dan voiceover, tanpa footage berhak cipta.

## Fakta terverifikasi (min. 2 sumber independen)

1. YECVT = CVT berkontrol elektronik. Pulley primer digerakkan motor listrik (dinamo), tidak lagi bergantung roller.
   - [Detik Oto: Begini Kerja Teknologi YECVT](https://oto.detik.com/motor/d-7864458/begini-kerja-teknologi-yecvt-yamaha-nmax-turbo-untuk-performa-maksimal)
   - [Autofun: Pulley Diatur Elektrik](https://www.autofun.co.id/berita-motor/pulley-diatur-elektrik-ini-komponen-cvt-yang-beda-dari-yamaha-nmax-turbo-79967)
   - [Rilis resmi Yamaha Jepang, NMAX155 ABS (JP)](https://global.yamaha-motor.com/jp/news/2025/0220/nmax.html) menyebut kontrol sheave/pulley lewat motor DC.
2. CVT konvensional: roller di pulley primer bergerak oleh gaya sentrifugal dan bukaan gas. Pada YECVT fungsi roller digantikan motor, jadi rasio bisa diatur aktif.
   - [Detik Oto](https://oto.detik.com/motor/d-7864458/begini-kerja-teknologi-yecvt-yamaha-nmax-turbo-untuk-performa-maksimal)
   - [Autofun: Masih Bingung? Cara Kerja YECVT](https://www.autofun.co.id/berita-motor/masih-bingung-ini-cara-kerja-yecvt-yamaha-nmax-turbo-80243)
3. Dinamo dikendalikan TCU (Transmission Control Unit). TCU membaca sensor kecepatan pulley primer dan sekunder serta data seperti bukaan gas, kecepatan, dan putaran mesin untuk menghitung rasio ideal.
   - [Autofun: Cara Kerja YECVT](https://www.autofun.co.id/berita-motor/masih-bingung-ini-cara-kerja-yecvt-yamaha-nmax-turbo-80243)
   - [Detik Oto](https://oto.detik.com/motor/d-7864458/begini-kerja-teknologi-yecvt-yamaha-nmax-turbo-untuk-performa-maksimal)
   - [Rilis Yamaha JP](https://global.yamaha-motor.com/jp/news/2025/0220/nmax.html) (throttle, kecepatan, rpm).
4. Komponen utama: ECVT Motor, gear reduction, sensor motor primer, speed sensor, TCU.
   - [Detik Oto](https://oto.detik.com/motor/d-7864458/begini-kerja-teknologi-yecvt-yamaha-nmax-turbo-untuk-performa-maksimal)
   - [Autofun](https://www.autofun.co.id/berita-motor/pulley-diatur-elektrik-ini-komponen-cvt-yang-beda-dari-yamaha-nmax-turbo-79967)
5. Ada dua mode berkendara: T-Mode (Town/commuting) dan S-Mode (sport). Pindah dari T ke S saat jalan konstan menaikkan rpm sekitar 500-1.000 rpm (*satu sumber, lihat bagian tidak terverifikasi).
   - [Detik Oto: Fitur YECVT dan Cara Pakainya](https://oto.detik.com/motor/d-7452321/ketahui-fitur-yecvt-turbo-di-yamaha-nmax-baru-dan-cara-pakainya)
   - [Rilis Yamaha JP](https://global.yamaha-motor.com/jp/news/2025/0220/nmax.html) (ada driving mode switch dan fungsi shift-down).
6. Tombol Y-Shift di setang kiri membantu "memaksa" akselerasi dan deselerasi (mirip engine brake/downshift).
   - [Detik Oto: Bedah Teknologi Nmax Turbo](https://oto.detik.com/editors-choice/d-7804854/bedah-teknologi-unggulan-yamaha-nmax-turbo-y-shift-hingga-sistem-navigasi-garmin)
   - [Autofun: Cara Kerja YECVT](https://www.autofun.co.id/berita-motor/masih-bingung-ini-cara-kerja-yecvt-yamaha-nmax-turbo-80243)
7. Mesin "Turbo" bukan turbocharger. Nama merujuk ke fitur YECVT/Y-Shift.
   - [RideApart](https://www.rideapart.com/news/723275/yamaha-nmax-turbo-not-turbocharged/)
   - [Zigwheels: Alasan Yamaha Memakai Kata Turbo](https://www.zigwheels.co.id/motovaganza/alasan-yamaha-memakai-kata-turbo-di-nmax-terbaru/)
8. Model yang memakai YECVT:
   - NMAX Turbo (Indonesia), diluncurkan 2024. Sumber: [Antara](https://megapolitan.antaranews.com/berita/293367/yamaha-resmi-luncurkan-skutik-premium-nmax-tercanggih-berteknologi-turbo), [Segmenty](https://segmenty.com/GenerateNewsStaticJsps/Yamaha_NMax_Turbo_launched_in_local_market.html).
   - NMAX155 ABS Jepang, rilis 20 Feb 2025, dijual 21 Mar 2025. Sumber: [Yamaha JP](https://global.yamaha-motor.com/jp/news/2025/0220/nmax.html).
   - NMAX non-Turbo (Neo, Neo S) memakai CVT konvensional. Sumber: [Autofun harga part](https://www.autofun.co.id/berita-motor/tak-pakai-roller-berapa-harga-part-yecvt-yamaha-nmax-turbo-81339), [Zigwheels 5 varian](https://www.zigwheels.co.id/motovaganza/yamaha-nmax-terbaru-dijual-dalam-5-varian-ini-perbedaannya/).
9. Kekurangan: part jauh lebih mahal. Primary Sheave Assy sekitar Rp 1,5 juta, dibanding pulley depan NMAX Neo sekitar Rp 122 ribu. Servis bergantung elektronik/TCU. V-belt NMAX Turbo lebih lebar (24,9 mm vs 24,1 mm).
   - [Autofun: Harga Part YECVT](https://www.autofun.co.id/berita-motor/tak-pakai-roller-berapa-harga-part-yecvt-yamaha-nmax-turbo-81339)
   - [Gridoto: Harga pulley depan](https://www.gridoto.com/read/224134794/enggak-pakai-roller-harga-pulley-depan-yamaha-nmax-turbo-tembus-segini?page=all)
   - [Autofun: Gak Boleh Asal Servis](https://www.autofun.co.id/berita-motor/yamaha-nmax-turbo-gak-boleh-asal-servis-ini-penyebabnya-80044)
10. Kelebihan: rentang rasio lebih lebar, akselerasi/deselerasi bisa diatur, dan komponen penggerak YECVT bergaransi 3 tahun (menurut Autofun).
    - [Autofun: Harga Part YECVT](https://www.autofun.co.id/berita-motor/tak-pakai-roller-berapa-harga-part-yecvt-yamaha-nmax-turbo-81339)
    - [Detik Oto: Teknologi YECVT](https://oto.detik.com/motor/d-7827243/teknologi-yecvt-di-yamaha-nmax-turbo-pertama-dan-tercanggih-di-kelasnya)
11. Mode darurat: jika dinamo gagal menggerakkan pulley, sistem masuk mode darurat (penjelasan YIMM, Ferry Nurul Fajar).
    - [Gridoto: Dinamo CVT Nmax Turbo bermasalah](https://www.gridoto.com/read/224113955/ini-jadinya-jika-dinamo-cvt-nmax-turbo-tiba-tiba-bermasalah?page=all)
    - [Autofun: Cara Kerja YECVT](https://www.autofun.co.id/berita-motor/masih-bingung-ini-cara-kerja-yecvt-yamaha-nmax-turbo-80243) (*sumber kedua belum dikonfirmasi isinya, hanya ringkasan).
12. Model lain: Yamaha AEROX ABS (Jepang, Juli 2026) disebut sebagai model YECVT ke-2 setelah NMAX155 (menurut rilis Yamaha JP). Bisa dipakai sebagai fakta bonus, tetapi tidak perlu untuk video NMAX.
    - [Rilis Yamaha JP AEROX](https://global.yamaha-motor.com/jp/news/2026/0709/aerox.html)

## Fakta tidak terverifikasi / bertentangan (jangan dipakai tanpa cek ulang)
- Jumlah sensor: satu sumber menyebut tiga sensor, sumber lain dua (primer dan sekunder). Di video cukup sebut "sensor di pulley primer dan sekunder".
- Penjelasan S-Mode: ada yang menulis "Sport", ada yang "Sport Touring". Pakai "S-Mode (sport)" saja.
- Batas aktif Y-Shift: satu uji menyebut aktif mulai 3.500 rpm dan mati otomatis sekitar 8.000 rpm, sumber lain menyebut batas minimum 3.000 rpm. Jangan sebut angka.
- 3 level Y-Shift (rendah/sedang/tinggi): hanya terlihat di satu ringkasan. Cek ulang.
- Kenaikan rpm 500-1.000 saat pindah T ke S: satu sumber.
- Harga motor: ada yang menyebut varian termurah Turbo Rp 37,75 juta (Jakarta OTR), Antara menyebut mulai Rp 32,7 juta. Angka berbeda, kemungkinan mencakup varian Neo. Jangan sebut harga motor.
- Bulan peluncuran Indonesia (diduga Juni 2024): belum dikonfirmasi langsung. Aman menyebut "2024".
- Spesifikasi mesin 155 cc Blue Core, 15,3 PS/8.000 rpm, 14,2 Nm/6.500 rpm: dari ringkasan pencarian atas halaman Jepang (motor-fan.jp/young-machine), perlu dicek untuk versi Indonesia.
- Spesifikasi dinamo, algoritma TCU, part number sensor: tidak ditemukan.
- Pernyataan "pertama di dunia/Indonesia" (judul Detik) bersifat klaim promosi. Hindari atau beri atribusi "menurut Yamaha".
- Jumlah klaim Yamaha tentang efisiensi BBM: tidak diverifikasi.

## 4 ide cadangan
1. Y-Shift NMAX Turbo: kapan dipakai dan kapan tidak (perlu verifikasi batas rpm dulu).
2. Kenapa NMAX Turbo bukan turbocharger? Meluruskan salah kaprah nama "Turbo".
3. Biaya servis CVT: roller biasa vs pulley YECVT (Rp 122 ribu vs Rp 1,5 juta).
4. Apa yang terjadi kalau dinamo YECVT rusak di jalan? (mode darurat, perlu satu sumber lagi).

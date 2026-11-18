# Daftar kebutuhan aset - yecvt-nmax

Status: BELUM DIHASILKAN. Terblokir: tidak ada TTS (espeak-ng, flite, piper tidak terpasang; apt-get install ditolak izin).
Tersedia: ffmpeg, Python 3 + PIL + numpy. Tidak ada: pycairo, font Montserrat/Poppins (hanya DejaVu, Liberation, Noto, FreeFont).

## Voiceover (TTS bahasa Indonesia), satu file per adegan
Naskah persis ada di 03-script.md. Target: vo-01.wav ... vo-06.wav, total sekitar 38 dtk.
1. NMAX Turbo nggak pakai turbo. Lalu apa bedanya?
2. Namanya merujuk ke fitur YECVT, CVT yang dikontrol elektronik. Bukan turbocharger.
3. Matic biasa punya roller di pulley primer. Putaran dan gas naik, roller terlempar karena gaya sentrifugal. Rasio mengikuti itu.
4. Di YECVT, roller diganti dinamo listrik. Dinamo ini menggerakkan pulley primer. Jadi digeser secara elektrik, bukan sentrifugal.
5. Dinamo diatur TCU, otak komputernya. Dia baca sensor pulley primer dan sekunder, gas, kecepatan, putaran mesin, lalu hitung rasio ideal.
6. Rasio bisa diatur aktif. Matic tanpa roller, worth it? Tulis di komentar. Follow untuk bedah motor lainnya.

## Visual (bisa digambar vektor dengan PIL, tanpa AI)
Prompt tiap adegan ada di 04-visual.md (blok STYLE wajib). 6 adegan, 1080x1920, 30 fps:
siluet motor generik, diagram pulley (draw-on), penampang pulley primer + 3 roller biru,
dinamo oranye, diagram alur TCU + 4 ikon input, split-screen + kartu CTA.
Teks layar ditambahkan saat render. Font Montserrat belum ada; cadangan lisensi bebas yang ada: DejaVu Sans Bold.

## SFX
"tek" dan whoosh pendek: bisa disintesis dengan ffmpeg (aevalsrc/anoisesrc), bebas hak cipta. Musik: tugas Agen Musik.

## Yang dibutuhkan untuk lanjut
Salah satu: izin memasang espeak-ng (apt-get install espeak-ng), atau file voiceover dari user/TTS eksternal.

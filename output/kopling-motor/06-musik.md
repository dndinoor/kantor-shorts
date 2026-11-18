# 06 - Musik: Cara Kerja Kopling Motor

Slug: kopling-motor | Mood: santai, ramah, tempo cepat tapi latar tidak mengganggu

## Pilihan
Audio **dibuat sendiri secara prosedural** (Python + numpy, tanpa sampel atau sumber eksternal):
- Bed ambient: akor Am9 dari sinus yang sedikit di-detune dengan tremolo lambat, plus denyut bas lembut 90 BPM. Fade-in 2 dtk, fade-out 3 dtk.
- Efek: 5 whoosh pendek (noise tersapu filter) di pergantian segmen (sekitar 6, 16,8, 27,4, 36,4, 48,2 dtk) dan 2 klik kecil (18,0 dan 28,5 dtk) untuk momen jepit/lepas.

## Sumber dan lisensi
- Tidak ada sumber eksternal, tidak ada lagu/sampel pihak ketiga. Tidak ada unduhan.
- Hak cipta: karya orisinal dari kode `05-asset/render/gen_musik.py`; aman dipakai tanpa atribusi.
- Judul: "Bed Kopling (prosedural)". Lisensi: milik produksi ini, tidak ada lisensi pihak lain.

## Level mix
- Musik: gain -24 dB (rata-rata sekitar -38 dB, sekitar 20 dB di bawah voiceover rata-rata -17,6 dB).
- Ducking: sidechaincompress dari voiceover (threshold 0,03, rasio 3, attack 20 ms, release 400 ms), jadi musik makin turun saat narasi.
- SFX: gain -12 dB.
- Limiter 0,95. Hasil akhir: rata-rata -17,2 dB, puncak -0,8 dB.

## Berkas
- `final.mp4`: versi baru dengan musik (video di-copy tanpa re-encode, audio AAC 44,1 kHz mono 160k, 51,2 dtk, 1080x1920).
- `05-asset/final_tanpa_musik.mp4`: cadangan versi sebelumnya.
- `05-asset/music.wav`, `05-asset/sfx.wav`: stem mentah. `05-asset/render/gen_musik.py`: generator.

## Catatan
- Cek ffprobe: durasi 51,2 dtk, stream h264 + aac, decode tanpa error.
- Belum diaudisi oleh telinga manusia; sebaiknya user mendengarkan sekali. Bila terlalu ramai, turunkan gain musik/SFX.
- Tidak ada unggahan yang dilakukan.

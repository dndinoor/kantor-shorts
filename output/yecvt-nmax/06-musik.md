# Musik - yecvt-nmax

## Keputusan
Musik latar dibuat sendiri secara prosedural (Python + numpy), jadi tidak ada pihak ketiga dan tidak ada lagu berhak cipta.

- Sumber: skrip `05-asset/musik-generator.py` (sintesis gelombang sinus, tanpa sampel atau lagu orang lain).
- Hasil: `05-asset/musik-latar.wav` (38 dtk, 44,1 kHz stereo).
- Lisensi: karya orisinal proyek ini, tanpa atribusi wajib. Progresi akor Am-F-C-G (umum, tidak dilindungi).
- Judul: "Latar Prosedural NMAX" (internal).
- Karakter: 100 bpm, pad lembut, bass ringan, arpeggio pluck 8th, hi-hat sangat pelan. Fade-in 1,5 dtk, fade-out 2,5 dtk. Sesuai mood santai dan tempo cepat di konsep.

## Pengaturan mix (ffmpeg)
- Video asli tanpa musik disimpan: `05-asset/video-sfx-only.mp4`.
- Musik: volume -20 dB, lalu sidechaincompress (key = audio SFX, threshold 0,02, ratio 4, attack 5 ms, release 300 ms) agar musik menyingkir saat SFX berbunyi.
- Dicampur dengan SFX (amix normalize=0), alimiter 0,95. Video di-copy tanpa re-encode, audio AAC 192k.
- Karena belum ada voiceover, ducking memakai SFX sebagai pemicu. Kalau voiceover nanti ditambahkan, ganti key sidechain ke track voiceover dan rakit ulang dari `video-sfx-only.mp4`.

## Opsi alternatif (TIDAK dipakai, tidak diunduh, belum diverifikasi)
- YouTube Audio Library (YouTube Studio): lisensi tergantung track, ada yang perlu atribusi. Cek label tiap track.
- Pixabay Music: Pixabay Content License, umumnya tanpa atribusi. Syarat dan Content ID perlu dicek saat pengunduhan.
- Kevin MacLeod (incompetech): CC BY, wajib mencantumkan atribusi di deskripsi.
Bila dipakai, catat judul, URL, dan lisensi di berkas ini sebelum rakit.

## Catatan jujur
- Kualitas musik sederhana (sintesis dasar), belum didengar manusia. Mohon didengarkan sebelum publish.
- Tidak ada pengunggahan yang dilakukan.

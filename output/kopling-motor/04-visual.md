# 04 - Visual: Cara Kerja Kopling Motor

Slug: kopling-motor | Format: 1080x1920 (9:16), 30 fps | Durasi: 48 dtk (mengikuti 03-script.md) | Tanpa logo, merek, atau karakter berhak cipta

## STYLE GUIDE (berlaku untuk semua adegan)

**Gaya:** animasi penampang 2D datar (flat vector), garis bersih, sudut sedikit membulat, tanpa gradasi rumit, tanpa tekstur foto. Semua dibuat sendiri. Tidak ada motor bermerek, tangan manusia realistis, atau maskot.

**Palet warna (tetap, jangan diubah antar adegan)**
| Elemen | Hex |
|---|---|
| Latar | #0F1B2D (navy gelap) |
| Area oli (kotak penampang) | #16314D, semi transparan, titik oli #2E6FA3 |
| Pelat gesek | #F2A541 (oranye) |
| Pelat baja | #9FB3C8 (abu-biru) |
| Keranjang luar (basket) | #5C6B80 |
| Hub dalam | #3E4C60 |
| Pegas | #3DDC97 (hijau) |
| Pelat penekan | #E8EEF5 (putih keabuan) |
| Sorotan celah / panah | #FFE14D (kuning) |
| Panas / peringatan | #FF4D4D (merah) |
| Aman / benar (rem, netral) | #3DDC97 |
| Teks | #FFFFFF, outline/bayangan #0F1B2D |

**Konsistensi "karakter" (objek tetap):** satu model penampang yang sama di semua adegan. Tumpukan pelat tegak lurus (vertikal): pelat penekan + pegas di ATAS, 4 pelat gesek (oranye) berselang-seling dengan 4 pelat baja (abu), keranjang luar di sisi kiri-kanan (menjepit tab pelat oranye), hub dalam di tengah (menjepit tab pelat abu). Posisi tumpukan tetap di tengah layar (pusat sekitar x=540, y=860) di semua adegan, hanya zoom/celah yang berubah. Putaran ditandai garis-garis penanda (strip) bergerak pada tepi pelat.

**Tipografi:** Poppins Bold (cadangan: Montserrat Bold, lalu DejaVu Sans Bold). Semua berlisensi bebas (OFL). Judul layar 84-96 px, label 48-56 px, CTA 72 px. Huruf kapital hanya untuk kata kunci (SEGINI, TERHUBUNG, TERPUTUS, JANGAN, REM). Maks 2 baris per blok, maks sekitar 22 karakter per baris.

**Posisi aman (YouTube Shorts UI)**
- Margin atas: 220 px kosong (status bar, judul channel).
- Margin bawah: 480 px kosong (deskripsi, tombol, judul).
- Margin kanan: 160 px kosong (tombol suka/komentar/bagikan).
- Margin kiri: 60 px.
- Jadi kotak aman teks = x 60-920, y 220-1440. Teks utama di y 240-420 (atas) atau y 1180-1420 (bawah). Diagram di y 480-1180.
- Jangan taruh teks penting di bawah y=1440 atau di kanan x=920.

**Gerak umum:** ease-in-out, jangan linear. Ganti visual tiap 2-4 dtk (sesuai konsep). Animasi "jepit lalu lepas" (celah menutup/membuka) diulang ringan sebagai penanda di adegan 1, 3, 4. Teks muncul dengan fade+naik 20 px dalam 0,25 dtk.

---

## ADEGAN 1 - Hook (0-5 dtk)

**VO:** "Tuas kopling kamu tarik jauh. Tapi di dalam, cuma geser beberapa milimeter. Kok bisa putus?"
**Teks layar:** "Tarik tuas kopling... di dalam cuma gerak SEGINI." (atas, y 240-420; "SEGINI" warna #FFE14D, ukuran 1,2x)

**Shot (0-1,5 dtk):** Wide ke tuas. Siluet tuas kopling datar (bentuk generik, tanpa merek) di sisi atas, panah melengkung kuning menunjukkan tarikan besar (sudut lebar). Latar navy.
**Shot (1,5-5 dtk):** Cut ke penampang tumpukan pelat terjepit rapat. Kamera diam, lalu push-in (zoom 1,0 -> 2,2x) ke antarpelat penekan dan pelat teratas. Celah kuning kecil terbuka (sekitar 6-10 px tampak, setelah zoom terlihat jelas), lingkaran sorot kuning berdenyut, tanda ukuran "?" kecil. Tutup-buka celah 2x.
**Gerak:** tuas ditarik 0,6 dtk (ease-out), celah terbuka bersamaan, tahan, tutup lagi.

**Prompt gambar (statis, bila memakai AI):**
> Flat 2D vector cross-section of a motorcycle wet clutch plate stack, vertical 9:16, dark navy background #0F1B2D, alternating orange (#F2A541) friction plates and blue-grey (#9FB3C8) steel plates, white pressure plate on top with green (#3DDC97) springs, tiny glowing yellow gap highlighted with a circle, clean geometric shapes, no text, no logos, no brand, no people, minimal shading.

**Prompt klip (bila memakai AI video):**
> Slow push-in on a flat vector clutch plate stack cross-section, a small yellow gap opens and closes twice between the top pressure plate and the first plate, dark navy background, orange and blue-grey plates, smooth ease motion, 9:16, 5 seconds, no logos, no text.

---

## ADEGAN 2 - Isi kopling (5-16 dtk, 11 dtk)

**VO:** "Motor umumnya pakai kopling basah. Pelatnya terendam oli. Isinya pelat gesek dan pelat baja, selang-seling. Pelat gesek nyangkut ke keranjang luar. Pelat baja ke hub dalam."
**Teks layar (muncul bertahap, bawah y 1180-1420 untuk judul; label dengan garis penunjuk di samping diagram, tetap di x<920):**
1. "Kopling basah (terendam oli)" (5-8 dtk)
2. "Pelat gesek" (oranye) dan "Pelat baja" (abu) (8-11 dtk)
3. "Keranjang luar" (11-13,5 dtk), "Hub dalam" (13,5-16 dtk)

**Sub-shot:**
- 5-8 dtk: Zoom out ke penampang utuh. Kotak oli biru terisi dari bawah (naik 1 dtk), titik-titik oli melayang pelan.
- 8-11 dtk: Pelat "meledak" terpisah vertikal (exploded view, jarak antarpelat +40 px). Pelat oranye berkedip bergantian dengan abu sesuai label. Lalu kembali merapat.
- 11-13,5 dtk: Pelat oranye menyala (yang lain redup 40%), tab kiri-kanan ditandai garis ke keranjang abu-gelap. Keranjang berkedip kuning sekali.
- 13,5-16 dtk: Pelat abu menyala, tab tengah ke hub. Hub berkedip kuning.

**Prompt gambar:**
> Flat vector exploded view of a wet clutch, vertical 9:16, dark navy background, oil-filled box in translucent blue, alternating orange friction plates attached to a grey outer basket on left and right, blue-grey steel plates attached to a dark central inner hub, clean thin white leader lines, no text, no logos, no brand.

**Prompt klip:**
> Flat vector animation, clutch plates separate slightly in exploded view then reassemble, orange plates highlight then blue-grey plates highlight, blue oil dots floating, dark navy background, smooth ease, 9:16, 11 seconds, no logos.

---

## ADEGAN 3 - Terjepit / terhubung (16-26 dtk, 10 dtk)

**VO:** "Tuas dilepas, pegas mendorong pelat penekan. Tumpukan pelat terjepit rapat. Gesekan antar pelat meneruskan tenaga mesin ke transmisi. Jadi aslinya, kopling itu nyambung."
**Teks layar:** "Tuas dilepas = TERHUBUNG" (atas, y 240-420, "TERHUBUNG" hijau #3DDC97) dan "Pegas -> pelat penekan -> terjepit" (bawah, y 1200-1360, tampilkan panah sebagai ikon, bukan karakter "->" jika font tidak mendukung).

**Sub-shot:**
- 16-19 dtk: Tuas kembali ke posisi lepas (ikon kecil di pojok atas kiri). Pegas hijau tertekan memanjang, panah hijau tebal ke bawah menekan pelat penekan. Celah menutup.
- 19-22 dtk: Zoom ke tumpukan, semua pelat menempel rapat. Tanda tekanan (panah kecil ke bawah) di sepanjang pelat.
- 22-26 dtk: Sisi keranjang (kiri-kanan) berputar: strip-strip penanda bergerak di tepi pelat oranye DAN pelat abu dengan kecepatan SAMA (tanda menyatu). Panah energi kuning dari "mesin" (ikon sisi kiri) lewat tumpukan ke "transmisi" (ikon roda gigi generik sisi kanan bawah). Teks tetap.

**Prompt gambar:**
> Flat vector cross-section of a clutch pack fully clamped, green springs compressed above a white pressure plate, thick green arrows pointing down, orange and blue-grey plates touching with no gap, yellow energy arrow flowing through the plates, dark navy background, 9:16, no text, no logos.

**Prompt klip:**
> Flat vector animation, green springs push a white pressure plate down, gap closes, clutch plates press together and rotate at the same speed, yellow energy arrow flows through to a generic gear icon, dark navy background, 9:16, 10 seconds, no logos, no text.

---

## ADEGAN 4 - Dilepas / terputus (26-34 dtk, 8 dtk)

**VO:** "Tuas ditarik, pelat penekan menjauh. Cuma beberapa milimeter. Pelat jadi bisa saling tergelincir. Putaran mesin pun terputus dari transmisi."
**Teks layar:** "Tuas ditarik = TERPUTUS" (atas, "TERPUTUS" merah #FF4D4D) dan "Celah cuma beberapa milimeter" (bawah, y 1200-1360). Jangan menulis angka mm.

**Sub-shot:**
- 26-28,5 dtk: Tuas ditarik, pegas hijau memendek (ditekan balik), pelat penekan naik, celah kuning terbuka antar pelat. Zoom ke celah (1,0 -> 1,8x), garis ukur kuning tipis tanpa angka.
- 28,5-31,5 dtk: Sisi keranjang (pelat oranye) berputar (strip bergerak cepat), sisi hub (pelat abu) diam. Pelat saling bergeser (strip beda kecepatan). Panah energi kuning berhenti di tumpukan, tanda putus (garis putus-putus) ke transmisi.
- 31,5-34 dtk: Ulangi "jepit lalu lepas" ringan 1x (celah tutup -> buka) dengan label kecil "nyambung / putus".

**Prompt gambar:**
> Flat vector cross-section of a clutch pack disengaged, small yellow gap between plates, pressure plate lifted, green springs retracted, orange plates marked with motion lines, blue-grey plates still, broken dashed yellow arrow, dark navy background, 9:16, no text, no logos.

**Prompt klip:**
> Flat vector animation, pressure plate lifts slightly, small yellow gap opens between plates, outer orange plates spin while inner blue-grey plates stay still, energy arrow breaks into dashes, dark navy background, 9:16, 8 seconds, no logos, no text.

---

## ADEGAN 5 - Kesalahan umum: setengah kopling (34-45 dtk, 11 dtk)

**VO:** "Jangan kebiasaan setengah kopling di tanjakan atau macet. Pelat nggak terjepit penuh, nggak lepas penuh. Hasilnya selip, panas, kampas cepat aus. Pakai rem. Netral kalau berhenti lama."
**Teks layar:**
1. "JANGAN setengah kopling" (34-38 dtk, atas, "JANGAN" merah)
2. "Selip - Panas - Kampas aus" (38-42 dtk, bawah, tiga kata muncul berurutan, tiap kata dengan ikon kecil)
3. "Pakai REM, netral saat berhenti lama" (42-45 dtk, bawah, "REM" hijau)

**Sub-shot:**
- 34-38 dtk: Ikon siluet tanjakan + deretan motor generik (siluet abu tanpa bentuk merek). Lalu cut ke penampang: pelat setengah menempel (celah sangat kecil, pelat tampak bergetar 2 px). Tanda silang merah besar di pojok atas.
- 38-42 dtk: Pelat oranye dan abu bergesekan, strip beda kecepatan, percikan kecil merah. Warna pelat oranye perlahan bergeser ke merah (#FF4D4D) dan garis panas bergelombang naik. Pelat oranye menipis sedikit (visual "aus").
- 42-45 dtk: Wipe ke ikon baru. Ikon rem (tuas rem generik) hijau berdenyut, centang hijau. Lalu ikon netral (kotak "N" hijau pada indikator generik). Warna panas kembali dingin (merah -> oranye).

**Prompt gambar:**
> Flat vector cross-section of clutch plates half-engaged, tiny uneven gap, orange friction plates turning red from heat with wavy heat lines and small sparks, big red cross icon, dark navy background, 9:16, no text, no logos, no brand.

**Prompt klip:**
> Flat vector animation, clutch plates vibrate in half contact, orange plates glow red with rising wavy heat lines, red X appears, then wipe to a green brake lever icon with checkmark and a green "N" neutral indicator, dark navy background, 9:16, 11 seconds, no logos, no brand.

---

## ADEGAN 6 - CTA (45-48 dtk, 3 dtk)

**VO:** "Follow buat bedah isi motor lainnya."
**Teks layar:** "Follow untuk bedah isi motor lainnya" (tengah atas, y 300-520, 72 px, putih, 2 baris).

**Shot:** Penampang pelat kembali dingin dan menempel, lalu terbuka lambat (callback hook). Teks muncul di atas. Fade out ke navy dalam 0,3 dtk terakhir. Jangan menaruh tombol follow palsu, cukup teks. Tanpa logo channel kecuali dibuat sendiri.

**Prompt gambar:**
> Flat vector clutch plate stack cross-section, calm, orange and blue-grey plates, dark navy background with empty space at top for text, 9:16, no text, no logos.

---

## Catatan teknis (render dengan tool yang ada)

**Pendekatan disarankan:** Python + PIL (gambar per frame) -> pipe ke ffmpeg. Tidak perlu AI video. Seluruh visual berupa persegi panjang, garis, panah, dan teks, jadi mudah digambar prosedural dan konsisten.

1. **Satu fungsi `draw_stack(gap, spin_outer, spin_inner, heat, zoom, focus)`** yang menggambar penampang dari parameter. Semua adegan memanggil fungsi yang sama dengan parameter berbeda, jadi gaya otomatis seragam.
   - `gap` (px): 0 = terjepit; sekitar 8-14 px = terputus (digambar berlebihan agar terlihat; teks tidak menyebut angka).
   - `spin_*`: offset strip penanda per frame (px/frame). Sama = menyatu, beda = tergelincir.
   - `heat` 0-1: interpolasi warna oranye -> merah.
2. **Zoom/pan:** gambar di kanvas 2160x3840 (2x), crop sesuai `zoom/focus`, lalu resize ke 1080x1920 (LANCZOS). Hindari buram saat zoom 2,2x.
3. **Frame:** 30 fps x 48 dtk = 1440 frame. Simpan sebagai PNG di folder scratch, atau pipe langsung: `ffmpeg -f rawvideo -pix_fmt rgb24 -s 1080x1920 -r 30 -i - -c:v libx264 -pix_fmt yuv420p -crf 18 out.mp4`.
4. **Easing:** fungsi `ease(t) = 3t^2 - 2t^3` untuk gerak celah, zoom, dan fade.
5. **Teks:** PIL `ImageFont.truetype` dengan Poppins Bold (cek ada di sistem; kalau tidak, DejaVuSans-Bold). Beri stroke (`stroke_width=6`, warna navy) agar terbaca. Tulis ke layer RGBA terpisah supaya bisa difade. Ukur lebar dengan `textbbox` agar tidak lewat x=920.
6. **Alternatif SVG:** buat 1 SVG penampang, animasi dengan Python (ubah atribut y per frame), render dengan `cairosvg` (bila terpasang) ke PNG. Dipakai kalau ingin vektor tajam.
7. **Ikon (tuas, rem, roda gigi, tanjakan, N, centang, silang):** gambar sendiri dari bentuk dasar PIL (lingkaran, poligon, garis). Jangan memakai paket ikon berlisensi tidak jelas dan jangan meniru bentuk tuas/rem merek tertentu.
8. **Penyusunan:** render tiap adegan jadi klip terpisah (`scene1.mp4` dst, tanpa audio), lalu gabungkan dengan `ffmpeg -f concat`. Tambah VO dan musik di tahap Asset/Musik. Durasi tiap klip harus pas dengan tabel (5, 11, 10, 8, 11, 3 dtk = 48).
9. **Sinkron VO:** setelah VO direkam, ukur durasi kalimat dan geser titik teks/transisi. Tabel di atas adalah patokan, bukan kunci mati.
10. **Prompt AI opsional:** hanya dipakai jika tool AI tersedia dan hasilnya konsisten. Selalu sertakan palet hex dan kata "flat vector, no logos, no text". Jika hasil AI tidak konsisten antar adegan, kembali ke render prosedural. Teks selalu ditambahkan lewat PIL/ffmpeg, bukan dari AI (AI sering salah ejaan).
11. **Hak cipta:** semua elemen buatan sendiri, font OFL, tanpa motor/merek nyata. Periksa ulang tidak ada siluet motor yang menyerupai model tertentu.
12. **Pemeriksaan akhir:** ekspor 1 frame per adegan, tempel overlay kotak aman (x 60-920, y 220-1440) dan pastikan semua teks di dalamnya. Kontras teks minimal terbaca di layar ponsel kecil.

## Batasan fakta yang dipatuhi
- Tanpa angka milimeter di layar, hanya "beberapa milimeter" (celah digambar berlebihan untuk keterbacaan; tidak mewakili ukuran nyata).
- Tanpa menyebut bahan pelat atau tipe pegas (hanya "pegas").
- Tanpa klaim "18% selip" dan tanpa bahasan oli JASO.
- Status verifikasi sumber utama masih sama seperti di 01-riset.md dan 03-script.md (belum dibaca langsung). Visual hanya mengikuti naskah.
- Tidak ada unggahan yang dilakukan.

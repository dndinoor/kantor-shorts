# Visual: "NMAX Turbo" Ini Bukan Turbo. Ini Matic Tanpa Roller!

Format: 9:16, 1080x1920 px, 30 fps, 38 detik, 6 adegan. Sumber: 02-konsep.md dan 03-script.md.

## Style guide (berlaku untuk semua adegan)

**Gaya:** animasi 2D flat vektor, tanpa gradasi berat, tanpa tekstur foto, garis tebal seragam (stroke 6 px, ujung membulat). Sudut membulat. Gaya diagram edukasi, bukan realistis.

**Palet (kode tetap, jangan diubah antar adegan)**

| Peran | Warna | Hex |
|---|---|---|
| Latar | biru-hitam gelap | #0E1117 |
| Panel/garis bantu | abu gelap | #1E2530 |
| Roller / CVT biasa | biru | #2F8CFF |
| Dinamo / YECVT | oranye | #FF8A1F |
| Pulley, sabuk, siluet motor | abu terang | #B8C0CC |
| Teks utama | putih | #FFFFFF |
| Coret "TURBO" / peringatan | merah | #FF3B30 |

Aturan warna: biru hanya untuk roller dan konsep CVT biasa. Oranye hanya untuk dinamo, TCU, dan YECVT. Merah hanya di adegan 1.

**Objek yang konsisten di semua adegan**
- Motor: siluet generik matic, satu warna abu terang #B8C0CC, tanpa detail, tanpa logo, tanpa tulisan, tanpa lampu/bodi khas merek. Tampak samping, menghadap kanan.
- Pulley: dua keping kerucut (belahan) abu terang dengan sabuk V abu gelap. Pulley primer di kiri/atas, sekunder di kanan/bawah, selalu pada posisi relatif yang sama.
- Roller: 3 bulatan biru #2F8CFF, diameter sama.
- Dinamo: kotak membulat oranye dengan ikon petir putih dan lingkaran rotor. Bukan gambar motor listrik merek tertentu.
- TCU: kotak membulat oranye outline, di dalamnya pola chip sederhana. Tanpa tulisan di gambar (teks ditambah saat editing).
- Tidak ada karakter manusia, maskot, logo, atau foto resmi.

**Teks layar**
- Font: Montserrat ExtraBold (judul/kata kunci) dan Montserrat SemiBold (keterangan). Lisensi SIL OFL, bebas pakai. Cadangan: Poppins Bold.
- Ukuran: judul 110-140 px, keterangan 56-64 px, label input 44 px (minimum, jangan lebih kecil agar terbaca di HP).
- Warna teks putih, dengan stroke gelap 6 px #0E1117 agar terbaca. Kata kunci diberi warna sesuai palet (biru/oranye).
- Muncul sinkron dengan kata yang diucapkan: pop-in 6 frame (scale 90% ke 100%), keluar fade 4 frame.
- Subtitle voiceover: besar, tengah-bawah, maks 2 baris, 32 karakter per baris, putih dengan stroke gelap.

**Safe area YouTube Shorts (kanvas 1080x1920)**
- Atas: kosongkan 0-250 px (bilah atas, judul/pencarian).
- Bawah: kosongkan 1440-1920 px (judul, nama channel, deskripsi, tombol subscribe).
- Kanan: kosongkan lebar 150 px terakhir (x 930-1080) untuk tombol like/komentar/share.
- Kiri: margin 60 px.
- Zona aman konten: x 60-930, y 250-1440. Teks judul di y 300-700. Subtitle di y 1180-1380 (tengah-bawah, masih di atas zona UI bawah). Visual utama (diagram) di y 600-1150.

**Transisi:** hard cut dengan whoosh pendek di batas adegan, kecuali disebut lain. Di dalam adegan ganti visual tiap 2-4 detik sesuai konsep.

**Aturan prompt AI (untuk Agen Asset)**
- Selalu tempel blok STYLE di bawah ke setiap prompt.
- Gambar AI tidak boleh berisi teks. Semua teks ditambah saat editing supaya tidak salah eja.
- Kalau hasil AI berubah gaya atau warna, buat ulang atau gambar manual di vektor (Figma/Inkscape) memakai palet di atas. Untuk diagram pulley, vektor/animasi manual lebih akurat daripada generasi AI.

```
STYLE: flat 2D vector illustration, educational diagram style, uniform thick
rounded outlines, no gradients, no textures, no shadows, solid dark background
#0E1117, vertical 9:16. Palette only: blue #2F8CFF (rollers), orange #FF8A1F
(electric motor, controller), light gray #B8C0CC (pulleys, motorcycle silhouette),
dark gray #1E2530 (belt, panels), white #FFFFFF. Motorcycle is a generic scooter
silhouette in a single flat gray, side view facing right, no logo, no brand, no
text, no letters, no people, no characters.
```

---

## Adegan 1 - Hook (0:00-0:03)

**Voiceover:** NMAX Turbo nggak pakai turbo. Lalu apa bedanya?

**Shot:** close-up tengah, statis lalu punch-in cepat. Teks "TURBO" memenuhi lebar layar di tengah. Di belakangnya, siluet motor generik pudar (opacity 25%) di y 900-1250.

**Animasi:**
- 0,0-0,5: "TURBO" pop-in dengan zoom cepat 120% ke 100% + SFX "tek" (bebas lisensi).
- 0,5-1,2: garis merah #FF3B30 menyapu dari kiri ke kanan mencoret "TURBO", teks menjadi abu redup.
- 1,2-3,0: "BUKAN TURBOCHARGER" masuk dari bawah di bawah teks yang dicoret. Siluet motor naik opacity ke 60%.

**Teks layar:**
- "TURBO" Montserrat ExtraBold 160 px putih, posisi tengah x, y 420-580.
- "BUKAN TURBOCHARGER" ExtraBold 90 px, dua baris ("BUKAN" / "TURBOCHARGER"), kata "BUKAN" merah, y 640-860. Pastikan "TURBOCHARGER" muat di lebar 870 px (turunkan ke 80 px kalau perlu).
- Subtitle di y 1180-1380.

**Prompt gambar (latar):**
```
Generic scooter motorcycle silhouette, side view facing right, centered lower
half of frame, single flat light gray shape, empty dark upper half for title
text. [STYLE]
```
Teks "TURBO", coretan merah, dan "BUKAN TURBOCHARGER" dibuat di editor, bukan AI.

**Prompt klip (opsional, bila memakai image-to-video):**
```
Subtle slow push-in zoom on the flat silhouette, 3 seconds, no morphing, no new
objects, keep flat 2D style. [STYLE]
```

---

## Adegan 2 - Pembuka YECVT (0:03-0:08)

**Voiceover:** Namanya merujuk ke fitur YECVT, CVT yang dikontrol elektronik. Bukan turbocharger.

**Shot:** medium, statis dengan gerakan ringan. Dua bagian (3-5,5 dan 5,5-8) agar tidak lebih dari 2,5-3 detik per visual.

**Animasi:**
- 3,0-5,5: transisi dari adegan 1 dengan siluet motor mengecil ke kiri-bawah. Judul "YECVT" pop-in di tengah atas, huruf oranye. Di bawahnya muncul diagram pulley sederhana (dua pulley + sabuk) digambar dengan efek "draw-on" garis.
- 5,5-8,0: teks "CVT berkontrol elektronik" muncul. Kabel/garis putus-putus oranye menjalar ke pulley primer sebagai petunjuk "elektronik". Diagram berdenyut sekali pada kata "elektronik".

**Teks layar:**
- "YECVT" ExtraBold 140 px oranye #FF8A1F, tengah x, y 320-470.
- "CVT berkontrol elektronik" SemiBold 60 px putih, dua baris, y 500-620.
- Diagram pulley di y 700-1150.

**Prompt gambar (diagram):**
```
Simple CVT pulley diagram, two conical split pulleys connected by a V-belt, primary
pulley on the left, secondary pulley on the right, front-facing technical diagram,
clean geometry, centered, empty space above. Thin dashed orange line running to the
left pulley. [STYLE]
```

**Prompt klip:**
```
Line-draw animation: the pulleys and belt are drawn on stroke by stroke, then a
dashed orange line extends to the left pulley and pulses once. 5 seconds, flat 2D,
no camera shake. [STYLE]
```

---

## Adegan 3 - CVT biasa (0:08-0:16)

**Voiceover:** Matic biasa punya roller di pulley primer. Putaran dan gas naik, roller terlempar karena gaya sentrifugal. Rasio mengikuti itu.

**Shot:** medium close-up pada pulley primer, tampak samping (penampang) supaya terlihat belahan kerucut dan roller. Tiga sub-visual: (a) 8-10,5 pulley dan roller diam, (b) 10,5-13,5 putaran naik, (c) 13,5-16 pulley menyempit dan sabuk naik.

**Animasi:**
- 8,0-10,5: label "CVT BIASA" masuk. Pulley primer penampang dengan 3 roller biru di bagian dalam dekat poros. Sorot ringan (glow biru tipis) pada roller saat kata "roller".
- 10,5-13,5: pulley berputar makin cepat (motion lines). Roller bergeser keluar menjauhi poros. Panah biru kecil menunjuk keluar diberi teks "sentrifugal" (hanya pada subtitle/label, bukan gambar AI).
- 13,5-16,0: roller mendorong belahan pulley saling mendekat, celah menyempit, sabuk terdorong ke diameter lebih besar. Ukur rasio tampil sebagai bar sederhana yang bergerak (tanpa angka).

**Teks layar:**
- "CVT BIASA" ExtraBold 100 px biru #2F8CFF, y 320-440.
- "Roller + gaya sentrifugal" SemiBold 60 px putih, y 460-600.
- Diagram di y 650-1150. Subtitle y 1180-1380.

**Prompt gambar (frame awal):**
```
Cross-section diagram of a CVT primary pulley: two conical halves with a gap, three
blue round rollers sitting near the center shaft, a gray V-belt between the halves,
side view, clean flat geometry, empty space above. [STYLE]
```
**Prompt gambar (frame akhir):**
```
Same cross-section CVT primary pulley, same composition, but the three blue rollers
have moved outward toward the outer edge, the two conical halves are closer together
with a narrow gap, the belt sits at a larger radius. Small blue arrow pointing
outward. [STYLE]
```
**Prompt klip (frame awal ke akhir):**
```
Interpolate from first frame to last frame over 8 seconds: the pulley spins faster
(radial motion lines), the blue rollers slide outward, the halves squeeze together
and push the belt outward. Smooth, mechanical, flat 2D, camera static. [STYLE]
```

---

## Adegan 4 - YECVT: roller diganti dinamo (0:16-0:23)

**Voiceover:** Di YECVT, roller diganti dinamo listrik. Dinamo ini menggerakkan pulley primer. Jadi digeser secara elektrik, bukan sentrifugal.

**Shot:** komposisi sama persis dengan adegan 3 (pulley primer penampang, posisi sama) supaya penonton langsung membandingkan. Sub-visual: (a) 16-18,5 roller memudar, (b) 18,5-21 dinamo masuk, (c) 21-23 pulley bergeser.

**Animasi:**
- 16,0-18,5: label berubah dari "CVT BIASA" ke "YECVT" (wipe cepat, warna biru ke oranye). Tiga roller biru memudar menjadi outline putus-putus lalu hilang (efek "dihapus").
- 18,5-21,0: kotak dinamo oranye geser masuk dari kanan ke posisi di samping pulley, ikon petir berkedip sekali, SFX "tek".
- 21,0-23,0: dinamo berputar, batang/ulir oranye mendorong belahan pulley menutup. Percikan petir kecil oranye. Garis biru "sentrifugal" dicoret/lenyap sebagai penegas.

**Teks layar:**
- "YECVT" ExtraBold 110 px oranye, y 320-450.
- "Roller diganti dinamo" SemiBold 60 px putih, kata "dinamo" oranye, y 470-600.
- Diagram y 650-1150.

**Prompt gambar (frame awal, roller menghilang):**
```
Cross-section diagram of a CVT primary pulley, same composition as before, the
three rollers are replaced by faded dashed blue outlines, a small orange rounded
box with a white lightning bolt icon and a rotor circle waits at the right side.
[STYLE]
```
**Prompt gambar (frame akhir):**
```
Cross-section diagram of a CVT primary pulley, same composition, no rollers, an
orange electric motor box with white lightning bolt attached beside the pulley,
an orange threaded shaft pushing the two conical halves together, small orange
sparks, belt at larger radius. [STYLE]
```
**Prompt klip:**
```
Over 7 seconds: dashed blue roller outlines fade away, an orange electric motor
box slides in from the right, its rotor spins and an orange shaft pushes the pulley
halves together. Same framing as the previous scene, flat 2D, camera static. [STYLE]
```

---

## Adegan 5 - TCU, otak komputernya (0:23-0:31)

**Voiceover:** Dinamo diatur TCU, otak komputernya. Dia baca sensor pulley primer dan sekunder, gas, kecepatan, putaran mesin, lalu hitung rasio ideal.

**Shot:** wide diagram alur (flow) vertikal, kamera statis dengan sedikit pan turun mengikuti alur. Adegan padat, jadi input dimunculkan satu per satu (stagger 0,6-0,8 detik).

**Animasi:**
- 23,0-25,0: kotak "TCU" oranye outline muncul di tengah (y 750-950), ikon chip berdenyut. Teks "TCU = otak komputer" masuk di atas.
- 25,0-29,0: empat ikon input muncul bergantian dari kiri dengan panah biru-abu masuk ke TCU: (1) sensor pulley primer dan sekunder (dua ikon pulley kecil), (2) gas (ikon handel gas), (3) kecepatan (ikon speedometer tanpa angka), (4) putaran mesin (ikon tachometer tanpa angka). Tiap ikon sinkron dengan kata yang diucapkan.
- 29,0-31,0: dari TCU keluar panah oranye tebal ke ikon dinamo (kecil, kanan/bawah). Dinamo berkedip, bar rasio bergeser ke posisi "ideal" (tanpa angka).

**Teks layar:**
- "TCU = otak komputer" ExtraBold 80 px, "TCU" oranye, y 300-420.
- Label input SemiBold 44 px putih, di samping ikon: "Sensor pulley primer + sekunder", "Gas", "Kecepatan", "Putaran mesin". Kolom ikon x 60-500, TCU di x 520-880. Jangan melewati x 930.
- Tidak ada angka rpm, tidak ada hitungan sensor (batasan konten).
- Subtitle y 1180-1380 (tepatnya tidak menimpa ikon: letakkan flow di y 480-1150).

**Prompt gambar (frame utama):**
```
Flow diagram, vertical layout: on the left a column of four simple flat icons
(two small pulleys, a throttle grip, a speedometer dial without numbers, an engine
tachometer dial without numbers) with thin gray arrows pointing right into a
central orange rounded-rectangle controller box with a simple chip pattern, from
which a thick orange arrow points to a small orange electric motor box with a
lightning bolt. No text, no numbers. [STYLE]
```
**Prompt klip:**
```
Stagger animation over 8 seconds: the controller box appears and pulses, the four
icons slide in one by one with arrows connecting to the controller, then a thick
orange arrow flows from the controller to the electric motor which blinks. Flat
2D, camera static with a very slight downward pan. [STYLE]
```
Catatan Asset: ikon dibuat terpisah (PNG transparan) supaya mudah dianimasikan di editor.

---

## Adegan 6 - Penutup + CTA (0:31-0:38)

**Voiceover:** Rasio bisa diatur aktif. Matic tanpa roller, worth it? Tulis di komentar. Follow untuk bedah motor lainnya.

**Shot:** split-screen vertikal singkat (31-34) lalu close tunggal untuk CTA (34-38).

**Animasi:**
- 31,0-34,0: layar dibagi dua horizontal dengan garis tengah putih di y 960. Atas: pulley dengan roller biru bergeser sendiri (loop pendek). Bawah: pulley dengan dinamo oranye menggeser aktif dengan panah dari TCU kecil. Label singkat tiap panel. Setelah itu panel biru meredup, panel oranye membesar.
- 34,0-36,0: panel oranye mengisi layar, teks "Rasio diatur aktif" pop-in.
- 36,0-38,0: kartu CTA masuk dari bawah (di dalam safe area): "Worth it? Tulis di komentar" lalu "Follow". Ikon komentar dan ikon follow generik (gelembung chat, tanda plus), bukan ikon resmi YouTube. Siluet motor generik kecil bergerak lewat di bawah kartu sebagai penutup. Akhiri dengan hold 0,5 detik, tanpa fade panjang supaya loop bersih.

**Teks layar:**
- Label panel: "Roller" (biru) atas, "Dinamo" (oranye) bawah, SemiBold 50 px, di x 60 dan y 300 / y 980.
- "Rasio diatur aktif" ExtraBold 100 px putih, "aktif" oranye, y 330-560.
- "Worth it? Tulis di komentar" ExtraBold 76 px, y 760-940, dua baris.
- "Follow" ExtraBold 90 px oranye di pil/tombol abu gelap, y 1000-1120. Semua di atas y 1440 dan kiri x 930, jadi tidak tertutup UI.

**Prompt gambar (split-screen, dua panel dibuat terpisah lalu digabung):**
```
Panel A: CVT primary pulley cross-section with three blue rollers slid outward,
labeled by color only. [STYLE]
```
```
Panel B: CVT primary pulley cross-section with an orange electric motor box pushing
the halves together, a small orange controller box with chip pattern and an arrow
to the motor. [STYLE]
```
**Prompt gambar (latar CTA):**
```
Dark empty background with a small flat gray scooter silhouette at the bottom-left
driving right, soft orange accent shape at the top right, large empty center for
text. [STYLE]
```
**Prompt klip:**
```
Short 7 second sequence: top panel blue rollers slide on their own, bottom panel
orange motor actively pushes the pulley, then the bottom panel expands to fill the
frame and the scene settles on a calm empty background with a small scooter
silhouette driving across the bottom. Flat 2D. [STYLE]
```

---

## Ringkasan timecode

| No | Detik | Visual utama | Warna dominan |
|----|-------|--------------|---------------|
| 1 | 0-3 | "TURBO" dicoret, "BUKAN TURBOCHARGER", siluet motor | putih, merah |
| 2 | 3-8 | Judul YECVT, diagram pulley draw-on | oranye |
| 3 | 8-16 | Pulley primer, roller terlempar | biru |
| 4 | 16-23 | Roller diganti dinamo, pulley bergeser elektrik | oranye |
| 5 | 23-31 | TCU, input sensor/gas/kecepatan/putaran, output ke dinamo | oranye |
| 6 | 31-38 | Split roller vs dinamo, CTA | biru + oranye |

## Catatan untuk Agen Asset dan editor
- Kata "NMAX" hanya ada di voiceover. Tidak ditampilkan sebagai teks di layar dan tidak ada logo/bentuk bodi khas. Siluet motor harus generik.
- Tidak boleh ada angka rpm, harga, jumlah sensor, mode darurat, garansi, atau Y-Shift di teks mana pun (lihat batasan di 02-konsep.md).
- Adegan 1 dan 5 padat. Kalau voiceover diperpanjang hingga sekitar 42 detik (opsi di 03-script.md), tambahkan hold 1-2 detik di akhir adegan 5 dan perpanjang adegan 6 dengan jumlah yang sama.
- Diagram pulley adalah penyederhanaan edukatif, bukan gambar teknis akurat. Kalau ada keraguan akurasi mekanis, cocokkan dengan hasil cek ulang fakta (*) di 01-riset.md sebelum final.
- Musik dan SFX hanya yang bebas lisensi. Keputusan musik ada di agen Musik.
- Tidak ada upload. Paket ini hanya untuk produksi aset.

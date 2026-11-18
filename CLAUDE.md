# Kantor YouTube Shorts

Ruang kerja 7 agen untuk memproduksi YouTube Shorts (vertikal 9:16, maks 60 detik).

## Aturan tetap
1. **Tidak ada agen yang boleh mengunggah atau mempublikasikan video.** Agen Publish hanya menyiapkan paket. Upload hanya dilakukan user secara manual atau setelah user menulis persetujuan eksplisit ("setuju upload").
2. Setiap agen menulis hasilnya ke `output/<slug-video>/` supaya agen berikutnya bisa membacanya.
3. Ide wajib diverifikasi (sumber/fakta dicek) sebelum lanjut ke konsep.
4. Jangan memakai karakter, logo, atau musik berhak cipta tanpa lisensi.

## Urutan kerja
Riset -> Konsep -> Script -> Visual -> Asset -> Musik -> Publish -> **menunggu izin user**

## Struktur output per video
```
output/<slug>/
  01-riset.md
  02-konsep.md
  03-script.md
  04-visual.md
  05-asset/        (gambar, klip, voiceover)
  06-musik.md
  07-publish.md    (judul, deskripsi, tag, checklist)
  final.mp4        (jika sudah dirakit)
```

Jalankan dengan perintah: `/produksi-shorts <topik atau niche>`

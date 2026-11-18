---
description: Jalankan seluruh kantor Shorts (7 agen) untuk satu video. Berhenti sebelum upload.
argument-hint: <topik atau niche>
---

Topik: $ARGUMENTS

Jalankan pipeline produksi satu video Shorts secara berurutan dengan subagent. Buat slug pendek dari topik dan folder `output/<slug>/`.

1. `riset` -> hasil ke 01-riset.md
2. `konsep` -> 02-konsep.md
3. `script` -> 03-script.md
4. `visual` -> 04-visual.md
5. `asset` -> 05-asset/ dan final.mp4
6. `musik` -> 06-musik.md
7. `publish` -> 07-publish.md

Aturan:
- Tunggu satu agen selesai sebelum memulai agen berikutnya.
- Jika satu agen gagal atau butuh tool/API yang belum ada, berhenti dan laporkan.
- Setelah agen Publish selesai, **berhenti**. Tampilkan ringkasan paket dan tanya user: "Upload sekarang?". Jangan unggah apa pun tanpa jawaban "setuju upload".

# Kas CLI — Pencatat Pengeluaran dari Terminal

![Python](https://img.shields.io/badge/python-3.12-blue) ![License](https://img.shields.io/badge/license-MIT-green)

CLI pencatat pengeluaran pribadi: tambah, laporan mingguan, total per kategori.
Data tersimpan lokal di `data/kas.json` — tanpa server, tanpa akun.

## Cara jalan
```bash
python3 kas.py tambah 25000 "kopi"
python3 kas.py laporan
```

## Fitur
- `tambah <jumlah> <deskripsi>` — catat pengeluaran
- `laporan` — total minggu ini + kategori terbesar
- `daftar` — semua entri

## Screenshot
(Tambahkan screenshot terminal setelah menjalankan `laporan`.)

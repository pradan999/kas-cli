#!/usr/bin/env python3
"""Kas CLI — pencatat pengeluaran sederhana (data lokal JSON)."""
import json, sys
from pathlib import Path
DATA = Path(__file__).parent / "data" / "kas.json"
def muat():
    return json.loads(DATA.read_text()) if DATA.exists() else []
def simpan(entri):
    DATA.parent.mkdir(exist_ok=True); DATA.write_text(json.dumps(entri, indent=2))
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "laporan"
    entri = muat()
    if cmd == "tambah":
        entri.append({"jumlah": int(sys.argv[2]), "deskripsi": sys.argv[3]})
        simpan(entri); print(f"Ditambahkan: Rp {int(sys.argv[2]):,}")
    elif cmd == "laporan":
        total = sum(e["jumlah"] for e in entri)
        print(f"Total: Rp {total:,} dari {len(entri)} entri")
    elif cmd == "daftar":
        for e in entri: print(f"- Rp {e['jumlah']:,} : {e['deskripsi']}")

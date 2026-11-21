"""Sistem Analisis Disparitas Pendapatan Daerah (SIDISPA) — entry point aplikasi Streamlit.

Jalankan dengan:  streamlit run app.py
"""

import sys
from pathlib import Path

import streamlit as st

# ------------------------------------------------------------------
# Muat ulang modul lokal bila filenya berubah.
# Di server (mis. Streamlit Cloud) proses Python bisa tetap hidup setelah
# kode di-update, sehingga utils/charts/laporan versi LAMA masih tersimpan
# di memori dan memicu "ImportError: cannot import name ..." pada halaman
# yang memakai fungsi baru. Blok ini membuang versi lama dari memori agar
# halaman selalu memakai file terbaru.
# ------------------------------------------------------------------
_FOLDER = Path(__file__).resolve().parent
_MODUL_LOKAL = ("utils", "charts", "laporan", "storage", "auth", "mailer", "db", "tema")
_cap_waktu = getattr(sys, "_ria_cap_waktu", {})
_berubah = False
for _nama in _MODUL_LOKAL:
    _berkas = _FOLDER / f"{_nama}.py"
    if _berkas.exists():
        _waktu = (_berkas.stat().st_mtime_ns, _berkas.stat().st_size)
        if _cap_waktu.get(_nama) != _waktu:
            _cap_waktu[_nama] = _waktu
            _berubah = True
if _berubah:
    if "db" in sys.modules:
        try:
            sys.modules["db"].tutup_semua()  # lepas koneksi database lama dengan rapi
        except Exception:
            pass
    for _nama in _MODUL_LOKAL:
        sys.modules.pop(_nama, None)
sys._ria_cap_waktu = _cap_waktu

import auth  # noqa: E402  (harus setelah pembersihan modul lama di atas)
import db  # noqa: E402
import storage  # noqa: E402
import tema  # noqa: E402
from sqlalchemy.exc import SQLAlchemyError  # noqa: E402

# ------------------------------------------------------------------
# Paksa tema TERANG dari kode.
# Bila .streamlit/config.toml tidak ikut ter-upload (folder berawalan titik sering
# terlewat) atau server belum di-restart, Streamlit memakai tema bawaan yang mengikuti
# mode gelap perangkat sehingga tabel, kolom isian, dan pilihan tampil hitam.
# Opsi tema di bawah menyamai config.toml; bila sudah sama, blok ini tidak melakukan apa pun.
# ------------------------------------------------------------------
def _paksa_tema_terang() -> None:
    pilihan = {
        "theme.base": "light",
        "theme.primaryColor": "#1b8fe8",
        "theme.backgroundColor": "#e8f7ff",
        "theme.secondaryBackgroundColor": "#d4efff",
        "theme.textColor": "#06284a",
    }
    try:
        sudah = all(st.get_option(k) == v for k, v in pilihan.items())
    except Exception:
        sudah = False
    if sudah:
        return
    for kunci, nilai in pilihan.items():
        try:
            st._config.set_option(kunci, nilai)
        except Exception:
            pass
    if not st.session_state.get("_tema_terang_diset"):
        st.session_state["_tema_terang_diset"] = True
        st.rerun()  # jalankan ulang sekali agar browser menerima tema baru


_paksa_tema_terang()

st.set_page_config(
    page_title="Sistem Analisis Disparitas Pendapatan Daerah",
    page_icon="📊",
    layout="wide",
)

tema.terapkan()  # tema Frutiger Aero (CSS global)

st.html(
    """
    <style>
    /* Teks metrik tidak boleh terpotong (...) - biarkan turun ke baris berikutnya */
    [data-testid="stMetricLabel"] *,
    [data-testid="stMetricValue"] * {
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
        overflow-wrap: anywhere;
    }
    [data-testid="stMetricValue"] { line-height: 1.25; }

    /* Tampilan layar kecil (HP) */
    @media (max-width: 640px) {
        .block-container {
            padding: 3.5rem 0.9rem 4rem 0.9rem !important;
        }
        h1 { font-size: 1.7rem !important; line-height: 1.25 !important; }
        h2, h3 { font-size: 1.3rem !important; line-height: 1.3 !important; }
        [data-testid="stMetricValue"] { font-size: 1.6rem !important; }
        [data-testid="stVerticalBlockBorderWrapper"] { padding: 0.25rem; }
        .stButton > button, .stDownloadButton > button {
            width: 100%;
            min-height: 2.75rem;
        }
    }
    </style>
    """
)

PESAN_DB = (
    "Tidak dapat terhubung ke database akun. Coba muat ulang beberapa saat lagi; "
    "bila terus terjadi, hubungi administrator aplikasi."
)


def tampilkan_galat_db(exc: Exception) -> None:
    """Catat galat database ke log (tanpa password) dan beri petunjuk penyebabnya.

    Detail teknis hanya ditampilkan di layar bila secret DEBUG_DB = "true"."""
    detail = db.samarkan(f"{type(exc).__name__}: {exc}")
    print(f"[SIDISPA] Galat database: {detail}", file=sys.stderr, flush=True)
    st.error(PESAN_DB)
    st.info("**Petunjuk untuk pemilik aplikasi:** " + db.petunjuk_galat(exc), icon=":material/build:")
    if str(db.config("DEBUG_DB", "")).strip().lower() in ("1", "true", "ya", "yes"):
        st.code(detail, language=None)


try:
    auth.pulihkan_sesi()   # masuk otomatis dari cookie (mis. setelah refresh)
    auth.segarkan_sesi()   # pastikan akun masih aktif dan peran terbaru
    storage.siapkan_data() # pulihkan data pengguna dari database bila folder lokal kosong
except SQLAlchemyError as exc:
    tampilkan_galat_db(exc)
    st.stop()

pengguna = auth.pengguna_aktif()

menu = {
    "MENU UTAMA": [
        st.Page("views/dashboard.py", title="Dashboard",
                icon=":material/dashboard:", default=True),
        st.Page("views/import_data.py", title="Import Data BPS",
                icon=":material/upload_file:", url_path="import-data"),
        st.Page("views/data_pendapatan.py", title="Data Pendapatan",
                icon=":material/table_chart:", url_path="data-pendapatan"),
        st.Page("views/analisis.py", title="Analisis Disparitas",
                icon=":material/calculate:", url_path="analisis"),
        st.Page("views/visualisasi.py", title="Visualisasi",
                icon=":material/bar_chart:", url_path="visualisasi"),
        st.Page("views/tentang.py", title="Tentang Aplikasi",
                icon=":material/info:", url_path="tentang"),
    ],
}
if pengguna:
    menu["AKUN"] = [
        st.Page("views/akun.py", title="Akun Saya",
                icon=":material/account_circle:", url_path="akun"),
    ]
    if auth.adalah_admin():
        menu["ADMINISTRASI"] = [
            st.Page("views/kelola_pengguna.py", title="Kelola Pengguna",
                    icon=":material/manage_accounts:", url_path="kelola-pengguna"),
        ]
else:
    # Aplikasi terbuka untuk tamu. Masuk/Daftar bersifat opsional: hanya pengguna yang
    # masuk yang datanya tersimpan permanen.
    menu["AKUN"] = [
        st.Page("views/login.py", title="Masuk",
                icon=":material/login:", url_path="login"),
        st.Page("views/register.py", title="Daftar",
                icon=":material/person_add:", url_path="register"),
        st.Page("views/lupa_password.py", title="Lupa Password",
                icon=":material/lock_reset:", url_path="lupa-password"),
    ]

halaman = st.navigation(menu)

with st.sidebar:
    if pengguna:
        st.markdown(
            f"**{auth.escape_markdown(pengguna['nama'])}**  \n"
            f"@{auth.escape_markdown(pengguna['username'])}"
        )
        if st.button("Keluar", icon=":material/logout:", key="btn_keluar_sidebar"):
            auth.keluar()
            st.rerun()
        peringatan = st.session_state.get(storage.PERINGATAN_KEY)
        if peringatan:
            st.warning(peringatan)
    st.caption("Academic Research Project · Version 1.0")

auth.tampilkan_toast()
auth.terapkan_cookie()  # tulis/hapus cookie sesi di browser bila ada yang tertunda

try:
    halaman.run()
except SQLAlchemyError as exc:
    tampilkan_galat_db(exc)
finally:
    try:
        storage.sinkronkan_data()  # simpan perubahan data pengguna ke database
    except SQLAlchemyError:
        pass

"""Tema visual FRUTIGER AERO untuk seluruh aplikasi.

Gaya langit biru, kaca bening (glass), gelembung, dan tombol mengilap ala Windows Vista/7.
Hanya mengubah tampilan (CSS). Tidak ada fitur, data, maupun teks aplikasi yang berubah.
Dipanggil sekali dari app.py lewat ``tema.terapkan()``.
"""

import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap');

:root {
    --a-langit-1: #7fd0ff;
    --a-langit-2: #bfe9ff;
    --a-langit-3: #eaf9ff;
    --a-biru: #1e9bf0;
    --a-biru-tua: #0a5bd3;
    --a-aqua: #2fd4ff;
    --a-hijau: #3fcf6a;
    --a-hijau-tua: #1f9d48;
    --a-oranye: #ff9a1f;
    --a-teks: #0b3556;
    --a-pudar: #4a7396;
    --a-kaca: rgba(255, 255, 255, 0.50);
    --a-kaca-tebal: rgba(255, 255, 255, 0.72);
    --a-tepi: rgba(255, 255, 255, 0.85);
    --a-bayang: 0 8px 28px rgba(18, 105, 180, 0.22);
    --a-kilap: linear-gradient(rgba(255,255,255,.75), rgba(255,255,255,.18) 50%, rgba(255,255,255,0) 51%);
    --a-font: 'Segoe UI', 'Frutiger', 'Open Sans', 'Helvetica Neue', Arial, sans-serif;
}

/* ---------- Latar: langit, cahaya matahari, gelembung, bukit hijau ---------- */
.stApp {
    background:
        radial-gradient(520px 520px at 88% 6%, rgba(255, 255, 255, .95), rgba(255, 255, 255, .0) 62%),
        radial-gradient(900px 420px at 10% 0%, rgba(255, 255, 255, .55), transparent 65%),
        radial-gradient(1200px 380px at 20% 108%, rgba(63, 207, 106, .55), transparent 70%),
        radial-gradient(1000px 340px at 90% 112%, rgba(30, 157, 72, .45), transparent 70%),
        linear-gradient(180deg, var(--a-langit-1) 0%, var(--a-langit-2) 45%, var(--a-langit-3) 80%, #f3fff0 100%) !important;
    background-attachment: fixed !important;
    color: var(--a-teks);
    font-family: var(--a-font);
}
/* gelembung melayang */
.stApp::before {
    content: "";
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background:
        radial-gradient(circle at 30% 30%, rgba(255,255,255,.85) 0, rgba(255,255,255,.25) 28%, rgba(120,210,255,.18) 60%, transparent 62%) 8% 78% / 150px 150px no-repeat,
        radial-gradient(circle at 30% 30%, rgba(255,255,255,.85) 0, rgba(255,255,255,.25) 28%, rgba(120,210,255,.18) 60%, transparent 62%) 92% 62% / 90px 90px no-repeat,
        radial-gradient(circle at 30% 30%, rgba(255,255,255,.85) 0, rgba(255,255,255,.25) 28%, rgba(120,210,255,.18) 60%, transparent 62%) 70% 14% / 60px 60px no-repeat,
        radial-gradient(circle at 30% 30%, rgba(255,255,255,.85) 0, rgba(255,255,255,.25) 28%, rgba(120,210,255,.18) 60%, transparent 62%) 40% 92% / 70px 70px no-repeat,
        radial-gradient(circle at 30% 30%, rgba(255,255,255,.85) 0, rgba(255,255,255,.25) 28%, rgba(120,210,255,.18) 60%, transparent 62%) 18% 20% / 44px 44px no-repeat;
    animation: a-melayang 14s ease-in-out infinite alternate;
}
/* berkas cahaya (light rays) */
.stApp::after {
    content: "";
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background: repeating-conic-gradient(from 200deg at 90% -5%,
        rgba(255,255,255,.14) 0deg 4deg, rgba(255,255,255,0) 4deg 12deg);
    mask-image: linear-gradient(200deg, #000 0%, transparent 60%);
    -webkit-mask-image: linear-gradient(200deg, #000 0%, transparent 60%);
}
@keyframes a-melayang { from { transform: translateY(0); } to { transform: translateY(-16px); } }
@keyframes a-kilau { from { background-position: -160% 0; } to { background-position: 260% 0; } }

[data-testid="stHeader"] { background: transparent !important; }
.block-container { position: relative; z-index: 1; }

/* ---------- Judul: teks tipis dengan pendar putih ala Aero ---------- */
h1, h2, h3, h4, [data-testid="stHeading"] {
    font-family: var(--a-font) !important;
    color: var(--a-teks) !important;
    letter-spacing: 0.005em;
}
h1 {
    font-weight: 300 !important;
    background: linear-gradient(180deg, #0a5bd3 0%, #1e9bf0 55%, #0a7fd0 100%);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent !important;
    filter: drop-shadow(0 2px 3px rgba(255, 255, 255, .95)) drop-shadow(0 4px 10px rgba(30, 155, 240, .35));
}
h2, h3 {
    font-weight: 600 !important;
    text-shadow: 0 1px 0 rgba(255, 255, 255, .95), 0 0 12px rgba(255, 255, 255, .8);
}
h4 { font-weight: 600 !important; color: var(--a-biru-tua) !important; text-shadow: 0 1px 0 rgba(255,255,255,.9); }
[data-testid="stHeading"] h2, [data-testid="stHeading"] h3 {
    border-bottom: 2px solid transparent;
    border-image: linear-gradient(90deg, var(--a-biru), rgba(255,255,255,.0)) 1;
    padding-bottom: .3rem;
}

p, li, span, div { font-family: var(--a-font); }
[data-testid="stCaptionContainer"], .stCaption, small { color: var(--a-pudar) !important; }
a { color: var(--a-biru-tua) !important; text-decoration: none; }
a:hover { color: var(--a-biru) !important; text-shadow: 0 0 8px rgba(255,255,255,.9); text-decoration: underline; }
hr { border: 0 !important; height: 2px; background: linear-gradient(90deg, transparent, rgba(255,255,255,.95), rgba(30,155,240,.45), rgba(255,255,255,.95), transparent) !important; }
strong, b { color: var(--a-teks); }

/* ---------- Sidebar: panel kaca ---------- */
[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, rgba(255,255,255,.65), rgba(255,255,255,.25) 40%, rgba(180,235,255,.35)),
        linear-gradient(180deg, #9fdcff, #d7f3ff) !important;
    backdrop-filter: blur(16px) saturate(140%);
    -webkit-backdrop-filter: blur(16px) saturate(140%);
    border-right: 1px solid var(--a-tepi);
    box-shadow: 4px 0 24px rgba(18, 105, 180, .25), inset -1px 0 0 rgba(255,255,255,.9);
}
[data-testid="stSidebarNav"] a, [data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] {
    border: 1px solid transparent;
    border-radius: 10px;
    color: var(--a-teks) !important;
    transition: all .2s ease;
}
[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"]:hover {
    border-color: rgba(255,255,255,.95);
    background: linear-gradient(rgba(255,255,255,.8), rgba(190,235,255,.45)) !important;
    box-shadow: 0 0 14px rgba(47, 212, 255, .65), inset 0 1px 0 #fff;
    text-decoration: none;
}
[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"][aria-current="page"] {
    border-color: rgba(10, 91, 211, .55);
    background: var(--a-kilap), linear-gradient(180deg, #5cc4ff, #1e9bf0 55%, #0a78d8) !important;
    color: #fff !important;
    text-shadow: 0 1px 2px rgba(0, 50, 110, .55);
    box-shadow: 0 3px 12px rgba(10, 91, 211, .45), inset 0 1px 0 rgba(255,255,255,.85);
}
[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"][aria-current="page"] * { color: #fff !important; }
[data-testid="stSidebarNavSeparator"],
[data-testid="stSidebar"] [data-testid="stNavSectionHeader"],
[data-testid="stSidebarNav"] span[class*="Header"] {
    color: var(--a-pudar) !important;
    font-weight: 700;
    letter-spacing: .12em;
    text-shadow: 0 1px 0 rgba(255,255,255,.9);
}

/* ---------- Tombol: kaca mengilap (glossy) ---------- */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button,
[data-testid="stPageLink"] a {
    font-family: var(--a-font);
    font-weight: 600;
    color: var(--a-teks) !important;
    background: var(--a-kilap), linear-gradient(180deg, #f4fbff, #bfe6fb 55%, #9fd6f5) !important;
    border: 1px solid rgba(60, 140, 200, .75) !important;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(18, 105, 180, .3), inset 0 1px 0 rgba(255,255,255,.95), inset 0 -1px 0 rgba(255,255,255,.35);
    text-shadow: 0 1px 0 rgba(255,255,255,.9);
    transition: all .18s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover,
[data-testid="stPageLink"] a:hover {
    background: var(--a-kilap), linear-gradient(180deg, #ffffff, #c9efff 55%, #8fe0ff) !important;
    color: var(--a-teks) !important;
    border-color: var(--a-aqua) !important;
    box-shadow: 0 0 18px rgba(47, 212, 255, .85), 0 3px 12px rgba(18, 105, 180, .35), inset 0 1px 0 #fff;
    transform: translateY(-1px);
    text-decoration: none;
}
.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primary"],
.stDownloadButton > button[kind="primary"],
button[data-testid="stBaseButton-primary"], button[data-testid="stBaseButton-primaryFormSubmit"] {
    background: var(--a-kilap), linear-gradient(180deg, #7fe08f, #3fcf6a 50%, #1f9d48) !important;
    color: #fff !important;
    border: 1px solid #168a3c !important;
    text-shadow: 0 1px 2px rgba(0, 70, 25, .65);
    box-shadow: 0 3px 12px rgba(31, 157, 72, .5), inset 0 1px 0 rgba(255,255,255,.9);
}
.stButton > button[kind="primary"]:hover, button[data-testid="stBaseButton-primary"]:hover,
button[data-testid="stBaseButton-primaryFormSubmit"]:hover {
    color: #fff !important;
    background: var(--a-kilap), linear-gradient(180deg, #98f0a6, #55e07f 50%, #28b058) !important;
    box-shadow: 0 0 20px rgba(63, 207, 106, .9), inset 0 1px 0 #fff;
}
.stButton > button:active, .stFormSubmitButton > button:active { transform: translateY(1px); filter: brightness(.96); }

/* ---------- Input ---------- */
[data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"] > div,
[data-testid="stNumberInput"] [data-baseweb="input"] {
    background: rgba(255, 255, 255, .85) !important;
    border: 1px solid rgba(60, 140, 200, .55) !important;
    border-radius: 10px !important;
    box-shadow: inset 0 2px 5px rgba(18, 105, 180, .14), 0 1px 0 rgba(255,255,255,.9);
    transition: all .2s ease;
}
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within,
[data-baseweb="select"] > div:focus-within {
    border-color: var(--a-aqua) !important;
    box-shadow: 0 0 0 3px rgba(47, 212, 255, .35), inset 0 2px 5px rgba(18, 105, 180, .12);
}
input, textarea { color: var(--a-teks) !important; font-family: var(--a-font) !important; }
label, [data-testid="stWidgetLabel"] p { color: var(--a-teks) !important; font-weight: 600; }
[data-testid="stFileUploaderDropzone"] {
    background: var(--a-kaca) !important;
    backdrop-filter: blur(10px);
    border: 2px dashed rgba(30, 155, 240, .7) !important;
    border-radius: 16px;
    box-shadow: var(--a-bayang), inset 0 1px 0 rgba(255,255,255,.9);
}

/* ---------- Kartu / kontainer kaca ---------- */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--a-kaca);
    backdrop-filter: blur(12px) saturate(140%);
    -webkit-backdrop-filter: blur(12px) saturate(140%);
    border: 1px solid var(--a-tepi) !important;
    border-radius: 16px !important;
    box-shadow: var(--a-bayang), inset 0 1px 0 rgba(255,255,255,.95);
}
[data-testid="stMetric"] {
    position: relative;
    background: linear-gradient(180deg, rgba(255,255,255,.85), rgba(255,255,255,.45) 50%, rgba(200,240,255,.5));
    backdrop-filter: blur(10px);
    border: 1px solid var(--a-tepi);
    border-radius: 16px;
    padding: .9rem 1rem;
    box-shadow: var(--a-bayang), inset 0 1px 0 #fff;
    overflow: hidden;
}
[data-testid="stMetricLabel"] { color: var(--a-pudar) !important; font-weight: 600; }
[data-testid="stMetricValue"] {
    font-weight: 300;
    color: var(--a-biru-tua) !important;
    text-shadow: 0 1px 0 #fff, 0 0 14px rgba(47, 212, 255, .55);
}

[data-testid="stExpander"] {
    background: var(--a-kaca);
    backdrop-filter: blur(12px);
    border: 1px solid var(--a-tepi) !important;
    border-radius: 16px !important;
    box-shadow: var(--a-bayang), inset 0 1px 0 rgba(255,255,255,.95);
}
[data-testid="stExpander"] summary { font-weight: 600; color: var(--a-teks); }

/* ---------- Tab ---------- */
[data-baseweb="tab-list"] { gap: .4rem; border-bottom: 1px solid rgba(255,255,255,.9); }
button[data-baseweb="tab"] { font-weight: 600; color: var(--a-pudar); }
button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--a-biru-tua) !important;
    text-shadow: 0 1px 0 #fff, 0 0 10px rgba(47, 212, 255, .8);
}
[data-baseweb="tab-highlight"] {
    background: linear-gradient(90deg, var(--a-aqua), var(--a-biru), var(--a-hijau)) !important;
    height: 3px !important;
    border-radius: 3px;
    box-shadow: 0 0 10px rgba(47, 212, 255, .85);
}

/* ---------- Tabel, grafik, kode ---------- */
[data-testid="stDataFrame"], [data-testid="stDataEditor"] {
    background: var(--a-kaca-tebal);
    border: 1px solid var(--a-tepi);
    border-radius: 14px;
    box-shadow: var(--a-bayang);
    overflow: hidden;
}
[data-testid="stArrowVegaLiteChart"], [data-testid="stVegaLiteChart"] {
    background: var(--a-kaca-tebal);
    backdrop-filter: blur(10px);
    border: 1px solid var(--a-tepi);
    border-radius: 16px;
    padding: .6rem;
    box-shadow: var(--a-bayang), inset 0 1px 0 #fff;
}
[data-testid="stCode"], pre, code {
    background: rgba(255, 255, 255, .8) !important;
    color: var(--a-biru-tua) !important;
    border-radius: 8px;
}
[data-testid="stCode"] { border: 1px solid rgba(60, 140, 200, .4); box-shadow: inset 0 1px 3px rgba(18,105,180,.12); }

/* ---------- Notifikasi ---------- */
[data-testid="stAlert"] {
    background: var(--a-kaca-tebal);
    border: 1px solid var(--a-tepi);
    border-radius: 14px;
    box-shadow: var(--a-bayang), inset 0 1px 0 #fff;
    backdrop-filter: blur(8px);
}
[data-testid="stToast"] {
    background: var(--a-kaca-tebal);
    border: 1px solid var(--a-tepi);
    border-radius: 14px;
    box-shadow: 0 8px 28px rgba(18, 105, 180, .35);
}

/* ---------- Pilihan (radio / checkbox) ---------- */
[data-baseweb="checkbox"] span, [data-baseweb="radio"] > div:first-child { box-shadow: 0 0 6px rgba(47, 212, 255, .65); }
[data-testid="stSpinner"] i, [data-testid="stSpinner"] svg { filter: drop-shadow(0 0 6px var(--a-aqua)); }

/* ---------- Bilah gulir ala Aero ---------- */
::-webkit-scrollbar { width: 12px; height: 12px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,.45); border-radius: 8px; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(90deg, #d8f2ff, #7fd0ff 50%, #4bb6f0);
    border: 1px solid rgba(60,140,200,.7);
    border-radius: 8px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.9);
}
::selection { background: rgba(30, 155, 240, .4); color: #062a47; }

/* Hormati pengguna yang mematikan animasi */
@media (prefers-reduced-motion: reduce) {
    .stApp::before { animation: none !important; }
}
</style>
"""


def terapkan() -> None:
    """Pasang tema Frutiger Aero ke halaman yang sedang dirender."""
    st.html(CSS)

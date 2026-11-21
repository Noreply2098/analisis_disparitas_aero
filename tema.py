"""Tema visual FRUTIGER AERO untuk seluruh aplikasi.

Gaya langit biru, kaca bening (glass), gelembung, dan tombol mengilap ala Windows Vista/7.
Hanya mengubah tampilan (CSS). Tidak ada fitur, data, maupun teks aplikasi yang berubah.
Dipanggil sekali dari app.py lewat ``tema.terapkan()``.
"""

import streamlit as st

CSS = r"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap');

:root {
    --a-biru: #1b8fe8;
    --a-biru-tua: #0a4fb3;
    --a-navy: #06284a;
    --a-aqua: #2fd4ff;
    --a-hijau: #3fcf6a;
    --a-oranye: #ff9a1f;
    --a-teks: #06284a;
    --a-pudar: #1c4a78;
    --a-tepi: rgba(255, 255, 255, 0.92);
    --a-bayang: 0 10px 30px rgba(0, 80, 170, 0.35);
    --a-kilap: linear-gradient(180deg, rgba(255,255,255,.78) 0%, rgba(255,255,255,.28) 49%, rgba(255,255,255,0) 50%);
    --a-font: 'Segoe UI', 'Frutiger', 'Open Sans', 'Helvetica Neue', Arial, sans-serif;
}

/* ================= LATAR: langit, matahari, bukit hijau ================= */
.stApp {
    background:
        radial-gradient(circle at 88% 3%, #fff 0, rgba(255,255,255,.96) 2.5%, rgba(255,255,255,.55) 8%, rgba(255,255,255,0) 26%),
        radial-gradient(circle at 70% 19%, rgba(255,255,255,0) 0 3%, rgba(255,255,255,.45) 3.4% 4.2%, rgba(255,255,255,0) 4.6%),
        radial-gradient(circle at 56% 31%, rgba(255,230,140,.55) 0 1.4%, rgba(255,255,255,0) 2%),
        radial-gradient(circle at 44% 43%, rgba(150,255,190,.45) 0 1.8%, rgba(255,255,255,0) 2.4%),
        linear-gradient(180deg, #0b72d9 0%, #35aaf5 14%, #7fd6ff 40%, #bfeeff 70%, #effcff 100%) !important;
    background-attachment: fixed !important;
    color: var(--a-teks);
    font-family: var(--a-font);
}
/* gelembung kaca */
.stApp::before {
    content: "";
    position: fixed; inset: 0; z-index: 0; pointer-events: none;
    background:
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 6% 74% / 190px 190px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 6% 74% / 190px 190px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 93% 58% / 120px 120px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 93% 58% / 120px 120px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 74% 10% / 70px 70px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 74% 10% / 70px 70px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 38% 90% / 90px 90px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 38% 90% / 90px 90px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 16% 16% / 54px 54px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 16% 16% / 54px 54px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 52% 40% / 36px 36px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 52% 40% / 36px 36px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 84% 86% / 60px 60px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 84% 86% / 60px 60px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 30% 55% / 28px 28px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 30% 55% / 28px 28px no-repeat,
        radial-gradient(circle at 32% 26%, rgba(255,255,255,.98) 0 6%, rgba(255,255,255,0) 8%) 62% 70% / 46px 46px no-repeat,
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.05) 0 56%, rgba(255,255,255,.70) 69%, rgba(150,225,255,.35) 73%, rgba(255,255,255,0) 75%) 62% 70% / 46px 46px no-repeat;
    animation: a-melayang 12s ease-in-out infinite alternate;
}
/* bukit hijau + berkas sinar */
.stApp::after {
    content: "";
    position: fixed; left: 0; right: 0; bottom: 0; height: 38vh; z-index: 0; pointer-events: none;
    background:
        radial-gradient(ellipse 55% 78% at 12% 112%, #b9f26a 0%, #6fd23c 38%, #2fa02e 62%, rgba(0,0,0,0) 63%),
        radial-gradient(ellipse 62% 66% at 62% 118%, #9fe65a 0%, #52bf33 42%, #25912c 62%, rgba(0,0,0,0) 63%),
        radial-gradient(ellipse 48% 56% at 98% 112%, #8ee04e 0%, #43b02f 45%, #1f8228 62%, rgba(0,0,0,0) 63%);
    filter: drop-shadow(0 -6px 14px rgba(255,255,255,.55));
}
@keyframes a-melayang { from { transform: translateY(0); } to { transform: translateY(-22px); } }

/* Bilah atas: kaca mengilap ala jendela Windows 7 */
[data-testid="stHeader"] {
    background: linear-gradient(180deg, rgba(255,255,255,.85) 0%, rgba(190,232,255,.65) 48%, rgba(120,200,250,.55) 52%, rgba(170,225,255,.7) 100%) !important;
    backdrop-filter: blur(12px) saturate(150%);
    -webkit-backdrop-filter: blur(12px) saturate(150%);
    border-bottom: 1px solid #fff;
    box-shadow: 0 4px 18px rgba(0, 70, 160, .35);
}

/* Panel utama: satu "jendela" kaca besar */
.block-container {
    position: relative; z-index: 1;
    background: linear-gradient(180deg, rgba(255,255,255,.55) 0%, rgba(255,255,255,.34) 30%, rgba(255,255,255,.40) 100%);
    backdrop-filter: blur(10px) saturate(140%);
    -webkit-backdrop-filter: blur(10px) saturate(140%);
    border: 2px solid rgba(255,255,255,.9);
    border-radius: 26px;
    box-shadow: 0 14px 50px rgba(0, 70, 160, .4), inset 0 0 50px rgba(255,255,255,.45), inset 0 2px 0 #fff;
    margin: 3.6rem auto 2.2rem auto;
    width: calc(100% - 2.4rem) !important;
    padding-top: 2.2rem !important;
}

/* ================= JUDUL ================= */
h1, h2, h3, h4, [data-testid="stHeading"] {
    font-family: var(--a-font) !important;
    color: var(--a-navy) !important;
}
h1 {
    font-weight: 600 !important;
    background: linear-gradient(180deg, #0a3f9c 0%, #1b8fe8 100%);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent; color: transparent !important;
    filter: drop-shadow(0 0 1px #fff) drop-shadow(0 2px 2px rgba(255,255,255,.95)) drop-shadow(0 0 14px rgba(255,255,255,.9));
}
/* subjudul = pita kaca mengilap */
[data-testid="stHeading"] h2, [data-testid="stHeading"] h3 {
    display: block;
    font-weight: 700 !important;
    padding: .4rem 1rem !important;
    border-radius: 14px;
    background: linear-gradient(180deg, rgba(255,255,255,.95) 0%, rgba(255,255,255,.55) 49%, rgba(170,225,255,.55) 50%, rgba(220,245,255,.8) 100%);
    border: 1px solid #fff;
    border-left: 8px solid var(--a-aqua);
    box-shadow: 0 4px 14px rgba(0, 80, 170, .3), inset 0 1px 0 #fff;
    text-shadow: 0 1px 0 #fff;
}
h4 { font-weight: 700 !important; color: var(--a-biru-tua) !important; text-shadow: 0 1px 0 #fff; }

p, li { font-family: var(--a-font); }
[data-testid="stCaptionContainer"], .stCaption, small { color: var(--a-pudar) !important; }
a { color: var(--a-biru-tua) !important; text-decoration: none; font-weight: 600; }
a:hover { color: #0d7be0 !important; text-shadow: 0 0 8px #fff; text-decoration: underline; }
hr { border: 0 !important; height: 3px; border-radius: 3px;
     background: linear-gradient(90deg, transparent, #fff, #2fd4ff, #fff, transparent) !important; }
strong, b { color: var(--a-navy); }

/* ================= SIDEBAR: kaca biru Aero ================= */
[data-testid="stSidebar"] {
    background:
        linear-gradient(118deg, rgba(255,255,255,.50) 0%, rgba(255,255,255,.10) 28%, rgba(255,255,255,0) 29%, rgba(255,255,255,.22) 58%, rgba(255,255,255,0) 59%),
        linear-gradient(180deg, #7fd3ff 0%, #2f9fee 45%, #1779d8 100%) !important;
    backdrop-filter: blur(16px) saturate(150%);
    -webkit-backdrop-filter: blur(16px) saturate(150%);
    border-right: 2px solid #fff;
    box-shadow: 6px 0 30px rgba(0, 70, 160, .45), inset -2px 0 0 rgba(255,255,255,.6);
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"],
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] * {
    color: #fff !important;
    text-shadow: 0 1px 3px rgba(0, 40, 110, .8);
}
[data-testid="stSidebar"] button [data-testid="stMarkdownContainer"] p { color: inherit !important; text-shadow: inherit !important; }
[data-testid="stSidebar"] [data-testid="stAlert"] * { color: var(--a-navy) !important; text-shadow: none !important; }
[data-testid="stSidebarNav"] a, [data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] {
    border: 1px solid transparent;
    border-radius: 12px;
    color: #fff !important;
    text-shadow: 0 1px 3px rgba(0, 40, 110, .85);
    transition: all .2s ease;
}
[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"] * { color: #fff !important; }
[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"]:hover {
    border-color: rgba(255,255,255,.95);
    background: var(--a-kilap), linear-gradient(180deg, rgba(255,255,255,.35), rgba(255,255,255,.15)) !important;
    box-shadow: 0 0 16px rgba(255,255,255,.8), inset 0 1px 0 #fff;
    text-decoration: none;
}
[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"][aria-current="page"] {
    border-color: #fff;
    background: var(--a-kilap), linear-gradient(180deg, #ffffff, #d6f3ff 55%, #aee6ff) !important;
    box-shadow: 0 4px 14px rgba(0, 50, 130, .5), 0 0 14px rgba(255,255,255,.8), inset 0 1px 0 #fff;
    text-shadow: 0 1px 0 #fff;
}
[data-testid="stSidebar"] a[data-testid="stSidebarNavLink"][aria-current="page"] * { color: var(--a-biru-tua) !important; font-weight: 700; }
[data-testid="stSidebarNavSeparator"],
[data-testid="stSidebar"] [data-testid="stNavSectionHeader"],
[data-testid="stSidebarNav"] span[class*="Header"] {
    color: #fff !important; font-weight: 700; letter-spacing: .14em;
    text-shadow: 0 1px 3px rgba(0, 40, 110, .85);
}

/* ================= TOMBOL: glossy 3D ================= */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button,
[data-testid="stPageLink"] a {
    font-family: var(--a-font);
    font-weight: 700;
    color: #fff !important;
    background: var(--a-kilap), linear-gradient(180deg, #5cc8ff 0%, #1b8fe8 55%, #0a6cc8 100%) !important;
    border: 1px solid #07529e !important;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0, 80, 170, .5), inset 0 1px 0 rgba(255,255,255,.95), inset 0 -2px 4px rgba(0, 40, 120, .25);
    text-shadow: 0 1px 2px rgba(0, 40, 110, .8);
    transition: all .18s ease;
}
.stButton > button *, .stDownloadButton > button *, .stFormSubmitButton > button * { color: #fff !important; }
.stButton > button:hover, .stDownloadButton > button:hover, .stFormSubmitButton > button:hover,
[data-testid="stPageLink"] a:hover {
    background: var(--a-kilap), linear-gradient(180deg, #86dcff 0%, #35a8fa 55%, #138be0 100%) !important;
    border-color: #fff !important;
    box-shadow: 0 0 22px rgba(47, 212, 255, 1), 0 4px 14px rgba(0, 80, 170, .5), inset 0 1px 0 #fff;
    transform: translateY(-2px);
    text-decoration: none;
}
.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primary"],
.stDownloadButton > button[kind="primary"],
button[data-testid="stBaseButton-primary"], button[data-testid="stBaseButton-primaryFormSubmit"] {
    background: var(--a-kilap), linear-gradient(180deg, #9cf27a 0%, #3fcf3a 55%, #1c9a2a 100%) !important;
    border: 1px solid #12761f !important;
    text-shadow: 0 1px 2px rgba(0, 70, 20, .85);
    box-shadow: 0 4px 12px rgba(20, 130, 40, .55), inset 0 1px 0 rgba(255,255,255,.95), inset 0 -2px 4px rgba(0, 80, 20, .25);
}
.stButton > button[kind="primary"]:hover, button[data-testid="stBaseButton-primary"]:hover,
button[data-testid="stBaseButton-primaryFormSubmit"]:hover {
    background: var(--a-kilap), linear-gradient(180deg, #b6ff98 0%, #58e052 55%, #25b036 100%) !important;
    box-shadow: 0 0 24px rgba(110, 240, 80, 1), inset 0 1px 0 #fff;
}
.stButton > button:active, .stFormSubmitButton > button:active { transform: translateY(1px); filter: brightness(.94); }
/* tombol di sidebar: putih kaca agar menonjol dari latar biru */
[data-testid="stSidebar"] .stButton > button {
    background: var(--a-kilap), linear-gradient(180deg, #ffffff, #d6f3ff 55%, #a9e3ff) !important;
    color: var(--a-biru-tua) !important; border-color: #fff !important; text-shadow: 0 1px 0 #fff;
}
[data-testid="stSidebar"] .stButton > button * { color: var(--a-biru-tua) !important; }

/* ================= INPUT ================= */
[data-baseweb="input"], [data-baseweb="textarea"], [data-baseweb="select"] > div,
[data-testid="stNumberInput"] [data-baseweb="input"] {
    background: linear-gradient(180deg, #e6f6ff, #ffffff 40%) !important;
    border: 2px solid #5fb6ee !important;
    border-radius: 12px !important;
    box-shadow: inset 0 3px 6px rgba(0, 90, 170, .2), 0 1px 0 #fff;
    transition: all .2s ease;
}
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within,
[data-baseweb="select"] > div:focus-within {
    border-color: var(--a-aqua) !important;
    box-shadow: 0 0 0 4px rgba(47, 212, 255, .45), inset 0 2px 5px rgba(0, 90, 170, .15);
}
input, textarea { color: var(--a-navy) !important; font-family: var(--a-font) !important; }
[data-baseweb="select"] * { color: var(--a-navy) !important; }
label, [data-testid="stWidgetLabel"] p { color: var(--a-navy) !important; font-weight: 700; text-shadow: 0 1px 0 rgba(255,255,255,.8); }
[data-testid="stFileUploaderDropzone"] {
    background: linear-gradient(180deg, rgba(255,255,255,.85), rgba(190,235,255,.6)) !important;
    backdrop-filter: blur(10px);
    border: 3px dashed #1b8fe8 !important;
    border-radius: 18px;
    box-shadow: var(--a-bayang), inset 0 2px 0 #fff;
}

/* ================= KARTU KACA ================= */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, rgba(255,255,255,.92) 0%, rgba(255,255,255,.66) 40%, rgba(214,242,255,.7) 100%);
    backdrop-filter: blur(14px) saturate(150%);
    -webkit-backdrop-filter: blur(14px) saturate(150%);
    border: 2px solid #fff !important;
    border-radius: 20px !important;
    box-shadow: var(--a-bayang), inset 0 2px 0 #fff, inset 0 0 24px rgba(120, 210, 255, .35);
}
[data-testid="stMetric"] {
    position: relative; overflow: hidden;
    background: linear-gradient(180deg, rgba(255,255,255,.98) 0%, rgba(255,255,255,.7) 49%, rgba(150,220,255,.65) 50%, rgba(220,245,255,.9) 100%);
    border: 2px solid #fff;
    border-radius: 18px;
    padding: .9rem 1rem;
    box-shadow: var(--a-bayang), inset 0 2px 0 #fff;
}
[data-testid="stMetric"]::after {  /* "orb" kaca di sudut kartu */
    content: ""; position: absolute; right: -14px; top: -14px; width: 56px; height: 56px; border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #fff 0 12%, #8fe9ff 30%, #1b8fe8 70%, #0a4fb3 100%);
    opacity: .85; box-shadow: 0 0 14px rgba(47,212,255,.9);
}
[data-testid="stMetricLabel"] { color: var(--a-pudar) !important; font-weight: 700; }
[data-testid="stMetricValue"] {
    font-weight: 600; color: var(--a-biru-tua) !important;
    text-shadow: 0 1px 0 #fff, 0 0 16px rgba(47, 212, 255, .8);
}

[data-testid="stExpander"] {
    background: linear-gradient(180deg, rgba(255,255,255,.92), rgba(214,242,255,.7));
    backdrop-filter: blur(12px);
    border: 2px solid #fff !important;
    border-radius: 18px !important;
    box-shadow: var(--a-bayang), inset 0 2px 0 #fff;
}
[data-testid="stExpander"] summary { font-weight: 700; color: var(--a-navy); }

/* ================= TAB: pil glossy ================= */
[data-baseweb="tab-list"] { gap: .5rem; border-bottom: 2px solid rgba(255,255,255,.9); padding-bottom: .3rem; }
button[data-baseweb="tab"] {
    font-weight: 700; color: var(--a-pudar);
    border-radius: 999px; padding: .35rem 1.1rem;
    background: linear-gradient(180deg, rgba(255,255,255,.8), rgba(190,232,255,.5));
    border: 1px solid rgba(255,255,255,.95);
}
button[data-baseweb="tab"][aria-selected="true"] {
    color: #fff !important;
    background: var(--a-kilap), linear-gradient(180deg, #5cc8ff, #1b8fe8 55%, #0a6cc8) !important;
    text-shadow: 0 1px 2px rgba(0, 40, 110, .8);
    box-shadow: 0 3px 10px rgba(0, 80, 170, .45), inset 0 1px 0 #fff;
}
[data-baseweb="tab-highlight"] { background: transparent !important; }

/* ================= TABEL, GRAFIK, KODE ================= */
[data-testid="stDataFrame"], [data-testid="stDataEditor"] {
    background: rgba(255,255,255,.9);
    border: 2px solid #fff;
    border-radius: 16px;
    box-shadow: var(--a-bayang);
    overflow: hidden;
}
[data-testid="stArrowVegaLiteChart"], [data-testid="stVegaLiteChart"] {
    background: linear-gradient(180deg, rgba(255,255,255,.95), rgba(215,243,255,.85) 60%, rgba(180,235,255,.8));
    border: 2px solid #fff;
    border-radius: 18px;
    padding: .8rem;
    box-shadow: 0 6px 22px rgba(0, 80, 170, .3), inset 0 2px 0 #fff, inset 0 0 26px rgba(120, 210, 255, .35);
}
[data-testid="stCode"], pre, code { background: rgba(255,255,255,.9) !important; color: var(--a-biru-tua) !important; border-radius: 8px; }
[data-testid="stCode"] { border: 1px solid #5fb6ee; box-shadow: inset 0 1px 4px rgba(0,90,170,.15); }

/* ================= NOTIFIKASI ================= */
[data-testid="stAlert"] {
    background: linear-gradient(180deg, rgba(255,255,255,.95), rgba(214,242,255,.8));
    border: 2px solid #fff;
    border-radius: 16px;
    box-shadow: var(--a-bayang), inset 0 2px 0 #fff;
}
[data-testid="stAlert"] * { color: var(--a-navy) !important; }
[data-testid="stToast"] { background: rgba(255,255,255,.95); border: 2px solid #fff; border-radius: 16px; box-shadow: 0 8px 28px rgba(0, 80, 170, .5); }

/* ================= PILIHAN, SCROLLBAR ================= */
[data-baseweb="checkbox"] span, [data-baseweb="radio"] > div:first-child { box-shadow: 0 0 8px rgba(47, 212, 255, .9); }
[data-testid="stSpinner"] i, [data-testid="stSpinner"] svg { filter: drop-shadow(0 0 6px var(--a-aqua)); }
::-webkit-scrollbar { width: 14px; height: 14px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,.5); border-radius: 8px; }
::-webkit-scrollbar-thumb {
    background: linear-gradient(90deg, #e4f7ff, #6fcfff 50%, #2f9fee);
    border: 1px solid #1b7fd0; border-radius: 8px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.95);
}
::selection { background: rgba(27, 143, 232, .45); color: #031a33; }

@media (max-width: 640px) {
    .block-container { margin-top: .5rem; width: calc(100% - 1rem) !important; border-radius: 18px; }
    .stApp::after { height: 22vh; }
}
@media (prefers-reduced-motion: reduce) { .stApp::before { animation: none !important; } }
</style>
"""


def terapkan() -> None:
    """Pasang tema Frutiger Aero ke halaman yang sedang dirender."""
    st.html(CSS)

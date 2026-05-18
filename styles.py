css_premium = """
<style>

/* ================================================== */
/* FUNDO GERAL */
/* ================================================== */

.stApp {
    background-color: #111111;
    color: #F5F5F5;
}

/* ================================================== */
/* CONTAINER */
/* ================================================== */

.block-container {
    max-width: 950px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ================================================== */
/* TEXTOS */
/* ================================================== */

h1, h2, h3, h4, h5 {
    color: #FFFFFF !important;
    font-weight: 700;
}

p, span, label, div {
    color: #E5E7EB;
}

/* ================================================== */
/* HERO */
/* ================================================== */

.hero {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    margin-bottom: 30px;
}

.hero img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    filter: brightness(0.55);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    color: white;
}

.hero-sub {
    margin-top: 12px;
    font-size: 18px;
    color: #E5E7EB;
}

/* ================================================== */
/* CARDS */
/* ================================================== */

[data-testid="stVerticalBlockBorderWrapper"] {

    border-radius: 22px;

    border: 1px solid #2A2A2A;

    background: #1A1A1A;

    box-shadow: 0 8px 24px rgba(0,0,0,0.25);

    padding: 10px;
}

/* ================================================== */
/* RESUMO */
/* ================================================== */

.resumo {

    background: #1A1A1A;

    border: 1px solid #2A2A2A;

    border-radius: 20px;

    padding: 24px;

    margin-bottom: 20px;
}

/* ================================================== */
/* INPUTS */
/* ================================================== */

.stTextInput input,
.stDateInput input {

    background-color: #222222 !important;

    color: white !important;

    border: 1px solid #3A3A3A !important;

    border-radius: 12px !important;
}

.stTextInput input:focus,
.stDateInput input:focus {

    border-color: #D4AF37 !important;

    box-shadow: 0 0 0 1px #D4AF37 !important;
}

/* ================================================== */
/* BOTÕES */
/* ================================================== */

.stButton > button {

    border-radius: 14px;

    border: none;

    background: #D4AF37;

    color: #111111;

    font-weight: 700;

    padding: 0.75rem 1rem;

    transition: 0.2s;
}

.stButton > button:hover {

    transform: translateY(-2px);

    background: #E6C65C;
}

/* ================================================== */
/* DATAFRAME */
/* ================================================== */

[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;

    border: 1px solid #2A2A2A;
}

/* ================================================== */
/* EXPANDER */
/* ================================================== */

.streamlit-expanderHeader {

    background: #1A1A1A;

    border-radius: 12px;

    color: white !important;
}

/* ================================================== */
/* ALERTAS */
/* ================================================== */

[data-testid="stSuccess"],
[data-testid="stWarning"],
[data-testid="stError"] {

    border-radius: 14px;
}

/* ================================================== */
/* SCROLLBAR */
/* ================================================== */

::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #111111;
}

::-webkit-scrollbar-thumb {

    background: #444444;

    border-radius: 20px;
}

::-webkit-scrollbar-thumb:hover {

    background: #666666;
}

</style>
"""

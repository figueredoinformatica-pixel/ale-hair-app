```python
css_premium = """
<style>

/* ================================================== */
/* FUNDO GERAL */
/* ================================================== */

.stApp {
    background: #0B0B0B;
    color: #F5F5F5;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 900px;
}

/* ================================================== */
/* TEXTOS */
/* ================================================== */

h1, h2, h3, h4, h5 {
    color: #FFFFFF !important;
    font-weight: 700;
}

p, span, label, div {
    color: #D1D5DB;
}

/* ================================================== */
/* HERO */
/* ================================================== */

.hero {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.45);
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
    letter-spacing: 2px;
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
    border: 1px solid #1F2937;
    background: linear-gradient(
        180deg,
        #111827 0%,
        #0F172A 100%
    );
    box-shadow: 0 8px 24px rgba(0,0,0,0.35);
    padding: 10px;
}

/* ================================================== */
/* RESUMOS */
/* ================================================== */

.resumo {
    background: linear-gradient(
        180deg,
        #111827 0%,
        #0B1220 100%
    );
    border: 1px solid #1F2937;
    border-radius: 20px;
    padding: 24px;
    margin-bottom: 20px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.30);
}

/* ================================================== */
/* INPUTS */
/* ================================================== */

.stTextInput input,
.stDateInput input {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #374151 !important;
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
    background: linear-gradient(
        90deg,
        #D4AF37 0%,
        #B8860B 100%
    );
    color: black;
    font-weight: 700;
    padding: 0.75rem 1rem;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(212,175,55,0.30);
}

/* ================================================== */
/* DATAFRAME */
/* ================================================== */

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid #1F2937;
}

/* ================================================== */
/* EXPANDER */
/* ================================================== */

.streamlit-expanderHeader {
    background: #111827;
    border-radius: 12px;
    color: white !important;
}

/* ================================================== */
/* ALERTAS */
/* ================================================== */

[data-testid="stSuccess"] {
    border-radius: 14px;
}

[data-testid="stWarning"] {
    border-radius: 14px;
}

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
    background: #111827;
}

::-webkit-scrollbar-thumb {
    background: #374151;
    border-radius: 20px;
}

::-webkit-scrollbar-thumb:hover {
    background: #4B5563;
}

</style>
"""
```

## Resultado visual

O app ficará com:

* fundo preto premium
* detalhes dourados
* cards estilo app de luxo
* visual parecido com:

  * Booksy
  * apps premium de barbearia
  * dashboards dark modernos

Também reduz bastante a aparência “padrão Streamlit”.

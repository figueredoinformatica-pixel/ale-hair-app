css_premium = """
<style>

/* ==================================================
FUNDO
================================================== */

.stApp {

    background-color: #F3F4F6;
}

/* ==================================================
REMOVE STREAMLIT
================================================== */

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}

/* ==================================================
TIPOGRAFIA
================================================== */

html, body, [class*="css"] {

    font-family: 'Inter', sans-serif;
}

/* ==================================================
HERO SECTION
================================================== */

.hero {

    position: relative;

    border-radius: 24px;

    overflow: hidden;

    margin-bottom: 28px;
}

.hero img {

    width: 100%;

    height: 320px;

    object-fit: cover;

    filter: brightness(0.55);
}

.hero-overlay {

    position: absolute;

    top: 0;

    left: 0;

    right: 0;

    bottom: 0;

    display: flex;

    flex-direction: column;

    justify-content: center;

    padding: 32px;

    color: white;
}

.hero-title {

    font-size: 42px;

    font-weight: 800;

    margin-bottom: 8px;
}

.hero-sub {

    font-size: 17px;

    opacity: 0.9;
}

/* ==================================================
SERVICE CARD
================================================== */

[data-testid="stVerticalBlockBorderWrapper"] {

    background: white !important;

    border: none !important;

    border-radius: 22px !important;

    padding: 10px !important;

    box-shadow:
        0 4px 20px rgba(0,0,0,0.04) !important;

    margin-bottom: 18px !important;

    transition: 0.2s ease;
}

[data-testid="stVerticalBlockBorderWrapper"]:hover {

    transform: translateY(-2px);
}

/* ==================================================
BOTÕES
================================================== */

div.stButton > button[kind="primary"] {

    background: #111827 !important;

    border-radius: 14px !important;

    border: none !important;

    height: 48px !important;

    transition: all 0.2s ease !important;
}

div.stButton > button[kind="primary"]:hover {

    background: #1F2937 !important;

    transform: scale(1.01);
}

div.stButton > button[kind="primary"] p {

    color: white !important;

    font-weight: 700 !important;

    font-size: 15px !important;
}

/* ==================================================
INPUTS
================================================== */

.stTextInput input {

    border-radius: 14px !important;

    border: 1px solid #E5E7EB !important;

    height: 50px !important;
}

.stDateInput input {

    border-radius: 14px !important;
}

/* ==================================================
HORÁRIOS
================================================== */

div[role="radiogroup"] {

    gap: 8px;
}

/* ==================================================
RESUMO PREMIUM
================================================== */

.resumo {

    background: white;

    padding: 24px;

    border-radius: 20px;

    box-shadow:
        0 4px 18px rgba(0,0,0,0.04);

    margin-bottom: 24px;
}

/* ==================================================
BARBEIRO CARD
================================================== */

.barbeiro-card {

    background: white;

    padding: 18px;

    border-radius: 18px;

    text-align: center;

    box-shadow:
        0 3px 12px rgba(0,0,0,0.04);
}

/* ==================================================
DATAFRAME
================================================== */

[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;
}

</style>
"""
css_premium = """
<style>

/* ==================================================
FUNDO
================================================== */

.stApp{
    background-color:#F3F4F6;
}

/* ==================================================
HERO
================================================== */

.hero{
    position:relative;
    width:100%;
    height:320px;
    overflow:hidden;
    border-radius:22px;
    margin-bottom:25px;
    box-shadow:0 10px 30px rgba(0,0,0,0.12);
}

.hero img{
    width:100%;
    height:100%;
    object-fit:cover;
}

.hero-overlay{
    position:absolute;
    inset:0;
    background:linear-gradient(
        to top,
        rgba(0,0,0,0.75),
        rgba(0,0,0,0.20)
    );

    display:flex;
    flex-direction:column;
    justify-content:flex-end;
    padding:28px;
}

.hero-title{
    color:white;
    font-size:42px;
    font-weight:800;
    line-height:1;
}

.hero-sub{
    color:#E5E7EB;
    margin-top:10px;
    font-size:16px;
}

/* ==================================================
TEXTOS
================================================== */

.info-local{
    margin-bottom:16px;
    color:#6B7280;
    font-size:15px;
}

.avaliacao{
    margin-bottom:28px;
    font-size:17px;
    font-weight:700;
    color:#111827;
}

.titulo-secao{
    margin-bottom:25px;
    color:#111827;
}

/* ==================================================
SERVIÇOS
================================================== */

.nome-servico{
    font-size:23px;
    font-weight:800;
    color:#111827;
    margin-top:8px;
}

.descricao-servico{
    color:#6B7280;
    font-size:14px;
    margin-top:5px;
}

.tempo-servico{
    margin-top:12px;
    font-size:14px;
    color:#111827;
    font-weight:600;
}

.preco-servico{
    text-align:right;
    margin-top:8px;
    font-size:28px;
    font-weight:800;
    color:#111827;
}

.icone-servico{
    font-size:60px;
    text-align:center;
}

/* ==================================================
CARDS
================================================== */

[data-testid="stVerticalBlockBorderWrapper"]{
    border-radius:22px !important;
    border:1px solid #E5E7EB !important;
    background:white !important;
    box-shadow:0 2px 10px rgba(0,0,0,0.04);
    padding:12px !important;
}

/* ==================================================
BOTÕES
================================================== */

.stButton > button{
    border-radius:14px !important;
    height:48px !important;
    font-weight:700 !important;
    border:none !important;
    transition:0.2s;
}

.stButton > button[kind="primary"]{
    background:#111827 !important;
    color:white !important;
}

.stButton > button[kind="primary"]:hover{
    background:#000000 !important;
    transform:translateY(-1px);
}

/* ==================================================
RESUMO
================================================== */

.resumo{
    background:white;
    border-radius:20px;
    padding:24px;
    margin-bottom:28px;
    border:1px solid #E5E7EB;
    box-shadow:0 2px 10px rgba(0,0,0,0.04);
}

.resumo h2{
    color:#111827;
    margin-bottom:12px;
}

.resumo p{
    color:#374151;
    font-size:16px;
}

/* ==================================================
BARBEIRO
================================================== */

.barbeiro-card{
    background:white;
    border-radius:18px;
    padding:24px;
    border:1px solid #E5E7EB;
    box-shadow:0 2px 10px rgba(0,0,0,0.04);
    height:100%;
}

.barbeiro-card h2{
    margin-bottom:5px;
    color:#111827;
}

.barbeiro-card p{
    color:#6B7280;
}

.avaliacao-barbeiro{
    margin-top:14px;
    font-weight:700;
    color:#111827;
}

/* ==================================================
INPUTS
================================================== */

.stTextInput input{
    border-radius:12px !important;
}

.stDateInput input{
    border-radius:12px !important;
}

/* ==================================================
HEADER STREAMLIT
================================================== */

header{
    visibility:hidden;
}

#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

</style>
"""

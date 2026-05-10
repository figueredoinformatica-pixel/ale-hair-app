import streamlit as st
import pandas as pd
import datetime
import os
import base64

# ==================================================
# DATABASE
# ==================================================

from database import engine, SessionLocal
from models import Base
from services import (
    criar_agendamento,
    listar_agendamentos,
    horarios_ocupados,
    excluir_agendamento
)

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Ale Hair Barbearia",
    page_icon="✂️",
    layout="centered"
)

# ==================================================
# CRIA TABELAS
# ==================================================

Base.metadata.create_all(bind=engine)

# ==================================================
# CSS PREMIUM
# ==================================================

css = """
<style>

.stApp{
    background-color:#F5F5F5;
}

/* HERO */

.hero{
    position:relative;
    border-radius:20px;
    overflow:hidden;
    margin-bottom:25px;
}

.hero img{
    width:100%;
    height:320px;
    object-fit:cover;
}

.hero-overlay{
    position:absolute;
    bottom:0;
    width:100%;
    padding:30px;
    background:linear-gradient(
        transparent,
        rgba(0,0,0,0.8)
    );
}

.hero-title{
    color:white;
    font-size:38px;
    font-weight:700;
}

.hero-sub{
    color:#E5E7EB;
    font-size:16px;
}

/* CARDS */

.servico-card{
    background:white;
    border-radius:18px;
    padding:16px;
    margin-bottom:15px;
    box-shadow:0 2px 10px rgba(0,0,0,0.05);
}

.resumo{
    background:white;
    border-radius:18px;
    padding:22px;
    box-shadow:0 2px 10px rgba(0,0,0,0.05);
    margin-bottom:25px;
}

.barbeiro-card{
    background:white;
    border-radius:18px;
    padding:20px;
    text-align:center;
    box-shadow:0 2px 10px rgba(0,0,0,0.05);
}

/* BUTTON */

div.stButton > button{
    border-radius:12px !important;
    height:50px !important;
    font-weight:600 !important;
    border:none !important;
}

div.stButton > button[kind="primary"]{
    background-color:#111827 !important;
    color:white !important;
}

div.stButton > button[kind="primary"]:hover{
    background-color:#1F2937 !important;
}

/* INPUTS */

.stTextInput input{
    border-radius:12px !important;
}

.stDateInput input{
    border-radius:12px !important;
}

/* REMOVE STREAMLIT */

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

</style>
"""

st.markdown(
    css,
    unsafe_allow_html=True
)

# ==================================================
# SESSION
# ==================================================

if "tela" not in st.session_state:
    st.session_state.tela = "catalogo"

if "servico" not in st.session_state:
    st.session_state.servico = {}

# ==================================================
# FUNÇÕES
# ==================================================

def mudar_tela(nome):
    st.session_state.tela = nome


def abrir_agendamento(servico):
    st.session_state.servico = servico
    st.session_state.tela = "agendamento"

# ==================================================
# SERVIÇOS
# ==================================================

dados = [
    {
        "Nome_Servico": "Corte Masculino",
        "Valor_Padrao": 40,
        "Tempo_Minutos": 30,
        "Imagem": "corte.png"
    },
    {
        "Nome_Servico": "Barba",
        "Valor_Padrao": 30,
        "Tempo_Minutos": 30,
        "Imagem": "barba.png"
    },
    {
        "Nome_Servico": "Combo Corte + Barba",
        "Valor_Padrao": 70,
        "Tempo_Minutos": 45,
        "Imagem": "corteebarba.png"
    }
]

df_servicos = pd.DataFrame(dados)

# ==================================================
# TELA CATÁLOGO
# ==================================================

if st.session_state.tela == "catalogo":

    hero = "assets/hero.jpg"

    if os.path.exists(hero):

        with open(hero, "rb") as img:
            hero_base64 = base64.b64encode(
                img.read()
            ).decode()

        st.markdown(
            f"""
            <div class="hero">

                <img src="data:image/jpeg;base64,{hero_base64}">

                <div class="hero-overlay">

                    <div class="hero-title">
                        Ale Hair
                    </div>

                    <div class="hero-sub">
                        Premium Barber Shop
                    </div>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.title("✂️ Ale Hair")

    st.markdown(
        """
        📍 Av. Amador Bueno da Veiga, 4438 - Penha de França
        """
    )

    st.write("")

    st.markdown("## Serviços")

    # ==================================================
    # CARDS SERVIÇOS
    # ==================================================

    for i, servico in df_servicos.iterrows():

        with st.container():

            st.markdown(
                """
                <div class="servico-card">
                """,
                unsafe_allow_html=True
            )

            c1, c2, c3 = st.columns([1.2, 3, 1.5])

            # FOTO

            with c1:

                caminho = f"assets/{servico['Imagem']}"

                if os.path.exists(caminho):

                    st.image(
                        caminho,
                        width=95
                    )

                else:

                    st.markdown("# ✂️")

            # INFO

            with c2:

                st.markdown(
                    f"### {servico['Nome_Servico']}"
                )

                st.caption(
                    "Acabamento premium profissional"
                )

                st.write(
                    f"⏱ {servico['Tempo_Minutos']} min"
                )

            # AÇÃO

            with c3:

                st.markdown(
                    f"""
                    <h2 style="
                        text-align:right;
                        margin-top:10px;
                    ">
                    R$ {servico['Valor_Padrao']}
                    </h2>
                    """,
                    unsafe_allow_html=True
                )

                st.button(
                    "Reservar",
                    key=i,
                    type="primary",
                    width="stretch",
                    on_click=abrir_agendamento,
                    args=(servico.to_dict(),)
                )

            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )

    st.write("")

    st.button(
        "📊 Painel Administrativo",
        width="stretch",
        on_click=mudar_tela,
        args=("painel",)
    )

# ==================================================
# TELA AGENDAMENTO
# ==================================================

elif st.session_state.tela == "agendamento":

    st.button(
        "⬅️ Voltar",
        on_click=mudar_tela,
        args=("catalogo",)
    )

    servico = st.session_state.servico

    # ==================================================
    # RESUMO
    # ==================================================

    st.markdown(
        f"""
        <div class="resumo">

            <h2>
            {servico['Nome_Servico']}
            </h2>

            <p>
            💰 R$ {servico['Valor_Padrao']}
            </p>

            <p>
            ⏱ {servico['Tempo_Minutos']} minutos
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # BARBEIRO
    # ==================================================

    st.markdown("## Seu barbeiro")

    col1, col2 = st.columns([1,2])

    with col1:

        foto = "assets/barbeiro_ale.jpg"

        if os.path.exists(foto):

            st.image(
                foto,
                width=120
            )

    with col2:

        st.markdown(
            """
            <div class="barbeiro-card">

                <h2>
                Ale
                </h2>

                <p>
                Especialista em degradê
                </p>

                <h4>
                ★ 5.0
                </h4>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    # ==================================================
    # DATA
    # ==================================================

    st.markdown("## Escolha a data")

    data = st.date_input(
        "Data",
        min_value=datetime.date.today(),
        label_visibility="collapsed"
    )

    # ==================================================
    # HORÁRIOS
    # ==================================================

    st.markdown("## Horários disponíveis")

    horarios = [
        "09:00",
        "10:00",
        "11:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00"
    ]

    db = SessionLocal()

    ocupados = horarios_ocupados(
        db,
        data,
        "Ale"
    )

    livres = [
        h for h in horarios
        if h not in ocupados
    ]

    db.close()

    if livres:

        horario = st.radio(
            "Horários",
            livres,
            horizontal=True,
            label_visibility="collapsed"
        )

    else:

        horario = None

        st.error(
            "Sem horários disponíveis."
        )

    st.write("")

    # ==================================================
    # CLIENTE
    # ==================================================

    st.markdown("## Seus dados")

    nome = st.text_input(
        "Nome Completo"
    )

    telefone = st.text_input(
        "WhatsApp"
    )

    st.write("")

    # ==================================================
    # CONFIRMAR
    # ==================================================

    if st.button(
        "Confirmar Reserva",
        type="primary",
        width="stretch"
    ):

        if not nome or not telefone:

            st.warning(
                "Preencha todos os campos."
            )

        elif not horario:

            st.warning(
                "Escolha um horário."
            )

        else:

            db = SessionLocal()

            criar_agendamento(
                db,
                nome,
                telefone,
                servico["Nome_Servico"],
                "Ale",
                data,
                horario
            )

            db.close()

            st.success(
                f"""
                Reserva confirmada para
                {data.strftime('%d/%m/%Y')}
                às {horario}
                """
            )

# ==================================================
# PAINEL
# ==================================================

elif st.session_state.tela == "painel":

    st.button(
        "⬅️ Voltar",
        on_click=mudar_tela,
        args=("catalogo",)
    )

    st.title("📊 Agenda")

    db = SessionLocal()

    agendamentos = listar_agendamentos(db)

    if agendamentos:

        dados = []

        for a in agendamentos:

            dados.append({
                "ID": a.id,
                "Cliente": a.nome,
                "Telefone": a.telefone,
                "Serviço": a.servico,
                "Barbeiro": a.barbeiro,
                "Data": a.data.strftime("%d/%m/%Y"),
                "Horário": a.horario
            })

        df = pd.DataFrame(dados)

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )

        st.write("")

        ids = [a.id for a in agendamentos]

        excluir_id = st.selectbox(
            "Excluir agendamento",
            ids
        )

        if st.button(
            "Excluir",
            type="primary"
        ):

            excluir_agendamento(
                db,
                excluir_id
            )

            st.success(
                "Agendamento removido."
            )

            st.rerun()

    else:

        st.info(
            "Nenhum agendamento."
        )

    db.close()

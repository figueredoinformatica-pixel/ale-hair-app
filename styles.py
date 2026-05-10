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
# STYLES
# ==================================================

from styles import css_premium

# ==================================================
# CRIA TABELAS
# ==================================================

Base.metadata.create_all(bind=engine)

# ==================================================
# CONFIG
# ==================================================

st.set_page_config(
    page_title="Ale Hair Barbearia",
    page_icon="✂️",
    layout="centered"
)

# ==================================================
# CSS
# ==================================================

st.markdown(
    css_premium,
    unsafe_allow_html=True
)

# ==================================================
# SESSION STATE
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
# FUNÇÃO HTML SEGURA
# ==================================================

def render_html(html):
    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ==================================================
# DADOS DOS SERVIÇOS
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

    hero_path = "assets/hero.jpg"

    if os.path.exists(hero_path):

        with open(hero_path, "rb") as img_file:

            hero_base64 = base64.b64encode(
                img_file.read()
            ).decode()

        render_html(
            f"""
            <div class="hero">

                <img src="data:image/jpg;base64,{hero_base64}">

                <div class="hero-overlay">

                    <div class="hero-title">
                        Ale Hair
                    </div>

                    <div class="hero-sub">
                        Premium Barber Shop em São Paulo
                    </div>

                </div>

            </div>
            """
        )

    else:

        st.title("✂️ Ale Hair")

    render_html(
        """
        <div class="info-local">
            📍 Av. Amador Bueno da Veiga, 4438 - Penha de França
        </div>
        """
    )

    render_html(
        """
        <div class="avaliacao">
            ★ 5.0 • 120 avaliações
        </div>
        """
    )

    render_html(
        """
        <h2 class="titulo-secao">
            Serviços
        </h2>
        """
    )

    # ==================================================
    # SERVIÇOS
    # ==================================================

    for i, servico in df_servicos.iterrows():

        with st.container(border=True):

            c1, c2, c3 = st.columns([1.2, 3, 1.5])

            # ==========================================
            # IMAGEM
            # ==========================================

            with c1:

                caminho = f"assets/{servico['Imagem']}"

                if os.path.exists(caminho):

                    st.image(
                        caminho,
                        width=95
                    )

                else:

                    render_html(
                        """
                        <div class="icone-servico">
                            ✂️
                        </div>
                        """
                    )

            # ==========================================
            # INFO
            # ==========================================

            with c2:

                render_html(
                    f"""
                    <div class="nome-servico">
                        {servico['Nome_Servico']}
                    </div>
                    """
                )

                render_html(
                    """
                    <div class="descricao-servico">
                        Serviço premium com acabamento profissional.
                    </div>
                    """
                )

                render_html(
                    f"""
                    <div class="tempo-servico">
                        ⏱ {servico['Tempo_Minutos']} minutos
                    </div>
                    """
                )

            # ==========================================
            # PREÇO
            # ==========================================

            with c3:

                render_html(
                    f"""
                    <div class="preco-servico">
                        R$ {servico['Valor_Padrao']}
                    </div>
                    """
                )

                st.write("")

                st.button(
                    "Reservar",
                    key=i,
                    type="primary",
                    width="stretch",
                    on_click=abrir_agendamento,
                    args=(servico.to_dict(),)
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

    # ==========================================
    # RESUMO
    # ==========================================

    render_html(
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
        """
    )

    # ==========================================
    # BARBEIRO
    # ==========================================

    st.markdown("## Seu barbeiro")

    col1, col2 = st.columns([1, 2])

    with col1:

        foto = "assets/barbeiro_ale.jpg"

        if os.path.exists(foto):

            st.image(
                foto,
                width=120
            )

        else:

            st.image(
                "https://cdn-icons-png.flaticon.com/512/4140/4140048.png",
                width=120
            )

    with col2:

        render_html(
            """
            <div class="barbeiro-card">

                <h2>
                    Ale
                </h2>

                <p>
                    Especialista em degradê
                </p>

                <div class="avaliacao-barbeiro">
                    ★ 5.0
                </div>

            </div>
            """
        )

    st.write("")

    # ==========================================
    # DATA
    # ==========================================

    st.markdown("## Escolha a data")

    data = st.date_input(
        "Data",
        min_value=datetime.date.today(),
        label_visibility="collapsed"
    )

    # ==========================================
    # HORÁRIOS
    # ==========================================

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

    # ==========================================
    # CLIENTE
    # ==========================================

    st.markdown("## Seus dados")

    nome = st.text_input(
        "Nome Completo"
    )

    telefone = st.text_input(
        "WhatsApp"
    )

    st.write("")

    # ==========================================
    # BOTÃO
    # ==========================================

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
# PAINEL ADMIN
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

        id_excluir = st.selectbox(
            "Excluir agendamento",
            ids
        )

        if st.button(
            "Excluir Agendamento",
            type="primary"
        ):

            excluir_agendamento(
                db,
                id_excluir
            )

            st.success(
                "Agendamento removido."
            )

            st.rerun()

    else:

        st.info(
            "Nenhum agendamento encontrado."
        )

    db.close()

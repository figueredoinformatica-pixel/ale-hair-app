# ==================================================
# IMPORTS
# ==================================================

import streamlit as st
import pandas as pd
import datetime
import os
import base64
import re

# ==================================================
# DATABASE
# ==================================================

from database import engine, SessionLocal
from models import Base

from services import (
    criar_agendamento,
    listar_agendamentos,
    horarios_disponiveis,
    excluir_agendamento,
    buscar_agendamentos_por_telefone
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
# SIDEBAR PREMIUM
# ==================================================

with st.sidebar:

    st.markdown(
        """
        <style>

        section[data-testid="stSidebar"]{
            background-color:#050505;
            border-right:2px solid #D4AF37;
        }

        section[data-testid="stSidebar"] *{
            color:white;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # LOGO
    # ==================================================

    st.markdown(
        """
        <div style="
            padding-top:20px;
            padding-bottom:10px;
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:12px;
            ">

                <div style="
                    font-size:42px;
                ">
                ✂️
                </div>

                <div>

                    <div style="
                        color:white;
                        font-size:30px;
                        font-weight:800;
                        line-height:1;
                    ">
                    Ale Hair
                    </div>

                    <div style="
                        color:#D4AF37;
                        font-size:12px;
                        letter-spacing:4px;
                        margin-top:5px;
                        font-weight:600;
                    ">
                    BARBEARIA PREMIUM
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # DIVISÓRIA
    # ==================================================

    st.markdown(
        """
        <div style="
            height:1px;
            background:linear-gradient(
                to right,
                transparent,
                #D4AF37,
                transparent
            );
            margin-top:20px;
            margin-bottom:25px;
        ">
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # ENDEREÇO
    # ==================================================

    st.markdown(
        """
        <div style="
            margin-bottom:25px;
        ">

            <div style="
                color:#D4AF37;
                font-size:17px;
                font-weight:700;
                margin-bottom:15px;
            ">
            📍 ENDEREÇO
            </div>

            <div style="
                color:white;
                font-size:15px;
                line-height:1.8;
            ">
            Av. Amador Bueno da Veiga, 4438
            </div>

            <div style="
                color:#9CA3AF;
                font-size:14px;
                margin-top:5px;
            ">
            Penha de França - São Paulo/SP
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # DIVISÓRIA
    # ==================================================

    st.markdown(
        """
        <div style="
            height:1px;
            background:linear-gradient(
                to right,
                transparent,
                #D4AF37,
                transparent
            );
            margin-top:10px;
            margin-bottom:25px;
        ">
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # HORÁRIOS
    # ==================================================

    st.markdown(
        """
        <div style="
            margin-bottom:25px;
        ">

            <div style="
                color:#D4AF37;
                font-size:17px;
                font-weight:700;
                margin-bottom:15px;
            ">
            🕒 HORÁRIO DE FUNCIONAMENTO
            </div>

            <div style="
                display:flex;
                justify-content:space-between;
                color:white;
                margin-bottom:10px;
                font-size:14px;
            ">
                <span>Seg a Sex</span>
                <span style="color:#D4AF37;">
                08h às 20h
                </span>
            </div>

            <div style="
                display:flex;
                justify-content:space-between;
                color:white;
                margin-bottom:10px;
                font-size:14px;
            ">
                <span>Sábado</span>
                <span style="color:#D4AF37;">
                08h às 18h
                </span>
            </div>

            <div style="
                display:flex;
                justify-content:space-between;
                color:white;
                font-size:14px;
            ">
                <span>Domingo</span>

                <span style="
                    color:#EF4444;
                    font-weight:600;
                ">
                Fechado
                </span>
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # DIVISÓRIA
    # ==================================================

    st.markdown(
        """
        <div style="
            height:1px;
            background:linear-gradient(
                to right,
                transparent,
                #D4AF37,
                transparent
            );
            margin-top:10px;
            margin-bottom:25px;
        ">
        </div>
        """,
        unsafe_allow_html=True
    )

    # ==================================================
    # REDES SOCIAIS
    # ==================================================

    st.markdown(
        """
        <div style="
            color:#D4AF37;
            font-size:17px;
            font-weight:700;
            margin-bottom:18px;
        ">
        💬 FALE CONOSCO
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "📱 WhatsApp",
        "https://wa.me/5511999999999",
        use_container_width=True
    )

    st.write("")

    st.link_button(
        "📸 Instagram",
        "https://instagram.com/alehair",
        use_container_width=True
    )
# ==================================================
# SESSION STATE
# ==================================================

if "tela" not in st.session_state:
    st.session_state.tela = "catalogo"

if "servico" not in st.session_state:
    st.session_state.servico = {}

if "horario" not in st.session_state:
    st.session_state.horario = None

if "admin_logado" not in st.session_state:
    st.session_state.admin_logado = False

# ==================================================
# FUNÇÕES
# ==================================================

def mudar_tela(nome):

    st.session_state.tela = nome


def abrir_agendamento(servico):

    st.session_state.servico = servico
    st.session_state.horario = None
    st.session_state.tela = "agendamento"


def login_admin(usuario, senha):

    USER = "alexandre"
    PASS = "ale123"

    if usuario == USER and senha == PASS:

        st.session_state.admin_logado = True
        st.session_state.tela = "painel"

        st.rerun()

    else:

        st.error(
            "Usuário ou senha inválidos."
        )


def logout_admin():

    st.session_state.admin_logado = False
    st.session_state.tela = "catalogo"

    st.rerun()

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

        st.markdown(
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
            """,
            unsafe_allow_html=True
        )



    # ==================================================
    # SERVIÇOS
    # ==================================================

    for i, servico in df_servicos.iterrows():

        with st.container(border=True):

            c1, c2, c3 = st.columns([1.2, 3, 1.5])

            # ==================================================
            # IMAGEM
            # ==================================================

            with c1:

                caminho = f"assets/{servico['Imagem']}"

                if os.path.exists(caminho):

                    st.image(
                        caminho,
                        width=95
                    )

            # ==================================================
            # INFO
            # ==================================================

            with c2:

                st.markdown(
                    f"""
                    <div style='
                        font-size:22px;
                        font-weight:700;
                        margin-top:8px;
                        color:white;
                    '>
                        {servico['Nome_Servico']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div style='
                        font-size:14px;
                        margin-top:4px;
                        color:#D1D5DB;
                    '>
                        Serviço premium com acabamento profissional.
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div style='
                        margin-top:10px;
                        font-size:14px;
                        font-weight:600;
                        color:white;
                    '>
                        ⏱ {servico['Tempo_Minutos']} minutos
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # ==================================================
            # PREÇO
            # ==================================================

            with c3:

                st.markdown(
                    f"""
                    <div style='
                        text-align:right;
                        margin-top:10px;
                        font-size:24px;
                        font-weight:700;
                        color:white;
                    '>
                    R$ {servico['Valor_Padrao']}
                    </div>
                    """,
                    unsafe_allow_html=True
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
        "🔐 Área Administrativa",
        width="stretch",
        on_click=mudar_tela,
        args=("login_admin",),
        key="admin_btn"
    )

# ==================================================
# TELA AGENDAMENTO
# ==================================================

elif st.session_state.tela == "agendamento":

    st.button(
        "⬅️ Voltar",
        on_click=mudar_tela,
        args=("catalogo",),
        key="voltar_agendamento"
    )

    servico = st.session_state.servico

    # ==================================================
    # RESUMO
    # ==================================================

    st.markdown(
        f"""
        <div class="resumo">

        <h2 style="margin-top:0;">
        {servico['Nome_Servico']}
        </h2>

        <p style="font-size:18px;">
        💰 R$ {servico['Valor_Padrao']}
        </p>

        <p style="font-size:16px;">
        ⏱ {servico['Tempo_Minutos']} minutos
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

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

    db = SessionLocal()

    horarios = horarios_disponiveis(
        db,
        data,
        "Ale",
        servico["Nome_Servico"]
    )

    db.close()

    colunas = st.columns(4)

    for i, hora in enumerate(horarios):

        with colunas[i % 4]:

            selecionado = (
                st.session_state.horario == hora
            )

            tipo_botao = "secondary"

            if selecionado:
                tipo_botao = "primary"

            if st.button(
                hora,
                key=f"hora_{hora}",
                type=tipo_botao,
                width="stretch"
            ):

                st.session_state.horario = hora

                st.rerun()

    horario = st.session_state.horario

    # ==================================================
    # DADOS CLIENTE
    # ==================================================

    if horario:

        st.success(
            f"Horário selecionado: {horario}"
        )

        st.markdown("## Seus dados")

        nome = st.text_input(
            "Nome Completo",
            key="nome_cliente"
        )

        telefone = st.text_input(
            "WhatsApp",
            placeholder="(11) 99999-9999",
            max_chars=15,
            key="telefone_cliente"
        )

        if telefone:

            numeros = re.sub(
                r"\D",
                "",
                telefone
            )

            if len(numeros) >= 11:

                telefone = (
                    f"({numeros[:2]}) "
                    f"{numeros[2:7]}-"
                    f"{numeros[7:11]}"
                )

        st.write("")

        if st.button(
            "Confirmar Reserva",
            type="primary",
            width="stretch",
            key="confirmar_reserva"
        ):

            if not nome or not telefone:

                st.warning(
                    "Preencha todos os campos."
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
        # CONSULTAR AGENDAMENTO
        # ==================================================

        st.markdown("---")

        st.markdown("## 🔎 Consultar agendamento")

        telefone_busca = st.text_input(
            "Digite seu WhatsApp",
            placeholder="(11) 99999-9999",
            max_chars=15,
            key="consulta_agendamento"
        )

        if st.button(
            "Consultar",
            key="btn_consultar"
        ):

            db = SessionLocal()

            resultados = buscar_agendamentos_por_telefone(
                db,
                telefone_busca
            )

            db.close()

            if resultados:

                st.success(
                    f"{len(resultados)} agendamento(s) encontrado(s)"
                )

                for ag in resultados:

                    st.markdown(
                        f"""
                        <div class="resumo">

                        <h3>
                        💈 {ag.servico}
                        </h3>

                        <p>
                        📅 {ag.data.strftime('%d/%m/%Y')}
                        </p>

                        <p>
                        ⏰ {ag.horario}
                        </p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.warning(
                    "Nenhum agendamento encontrado."
                )

# ==================================================
# LOGIN ADMIN
# ==================================================

elif st.session_state.tela == "login_admin":

    st.button(
        "⬅️ Voltar",
        on_click=mudar_tela,
        args=("catalogo",),
        key="voltar_login"
    )

    st.title("🔐 Área Administrativa")

    usuario = st.text_input(
        "Usuário",
        key="usuario_admin"
    )

    senha = st.text_input(
        "Senha",
        type="password",
        key="senha_admin"
    )

    if st.button(
        "Entrar",
        type="primary",
        width="stretch",
        key="entrar_admin"
    ):

        login_admin(
            usuario,
            senha
        )

# ==================================================
# PAINEL ADMIN
# ==================================================

elif st.session_state.tela == "painel":

    if not st.session_state.admin_logado:

        st.warning(
            "Faça login para acessar."
        )

        st.stop()

    st.button(
        "⬅️ Voltar",
        on_click=mudar_tela,
        args=("catalogo",),
        key="voltar_painel"
    )

    st.title("📊 Agenda")

    st.button(
        "🚪 Sair",
        on_click=logout_admin,
        key="logout_admin"
    )

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
                "Data": a.data.strftime("%d/%m/%Y"),
                "Horário": a.horario

            })

        df = pd.DataFrame(dados)

        st.dataframe(
            df,
            width="stretch",
            hide_index=True
        )

        ids = [a.id for a in agendamentos]

        id_excluir = st.selectbox(
            "Excluir agendamento",
            ids,
            key="select_excluir"
        )

        if st.button(
            "Excluir Agendamento",
            type="primary",
            key="btn_excluir"
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


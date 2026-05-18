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

    else:

        st.title("✂️ Ale Hair")

    st.markdown(
        """
        <div style='
            margin-bottom:20px;
            color:#6B7280;
            font-size:15px;
        '>
        📍 Av. Amador Bueno da Veiga, 4438 - Penha de França
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style='
            margin-bottom:25px;
            font-size:16px;
            font-weight:600;
            color:#111827;
        '>
        ★ 5.0 • 120 avaliações
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h2 style='margin-bottom:25px;'>
        Serviços
        </h2>
        """,
        unsafe_allow_html=True
    )

 
    # ==================================================
    # LISTA DE SERVIÇOS
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

                    st.markdown(
                        """
                        <div style='
                            font-size:60px;
                            text-align:center;
                        '>
                        ✂️
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            # ==========================================
            # INFO
            # ==========================================

            with c2:

                st.markdown(
                    f"""
                    <div style='
                        font-size:22px;
                        font-weight:700;
                        margin-top:8px;
                        color:#111827;
                    '>
                        {servico['Nome_Servico']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div style='
                        color:#6B7280;
                        font-size:14px;
                        margin-top:4px;
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
                        color:#111827;
                        font-weight:600;
                    '>
                        ⏱ {servico['Tempo_Minutos']} minutos
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # ==========================================
            # PREÇO + BOTÃO
            # ==========================================

            with c3:

                st.markdown(
                    f"""
                    <div style='
                        text-align:right;
                        margin-top:10px;
                        font-size:24px;
                        font-weight:700;
                        color:#111827;
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
        args=("login_admin",)
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

    # ==========================================
    # RESUMO SERVIÇO
    # ==========================================

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

    st.write("")

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

    with col2:

        st.markdown(
            """
            <div class="barbeiro-card">

            <h2 style="margin-bottom:0;">
            Ale
            </h2>

            <p style="
            color:#6B7280;
            margin-top:8px;
            ">
            Especialista em degradê
            </p>

            <p style="
            font-weight:700;
            margin-top:14px;
            ">
            ★ 5.0
            </p>

            </div>
            """,
            unsafe_allow_html=True
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

    db.close()

    # cria session state se não existir
    if "horario" not in st.session_state:
        st.session_state.horario = None

    # grid dos horários
    colunas = st.columns(4)

    for i, hora in enumerate(horarios):

        with colunas[i % 4]:

            ocupado = hora in ocupados

            selecionado = (
                st.session_state.horario == hora
            )

            texto_botao = hora

            if ocupado:
                texto_botao = f"🔒 {hora}"

            tipo_botao = "secondary"

            if selecionado:
                tipo_botao = "primary"

            if st.button(
                texto_botao,
                key=f"hora_{hora}",
                disabled=ocupado,
                type=tipo_botao,
                width="stretch"
            ):

                st.session_state.horario = hora
                st.rerun()

    horario = st.session_state.horario

    if horario:

        st.success(
            f"Horário selecionado: {horario}"
        )

        # ==========================================
        # CLIENTE
        # ==========================================

        st.markdown("## Seus dados")

        nome = st.text_input(
            "Nome Completo"
        )

    import re

    telefone = st.text_input(
    "WhatsApp",
    placeholder="(11) 99999-9999",
    max_chars=15,
    key="telefone_cliente"
)

    # mascara automática
    if telefone:
        
            numeros = re.sub(r"\D", "", telefone)

            if len(numeros) >= 11:

                telefone_formatado = (
                f"({numeros[:2]}) "
                f"{numeros[2:7]}-"
                f"{numeros[7:11]}"
            )

            telefone = telefone_formatado

    

        # ==========================================
        # CONFIRMAR
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
    # CONSULTAR AGENDAMENTO
    # COLOCAR DENTRO DA TELA "agendamento"
    # ==================================================

    with st.expander("🔎 Já possui agendamento?"):

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

                        <p>
                        ✂️ {ag.barbeiro}
                        </p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.warning(
                    "Nenhum agendamento encontrado."
                )

    st.button(
    "⬅️ Voltar",
    on_click=mudar_tela,
    args=("catalogo",),
    key="voltar_login"
)

# ==================================================
# LOGIN ADMIN
# ==================================================

elif st.session_state.tela == "login_admin":

    st.button(
        "⬅️ Voltar",
        on_click=mudar_tela,
        args=("catalogo",)
    )

    st.markdown(
        """
        <h1 style='margin-bottom:0;'>
        🔐 Área Administrativa
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='color:#6B7280;'>
        Acesso restrito para administradores.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    usuario = st.text_input(
        "Usuário"
    )

    senha = st.text_input(
        "Senha",
        type="password"
    )

    st.write("")

    if st.button(
        "Entrar",
        type="primary",
        width="stretch"
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
        key="voltar_consulta"
    )

    st.title("📊 Agenda")

    st.button(
        "🚪 Sair",
        on_click=logout_admin
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

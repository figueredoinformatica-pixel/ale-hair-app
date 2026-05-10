import streamlit as st
import datetime
import calendar
import pandas as pd
import os

st.set_page_config(page_title="Ale Hair Barbearia", page_icon="✂️", layout="centered")

# ==========================================
# 0. VISUAL PREMIUM (PALETA PRETO E BRANCO)
# ==========================================
css_premium = """
<style>
    .stApp { background-color: #F9FAFB; }
    
    div.stButton > button[kind="primary"] {
        background-color: #111827 !important;
        border-radius: 8px !important;
        padding: 4px 16px !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }
    
    div.stButton > button[kind="primary"] p {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }

    div.stButton > button[kind="primary"]:hover { 
        background-color: #1F2937 !important; 
        box-shadow: 0 4px 6px rgba(17, 24, 39, 0.15) !important;
    }

    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #FFFFFF !important;
        border-radius: 12px !important;
        border: 1px solid #e5e7eb !important; 
        box-shadow: 0 1px 3px rgba(17, 24, 39, 0.05) !important;
        padding: 0px !important;
        margin-bottom: 10px !important;
    }

    div.stButton > button p {
        white-space: nowrap !important;
        font-size: 15px !important;
        color: #374151 !important; 
    }
    
    div[data-testid="column"] div.stButton > button {
        padding: 0px !important;
        height: 45px !important;
        border-radius: 8px !important;
        border: 1px solid #f3f4f6 !important;
        background-color: #FFFFFF !important;
    }
    
    div[data-testid="column"] div.stButton > button:focus {
        border-color: #111827 !important;
        background-color: #111827 !important;
    }
    div[data-testid="column"] div.stButton > button:focus p {
        color: #FFFFFF !important;
    }

    .resumo-card {
        background-color: #FFFFFF;
        border-left: 4px solid #111827;
        padding: 16px;
        border-radius: 6px;
        margin-bottom: 30px;
        box-shadow: 0 1px 3px rgba(17, 24, 39, 0.08);
    }

    .stMarkdown, .stText { color: #111827 !important; }
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
</style>
"""
st.markdown(css_premium, unsafe_allow_html=True)

# ==========================================
# 1. CONTROLE DE ESTADO
# ==========================================
if 'tela_atual' not in st.session_state:
    st.session_state.tela_atual = 'catalogo'
if 'servico_escolhido' not in st.session_state:
    st.session_state.servico_escolhido = {}
if 'agendamentos_salvos' not in st.session_state:
    st.session_state.agendamentos_salvos = {}
if 'data_escolhida' not in st.session_state:
    st.session_state.data_escolhida = datetime.date.today()

def mudar_tela(nova_tela):
    st.session_state.tela_atual = nova_tela

def ir_para_agendamento(servico_dict):
    st.session_state.servico_escolhido = servico_dict
    st.session_state.data_escolhida = datetime.date.today()
    st.session_state.tela_atual = 'agendamento'

# ==========================================
# 2. DADOS DOS SERVIÇOS
# ==========================================
dados_planilha = [
    {"Nome_Servico": "Corte Masculino", "Valor_Padrao": 40.00, "Tempo_Minutos": 30, "Imagem": "corte.png"},
    {"Nome_Servico": "Barba", "Valor_Padrao": 30.00, "Tempo_Minutos": 30, "Imagem": "barba.png"},
    {"Nome_Servico": "Combo (Corte + Barba)", "Valor_Padrao": 70.00, "Tempo_Minutos": 45, "Imagem": "corteebarba.png"}
]
df_servicos = pd.DataFrame(dados_planilha)

# ==========================================
# 3. TELA: CATÁLOGO
# ==========================================
if st.session_state.tela_atual == 'catalogo':
    col_logo, col_texto = st.columns([1, 4])
    with col_logo:
        if os.path.exists("assets/logo.png"):
            st.image("assets/logo.png", width=120)
        else:
            st.markdown("<h1 style='color: #111827; font-size:40px;'>AH</h1>", unsafe_allow_html=True)
            
    with col_texto:
        st.markdown("<h1 style='margin-bottom: 0px; color: #111827; margin-top:0px;'>Ale Hair</h1>", unsafe_allow_html=True)
        st.markdown("<p style='color: #374151; font-size: 14px; margin-top: 0px;'>Av. Amador Bueno da Veiga, 4438 - Penha de França, São Paulo - SP</p>", unsafe_allow_html=True)
    
    st.markdown("**★ 5.0** <span style='color: #111827; font-size: 14px; font-weight: 500;'>(120 avaliações)</span>", unsafe_allow_html=True)
    st.divider()
    
    st.markdown("<h2 style='color: #111827;'>Serviços</h2>", unsafe_allow_html=True)

    for index, servico in df_servicos.iterrows():
        with st.container(border=True):
            c_img, c_info, c_action = st.columns([1.2, 3, 1.5])
            with c_img:
                caminho_imagem = f"assets/{servico['Imagem']}"
                if os.path.exists(caminho_imagem):
                    st.image(caminho_imagem, width=80)
                else:
                    st.markdown("<div style='font-size:40px; text-align:center;'>✂️</div>", unsafe_allow_html=True)
            with c_info:
                st.markdown(f"<p style='font-size:17px; font-weight:600; color:#111827; margin-top:15px;'>{servico['Nome_Servico']}</p>", unsafe_allow_html=True)
            with c_action:
                st.markdown(f"<div style='text-align: right; color: #111827; margin-top:8px;'><b style='font-size:15px;'>R$ {servico['Valor_Padrao']:.2f}</b><br><span style='font-size:12px; color: #374151;'>{servico['Tempo_Minutos']}min</span></div>", unsafe_allow_html=True)
                st.button("Reservar", key=f"res_{index}", type="primary", use_container_width=True, on_click=ir_para_agendamento, args=(servico.to_dict(),))

    st.write("")
    st.button("🔐 Acesso Profissional", on_click=mudar_tela, args=('login',))

# ==========================================
# 4. TELA: AGENDAMENTO
# ==========================================
elif st.session_state.tela_atual == 'agendamento':
    st.button("⬅️ Voltar", on_click=mudar_tela, args=('catalogo',))
    
    serv_selecionado = st.session_state.servico_escolhido
    st.markdown(f"""<div class="resumo-card"><h3 style="margin:0;">{serv_selecionado['Nome_Servico']}</h3><p style="margin:0; color:#374151; font-size:14px;">Valor: R$ {serv_selecionado['Valor_Padrao']:.2f} | Duração: {serv_selecionado['Tempo_Minutos']}min</p></div>""", unsafe_allow_html=True)
    
    st.markdown("<h4>1. Profissional</h4>", unsafe_allow_html=True)
    barbeiro = st.radio("Selecione:", ["Ale"], horizontal=True, label_visibility="collapsed")
    
    st.markdown("<h4>2. Escolha o Dia</h4>", unsafe_allow_html=True)
    hoje = datetime.date.today()
    matriz_mes = calendar.Calendar(firstweekday=6).monthdatescalendar(hoje.year, hoje.month)
    
    _, col_c, _ = st.columns([1, 6, 1])
    with col_c:
        cols_d = st.columns(7)
        for i, d in enumerate(["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sáb"]):
            cols_d[i].markdown(f"<div style='text-align:center; font-size:12px; font-weight:bold; color:#888;'>{d}</div>", unsafe_allow_html=True)
        for semana in matriz_mes:
            cols = st.columns(7)
            for i, dia_data in enumerate(semana):
                if dia_data.month == hoje.month:
                    tipo = "primary" if st.session_state.data_escolhida == dia_data else "secondary"
                    if cols[i].button(str(dia_data.day), key=f"d_{dia_data}", disabled=(dia_data < hoje), type=tipo, use_container_width=True):
                        st.session_state.data_escolhida = dia_data
                        st.rerun()
    
    st.markdown("<h4>3. Horário</h4>", unsafe_allow_html=True)
    data_s = str(st.session_state.data_escolhida)
    horarios = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
    ocupados = list(st.session_state.agendamentos_salvos.get(data_s, {}).keys())
    livres = [h for h in horarios if h not in ocupados]
    
    if livres:
        h_esc = st.radio("Horários:", livres, horizontal=True, label_visibility="collapsed")
    else:
        st.error("Agenda cheia.")
        h_esc = None

    st.markdown("<h4>4. Seus Dados</h4>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    nome = c1.text_input("Nome:")
    tel = c2.text_input("WhatsApp:")
    
    if st.button("Confirmar Reserva", type="primary", use_container_width=True):
        if nome and tel and h_esc:
            if data_s not in st.session_state.agendamentos_salvos: st.session_state.agendamentos_salvos[data_s] = {}
            st.session_state.agendamentos_salvos[data_s][h_esc] = {"nome": nome, "telefone": tel, "servico": serv_selecionado['Nome_Servico'], "barbeiro": barbeiro}
            st.success(f"Confirmado para {st.session_state.data_escolhida.strftime('%d/%m/%Y')} às {h_esc}!")
        else: st.warning("Preencha tudo.")

# ==========================================
# 5. ADMIN
# ==========================================
elif st.session_state.tela_atual == 'login':
    st.button("⬅️ Voltar ao Início", on_click=mudar_tela, args=('catalogo',))
    st.title("🔒 Acesso Restrito")
    u = st.text_input("Usuário")
    s = st.text_input("Senha", type="password")
    if st.button("Entrar", type="primary"):
        if u == "admin" and s == "123": 
            mudar_tela('painel') # Vai para a tela painel
            st.rerun()
        else: 
            st.error("❌ Usuário ou senha incorretos! Tente admin e 123.")

# Aqui estava o erro! Eu tinha escrito 'panel' em vez de 'painel'
elif st.session_state.tela_atual == 'painel': 
    st.button("🚪 Sair do Sistema", on_click=mudar_tela, args=('catalogo',))
    st.title("📊 Agenda do Ale Hair")
    
    # Recoloquei a lógica para mostrar a tabela bonita e organizada
    lista_completa = []
    for data, horarios in st.session_state.agendamentos_salvos.items():
        for hora, info in horarios.items():
            info_completa = info.copy()
            data_formatada = datetime.datetime.strptime(data, "%Y-%m-%d").strftime("%d/%m/%Y")
            info_completa['Data'] = data_formatada
            info_completa['Hora'] = hora
            lista_completa.append(info_completa)
    
    if lista_completa:
        df = pd.DataFrame(lista_completa)
        df = df[['Data', 'Hora', 'nome', 'telefone', 'servico']]
        df.columns = ['Data', 'Horário', 'Cliente', 'WhatsApp', 'Serviço']
        df = df.sort_values(by=['Data', 'Horário'])
        
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("Sua agenda está vazia no momento. Quando um cliente agendar, aparecerá aqui.")

import streamlit as st
import datetime
import pandas as pd

# Configuração inicial
st.set_page_config(page_title="Nerys97 - Barber System", page_icon="✂️", layout="centered")

# ==========================================
# 1. CONTROLE DE TELAS E BANCO DE DADOS
# ==========================================
# Controla qual tela deve aparecer: 'inicio', 'cliente', 'login', ou 'painel'
if 'tela_atual' not in st.session_state:
    st.session_state['tela_atual'] = 'inicio'

if 'agendamentos_salvos' not in st.session_state:
    st.session_state['agendamentos_salvos'] = {}

# Funções de navegação (botões vão acionar isso)
def ir_para_inicio():
    st.session_state['tela_atual'] = 'inicio'

def ir_para_cliente():
    st.session_state['tela_atual'] = 'cliente'

def ir_para_login():
    st.session_state['tela_atual'] = 'login'

def ir_para_painel():
    st.session_state['tela_atual'] = 'painel'

# ==========================================
# 2. TELA 1: INÍCIO (O Menu que você sugeriu)
# ==========================================
if st.session_state['tela_atual'] == 'inicio':
    st.title("✂️ Bem-vindo à Nerys97")
    st.write("Selecione uma opção abaixo para começar:")
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("👨‍🦱 Sou Cliente \n(Quero Agendar)", use_container_width=True, on_click=ir_para_cliente)
    with col2:
        st.button("💈 Sou Barbeiro \n(Acesso Restrito)", use_container_width=True, on_click=ir_para_login)

# ==========================================
# 3. TELA 2: LOGIN DO BARBEIRO
# ==========================================
elif st.session_state['tela_atual'] == 'login':
    st.button("⬅️ Voltar", on_click=ir_para_inicio)
    
    st.title("🔒 Acesso do Profissional")
    usuario = st.text_input("Usuário (ex: admin):")
    senha = st.text_input("Senha (ex: barber123):", type="password")
    
    if st.button("Entrar", type="primary"):
        if usuario == "admin" and senha == "barber123":
            ir_para_painel()
            st.rerun() # Atualiza a tela imediatamente
        else:
            st.error("Usuário ou senha incorretos.")

# ==========================================
# 4. TELA 3: PAINEL DO BARBEIRO
# ==========================================
elif st.session_state['tela_atual'] == 'painel':
    st.button("Sair (Logout)", on_click=ir_para_inicio)
    
    st.title("📊 Painel - Nerys97")
    st.write("Bem-vindo de volta! Aqui estão seus agendamentos.")
    
    # Criando a lista de agendamentos para mostrar na tabela
    lista_completa = []
    for data, horarios in st.session_state['agendamentos_salvos'].items():
        for hora, info in horarios.items():
            info_completa = info.copy()
            info_completa['Data'] = data
            info_completa['Hora'] = hora
            lista_completa.append(info_completa)
    
    if lista_completa:
        df_todos = pd.DataFrame(lista_completa)[['Data', 'Hora', 'nome', 'telefone', 'servico', 'barbeiro']]
        st.dataframe(df_todos, use_container_width=True)
    else:
        st.info("Nenhum agendamento realizado ainda.")

# ==========================================
# 5. TELA 4: AGENDAMENTO DO CLIENTE
# ==========================================
elif st.session_state['tela_atual'] == 'cliente':
    st.button("⬅️ Voltar ao Início", on_click=ir_para_inicio)
    
    st.title("✂️ Agendar Horário")
    st.divider()

    # Campos do formulário
    nome_cliente = st.text_input("Seu Nome:")
    tel_cliente = st.text_input("Seu WhatsApp:")

    col_serv, col_barb = st.columns(2)
    with col_serv: servico = st.selectbox("Serviço:", ["Corte", "Barba", "Corte + Barba"])
    with col_barb: barbeiro = st.selectbox("Profissional:", ["Josué", "Erik", "Qualquer um"])

    col_dat, col_hor = st.columns(2)
    with col_dat:
        data = st.date_input("Data:", min_value=datetime.date.today())
        data_str = str(data)
    with col_hor:
        horarios_totais = ["09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00", "18:00"]
        ocupados = list(st.session_state['agendamentos_salvos'].get(data_str, {}).keys())
        disponiveis = [h for h in horarios_totais if h not in ocupados]
        
        if disponiveis:
            horario_escolhido = st.selectbox("Horários Livres:", disponiveis)
        else:
            st.error("Lotado para este dia!")
            horario_escolhido = None

    if st.button("Confirmar Agendamento", type="primary", use_container_width=True):
        if not nome_cliente or not tel_cliente or not horario_escolhido:
            st.warning("Preencha todos os campos para confirmar.")
        else:
            if data_str not in st.session_state['agendamentos_salvos']:
                st.session_state['agendamentos_salvos'][data_str] = {}
            
            st.session_state['agendamentos_salvos'][data_str][horario_escolhido] = {
                "nome": nome_cliente, "telefone": tel_cliente, 
                "servico": servico, "barbeiro": barbeiro
            }
            st.success("✅ Agendado com sucesso!")
            st.balloons()
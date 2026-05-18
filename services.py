from models import Agendamento
import re

from datetime import datetime, timedelta

# ==================================================
# LIMPAR TELEFONE
# ==================================================

def limpar_telefone(telefone):

    return re.sub(r"\D", "", telefone)

# ==================================================
# DURAÇÃO DOS SERVIÇOS
# ==================================================

SERVICOS_TEMPO = {
    "Corte Masculino": 30,
    "Barba": 30,
    "Combo Corte + Barba": 45
}

# ==================================================
# GERAR HORÁRIOS
# ==================================================

def gerar_horarios():

    inicio = datetime.strptime("08:00", "%H:%M")

    fim = datetime.strptime("20:00", "%H:%M")

    horarios = []

    atual = inicio

    while atual < fim:

        horarios.append(
            atual.strftime("%H:%M")
        )

        atual += timedelta(minutes=30)

    return horarios

# ==================================================
# VERIFICAR CONFLITO
# ==================================================

def horario_conflita(
    inicio_novo,
    fim_novo,
    inicio_existente,
    fim_existente
):

    return (
        inicio_novo < fim_existente
        and fim_novo > inicio_existente
    )

# ==================================================
# HORÁRIOS DISPONÍVEIS
# ==================================================

def horarios_disponiveis(
    db,
    data,
    barbeiro,
    servico
):

    todos_horarios = gerar_horarios()

    duracao_servico = SERVICOS_TEMPO[servico]

    agendamentos = db.query(
        Agendamento
    ).filter(
        Agendamento.data == data,
        Agendamento.barbeiro == barbeiro
    ).all()

    horarios_livres = []

    for horario in todos_horarios:

        inicio_novo = datetime.strptime(
            horario,
            "%H:%M"
        )

        fim_novo = inicio_novo + timedelta(
            minutes=duracao_servico
        )

        # impede passar das 20h
        limite = datetime.strptime(
            "20:00",
            "%H:%M"
        )

        if fim_novo > limite:
            continue

        conflito = False

        for ag in agendamentos:

            inicio_existente = datetime.strptime(
                ag.horario,
                "%H:%M"
            )

            duracao_existente = SERVICOS_TEMPO.get(
                ag.servico,
                30
            )

            fim_existente = (
                inicio_existente
                + timedelta(
                    minutes=duracao_existente
                )
            )

            if horario_conflita(
                inicio_novo,
                fim_novo,
                inicio_existente,
                fim_existente
            ):

                conflito = True
                break

        if not conflito:

            horarios_livres.append(horario)

    return horarios_livres

# ==================================================
# CRIAR AGENDAMENTO
# ==================================================

def criar_agendamento(
    db,
    nome,
    telefone,
    servico,
    barbeiro,
    data,
    horario
):

    telefone = limpar_telefone(telefone)

    novo = Agendamento(
        nome=nome,
        telefone=telefone,
        servico=servico,
        barbeiro=barbeiro,
        data=data,
        horario=horario
    )

    db.add(novo)

    db.commit()

    db.refresh(novo)

    return novo

# ==================================================
# LISTAR AGENDAMENTOS
# ==================================================

def listar_agendamentos(db):

    return db.query(
        Agendamento
    ).all()

# ==================================================
# EXCLUIR AGENDAMENTO
# ==================================================

def excluir_agendamento(
    db,
    id_agendamento
):

    agendamento = db.query(
        Agendamento
    ).filter(
        Agendamento.id == id_agendamento
    ).first()

    if agendamento:

        db.delete(agendamento)

        db.commit()

# ==================================================
# BUSCAR POR TELEFONE
# ==================================================

def buscar_agendamentos_por_telefone(
    db,
    telefone
):

    telefone = limpar_telefone(telefone)

    return db.query(
        Agendamento
    ).filter(
        Agendamento.telefone == telefone
    ).all()

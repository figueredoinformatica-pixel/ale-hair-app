from models import Agendamento

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
    ).order_by(
        Agendamento.data,
        Agendamento.horario
    ).all()

# ==================================================
# HORÁRIOS OCUPADOS
# ==================================================

def horarios_ocupados(
    db,
    data,
    barbeiro
):

    resultados = db.query(
        Agendamento
    ).filter(
        Agendamento.data == data,
        Agendamento.barbeiro == barbeiro
    ).all()

    return [r.horario for r in resultados]

# ==================================================
# EXCLUIR
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
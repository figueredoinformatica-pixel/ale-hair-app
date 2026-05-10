from sqlalchemy.orm import Session
from models import Agendamento

# ==================================================
# CRIAR AGENDAMENTO
# ==================================================

def criar_agendamento(
    db: Session,
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

def listar_agendamentos(db: Session):

    return db.query(Agendamento).all()

# ==================================================
# HORÁRIOS OCUPADOS
# ==================================================

def horarios_ocupados(
    db: Session,
    data,
    barbeiro
):

    agendamentos = db.query(
        Agendamento
    ).filter(
        Agendamento.data == data,
        Agendamento.barbeiro == barbeiro
    ).all()

    return [a.horario for a in agendamentos]

# ==================================================
# EXCLUIR
# ==================================================

def excluir_agendamento(
    db: Session,
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

        return True

    return False
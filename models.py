from sqlalchemy import Column, Integer, String, Date
from database import Base

# ==================================================
# AGENDAMENTOS
# ==================================================

class Agendamento(Base):

    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String, nullable=False)

    telefone = Column(String, nullable=False)

    servico = Column(String, nullable=False)

    barbeiro = Column(String, nullable=False)

    data = Column(Date, nullable=False)

    horario = Column(String, nullable=False)
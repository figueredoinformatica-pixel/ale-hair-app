from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class Agendamento(Base):

    __tablename__ = "agendamentos"

    id = Column(Integer, primary_key=True, index=True)

    nome = Column(String)

    telefone = Column(String)

    servico = Column(String)

    barbeiro = Column(String)

    data = Column(Date)

    horario = Column(String)

UniqueConstraint(
    "data",
    "horario",
    "barbeiro"
)

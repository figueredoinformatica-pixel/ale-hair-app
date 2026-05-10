from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ==================================================
# BANCO SQLITE
# ==================================================

DATABASE_URL = "sqlite:///barbearia.db"

# ==================================================
# ENGINE
# ==================================================

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# ==================================================
# SESSÃO
# ==================================================

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ==================================================
# BASE
# ==================================================

Base = declarative_base()
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ==================================================
# DATABASE
# ==================================================

DATABASE_URL = "sqlite:///alehair.db"

# ==================================================
# ENGINE
# ==================================================

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# ==================================================
# SESSION
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
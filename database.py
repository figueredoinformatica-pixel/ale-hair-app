from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://neondb_owner:npg_u2RL4hCYbOTH@ep-muddy-glade-acral3e1.sa-east-1.aws.neon.tech/neondb?sslmode=require"

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
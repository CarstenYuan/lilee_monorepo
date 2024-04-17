from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ENGINE_URL = "mysql+pymysql://root:1qaz2wsx@ABCDEFGHIJKLMNOPQRSTUVWXYZ:3306/lilee"
# ENGINE_URL = "mysql+pymysql://root:1qaz2wsx@localhost:3306/lilee"  # for local tests
ENGINE_URL = "mysql+pymysql://root:1qaz2wsx@mysqlDB:3306/lilee"


engine = create_engine(ENGINE_URL)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, expire_on_commit=False
)


def get_session():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

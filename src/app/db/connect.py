from sqlalchemy import create_engine
from db.credentials import credentials
from sqlalchemy import create_engine

conn_str = (
   f"postgresql+psycopg2://{credentials['pg_user']}:{credentials['pg_password']}"
   f"@{credentials['pg_host']}:{credentials['pg_port']}/{credentials['pg_database']}"
)

engine = create_engine(conn_str)

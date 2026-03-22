# Product_API

uv init <br>
uv add fastapi "uvicorn[standard]" sqlalchemy psycopg2-binary pydantic <br>
uv run setup_db.py <br>
uv run uvicorn main:app --reload<br>

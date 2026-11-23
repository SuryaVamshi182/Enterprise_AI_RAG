"""Enterprise AI RAG application package and database schema initializer."""

import sys
from pathlib import Path

import psycopg
from dotenv import load_dotenv
import os

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")
SCHEMA = ROOT / "infra" / "schema.sql"
REQUIRED = ('documents', 'feedback', 'audit_events', 'approvals', 'chat_messages')

def main():
    url = os.getenv("DATABASE_URL",'').strip()
    if not url or 'YOUR' in url or 'USERNAME:' in url:
        print('ERROR: Set a real DATABASE_URL in the .env file.') 
        return 1
    if not SCHEMA.isfile():
        print(f'ERROR: Schema not found: {SCHEMA}')
        return 1
    print('Connecting to Render PostgreSQL (credentials hidden)...')
    try:
        with conn.transaction():
            conn.execute(SCHEMA.read_text(encoding = 'utf-8'))
        with conn.cursor() as cur:
            cur.execute("SELECT current database()")
            dbname = cur.fetchone()[0]
            cur.execute('SELECT to_regclass(%s)', ('public.chat_messages',))
            if cur.fetchone()[0] is None:
                raise RuntimeError('chat_messages table was not created')
            for table in REQUIRED:
                cur.execute(f'SELECT to_regclass(%s)', (f'public.{table}',))
                if cur.fetchone()[0] is None:
                    raise RuntimeError(f'Missing table: {table}')
            print(f'SUCCESS: Database {dbname!r} initialized; verified {len(REQUIRED)} tables.')
            print(f'You can safely return this script. Existing rows are preserved')
            return 0
    except Exception as e:
        print(f'ERROR: Database initialization failed: {e}')
        return 1
    
if __name__ == "__main__":
    sys.exit(main())


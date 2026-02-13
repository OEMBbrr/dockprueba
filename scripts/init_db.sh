#!/bin/sh
set -e

echo "🔄 Esperando a que PostgreSQL esté listo..."
echo "POSTGRES_USER: $POSTGRES_USER"
echo "POSTGRES_DB: $POSTGRES_DB"
echo "DATABASE_URL: $DATABASE_URL"

until pg_isready -h db -U $POSTGRES_USER -d $POSTGRES_DB; do
  >&2 echo "⏳ Postgres no está listo - esperando 1 segundo..."
  sleep 1
done

echo "✅ PostgreSQL listo. Ejecutando migraciones (si las hubiera)..."
alembic upgrade head || echo "⚠️  No hay migraciones, se crearán las tablas mediante seed."

echo "🌱 Sembrando datos de ejemplo (las tablas se crearán automáticamente si no existen)..."
python scripts/seed_db.py

echo "🚀 Iniciando servidor..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
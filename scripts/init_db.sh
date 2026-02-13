#!/bin/sh
set -e

echo "🔄 Esperando a que PostgreSQL esté listo..."
echo "POSTGRES_USER: $POSTGRES_USER"
echo "POSTGRES_DB: $POSTGRES_DB"
echo "DATABASE_URL: $DATABASE_URL"

# Usamos template1 porque siempre existe en PostgreSQL
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -d template1 -c 'SELECT 1'; do
  echo "⏳ Error al conectar, reintentando en 1 segundo..."
  sleep 1
done

echo "✅ PostgreSQL listo. Ejecutando migraciones..."

# Intentar aplicar migraciones existentes
alembic upgrade head || {
  echo "⚠️  No hay migraciones aplicadas. Generando migración inicial..."
  alembic revision --autogenerate -m "initial"
  alembic upgrade head
}

echo "🌱 Sembrando datos de ejemplo..."
python scripts/seed_db.py

echo "🚀 Iniciando servidor..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
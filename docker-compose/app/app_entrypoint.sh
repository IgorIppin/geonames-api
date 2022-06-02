#! bin/bash


until PGPASSWORD=$db_password psql -h "$db_host" -U "$db_user" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done

alembic upgrade head

uvicorn mastermind_api.api.app:app --host 0.0.0.0 --port 5000 --workers 1

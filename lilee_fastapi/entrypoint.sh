#!/bin/bash

echo "Waiting for MySQL..."
while ! nc -z mysqlDB 3306; do
  sleep 1
done
echo "MySQL started"

alembic upgrade head

sleep 5

python data/populate_data.py

cd src

exec uvicorn main:app --host 0.0.0.0 --port 9000

#!/bin/bash

echo "Waiting for MySQL..."
while ! nc -z mysqlDB 3306; do
  sleep 1
done
echo "MySQL started"

alembic upgrade head

sleep 5

cd src

python populate_mock_data/mock_data_creator.py

exec uvicorn main:app --host 0.0.0.0 --port 9000

#!/bin/bash

echo "Waiting for MySQL..."
while ! nc -z mysqlDB 3306; do
  sleep 1
done
echo "MySQL started"

exec npm run dev
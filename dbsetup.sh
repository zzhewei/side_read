#!/usr/bin/env bash
echo waiting for db ...

while ! nc -z hcc_mysql 3306; do
  sleep 0.1
done

echo MySQL started

exec gunicorn -b :8999 --threads 4 app:app --preload
#!/usr/bin/env bash
echo waiting for db ...

while ! nc -z read_postgresql 5432; do
  sleep 0.1
done

echo SQL started

exec gunicorn -b :5555 --threads 4 app:app --preload
#!/bin/sh
#python3  app.py

gunicorn -b :5000 --workers=3 --threads 10 --log-level debug src.application:app --log-config src/config/gunicorn.conf

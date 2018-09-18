#!/usr/bin/env bash
export FLASK_ENV=development
export FLASK_APP=domain1.py
flask run --port 5000 &
export FLASK_APP=domain2.py
flask run --port=5001 &
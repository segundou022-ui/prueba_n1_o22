#!/usr/bin/env bash
gunicorn server:app --bind 0.0.0.0:$PORT

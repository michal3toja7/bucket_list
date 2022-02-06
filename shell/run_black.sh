#!/usr/bin/env bash
# this script adapts Python code using Black

source shell/consts.sh
black . --line-length "79" --exclude venv/
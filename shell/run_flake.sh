#!/usr/bin/env bash
# this script checks Python code style using flake8

source shell/consts.sh
flake8 . --exclude venv/ --count --max-line-length=79 --show-source --statistics
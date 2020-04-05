#!/usr/bin/env bash
set -e


echo "Running pytest..."
pytest

echo "Running black..."
black --quiet duke tests

echo "Running isort..."
isort --quiet --recursive --apply .

echo "Running mypy..."
mypy duke

echo "Running flake8..."
flake8 duke

echo "Running pydocstyle..."
pydocstyle duke**/*

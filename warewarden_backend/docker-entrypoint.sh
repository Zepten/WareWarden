#!/bin/sh

set -e

# Activate virtual environment:
. /opt/pysetup/.venv/bin/activate

# Evaluating passed command:
exec "$@"
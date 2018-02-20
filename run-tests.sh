# -*- coding: utf-8 -*-

set -e

flake8 arxiv_cli tests
py.test tests

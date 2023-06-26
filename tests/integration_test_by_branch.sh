#!/bin/bash

BRANCH_NAME=$1

python3 tests/integration_test/"$BRANCH_NAME"_integration_test.py
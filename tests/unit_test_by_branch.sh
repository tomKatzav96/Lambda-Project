#!/bin/bash

BRANCH_NAME=$1

python3 tests/unit_test/"$BRANCH_NAME"_unit_test.py
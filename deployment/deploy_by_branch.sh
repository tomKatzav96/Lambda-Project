#!/bin/bash

BRANCH_NAME=$1

./deployment/deploy_"$BRANCH_NAME"_lambda.sh
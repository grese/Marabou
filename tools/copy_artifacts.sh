#!/bin/bash

ARTIFACTS_DIR="$1"

mkdir -p $ARTIFACTS_DIR
ls ./build ./build/bin
cp -R maraboupy build/Marabou $ARTIFACTS_DIR

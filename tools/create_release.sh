#!/bin/bash

RELEASE_VERSION="$1"

echo "copying release assets to ./release"
mkdir release
cp -R ./dist/Linux/g++/maraboupy MANIFEST.in pyproject.toml setup.cfg setup.py README.md ./release/
cp ./release/COPYING ./release/LICENSE
mkdir ./release/maraboupy/bin
cp ./dist/Linux/g++/Marabou ./release/maraboupy/bin/Marabou-linux
# cp ./dist/MacOS/g++/Marabou ./release/maraboupy/

echo "removing unnecessary files from maraboupy package"
cd ./release/maraboupy/ && rm -rf test __pycache__ .pytest_cache test_requirements.txt && cd -

echo "updating version in setup.py & setup.cfg"
perl -pe "s/version = '(\d+\.)*\d+'/version = '$RELEASE_VERSION'/" -i ./release/setup.py
perl -pe "s/version = (\d+\.)*\d+/version = $RELEASE_VERSION/" -i ./release/setup.cfg

echo "generating package"
cd ./release
python3 setup.py bdist_wheel --universal
cd -

#!/bin/bash

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

pip install -e .

pytest -x -vv .

if [ $? -ne 0 ]; then
    exit 1
fi

codecov
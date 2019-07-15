#!/bin/bash -ex

source $HOME/miniconda/etc/profile.d/conda.sh
conda activate test

pip install -e .

pytest -x -vv .

codecov
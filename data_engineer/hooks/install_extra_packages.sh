#!/bin/bash

conda install --yes --file work/requirements.txt
conda clean --all -f -y
fix-permissions $CONDA_DIR
fix-permissions /home/$NB_USER

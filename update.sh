#!/bin/bash
python analyze.py
git add *
git commit -m "plot updated"
git push

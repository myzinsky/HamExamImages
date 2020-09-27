#!/usr/bin/python
import glob, os

os.chdir("./questions/")
for file in glob.glob("*.tex"):
    os.system("TEXINPUTS=.:../common//: pdflatex -output-directory=../build "+file);

os.chdir("../build/")
os.system("rm *.aux *.log");

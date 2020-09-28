# Makefile:

TEXS = $(wildcard *.tex)
#PDFS = $(patsubst %.tex,%.pdf, $(TEXS)) 
PDFS = $(patsubst %.tex,../build/%.pdf, $(TEXS))

all: $(PDFS)

../build/%.pdf: %.tex 
	TEXINPUTS=.:../common//: pdflatex -output-directory=../build $< > /dev/null
	rm ../build/*.aux ../build/*.log

clean:
	rm ../build/*.pdf

# Makefile:

TEXS = $(wildcard *.tex)
PDFS = $(patsubst %.tex,../build/pdf/%.pdf, $(TEXS))
SVGS = $(patsubst %.tex,../build/svg/%.svg, $(TEXS))

all: $(SVGS)

.SECONDARY:

../build/svg/%.svg: ../build/pdf/%.pdf
	pdftocairo -svg $< $@
	svgo $@

../build/pdf/%.pdf: %.tex 
	TEXINPUTS=.:../common//: lualatex -output-directory=../build/pdf $< > /dev/null
	rm -f ../build/pdf/*.aux ../build/pdf/*.log

clean:
	rm -f ../build/pdf/*.pdf
	rm -f ../build/svg/*.svg

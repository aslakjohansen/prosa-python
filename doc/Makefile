TARGETS = \
	PROSA\ -\ Python\ Introduction\ Part\ 1\ Handouts.pdf \
	PROSA\ -\ Python\ Introduction\ Part\ 1\ Presentation.pdf \
	PROSA\ -\ Python\ Introduction\ Part\ 2\ Handouts.pdf \
	PROSA\ -\ Python\ Introduction\ Part\ 2\ Presentation.pdf \
	PROSA\ -\ Python\ Introduction\ Part\ 3\ Handouts.pdf \
	PROSA\ -\ Python\ Introduction\ Part\ 3\ Presentation.pdf \



all: ${TARGETS}

clean:
	rm -f ${TARGETS}

mrproper: clean
	touch d.aux d.log d~ d.nav d.out d.snm d.toc d.vrb includes.d
	rm -f *.aux *.log *~ *.nav *.out *.snm *.toc *.vrb includes.*



includes:
	rm -Rf includes
	mkdir includes

includes.part1.timestamp: ../bin/generate-tex-includes includes part1_*.tex shared.tex # figs/*.svg
	cd .. ; bin/generate-tex-includes PDF doc/part1_handouts.tex doc
	touch includes.part1.timestamp

includes.part2.timestamp: ../bin/generate-tex-includes includes part2_*.tex shared.tex # figs/*.svg
	cd .. ; bin/generate-tex-includes PDF doc/part2_handouts.tex doc
	touch includes.part2.timestamp

includes.part3.timestamp: ../bin/generate-tex-includes includes part3_*.tex shared.tex # figs/*.svg
	cd .. ; bin/generate-tex-includes PDF doc/part3_handouts.tex doc
	touch includes.part3.timestamp



PROSA\ -\ Python\ Introduction\ Part\ 1\ Handouts.pdf: part1_*.tex shared.tex includes.part1.timestamp
	pdflatex -shell-escape part1_handouts.tex
	pdflatex -shell-escape part1_handouts.tex
	mv part1_handouts.pdf PROSA\ -\ Python\ Introduction\ Part\ 1\ Handouts.pdf

PROSA\ -\ Python\ Introduction\ Part\ 1\ Presentation.pdf: part1_*.tex shared.tex includes.part1.timestamp
	pdflatex -shell-escape part1_presentation.tex
	pdflatex -shell-escape part1_presentation.tex
	mv part1_presentation.pdf PROSA\ -\ Python\ Introduction\ Part\ 1\ Presentation.pdf

PROSA\ -\ Python\ Introduction\ Part\ 2\ Handouts.pdf: part2_*.tex shared.tex includes.part2.timestamp
	pdflatex -shell-escape part2_handouts.tex
	pdflatex -shell-escape part2_handouts.tex
	mv part2_handouts.pdf PROSA\ -\ Python\ Introduction\ Part\ 2\ Handouts.pdf

PROSA\ -\ Python\ Introduction\ Part\ 2\ Presentation.pdf: part2_*.tex shared.tex includes.part2.timestamp
	pdflatex -shell-escape part2_presentation.tex
	pdflatex -shell-escape part2_presentation.tex
	mv part2_presentation.pdf PROSA\ -\ Python\ Introduction\ Part\ 2\ Presentation.pdf

PROSA\ -\ Python\ Introduction\ Part\ 3\ Handouts.pdf: part3_*.tex shared.tex includes.part3.timestamp
	pdflatex -shell-escape part3_handouts.tex
	pdflatex -shell-escape part3_handouts.tex
	mv part3_handouts.pdf PROSA\ -\ Python\ Introduction\ Part\ 3\ Handouts.pdf

PROSA\ -\ Python\ Introduction\ Part\ 3\ Presentation.pdf: part3_*.tex shared.tex includes.part3.timestamp
	pdflatex -shell-escape part3_presentation.tex
	pdflatex -shell-escape part3_presentation.tex
	mv part3_presentation.pdf PROSA\ -\ Python\ Introduction\ Part\ 3\ Presentation.pdf


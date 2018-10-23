default: bibl2.ps bibl.ps
clean:
	rm *.{aux,log,toc,dvi,ps}

generated.tex: gentex.py
	./gentex.py generated.tex
bibl2.ps: bibl2.dvi
	dvips bibl2.dvi
bibl2.dvi: bibl2.tex generated.tex
	latex bibl2.tex < /dev/null

bibl.ps: bibl.dvi
	dvips bibl.dvi
bibl.dvi: bibl.tex
	latex bibl.tex < /dev/null

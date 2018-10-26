NIVFILES=305.html 306.html 307.html 308.html 309.html 310.html 311.html 312.html 313.html 314.html 315.html 316.html 317.html 318.html 319.html 320.html 321.html 322.html 323.html 324.html 325.html 326.html 327.html 328.html 329.html 330.html 331.html 332.html 333.html 334.html 335.html 336.html 337.html 338.html 339.html 340.html 341.html 342.html 343.html 344.html 345.html 346.html 347.html 348.html 349.html 350.html 351.html 352.html 353.html 354.html 355.html 356.html 357.html 358.html 359.html 360.html 361.html 362.html 363.html 364.html 365.html 366.html 367.html 368.html 369.html 370.html
CODE=niv1984.py

default: niv1984.txt 

niv1984.txt: $(NIVFILES) $(CODE)
	./niv1984.py $(NIVFILES) > niv1984.txt 2> niv1984.log

370.html:
	./niv1984-downloader.sh


niv1984verses: $(CODE) niv1984.txt
	sed 's/^NIV 1984[ :]*//; s/\(:[0-9]*\) .*/\1/' < niv1984.txt > niv1984verses
	sed 's/\(:[0-9]*\) .*/\1/' < ../kjv.txt > kjvverses

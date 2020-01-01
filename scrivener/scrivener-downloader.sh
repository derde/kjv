#! /bin/bash

UA='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0' 
curl() {
    command curl -A "$UA" "$@"
}

echo Download http://www.textusreceptusbibles.com/Scrivener/40/1

echo "
28    40	Matthew	                
16    41	Mark	                
24    42	Luke	                
21    43	John	                
28    44	Acts	                
16    45	Romans	                
16    46	1 Corinthians	        
13    47	2 Corinthians	        
6     48	Galatians	        
6     49	Ephesians	        
4     50	Philippians	        
4     51	Colossians	        
5     52	1 Thessalonians	        
3     53	2 Thessalonians	        
6     54	1 Timothy	        
4     55	2 Timothy	        
3     56	Titus	                
1     57	Philemon	        
13    58	Hebrews	                
5     59	James	                
5     60	1 Peter	                
3     61	2 Peter	                
5     62	1 John	                
1     63	2 John	                
1     64	3 John	                
1     65	Jude	                
22    66	Revelation	        
" | while read CHAPTERS BOOK TITLE; do
    [ "$CHAPTERS" ] || continue
    for CHAPTER in `seq $CHAPTERS` ; do
        OFILE=`printf %03d-%03d-%s-%02d.html $BOOK $CHAPTER "$TITLE" $CHAPTER `
        URL=http://www.textusreceptusbibles.com/Scrivener/$BOOK/$CHAPTER
        [ -f "$OFILE" ] && continue
        echo "curl '$URL' > '$OFILE'"
        curl -s "$URL" > "$OFILE"
        sleep 0.$((RANDOM % 10))1
    done
done

grep '"greek"' 0*.html | sed 's/^...-...-//; s/-.*ref">/ /; s/<\/td><td class="greek">/ /; s/<\/td><\/tr>//'  > scrivener1894.txt


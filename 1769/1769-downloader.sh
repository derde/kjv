#! /bin/bash

UA='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0' 
curl() {
    command curl -A "$UA" "$@"
}

SOURCE=KJV1769
echo Download http://www.textusreceptusbibles.com/$SOURCE/1/1

echo "
50    1	Genesis
40    2	Exodus
27    3	Leviticus
36    4	Numbers
34    5	Deuteronomy
24    6	Joshua
21    7	Judges
4     8	Ruth
31    9	1 Samuel
24    10	2 Samuel
22    11	1 Kings
25    12	2 Kings
29    13	1 Chronicles
36    14	2 Chronicles
10    15	Ezra
13    16	Nehemiah
10    17	Esther
42    18	Job
150   19	Psalms
31    20	Proverbs
12    21	Ecclesiastes
8     22	Song of Solomon
66    23	Isaiah
52    24	Jeremiah
5     25	Lamentations
48    26	Ezekiel
12    27	Daniel
14    28	Hosea
3     29	Joel
9     30	Amos
1     31	Obadiah
4     32	Jonah
7     33	Micah
3     34	Nahum
3     35	Habakkuk
3     36	Zephaniah
2     37	Haggai
14    38	Zechariah
4     39	Malachi
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
        URL=http://www.textusreceptusbibles.com/$SOURCE/$BOOK/$CHAPTER
        [ -f "$OFILE" ] && continue
        echo "curl '$URL' > '$OFILE'"
        curl -s "$URL" > "$OFILE"
        sleep 0.$((RANDOM % 10))1
    done
done

grep '"ref"' 0*.html | sed '
  s/^...-...-//;
  s/-.*ref">/ /;
  s:</td><td>: :;
  s/<\/td><\/tr>// ;
  s:<i>:[:g; s:</i>:]:g;
  s:<br /><span class=.selectfooter.>:[: ;
  s:</span>:]: ;
'  > 1769.txt


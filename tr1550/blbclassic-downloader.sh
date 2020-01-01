#! /bin/bash

# http://www.blbclassic.org/Bible.cfm?b=Mat&c=1&v=1&t=TR

UserAgent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0' 

echo "
28    40 Mat       Matthew	                
16    41 Mar       Mark	                
24    42 Luk       Luke	                
21    43 Jhn       John	                
28    44 Act       Acts	                
16    45 Rom       Romans	                
16    46 1Co       1 Corinthians	        
13    47 2Co       2 Corinthians	        
6     48 Gal       Galatians	        
6     49 Eph       Ephesians	        
4     50 Phl       Philippians	        
4     51 Col       Colossians	        
5     52 1Th       1 Thessalonians	        
3     53 2Th       2 Thessalonians	        
6     54 1Ti       1 Timothy	        
4     55 2Ti       2 Timothy	        
3     56 Tit       Titus	                
1     57 Phm       Philemon	        
13    58 Heb       Hebrews	                
5     59 Jas       James	                
5     60 1Pe       1 Peter	                
3     61 2Pe       2 Peter	                
5     62 1Jo       1 John	                
1     63 2Jo       2 John	                
1     64 3Jo       3 John	                
1     65 Jde       Jude	                
22    66 Rev       Revelation	        
" | while read CHAPTERS num BOOK TITLE; do
    [ "$CHAPTERS" ] || continue
    for CHAPTER in `seq $CHAPTERS` ; do
        OFILE=`printf %03d-%03d-%s-%02d.html $num $CHAPTER "$TITLE" $CHAPTER `
        [ -f "$OFILE" ] && continue
        URL="http://www.blbclassic.org/Bible.cfm?b=$BOOK&c=$CHAPTER&v=1&t=TR"
        echo "curl -s -A UA='$UserAgent' '$URL' > '$OFILE'"
    done
done | shuf | bash -x


grep -Po '>\S{3}\s+\d+:\d+<|.*GkBibleText.*' 0*.html |
   perl -n -e '
      if (m/:>\S\S\S\s\d+:(\d+)</) { $verse=$1; };
      if (m/^\d+-\d+-(.*?)-0*(\d+).*GkBibleText.>(.*?)<\/div>/) {
        print "$1 $2:$verse $3\n";
      } 
'

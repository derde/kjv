#! /bin/bash

# It looks like it's been pulled

exit

echo Download NIV1984 from christunite.com
for M in $( seq 305 370 ) ; do
    [ -f $M.html ] || wget -O $M.html "http://www.christunite.com/index.php/bible?id=$M";
done



#! /bin/bash

{
    # KJV
    cat 1769/1769.txt  \
      | sed '30674 i -\' \
      | sed '30912 i -\' \
      | nl \
      | sed 's/ *\([0-9]\+\)/\101/' ;

    # Hebrew and Greek
    {
        < masoretic/masoretic1524.txt cat
        < scrivener/scrivener1894.txt cat #  sed '5911 i -\' # add missing blank verse at the end of 2 Corinthians
    } | sed '29057 i -\' | nl | sed 's/ *\([0-9]\+\)/\102/'
} | sort -n | cut -f 2 | sed '/^-/ d' > parallel.txt
#} | sort -n | sed '/^-/ d' > parallel.txt


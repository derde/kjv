#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
Read article from stdin and annotate verses from the text
'''

import re
import sys
import collections

lastbook=''

class BibleDb:
    fd=open(sys.argv[0].replace('.py','.txt'),'r') # kjv.txt
    cache=collections.OrderedDict()
    key_re=re.compile('(.*? \d+:\d+) (.*)')
    
    def __getitem__(self,searchfor):
        if self.cache.has_key(searchfor):
            return self.cache[searchfor]
        if not self.fd:
            return ''
        while True:
            line = self.fd.readline()
            if not line: break
            m=self.key_re.match(line)
            if not m: continue
            key,value=m.groups()
            self.cache[key]=value
            if key==searchfor:
                return value
        self.fd.close()
        self.fd=None
        return ''

def format_verserefs(book,chapter,verse,ranges):
    global lastbook
    if not book: book=lastbook
    lastbook=book
    book=book.title()
    m=re.search('^(III|3)\s*(.*)',book,re.I);
    if m: book='3'+m.group(2)
    m=re.search('^(II|2)\s*(.*)',book,re.I);
    if m: book='2'+m.group(2)
    m=re.search('^(I|1)\s*(.*)',book,re.I);
    if m and not re.search(r'^is',book,re.I): book='1'+m.group(2)
    refs = {
        '1 Chronicles':    [ '1ch',       ],   
        '1 Corinthians':   [ '1co','1cr', ],
        '1 John':          [ '1j',        ],
        '1 Kings':         [ '1k',        ],
        '1 Peter':         [ '1p',        ],
        '1 Samuel':        [ '1sam',      ],
        '1 Thessalonians': [ '1th',       ],
        '1 Timothy':       [ '1ti','1tm', ],
        '2 Chronicles':    [ '2ch',       ],
        '2 Corinthians':   [ '2co','2cr', ],
        '2 John':          [ '2j',        ],
        '2 Kings':         [ '2k',        ],
        '2 Peter':         [ '2p',        ],
        '2 Samuel':        [ '2s'         ],
        '2 Thessalonians': [ '2th',       ],
        '2 Timothy':       [ '2ti','2tm', ],
        '3 John':          [ '3j',        ],
        'Acts':            [ 'ac',        ],
        'Amos':            [ 'am',        ],
        'Colossians':      [ 'co', 'cl',  ],
        'Daniel':          [ 'da','dn',   ],
        'Deuteronomy':     [ 'de','dt',   ],
        'Ecclesiastes':    [ 'ec',        ],
        'Ephesians':       [ 'ep','ef',   ],
        'Esther':          [ 'es',        ],
        'Exodus':          [ 'ex',        ],
        'Ezekiel':         [ 'ez',        ],
        'Ezra':            [ 'ezr',       ],
        'Galatians':       [ 'ga','gl',   ],
        'Genesis':         [ 'ge','gn',   ],
        'Habakkuk':        [ 'ha','hk',   ],
        'Haggai':          [ 'hag',       ],
        'Hebrews':         [ 'he','hb'    ],
        'Hosea':           [ 'ho',        ],
        'Isaiah':          [ 'is',        ],
        'James':           [ 'ja','jm','jas' ],
        'Jeremiah':        [ 'je',        ],
        'Job':             [ 'job',       ],
        'Joel':            [ 'joe','jol', ],
        'John':            [ 'jo','jn',   ],
        'Jonah':           [ 'jon','jnh', ],
        'Joshua':          [ 'jos',       ],
        'Jude':            [ 'jude',      ],
        'Judges':          [ 'jud','jdg', ],
        'Lamentations':    [ 'la',        ],
        'Leviticus':       [ 'le','lv',   ],
        'Luke':            [ 'lu',        ],
        'Malachi':         [ 'mal','ml',  ],
        'Mark':            [ 'mk','mar', 'mr', 'mrk' ],
        'Matthew':         [ 'mt','mat','matt'  ],
        'Micah':           [ 'mi','mc',   ],
        'Nahum':           [ 'na','nh',   ],
        'Nehemiah':        [ 'ne',        ],
        'Numbers':         [ 'nu',        ],
        'Obadiah':         [ 'ob',        ],
        'Philemon':        [ 'phm',       ],
        'Philippians':     [ 'ph',        ],
        'Proverbs':        [ 'pr',        ],
        'Psalms':          [ 'ps',        ],
        'Revelation':      [ 're','rev'   ],
        'Romans':          [ 'ro',        ],
        'Ruth':            [ 'ru',        ],
        'Song of Solomon': [ 'so','ss',   ],
        'Titus':           [ 'ti',        ],
        'Zecharia':        [ 'ze','zc',   ],
        'Zephania':        [ 'zp','zep'   ],
    }
    verses=[int(verse),]
    range_re=re.compile('(\D*)(\d+)')
    not_range_re=re.compile('^is')
    for group in range_re.findall(ranges):
      endverse=int(group[1])
      if group[0].startswith('-'):
        verses.extend(range(verses[-1]+1,endverse+1))
      else:
        verses.append(endverse)
    abook=''
    for bookname,reflist in refs.items():
      for prefix in reflist:
        if book.lower().startswith(prefix):
          abook=bookname
    if abook:
      for verse in verses:
        yield '%s %s:%s' % (abook,chapter,verse)

def getverserefs(text):
    verseref = re.compile('(((1|2|3|I|II|III|song\s*of)\s{0,2})?\w{2,}|)\.?\s{0,2}(\d+)[:-v](\d+)(\s*[-,\&]\s*\d+)*',re.I)
    for group in verseref.findall(text):
        for ref in format_verserefs(group[0],group[3],group[4],group[5]):
            yield ref

bibledb=BibleDb()
for line in sys.stdin:
    sys.stdout.write( line )
    for ref in getverserefs(line):
        text=bibledb[ref]
        if text:
            sys.stdout.write('  %s %s\n' % ( ref,text ))


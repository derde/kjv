#! /usr/bin/python
# -*- coding: utf-8 -*-

'''
Read article from stdin and annotate verses from the text
1 Corinthians 3:11–15
–
'''

import re
import sys
import collections

lastbook=''
lastchapter=''
DEBUG = 0


class smallcaps:
    normal    = r'''a b c d e f g h i j k l m n o p q r s t u v w x y z'''
    smallcaps = r'''ᴀ ʙ ᴄ ᴅ ᴇ ꜰ ɢ ʜ ɪ ᴊ ᴋ ʟ ᴍ ɴ ᴏ ᴘ ǫ ʀ ꜱ ᴛ ᴜ ᴠ ᴡ x ʏ ᴢ'''

    def __init__(self,value):
        self.x = value

    def __repr__(self):
        #if x.endswith('\n'):
        #    x='\n'+x[:-1]
        o=[]
        input = self.normal.split(' ')
        output = self.smallcaps.split(' ')
        for c in self.x:
            try:
                c=output[input.index(c)]
            except ValueError:
                pass
            o.append(c)
        r = ''.join(o)
        return r


class BibleDb:
    fd=open(sys.argv[0].replace('.py','.txt'),'r') # kjv.txt
    cache=collections.OrderedDict()
    key_re=re.compile('(.*? \d+:\d+) (.*)')
    big_bible_book_regex=''
    
    abbreviations={
        '1 Chronicles': ['1 Chr','1 Chr','1 Ch'],
        '1 Corinthians':   [ '1co','1cr', ],
        '1 Corinthians': ['1 Cor','1 Co','1 Cr'],
        '1 John': ['1 Jn','1 Jhn','1 J'],
        '1 Kings': ['1 Kings','1 Kgs','1 Kin','1 Ki','1K'],
        '1 Peter': ['1 Pet','1 Pe','1 Pt','1 P'],
        '1 Samuel': ['1 Sam','1 Sm','1 Sa','1 S'],
        '1 Thessalonians': ['1 Thess','1 Thes','1 Th', '1 thesalonians'],
        '1 Timothy': ['1 Tim','1 Ti','1 Tm'],
        '2 Chronicles': ['2 Chr','2 Ch','2 Chron'],
        '2 Corinthians': ['2 Cor','2 Co'],
        '2 John': ['2 Jn','2 Jhn','2 J'],
        '2 Kings': ['2 Kings','2 Kgs','2 Kin','2 Ki'],
        '2 Peter': ['2 Pet','2 Pe','2 Pt','2 P'],
        '2 Samuel': ['2 Sam','2 Sm','2 Sa','2 S'],
        '2 Thessalonians': ['2 Thess','2 Thes','2 Th', '2 thesalonians'],
        '2 Timothy': ['2 Tim','2 Ti','2 Tm'],
        '3 John': ['3 Jn','3 Jhn','3 J'],
        'Acts':            [ 'ac','act'        ],
        'Amos':            [ 'am',        ],
        'Colossians': ['Col','co','cl','colosians' ],
        'Daniel': ['Dan','Da','Dn'],
        'Deuteronomy': ['Deut','De','Dt'],
        'Ecclesiastes': ['Eccl','Eccles','Eccle','Ecc','Ec'],
        'Ephesians':       [ 'ep','ef','eph','ephes'   ],
        'Esther': ['Esth','Est','Es'],
        'Exodus': ['Ex','Exod'],
        'Ezekiel': ['Ezek','Eze','Ezk',],
        'Ezra': ['Ezra','Ezr','Ez'],
        'Galatians': ['Gal','Ga','gl'],
        'Genesis': ['Gen','Ge','Gn'],
        'Habakkuk': ['Hab','hk'],
        'Haggai': ['Hag','Hg'], 
        'Hebrews': ['he', 'Heb','hb','hebr'],
        'Hosea': ['Hos','Ho'],
        'Isaiah': ['Isa','Is'],
        'James': ['Jas','Jm','jam'],
        'Jeremiah': ['Jer','Je','Jr'],
        'Job': ['Job','Jb'],
        'Joel': ['Joel','Jl','jol'],
        'John': ['Jn','Jhn','jo'],
        'Jonah': ['Jon','Jnh'],
        'Joshua': ['Josh','Jos','Jsh'],
        'Jude': ['Jude','Jud','Jd'],
        'Judges': ['Judg','Jdg','Jg','Jdgs','jud'],
        'Lamentations': ['Lam','La'],
        'Leviticus': ['Lev','Le','Lv'],
        'Luke': ['Lk','Luk','lu'],
        'Malachi': ['Mal','Ml'],
        'Mark':            [ 'mk','mar', 'mr', 'mrk' ],
        'Matthew':         [ 'mt','mat','matt'  ],
        'Micah':           [ 'mic', 'mi','mc',   ],
        'Nahum':           [ 'na','nh',   ],
        'Nehemiah': ['Neh','Ne'],
        'Numbers': ['Num','Nu','Nm','Nb'],
        'Obadiah':         [ 'ob',        ],
        'Philemon': ['Philemon',' Philem','Phm','Pm'],
        'Philippians': ['Philipians','Phil','Php','Pp','Phl','Ph'],
        'Proverbs': ['Prov','Pro','Prv','Pr','pvb','pvbs'],
        'Psalms': ['Ps','Psalm','Pslm','Psa','Psm'],
        'Revelation': ['Rev','Rv','re','apo','apoc','apocalypse'],
        'Romans': ['Rom','Ro','Rm'],
        'Ruth': ['Ruth','Rth','Ru'],
        'Song of Solomon': ['Song','ss','so'],
        'Titus':           [ 'ti',        ],
        'Zechariah': ['Zech','Zec','Zc'],
        'Zephaniah': ['Zeph','Zep','Zp'],
    }

    def __init__(self):
        if not self.big_bible_book_regex:
            self.build_big_bible_book_regex()
    
    def __getitem__(self,verseref):
        '''Get a verse without necessarily scanning the whole Bible'''
        if self.cache.has_key(verseref):
            return self.cache[verseref]
        if not self.fd:
            return ''
        while True:
            line = self.fd.readline()
            if not line: break
            m=self.key_re.match(line)
            if not m: continue
            key,value=m.groups()
            value=value.rstrip('\r\n ')
            self.cache[key]=value
            if key==verseref:
                return value
        self.fd.close()
        self.fd=None
        return ''

    def build_big_bible_book_regex(self):
        ''' Big regular expression string for all the books in the Bible (in English) '''
        biglist=[]
        for k,v in self.abbreviations.items():
            v.append(k)
            for i in v:
                i=i.replace(' ',' ?')
                biglist.append(i.lower())
                if i.startswith('1'):
                    for prefix in ('first','1st','I'):   biglist.append( (prefix+i[1:]).lower() )
                    for prefix in ('second','2nd','II'): biglist.append( (prefix+i[1:]).lower() )
                    for prefix in ('third','3rd','III'): biglist.append( (prefix+i[2:]).lower() )
        biglist.sort(reverse=True)
        self.big_bible_book_regex = '|'.join(biglist) 
        return self.big_bible_book_regex

    def getverserefs(self,text):
        global DEBUG
        verseref = re.compile( \
            (
            #01               2       34
            r'((verses?|v\.)\s*(\d+)\s*(([-,\&]|–|\.\.)\s*\d+)*)|' \
            #5
            r'\b('+self.big_bible_book_regex+r')\b.?\s{0,2}' \
            #chapter                                 verse
            #678        9                    10      11   12  13                  14       15-16            17      18-19
            r'(((\d+)\s?([-:.v]|verses?|vers)(\s|\.)?(\d+)(\s*([-,\&]|-|–|\.\.)\s*(\d+))*)|((verses?|v\.)\s+(\d+)\s*(([-,\&]|–|\.\.)\s*\d+)*)|)|' \
            #20-22      23                   24      25   26  27                  28       29-30            31      32-33
            r'(((\d+)\s?([-:.v]|verses?|vers)(\s|\.)?(\d+)(\s*([-,\&]|-|–|\.\.)\s*(\d+))*)|((verses?|v\.)\s+(\d+)\s*(([-,\&]|–|\.\.)\s*\d+)*))' \
            ), re.I)
        for group in verseref.findall(text):
            if DEBUG>2 and ''.join(group[2:])!='':
                for r in range(0,len(group)):
                    if group[r]: sys.stdout.write(' %d=[%s]' % (r,group[r]))
                sys.stdout.write('\n')
            if group[2]:
                if DEBUG>2: sys.stdout.write('Bare verse ref: \n')
                for ref in format_verserefs('','',group[2],group[4]):
                    yield ref
            elif group[17]:
                if DEBUG>2: sys.stdout.write('Following verse ref: \n')
                for ref in format_verserefs('','',group[17],group[18]):
                    yield ref
            elif group[22]:
                if DEBUG>2: sys.stdout.write('Bare ref: \n')
                for ref in format_verserefs('',group[22],group[25],group[26]):
                    yield ref
            else:
                if DEBUG>2: sys.stdout.write('Complete ref: \n')
                for ref in format_verserefs(group[5],group[8],group[11],group[12]):
                    yield ref

def format_verserefs(book,chapter,verse,ranges):
    global lastbook
    global lastchapter
    if not book: book=lastbook
    if not chapter: chapter=lastchapter
    lastchapter=chapter
    book=book.title()
    if DEBUG>2: print "Lookup bookpart[%s] chapter[%s] verse[%s] range[%s]" % (book,chapter,verse,ranges)
    m=re.search('^(third|III|3)\s*(.*)',book,re.I);
    if m: book='3'+m.group(2)
    m=re.search('^(second|II|2)\s*(.*)',book,re.I);
    if m: book='2'+m.group(2)
    m=re.search('^(first|I|1)\s*(.*)',book,re.I);
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
        'Luke':            [ 'lu','lk',   ],
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
    verses=[]
    if verse:
        verses.append(int(verse))
        range_re=re.compile('(\D*)(\d+)')
        not_range_re=re.compile('^is')
        for group in range_re.findall(ranges):
          endverse=int(group[1])
          mm=re.search(r'^\s*(-|\.\.|–)',group[0]) # range, not list ...
          if mm:
            verses.extend(range(verses[-1]+1,endverse+1))
          else:
            verses.append(endverse)
    abook=''
    for bookname,reflist in refs.items():
      for prefix in reflist:
        if book.lower().startswith(prefix):
          abook=bookname
    if abook:
      if len(verses) or len(book)>2:  # don't use "is" and "he" as book changers
          lastbook=abook
      for verse in verses:
        yield '%s %s:%s' % (abook,chapter,verse)


bibledb=BibleDb()

textstream = sys.stdin
if len(sys.argv)>1:
    textstream=open(sys.argv[1],'r')

for line in textstream:
    if not line.endswith('\n'): line+='\n'
    sys.stdout.write( line )
    spacer='\n'
    for ref in bibledb.getverserefs(line):
        text=bibledb[ref]
        if text:
            sys.stdout.write( spacer )
            spacer=''
            # sys.stdout.write('  %s %s\n' % ( ref.upper(),text ))
            sys.stdout.write('  %s %s\n' % ( ref,text ))
    if spacer=='': 
        sys.stdout.write('\n')



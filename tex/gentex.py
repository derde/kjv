#! /usr/bin/python
# coding: utf-8

import re
import itertools
import sys

class paragraphdivisions:
    def staticdata(self):
        self.paragraphs={}
        self.bookmapdata='''\
GEN      : Genesis         :  Genesis 
EXOD     : Exodus          :  Exodus 
LEV      : Leviticus       :  Levitikus 
NUM      : Numbers         :  Numeri 
DEUT     : Deuteronomy     :  Deuteronomium 
JOSH     : Joshua          :  Josua 
JUDG     : Judges          :  Rigters 
RUTH     : Ruth            :  Rut 
1SAM     : 1 Samuel        :  1 Samuel 
2SAM     : 2 Samuel        :  2 Samuel 
1KGS     : 1 Kings         :  1 Konings 
2KGS     : 2 Kings         :  2 Konings 
1CHRON   : 1 Chronicles    :  1 Kronieke 
2CHRON   : 2 Chronicles    :  2 Kronieke 
EZRA     : Ezra            :  Esra 
NEH      : Nehemiah        :  Nehemia 
ESTH     : Esther          :  Ester 
JOB      : Job             :  Job 
PS       : Psalms          :  Psalms 
PROV     : Proverbs        :  Spreuke 
ECC      : Ecclesiastes    :  Prediker 
SONG     : Song of Solomon :  Hooglied 
ISA      : Isaiah          :  Jesaja 
JER      : Jeremiah        :  Jeremia 
LAM      : Lamentations    :  Klaagliedere 
EZEK     : Ezekiel         :  Esegiel 
DAN      : Daniel          :  Daniel 
HOSEA    : Hosea           :  Hosea 
JOEL     : Joel            :  Joel 
AMOS     : Amos            :  Amos 
OBAD     : Obadiah         :  Obadja 
JONAH    : Jonah           :  Jona 
MICAH    : Micah           :  Miga 
NAHUM    : Nahum           :  Nahum 
HAB      : Habakkuk        :  Habakuk 
ZEPH     : Zephaniah       :  Sefanja 
HAG      : Haggai          :  Haggai 
ZECH     : Zechariah       :  Sagaria 
MAL      : Malachi         :  Maleagi 
MATT     : Matthew         :  Mattheus 
MARK     : Mark            :  Markus 
LUKE     : Luke            :  Lukas 
JOHN     : John            :  Johannes 
ACTS     : Acts            :  Handelinge 
ROM      : Romans          :  Romeine 
1COR     : 1 Corinthians   :  1 Korinthiers 
2COR     : 2 Corinthians   :  2 Korinthiers 
GAL      : Galatians       :  Galasiers 
EPH      : Ephesians       :  Efesiers 
PHIL     : Philippians     :  Filippense 
COL      : Colossians      :  Kolossense 
1THES    : 1 Thessalonians :  1 Thessalonicense 
2THES    : 2 Thessalonians :  2 Thessalonicense 
1TIM     : 1 Timothy       :  1 Timotheus 
2TIM     : 2 Timothy       :  2 Timotheus 
TITUS    : Titus           :  Titus 
PHILEM   : Philemon        :  Filemon 
HEB      : Hebrews         :  Hebreers 
JAS      : James           :  Jakobus 
1PET     : 1 Peter         :  1 Petrus 
2PET     : 2 Peter         :  2 Petrus 
1JOHN    : 1 John          :  1 Johannes 
2JOHN    : 2 John          :  2 Johannes 
3JOHN    : 3 John          :  3 Johannes 
JUDE     : Jude            :  Judas 
REV      : Revelation      :  Openbaring'''

    def __init__(self,file):
        self.staticdata()
        self.bookmap=[]
        for line in self.bookmapdata.split('\n'):
            bits=re.split(' *: *',line.strip())
            if len(bits)==3:
                self.bookmap.append(bits)

        self.refs={}
        fd=open(file,'r')
        line1=fd.readline()
        self.headings=line1.strip('\n').split('\t')
        verse_range_i = self.headings.index('Verse Range')
        for line in fd:
            bits=line.strip('\n').split('\t')
            self.addparagraph(bits[verse_range_i])

    def bookmaplookup(self,srccol,dstcol,value):
        for r in self.bookmap:
            if r[srccol]==value: return r[dstcol]
        return ''

    def addparagraph(self,refs):
        m=re.search('(\S+) (\d+:\d+)',refs)
        chapverse = m.group(2)
        book = self.bookmaplookup(0,1,m.group(1))
        self.paragraphs[book+' '+chapverse] = True
        book = self.bookmaplookup(0,2,m.group(1))
        self.paragraphs[book+' '+chapverse] = True

    def isnewparagraph(self,ref):
        return self.paragraphs.has_key(ref)
        

class bibleformatter:
    paragraph_wl_re=re.compile("^('n )?[A-Z]{2,}")
    paragraph_bl_re=re.compile("^HERE ")

    def __init__(self,file, is_afrikaans=False):
        self.state={
            'book': '',
            'chapter': '',
            'chapter': '', }
        self.paragraphdivisions=paragraphdivisions('1526.Pericopes.csv')
        if is_afrikaans:
            self.reformat=self.reformat_afrikaans
            self.markheading=r'\markleft';
        else:
            self.reformat=self.reformat_english
            self.markheading=r'\markright';
        self.fd=open(file,'r')


    def booktochapters(self):
        lineformat_re=re.compile('(.*?) (\d+):(\d+) (.*)')
        for line in self.fd:
            m=lineformat_re.search(line.strip())
            book,chapter,verse,text=m.groups()
            text=text.replace('’',"'")
            yield book,chapter,verse,text

    def chapterheading(self,chapter, one_chapter=False):
        if one_chapter:
            return self.setverseforheading() +self.verseheading('1') + '\n';
        return self.verseheading('1') + r'\bibldropcapschapter{'+chapter+'} ' + '\n'

    def verseheading(self,verse):
        r= self.setverseforheading()
        if verse!='1': r+=  r'\verse{'+verse+'}' 
        return r

    def setverseforheading(self):
        ref = '%(book)s %(chapter)s:%(verse)s' % self.state
        # return self.markheading+'{'+ref+'}' ;
        return r'\markright{%s}' % (ref)
        # return r'\markboth{%s}{%s}' % (ref,ref)

    def isnewparagraph(self,book,chapter,verse,text):
        # Afrikaans text has capital words indicating new paragraphs
        if book.startswith('Psa'):
            return True;
        #isnew = self.paragraph_wl_re.search(text) and not self.paragraph_bl_re.search(text)
        isnew = self.paragraphdivisions.isnewparagraph(book+' '+chapter+':'+verse)
        return isnew

    def sub_format_smallcaps(self,m):
        if m.span(1)[0]==0:
            return m.group(1)+m.group(2)
        smallcapsd= r'\textsc{'+m.group(1).title()+'}'
        whitespace=m.group(2)
        if not whitespace: whitespace='%\n'
        return smallcapsd+whitespace

    def reformat_english(self,text):
        # Rewrite CAPITALISED WORDS as smallcaps .. this might do the wrong thing in the new testament and odd places
        text=re.sub(r"([A-Z]{2,})(\s*)", self.sub_format_smallcaps, text)
        return text

    def afrikaans_titlecase(self,m):
        indefinitearticle=''
        if m.group(1): indefinitearticle=m.group(1)
        word=m.group(2)
        if word=='HERE':
            return word
        return indefinitearticle+word.title()

    def reformat_afrikaans(self,text):
        # Rewrite paragraph capitalisation
        text=re.sub(r"(^'n )?([A-Z]{2,})", self.afrikaans_titlecase, text, 1)
        text=re.sub(r"([A-Z]{2,})(\s*)", self.sub_format_smallcaps, text)
        hypenateme = (
            re.compile('([a-z])(honderd|duisend|miljoen)') , re.compile(r'(skrif)(geleerde)') )
        hyphenwords=('skrif-geleerde', 'ge-reg-tig-heid', 'Goeder-tieren-heid',
            'Egipte-naars', 'eers-ge-borenes', 'goeder-tieren-heid',
            'ver-slaan','ver-plet-ter', 'lank-moedig-heid','lyd-saam-heid',
            'on-der-tussen', 'oop-ge-sny')
        for h in hypenateme:
            text=h.sub(r'\1\\-\2',text)
        for h in hyphenwords:
            text=text.replace(h.replace('-',''),h.replace('-','\\-'))
        return text

    def parsebooks(self):
        obook=''
        ochapter=''
        chaptertext=[]
        for book,chapter,verse,text in self.booktochapters():
            self.state['book']=book
            self.state['chapter']=chapter
            self.state['verse']=verse
            self.state['text']=text
            if book!=obook:
                if obook:
                    yield { 'chapter': ''.join(chaptertext) }
                    chaptertext=[]
                yield { 'book': book }
            if chapter!=ochapter:
                yield { 'chapter': ''.join(chaptertext) }
                chaptertext=[]
                chaptertext.append(self.chapterheading(chapter))
            if verse!='1':
                if self.isnewparagraph(book,chapter,verse,text):
                    if verse=='2':
                        chaptertext.append(r'\biblsyntheticpar'+'\n')  # local def
                    else:
                        chaptertext.append(r'\par'+'\n');
                chaptertext.append(self.verseheading(verse))
            chaptertext.append(self.reformat(text)+'\n');
            obook = book
            ochapter = chapter
        yield { 'chapter': ''.join(chaptertext) }

def sidebysidechapters():
    af=bibleformatter('../af1953.txt',is_afrikaans=True)
    en=bibleformatter('../kjv.txt')
    for left,right in itertools.izip( en.parsebooks(), af.parsebooks() ):
        if left.has_key('book'):
            # yield r'\biblchapter{'+left['book']+' / ' + right['book']+'}\n'  # TeX chapter, which is a book of the Bible
            yield r'\biblchapters{'+left['book'] + '}{' + right['book'] + '}\n' 
        elif left.has_key('chapter'):
            yield (
                # r'\selectlanguage{english}\n'+ \
                r'\begin{paracol}{2}' '\n'
                ) + left['chapter'] + ( r'\switchcolumn' '\n'
                # r'\selectlanguage{dutch}\n'
                ) + right['chapter'] + ( '\end{paracol}\n' 
                '%%%%%%%%\n' ) ;

outfd=sys.stdout
if len(sys.argv)>1:
    outfd=open(sys.argv[1],'w')
for splurge in sidebysidechapters():
    outfd.write( splurge + '\n')


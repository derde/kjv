#! /usr/bin/python

import sys
import re
import os
import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.content=[]
        self.context=''
        self.verse='0'
        self.tags = ['h2','p','strong','span','sup','a']
        self.expect=None
        self.maps = {
            '.h2': 'book',
            '.p.strong.span': 'chapter',
            '.p.strong.span.a': 'chapter',
            '.p.strong.span.strong.span.a': 'chapter',

            '.p.sup.span': 'verse',
            '.p.span.sup.span': 'verse',
            '.sup.span': 'verse',

            '.p.span': 'text', 
            '.p.span.a': 'text',
            '.p.span.span': 'text', 
        }
        return HTMLParser.HTMLParser.__init__(self)

    def setbook(self,book):
        self.book = book.replace(':',' ').\
            replace('  ',' ').\
            replace('  ',' ').\
            replace('1st','1'). \
            replace('2nd','2'). \
            replace('3rd','3') 
        return self.book

    def handle_starttag(self, tag, attrs):
        # print "Encountered a start tag:", tag
        if tag in self.tags:
            self.context += '.'+tag

    def handle_endtag(self, tag):
        # print "Encountered an end tag :", tag
        if self.context.endswith('.'+tag):
            self.context=self.context[:-len(tag)-1]

    def handle_data(self, data):
        sys.stderr.write('%s %s\n' % (  self.context,data.strip() ))
        type=self.maps.get(self.context)
        if not type and self.expect and self.context.find(self.expect)>=0:
            type='text'
        if type:
            self.expect=None
            # print type,"::", data.strip()
            if type=='book': self.setbook(data.strip())
            if type=='chapter':
                self.chapter=data.strip()
                self.verse='1'
            if type=='verse':
                self.verse=data.strip()
                self.expect='.span'
            if type=='text': 
                ref=self.book+' '+self.chapter+':'+self.verse+' '
                sys.stderr.write('%s %s\n' % (  ref, data.strip() ))
                if len(self.content) and self.content[len(self.content)-1].startswith(ref):
                    self.content[-1]=self.content[-1].strip()+' '+data.strip()+'\n'
                else:
                    self.content.append(ref+data.strip()+'\n')

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

books=[]
for filename in sys.argv[1:]:
    parser.feed(open(filename,'r').read())
    sys.stdout.writelines(parser.content)
    parser.content=[]
    #    book='';
    #    chapter=0
    #    fd = os.popen('lynx -dump '+filename,'r')
    #    verse=0
    #    for line in fd:
    #        if line.find('NIV 1984')==0:
    #            book=line.strip().split("1984")[1].strip(':').strip()
    #            continue
    #        if line.find('Copyright')>=0:
    #            book='';
    #        if not book:
    #            continue
    #        m=re.search('^\s+('+str(chapter+1)+')',line)
    #        if m:
    #            verse=1;
    #            chapter=int(m.group(1))
    #            text = '%s %d:%d %s' % (book,chapter,verse,line.strip())
    #            books.append(text)
    #        else:
    #            line=line.strip()
    #            m=re.search('^\s+\^(%d)(.*)' % (verse+1),line)
    #            if m:
    #                verse=int(m.group(1))
    #                line=m.group(2)
    #                text = '%s %s:%s %s' % (book,chapter,verse,line.strip())
    #                books.append(text)
    #            elif len(line) and len(books):
    #                books[len(books)-1] += ' '+line

#print '\n'.join(books)


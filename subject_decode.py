#!/usr/bin/env python
# coding: utf-8
#
# spam mail subject garbled process
# Author: guoxiangcheng
# Mail: guoxiangcheng@comon.cn
#
# Date: 2013-09-23

# Load module
import re
import base64
import quopri

# Decode subject
def subdecode(char,code,title):
    if code == 'B' or code == 'b':
        try:
            dtitle = base64.decodestring(title)
        except TypeError:
            lens = len(title)
            lenx = lens - (lens % 4 and lens % 4 or 4)
            dtitle = base64.decodestring(title[:lenx])
    elif code == 'Q' or code == 'q':
        dtitle = quopri.decodestring(title)
    
    dtitle = dtitle.decode(char, 'ignore')
    
    return(dtitle)

# Subject process
# Default input strings 'utf-8'
# Defautl output strings 'unicode'
def subjectproc(subject):
    subdec = ''
    pattern = re.compile('(.*)=\?(.*)\?(\w?)\?(.*)\?=(.*)', re.S)
    
    while str(subject) <> '':
        subre = pattern.match(subject)
        if subre is not None:
            subtupl = subre.groups()
            char = subtupl[1]
            code = subtupl[2]
            title = subtupl[3]
            if str(subtupl[4]) <> '':
                subdec = subdecode(char,code,title) + subtupl[4] + subdec
            else:
                subdec = subdecode(char,code,title) + subdec
            
            subject = subtupl[0]
        else:
            sbjdec = subject.decode('utf8', 'ignore')
            subdec = sbjdec + subdec
            subject = ''
    
    return(subdec)

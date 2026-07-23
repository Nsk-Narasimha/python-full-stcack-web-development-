"""regular expression
functions:
findall
search
split
sub
fullmatch

metachar:[] ^ $ . * + {}
"""
import re
txt='Python is Pr0gramming language'
print(re.findall('[an]',txt))
print(re.search('[a]',txt))
print(re.split(' ',txt))
print(re.sub(' ','3',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))
print(re.findall('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))
print(re.search('[0-9]',txt))
print(re.findall('^Python',txt))#start
print(re.search('^Python',txt))
print(re.findall('age$',txt))#end
print(re.search('age$',txt))
print(re.findall('P.....',txt))
print(re.search('P.....',txt))
print(re.findall('P.*',txt))
print(re.findall('P.*n',txt))
print(re.findall('P.*ython',txt))
print(re.search('P.*',txt))
print(re.search('P.*n',txt))
print(re.search('P.*ython',txt))
print(re.findall('P.+',txt))
print(re.findall('P.+n',txt))
print(re.findall('P.+ython',txt))#atleast one character
print(re.search('P.+',txt))
print(re.search('P.+n',txt))
print(re.search('P.+ython',txt))
print(re.findall('P.{4}',txt))
print(re.findall('P.{100}',txt))
print(re.search('P.{4}',txt))


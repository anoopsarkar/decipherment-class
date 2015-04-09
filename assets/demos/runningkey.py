import string
import sys
#keytext = 'thequickbrownfoxjumpsoverthelazydog'
keytext = 'almosteverypaperwewillreadiswrittenbykevinknightandhisjustlyfamousdisciples'

plaintext = """ this course is about machine learning and natural language processing methods applied to the task of decipherment 
 codes ciphers and scripts are examples of things that need decipherment 
 the problem of decipherment is a canonical example of unsupervised learning as there is no human annotation available 
 so the course will focus on many unsupervised learning methods applicable to the decipherment task 
 we will also study how decipherment methods can be useful for other nlp tasks such as machine translation """
#plaintext = """This course is about machine learning and natural language processing
# methods applied to the task of decipherment. Codes, ciphers,
#and scripts are examples of things that need decipherment. The
#problem of decipherment is a canonical example of unsupervised
#learning, as there is no human annotation available. So, the course
#will focus on many unsupervised learning methods applicable to the
#decipherment task. We will also study how decipherment methods can
#be useful for other NLP tasks such as machine translation."""

if set(list(keytext)) - set(string.lowercase) != set():
    print >>sys.stderr, 'missing characters:', set(list(keytext)) - set(list(string.lowercase))

out = []
for i, c in enumerate(plaintext):
    if c.lower() not in string.lowercase: 
        out += c
    else:
        cipherindex = ( ord(c.lower()) + ord(keytext[i % (len(keytext)-1)]) ) % 26
        cipherchar = string.lowercase[cipherindex]
        if c.isupper(): out += cipherchar.upper()
        else: out += cipherchar
print
for c in out:
    if c == ' ':
        print '\"_\"',
    elif c == '\n':
        print
        print
    elif c.lower() in string.lowercase: 
        print '\"%s\"' % (c.lower()),
    else: 
        pass

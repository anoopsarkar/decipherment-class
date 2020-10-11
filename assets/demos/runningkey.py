import string
import sys
#keytext = 'thequickbrownfoxjumpsoverthelazydog'
#keytext = 'almosteverypaperwewillreadiswrittenbykevinknightandhisjustlyfamousdisciples'
keytext = 'imagineaworldwhereyoucanpickupaphoneandtalkinenglish'

plaintext = """imagine a world where you can pick up a phone and talk in english, while at the other end of the line your words are spoken in chinese. imagine a computer animated representation of yourself speaking fluently what you have written in an email. imagine automatically uncovering protein/drug interactions in petabytes of medical abstracts. imagine feeding a computer an ancient script that no living person can read, then listening as the computer reads aloud in this dead language. imagine a computer that can do better than humans at answering questions.

natural language processing is the automatic analysis of human languages such as english, korean, and thousands of others analyzed by computer algorithms. unlike artificially created programming languages where the structure and meaning of programs is easy to encode, human languages provide an interesting challenge, both in terms of its analysis and the learning of language from observations."""
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
print "".join(out)
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

import string
import sys
#keytext = 'thequickbrownfoxjumpsoverthelazydog'
keytext = 'almosteverypaperwewillreadiswrittenbykevinknightandhisjustlyfamousdisciplesoftheunderworld'
plaintext = """This course is about machine learning and natural language processing
(NLP) methods applied to the task of decipherment. Codes, ciphers,
and scripts are examples of things that need decipherment. The
problem of decipherment is a canonical example of unsupervised
learning, as there is no human annotation available. So, the course
will focus on many unsupervised learning methods applicable to the
decipherment task. We will also study how decipherment methods can
be useful for other NLP tasks such as machine translation."""

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
print ''.join(out)

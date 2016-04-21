import string
state = '0'
print state
print '(%c (%c \"_\" \"_\"))' % (state, state)
for i in string.uppercase:
    for j in string.lowercase:
        print '(%c (%c \"%s\" \"%s\"))' % (state, state, i, j)

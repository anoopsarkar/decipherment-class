import string
import sys
#keytext = 'thequickbrownfoxjumpsoverthelazydog'
keytext = 'almosteverypaperwewillreadiswrittenbykevinknightandhisjustlyfamousdisciplesoftheunderworld'

plaintext = """_this_course_is_about_machine_learning_and_natural_language_processing_methods_applied_to_the_task_of_decipherment_
_codes_ciphers_and_scripts_are_examples_of_things_that_need_decipherment_
_the_problem_of_decipherment_is_a_canonical_example_of_unsupervised_learning_as_there_is_no_human_annotation_available_
_so_the_course_will_focus_on_many_unsupervised_learning_methods_applicable_to_the_decipherment_task_
_we_will_also_study_how_decipherment_methods_can_be_useful_for_other_nlp_tasks_such_as_machine_translation_
"""
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
for c in out:
    if c == '\n': print '\n'
    else: print '\"%s\"' % (c),
print

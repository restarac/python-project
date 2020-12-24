import random
import samples.adjectives as adj

verbs = ['ask to','be','become','begin','call for','can do','come','could','do','feel','find','get','give','go','have','hear','help','keep','know','leave','let','like','live','look','make','may','mean','might','move','need','play','put','run','say','see','seem','should','show','start','take','talk','tell','think','try','turn','use','want','will','work','would']
nouns = ['area','book','business','case','child','company','country','day','eye','family','group','hand','job','life','man','money','month','mother','night','people','place','point','problem','program','question','room','school','state','story','student','study','system','thing','time','water','woman','word','work','year']
# A pronoun is a type of word that replaces a noun (reminder, a noun is a person, place, or thing)
pronouns = [ 'I', 'he','it', 'she', 'you', 'him', 'them', 'this', 'who']
adverb_connection = ['just', 'because', 'while']

def random_verb(): return random.choice(verbs)
def random_noun(): return random.choice(nouns)
def random_adjective(): return random.choice(adj.descriptive)
def random_pronouns(): return random.choice(pronouns)
def random_quantitative(): return random.choice(adj.quantitative)
def random_adverb_connection(): return random.choice(adverb_connection)

from samples import samples
import random
# https://www.thoughtco.com/phrase-grammar-1691625
#  Types of Phrases With Examples
#     Noun Phrase
#     "Buy a big bright green pleasure machine!" — Paul Simon, "The Big Bright Green Pleasure Machine," 1966
#     Verb Phrase
#     "Your father may be going away for a little while." — Ellen Griswold in the movie "Vacation," 1983
#     Adjective Phrase
#     "It is always the best policy to speak the truth—unless, of course, you are an exceptionally good liar." — Jerome K. Jerome, "The Idler," February 1892
#     Adverb Phrase
#     "Movements born in hatred very quickly take on the characteristics of the thing they oppose." — J. S. Habgood, "The Observer," May 4, 1986
#     Prepositional Phrase
#     "I could dance with you till the cows come home. On second thought, I'd rather dance with the cows till you come home." —Groucho Marx in "Duck Soup," 1933

def noum_phrases():
    return f'{samples.random_verb()} {samples.random_quantitative()} {samples.random_noun()} for {samples.random_pronouns()}'

def verb_phrases():
    return f'{samples.random_pronouns()} {samples.random_noun()} may {samples.random_pronouns()} {samples.random_verb()} {samples.random_quantitative()}'

def compound_phrases():
    return f'{noum_phrases()} {samples.random_adverb_connection()} {verb_phrases()}.'

def random_compound_phrases():
    result = f'{noum_phrases()} {samples.random_adverb_connection()} {verb_phrases()}.'
    if more():
        result = " ".join([result, random_compound_phrases()])

    return result

def more(): return random.choice([True, False])

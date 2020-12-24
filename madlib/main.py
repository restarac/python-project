# print("How operation works, 1 + 1:")
# print(1 + 1)
# print(0.1 + 0.2) # This is weird... https://0.30000000000000004.com/
# print(.2 + .3)
# print(float("1") + 0.3)


# print("how interpolations works:")
# string_value = "concatenation"
# print("This is a " + string_value)
# print("This is a {}".format(string_value))
# print(f"This is a {string_value}") # this is likable

# adj1 = input("Adjective: ")
# verb1 = input("Verb: ")
# noun1 = input("Noum: ")
# madlib = f"Studying is so {adj1}! This is because we can't {verb1} as we want. Besides you must think \
#     about how this {noun1} affect your life."

from samples import phrases

def paragraph(): return " ".join([phrases.random_compound_phrases() for _ in range(3)])

text = "\n\n".join([paragraph() for _ in range(3)])

print(text)

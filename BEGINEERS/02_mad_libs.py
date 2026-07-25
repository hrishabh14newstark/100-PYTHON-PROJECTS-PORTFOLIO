"""
02: Mad Libs Generator
An exercise in string formatting and user input.
"""
def mad_libs():
    print("--- Mad Libs Generator ---")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")

    story = f"The {adjective} {noun} decided to {verb} {adverb} across the road."
    print("
Here is your story:")
    print(story)

if __name__ == "__main__":
    mad_libs()

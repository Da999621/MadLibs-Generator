#                                           madlibs generator

def madlibs():
    # Story template with placeholders
    story = """
    Once upon a time, in a <place> far away, there lived a <adjective> <noun>. 
    This creature was known for its <adjective> <body part> and its ability to <verb> 
    faster than anyone else in the <place>. One day, while exploring the <adjective> 
    <noun>, the creature stumbled upon a <noun> made entirely of <material>. 
    
    Without hesitation, the creature decided to <verb> the <noun> and discovered a 
    <adjective> <noun> inside. Amazed by this <adjective> treasure, the creature 
    decided to <verb> it back to its <home>.
    
    From that day on, the <adjective> <noun> became a legend in the <place>, known 
    for its <adjective> adventures and its <adjective> heart.
    """
    
    # Prompting the user for words
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    place = input("Enter a place: ")
    body_part = input("Enter a body part: ")
    verb = input("Enter a verb: ")
    material = input("Enter a material: ")
    home = input("Enter a home: ")
    
    # Fill in the story with user's input
    filled_story = story.replace("<adjective>", adjective)\
                        .replace("<noun>", noun)\
                        .replace("<place>", place)\
                        .replace("<body part>", body_part)\
                        .replace("<verb>", verb)\
                        .replace("<material>", material)\
                        .replace("<home>", home)
    
    # Print the completed story
    print("\nHere is your madlibs story:\n")
    print(filled_story)

# Call the function to run the madlibs generator
madlibs()


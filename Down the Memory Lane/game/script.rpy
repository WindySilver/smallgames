# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Sylvia")
define y =  Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene entrance path

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show natsumi casual smile at center:
        zoom 0.6

    # These display lines of dialogue.

    n "We're almost there. Just through this path and it should be within our sights."

    n "Man. It feels so weird to be back. I haven't been here in years."
    
    n "Not since..."
    
    show natsumi casual frown
    
    n "Not since you died."
    
    "You nod. You know that it has been years since you have been there, but that was only because of logic."
    
    "Well, logic and the fact that it was quite literally a lifetime ago for you."
    
    "What a weird world this was."
    
    n "Does this place look familiar to you, Jake?"
    
    y "It looks quite similar to the photos you showed me of us, but otherwise no."
    
    n "I figured as much."
    
    show natsumi casual smile
    
    n "But I'm sure that once we get to the house, you'll start to remember! You'll see."
    
    "You wish you were as hopeful as her."

    # This ends the game.

    return

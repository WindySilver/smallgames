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
    
    "What a weird world."
    
    n "Does this place look familiar to you, Jake?"
    
    y "It looks quite similar to the photos you showed me of us, but otherwise no."
    
    n "I figured as much."
    
    show natsumi casual smile
    
    n "But I'm sure that once we get to the house, you'll start to remember! You'll see."
    
    "You wish you were as hopeful as her."

    jump two
    
label two:
    
    scene house
    
    show natsumi casual smile
    
    n "Here we are!"
    
    n "It hasn't changed pretty much at all since the last time."
    
    show natsumi casual frown
    
    n "I... I am glad. That it's still like this. Like it used to be."
    
    show natsumi casual open
    
    n "Umm... Jake?"
    
    y "Yes?"
    
    n "Does this... remind you of anything?"
    
    menu:
        
        "Just the photos.":
            jump housetrue
        
        "Yes. I... I remember living here with my parents.":
            jump houselie
    
label housetrue:
    
    show natsumi casual frown
    
    n "That's too bad. You always missed home when we were away."
    
    y "I wish I did remember something. This looks like a lovely place to grow up in."
    
    n "Yeah... I've thought so too, whenever I've been here."
    
    jump three
    
label houselie:
    
    show natsumi casual open
    
    n "You do?! You remember your family?"
    
    y "Yeah. It... It's starting to come back to me."
    
    n "That's wonderful! Tell me about them!"
    
    y "Well, like you know, Mom was beautiful. Golden hair and blue eyes. She loved to wear blue."
    
    y "Dad, on the other hand, he was a gardener and dressed like one most of the time. He taught me a lot of what he knew to me when I was a child."
    
    "..."
    
    n "What about your brothers?"
    
    y "My brothers?"
    
    n "Yeah, your brothers. What about them? What do you remember of them?"
    
    y "Oh right, yes, my brothers. Well, my older brother, he... he got Mom's eyes and hair. A real pretty boy."
    
    show natsumi casual frown
    
    y "My younger brother... He and I look similar, I'd say. More of a mixture of our parents."
    
    n "..."
    
    y "Is... is something wrong?"
    
    n "You don't have an older brother. And none of you four look inherited both your mother's hair and eyes."
    
    "{i}Oops.{/i}"
    
    n "Jake, please don't lie about your memory."
    
    y "I'm... I'm sorry, Sylvia."
    
    n "It's okay. Let's head on."
    
    show natsumi casual smile
    
    n "There's a lot I want to show you."
    
    jump three
    
label three: TODO




    # This ends the game.

    return

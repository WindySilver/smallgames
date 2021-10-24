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
    
    n "You don't have an older brother. And none of you three look inherited both your mother's hair and eyes."
    
    "{i}Oops.{/i}"
    
    n "Jake, please don't lie about your memory."
    
    y "I'm... I'm sorry, Sylvia."
    
    n "It's okay. Let's head on."
    
    show natsumi casual smile
    
    n "There's a lot I want to show you."
    
    jump three
    
label three:
    
    scene outdoor dining
    
    show natsumi casual smile
    
    n "This takes me back. Your parents used to joke that once Julian or Jordan would start dating, they'd have to get more chairs here."
    
    show natsumi casual closed smile
    
    n "*chuckle*"
    
    show natsumi casual smile
    
    n "Those were good times..."
    
    show natsumi casual open
    
    n "Do you..."
    
    show natsumi casual frown
    
    n "Do you remember anything about those times?"
    
    menu:
        "Nothing.":
            jump outdoortruth
        
        "You were so beautiful back then, too.":
            jump outdoorlie
    
label outdoortruth:
    
    "You shake your head."
    
    y "Nothing."
    
    "You look down."
    
    y "I wish I did remember something. I can see that all these memories are do fond to you but I just... I just can't."
    
    show natsumi casual closed frown
    
    n "..."
    
    show natsumi casual frown
    
    n "We'll just keep trying. I'm not going to give up on you."
    
    show natsumi casual open
    
    n "If I didn't give up on you before — even if you don't remember it — I'm definitely not going to give up on you now."
    
    n "Come on, let's head to the swings!"
    
    jump four
    
label outdoorlie:
    
    show natsumi casual frown
    
    n "..."
    
    n "You don't mean that."
    
    y "Huh?"
    
    n "I wasn't beautiful back then, and you were quick to note that. I was plain and rather inelegant. You told me as much."
    
    y "I did? Why did I say that?"
    
    show natsumi casual smile
    
    n "Because you were a melodramatic ass."
    
    show natsumi casual closed smile
    
    n "Heh..."
    
    n "You always were such a melodramatic ass. You just grew a brain-to-mouth filter along the way."
    
    y "Okay, I didn't expect to hear that."
    
    show natsumi casual smile
    
    n "I may or may not have reserved the exclusive right to call you that. After all, you're {i}my{/i} melodramatic ass."
    
    n "Come on, let's head to the swings."
    
    show natsumi casual frown
    
    n "Just please don't lie to me again."
    
    y "Okay. I... I'm sorry."
    
    "{i}Oops.{/i}"
    
    jump four
    
label four:
    
    scene swing
    
    show natsumi casual open
    
    n "Wow, it's still like it used to be!"
    
    n "I was half-expecting it to have been replaced."
    
    show natsumi casual smile
    
    n "All four of us — you, me, Julian and Jordan — used this a lot growing up. It was so much fun, even when you 'grew too old to play with us kids' since Jordan always convinced you to come push the swing."
    
    y "I bet he bribed me with whatever allowance he had."
    
    show natsumi casual closed smile
    
    n "Haha, I wouldn't put it past him to do that."
    
    show natsumi casual frown
    
    n "He really loved you, you know. Even more than he ever let on. The same with Julian, even if he never said it."
    
    n "You meant the whole world to them."
    
    y "..."
    
    "A clench in your stomach tells you that you don't want to think about your brothers."
    
    "You don't remember what happened to them, but thinking about them fills your gut with emotions you don't want to deal with. Not now."
    
    "Maybe not ever."
    
    n "You don't remember, do you?"
    
    y "No, not really. Are they dead?"
    
    show natsumi casual closed frown
    
    n "...Yes."
    
    show natsumi casual frown
    
    n "They died before you. I never got the details but... it seemed that things went really bad out there."
    
    "You nod. You don't remember anything, but your gut is telling you that things hit the fan back then."
    
    "You don't want to think about it. Even without dying and being reborn, you'd had enough of death."
    
    n "Have you recovered any memories?"
    
    "You shake your head."
    
    show natsumi casual closed frown
    
    n "*sigh*"
    
    show natsumi casual frown
    
    n "Well, let's finish the tour anyway. Even if you don't remember anything today, all this might stir something and you'll recover memories later on."
    
    n "At least that's what I hope will happen."
    
    jump five
    
label five:
    
    scene garden path
    
    show natsumi casual open
    
    n "I didn't expect Raymond to have developed a green thumb."
    
    y "Raymond?"
    
    n "Yeah. He's been taking care of this place ever since he retired. Said he wanted some peace and quiet after the long, hectic life he's lead so far."
    
    y "Who was he again?"
    
    show natsumi casual frown
    
    n "He was our doctor, the one who taught me medicine back in the day."
    
    show natsumi casual smile
    
    n "Although he certainly had his way with hatchets too. Never get between Raymond and his hatchet."
    
    y "So, who owns this place?"
    
    show natsumi casual frown
    
    n "I inherited it after you passed away."
    
    n "Although, I've had friends and family keep the place in an order. Then Raymond retired and I asked if he wanted to move in here to have something to do with his time and he said yes."
    
    y "So where is he now?"
    
    n "Visiting Peter and the others."




    # This ends the game.

    return

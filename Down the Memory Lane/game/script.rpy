# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Sylvia")
define y =  Character("You")

default lied = False


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
    $ lied = True
    
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
    $ lied = True
    
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
    
    y "Huh. I haven't seen him here, though. Is he not here?"
    
    n "Not today. He's out visiting family."

    n "He also figured that it'd be for the best to give us some privacy, especially since I haven't visited here for a while either."
    
    show natsumi casual closed frown

    y "Is something wrong?"
    
    n "*sigh*"
    
    show natsumi casual frown
    
    n "I'm just frustrated. I'd hoped that you'd recover at least a little bit of your memories. We spent so much time here growing up."
    
    show natsumi casual closed frown
    
    n "Jake, you were my partner in your previous life. I loved you so, {i}so{/i} much. And you... you died in my arms."
    
    hide natsumi casual closed frown
    
    "Sylvia turns away from you. Her whole body trembles and you can hear her voice shake from the dammed tears."
    
    n "There was nothing I could do except smile for you since you asked me to and say whatever I needed to say before you were gone forever. And I... I'm not entirely sure about what happened after you... you were gone."
    
    n "What the others told... they said that I snapped in some way. And after it was all over, I got a PTSD diagnosis and sick time whatnot... And all I remember is that it hurt {i}so fucking much{/i}."
    
    n "I thought you were gone forever and acted that according to that. I moved away from our quarters because I couldn't stand being there alone and took over your old ones, the ones you never wanted to use."
    
    n "You know how I turned out. I don't know how I made it, aside from everyone's immense support and all the counseling."
    
    n "I never even thought of having another partner, not after everything we went through together. No one could ever measure up to you, you know?"
    
    n "And then you suddenly came back to life. You just... reappeared into our world, without a memory. But it was still you."
    
    y "I remember that. You almost crushed me with that bear hug."
    
    "Sylvia lets out a broken laugh. You are almost certain that she is either on the verge of tears or already crying."
    
    n "I was convinced that if I let go of you, you'd disappear again."
    
    n "And when you didn't..."
    
    n "It was the happiest day of my life."
    
    n "I'd gotten my partner back somehow. The love of my life, my other half, the one I'd missed more than anyone else ever. By the will of whatever higher powers, you'd returned to life."
    
    n "And I still am happy that you're with me again, don't get me wrong. But there's so much we experienced together that you don't remember and it... it hurts a lot, too."
    
    n "And... When you won't remember anything no matter how hard I try, it feels like I'm losing you all over again. It's not fair."
    
    "Sylvia turns to the sky."
    
    n "IT'S NOT FAIR, YOU HEAR?!"
    
    "Sylvia breaks into tears. You look for words that might appease her. You need to get her to calm down somehow."
    
    menu:
        "Hey, calm down. It's not as bad as it looks. I'll remember stuff.":
            jump sixbad
        "I'm sorry that I don't remember anything. I can see that it's important to you.":
            jump sixguilty
        "I'm sure I will remember sooner or later. It's just going to take more time than either of us expected.":
            jump sixgood
            
label sixbad:
    if lied:
        "Sylvia turns to you, tears streaming down her face."
        
        n "How can I believe that when you've already lied to me about remembering things?!"
        
        "You have no answer to that."
        
        "Sylvia wiped her tears away, still looking angry."
        
        n "I thought so."
        
        "She turns away."
        
        n "You're not the Jake I knew. You're a liar and I'm done."
        
        n "It's like The Broken View sang in {i}Something Better{/i}."
        
        n "{i}You don't have to be the one to lose/You don't have to be the one to tell a lie{/i}"
        
        n "{i}And I don't have to bе the one to take all this/Timе you've wasted being dishonest{/i}"
        
        n "When you're ready to be honest with me about what you remember, I'm done with you."
        
        show natsumi casual frown
        
        n "Goodbye, Jake."
        
        hide natsumi casual frown
        
        "With those words, Sylvia walks away, leaving you at the garden path to find your own way back."
        
        "As you walk away, you mull over what happened. You had known how important you regaining your memory had been to Sylvia, but your white lies that were meant to make her feel better, more confident, only hurt her more."
        
        scene bridge
        
        "As you cross the bridge leading away from your childhood home, you decide that you need to work on your memory on your own first, then figure out how to make it up to Sylvia."
        
        "You have no idea what Raymond finds a couple of days later when he returns to his home."
        
        return
        
    else:
        "Sylvia falls silent but doesn't turn to you."
        
        n "That's not helping. You haven't remembered anything so far. Why do you think you're going to remember anything at all at any point?"
        
        "You try to find an answer to that, but Sylvia doesn't give you enough time."
        
         n "I thought so."
         
         "You two are silent for a while. Then Sylvia speaks up again."
         
         n "I think I'm done trying to force the impossible to happen."
         
         "She starts to walk away."
         
         y "Where are you going? What are we going to do?!"
         
         n "{i}We{/i} are not going to do anything. {i}I{/i} am going home to rethink if I want to have anything to do with you. What {i}you{/i} want to do is up to you."
         
         n "Goodbye for now, Jake."
         
         "With those words, Sylvia walks away, leaving you at the garden path to find your own way back."
        
        "As you walk away, you mull over what happened. You had known how important you regaining your memory had been to Sylvia, so for her to give in to despair and give up on it like that had come as a surprise."
        
        "Confused and completely out of your depth, you text Raymond for advice. The retired doctor probably knows your partner well enough to help you with how you should proceed with her."
        
        scene bridge
        
        "As you cross the bridge leading away from your childhood home, you get a reply back. It says, 'Give her time and space. The years without you have been tough for her. She'll come around.'"
        
        "Another text comes a while afterwards, 'In the meantime, if you have the time, stop by once I've come back home. I'll see what I can do to help you regain your memory.'"
        
        "You send Raymond a quick 'Thank you' and keep walking. Perhaps there is still hope for you and Silvia."
        
        "At least you want to hold onto that hope."
        
        return
    
label sixguilty:
    "TODO"
    
    return

label sixgood:
    "TODO"
        
        
    

    # This ends the game.

    return

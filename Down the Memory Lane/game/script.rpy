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

    scene entrance path with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show natsumi casual smile at center:
        zoom 0.6

    # These display lines of dialogue.
    
    #PLAY Friday Afternoon or New Road
    
    play music "New Road Loop.ogg"

    n "We're almost there. Just through this path and it should be within our sights."

    n "Man. It feels so weird to be back. I haven't been here in years."
    
    n "Not since..."
    
    show natsumi casual frown
    
    n "Not since you died."
    
    "You nod. You know that it has been years since you have been there, but that was only because of logic."
    
    "Well, logic and the fact that it was quite literally a lifetime ago for you."
    
    "What a strange world."
    
    n "Does this place look familiar to you, Jake?"
    
    y "It looks quite similar to the photos you showed me of us, but otherwise no."
    
    n "I figured as much."
    
    show natsumi casual smile
    
    n "But I'm sure that once we get to the house, you'll start to remember! You'll see."
    
    "You wish you were as hopeful as her."
    
    stop music fadeout 1.0

    jump two
    
label two:
    
    scene house with dissolve
    
    #PLAY Friday Afternoon
    play music "Friday Afternoon Loop.ogg"
    
    show natsumi casual smile at center:
        zoom 0.6
    
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
    
    show natsumi casual frown at center:
        zoom 0.6
        
    y "Just the photos."
    
    n "That's too bad. You always missed home when we were away."
    
    y "I wish I did remember something. This looks like a lovely place to grow up in."
    
    n "Yeah... I've thought so too, whenever I've been here."
    
    jump three
    
label houselie:
    $ lied = True
    
    show natsumi casual open at center:
        zoom 0.6
    
    y"Yes. I... I remember living here with my parents."
    
    n "You do?! You remember your family?"
    
    y "Yeah. It... It's starting to come back to me."
    
    show natsumi casual smile
    
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
    
    stop music fadeout 1.0
    
    n "You don't have an older brother. And none of you three look inherited both your mother's hair and eyes."
    
    "{i}Oops.{/i}"
    
    n "Jake, please don't lie about your memory."
    
    y "I'm... I'm sorry, Sylvia."
    
    n "It's okay. Let's head on."
    
    show natsumi casual smile
    
    play music "Friday Afternoon Loop.ogg"
    
    n "There's a lot I want to show you."
    
    jump three
    
label three:
    
    scene outdoor dining with dissolve
    
    #play music "Friday Afternoon Loop.ogg" #OR MAYBE SOMETHING ELSE
    
    show natsumi casual smile at center:
        zoom 0.6
    
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
    
    show natsumi casual closed frown at center:
        zoom 0.6
    
    n "..."
    
    show natsumi casual frown
    
    n "We'll just keep trying. I'm not going to give up on you."
    
    show natsumi casual smile
    
    n "If I didn't give up on you before — even if you don't remember it — I'm definitely not going to give up on you now."
    
    n "Come on, let's head to the swings!"
    
    jump four
    
label outdoorlie:
    $ lied = True
    
    y "You were so beautiful back then, too."
    
    show natsumi casual frown at center:
        zoom 0.6
    
    n "..."
    
    stop music fadeout 1.0
    
    n "You don't mean that."
    
    y "Huh?"
    
    play music "Try and Solve This Loop.ogg" volume 0.6
    
    n "I wasn't beautiful back then, and you were quick to note that. I was plain and rather inelegant. You told me as much."
    
    y "I did? Why did I say that?"
    
    show natsumi casual smile
    
    n "Because you were a melodramatic ass."
    
    show natsumi casual closed smile
    
    n "Heh..."
    
    n "You were always such a melodramatic ass. You just grew a brain-to-mouth filter along the way."
    
    y "Okay, I did not expect to hear that."
    
    show natsumi casual smile
    
    n "I may or may not have reserved the exclusive right to call you that. After all, you are {i}my{/i} melodramatic ass."
    
    n "Come on, let's head to the swings."
    
    show natsumi casual frown
    
    n "Just please don't lie to me again."
    
    y "Okay. I-I'm sorry."
    
    stop music fadeout 1.5
    
    "{i}Oops.{/i}"
    
    play music "Friday Afternoon Loop.ogg" fadein 1.0
    
    jump four
    
label four:
    
    scene swing with dissolve
    
    #play music "Friday Afternoon Loop.ogg" #OR MAYBE SOMETHING ELSE
    
    show natsumi casual open at center:
        zoom 0.6
    
    n "Wow, it's still like it used to be!"
    
    n "I was half-expecting it to have been replaced."
    
    show natsumi casual smile
    
    n "All four of us — you, me, Julian and Jordan — used this a lot growing up. It was so much fun, even when you 'grew too old to play with us kids' since Jordan always convinced you to come push the swing."
    
    y "I bet he bribed me with whatever allowance he had."
    
    show natsumi casual closed smile
    
    n "Heh, I wouldn't put it past him to do that."
    
    show natsumi casual frown
    
    n "He really loved you, you know. Even more than he ever let on. The same with Julian, even if he never said it."
    
    n "You meant the whole world to them."
    
    stop music fadeout 1.5
    
    y "..."
    
    play music "Purple Black Loop.ogg" fadein 3.0 volume 0.4
    
    #MAYBE SWITCH TO SOMETHING MORE DRAMATIC, MAYBE PURPLE BLACK ON A LOW VOLUME IF IT'S NOT USED ELSEWHRE
    
    "A clench in your stomach tells you that you don't want to think about your brothers."
    
    "You don't remember what happened to them, but thinking about them fills your gut with emotions you don't want to deal with. Not now."
    
    "Maybe not ever."
    
    n "You don't remember, do you?"
    
    y "No, not really, aside from a bad feeling in my gut. Are they... are they dead?"
    
    show natsumi casual closed frown
    
    n "..."
    
    n "Yes."
    
    show natsumi casual frown
    
    n "They died long before you did. I never got the details — you never told what exactly happened — but... it seemed that things turned out really bad out there."
    
    "You nod. You don't remember anything, but your gut is telling you that things hit the fan back then."
    
    "You don't want to think about it. Even without dying and being reborn, you've had enough of death."
    
    n "Have you recovered any memories?"
    
    "You shake your head."
    
    show natsumi casual closed frown
    
    n "*sigh*"
    
    show natsumi casual frown
    
    n "Well, let's finish the tour anyway. Even if you don't remember anything today, all this might stir something and you'll recover memories later on."
    
    stop music fadeout 4.0
    
    n "At least that's what I hope will happen."
    
    jump five
    
label five:
    
    scene garden path with dissolve
    
    play music "Friday Afternoon Loop.ogg" #OR MAYBE SOMETHING ELSE
    
    show natsumi casual open at center:
        zoom 0.6
    
    n "Wow, it's still just like it used to be!"
    
    n "I didn't expect Raymond to have developed a green thumb of any sort."
    
    y "Raymond?"
    
    n "Yeah. He's been taking care of this place ever since he retired. Said he wanted some peace and quiet after the long, hectic life he's lead so far."
    
    y "Who was he again?"
    
    show natsumi casual frown
    
    n "He was our doctor, the one who taught me medicine back in the day."
    
    show natsumi casual smile
    
    n "Although he certainly has his way with hatchets too. Never get between Raymond and his hatchet."
    
    y "Heh, I'll keep that in mind."
    
    y "So, who owns this place?"
    
    show natsumi casual frown
    
    n "I inherited it when you died."
    
    n "Although, I've had friends and family keep the place in an order. I... didn't want to return here after the paperwork was done, so I delegated the work to people I trust. Those who wanted to stay here took turns."
    
    n "Then Raymond retired and I asked if he wanted to move in here to have something to do with his newfound free time and he said yes, especially since I didn't ask for rent."
    
    y "Huh. I haven't seen him here, though. Is he not here?"
    
    n "Not today. He's out visiting family."

    n "He also figured that it'd be for the best to give us some privacy, especially since I haven't been here in such a long time either."
    
    show natsumi casual closed frown
    
    stop music fadeout 1.5
    
    n "..."

    y "Is something wrong?"
    
    n "*sigh*"
    
    show natsumi casual frown
    
    play music "Pink Blue loop Loop.ogg" fadein 2.0
    
    #PLAY Pink Blue loop or Purple Black loop
    
    n "I'm just frustrated. I'd hoped that you'd recover at least a little bit of your memories. We spent so much time here growing up."
    
    show natsumi casual closed frown
    
    n "Jake, you were my partner in your previous life. I loved you so, {i}so{/i} much. And you... you died in my arms."
    
    hide natsumi casual closed frown
    
    "Sylvia turns away from you. Her body trembles and you can hear her voice shake from the dammed tears."
    
    n "There was nothing I could do except smile for you since you asked me to and say whatever I needed to say before you were gone forever. And I... I'm not entirely sure about what happened after you... after you..."
    
    n "...After you passed away right there and then, on that damn battlefield."
    
    n "What the others told... they said that I snapped in some way. And after it was all over, I got a PTSD diagnosis and sick time and whatnot... But all I remember is that it hurt {i}so fucking much{/i}."
    
    n "I thought you were gone forever and acted accordingly. I moved out of our quarters because I couldn't stand being there alone and took over your old quarters which you'd been using as a storage space."
    
    n "You know how I turned out. I don't know how I made it, aside from everyone's immense support and all the counseling."
    
    n "I never even thought of having another partner, not after everything we went through together. No one could ever measure up to you, you know?"
    
    n "And then you suddenly came back to life. You just... reappeared into our world, without a memory. But it was still you. Jake, my partner whom I thought I'd lost for good."
    
    y "I remember that. You almost crushed me with that bear hug."
    
    "Sylvia lets out a broken laugh. You are almost certain that she is either on the verge of tears or already crying."
    
    n "I was convinced that if I let go of you, you'd disappear again. That I'd be all alone again in this world even though even then I was surrounded by people I'd worked with for most of my life."
    
    n "And when you didn't disappear..."
    
    n "It was the happiest day of my life."
    
    n "I'd gotten my partner back somehow. The love of my life, my other half, the one I'd missed more than anyone else ever. By the will of powers that govern over life and death, you'd returned to life."
    
    n "And I still am happy that you're with me again, don't get me wrong. But there's so much we experienced together that you don't remember and it... it hurts a lot, too."
    
    n "And... When you won't remember anything no matter how hard I try, it feels like I'm losing you all over again. It's not fair."
    
    "Sylvia turns to the sky."
    
    n "{b}{i}IT'S NOT FAIR, YOU HEAR?!{/i}{/b}"
    
    "Sylvia breaks into tears. You look for words that might appease her. You need to get her to calm down somehow."
    
    menu:
        "Hey, calm down. It's not as bad as it looks. I'll remember stuff.":
            jump sixbad
        "I'm sorry that I don't remember anything. I can see that it's important to you.":
            jump sixguilty
        "I'm sure I will remember sooner or later. It's just going to take more time than either of us expected.":
            jump sixgood
            
label sixbad:
    
    y "Hey, calm down. It's not as bad as it looks. I'll remember stuff."
    
    if lied:

        "Sylvia turns to you, tears streaming down her face."
        
        show natsumi casual frown at center:
            zoom 0.6
        
        n "How can I believe that when you've already lied to me about remembering things?!"
        
        "You have no answer to that."
        
        "Sylvia wipes her tears away, still looking angry."
        
        n "I thought so."
        
        hide natsumi casual frown
        
        "Sylvia turns away."
        
        n "You're not the Jake I knew. You're a liar and I'm done."
        
        n "It's like The Broken View sang in {i}Something Better{/i}."
        
        n "{i}You don't have to be the one to lose/You don't have to be the one to tell a lie{/i}"
        
        n "{i}And I don't have to bе the one to take all this/Timе you've wasted being dishonest{/i}"
        
        n "Until you're ready to be honest with me about what you remember, I'm done with you."
        
        stop music fadeout 3.0
        
        n "Goodbye, Jake."
        
        hide natsumi casual frown
        
        play music "Little Apprentice Loop.ogg" fadein 3.0
        
        #END TRACK HERE, CHANGE TO Little Apprentice
        
        "With those words, Sylvia walks away, leaving you at the garden path to find your own way back."
        
        "As you walk away, you mull over what happened. You had known how important you regaining your memory had been to Sylvia, but your white lies that were meant to make her feel better, more confident, only hurt her."
        
        scene bridge with dissolve
        
        "As you cross the bridge leading away from your childhood home, you decide that you need to work on your memory on your own first, then figure out how to make it up to Sylvia."
        
        "You have no idea what Raymond finds a couple of days later when he returns to his home."
        
    else:
        "Sylvia falls silent but doesn't turn to you."
        
        n "That's not helping. You haven't remembered anything so far. Why do you think you're going to remember anything at all at any point?"
        
        "You try to find an answer to that, but Sylvia doesn't give you enough time."
        
        n "I thought so."
         
        "You two are silent for a while. Then Sylvia speaks up again."
         
        n "I think I'm done trying to force the impossible to happen."
         
        "She starts to walk away."
         
        y "Where are you going? What are we going to do?!"
         
        n "{i}We{/i} are not going to do anything. {i}I{/i} am going home to rethink if I want to have anything to do with you. What {i}you{/i} are going to do is up to you."
        
        stop music fadeout 3.0
         
        n "Goodbye for now, Jake."
        
        play music "Little Apprentice Loop.ogg" fadein 3.0
        
        #END TRACK HERE, CHANGE TO Little Apprentice
         
        "With those words, Sylvia walks away, leaving you at the garden path to find your own way back."
        
        "As you walk away, you mull over what happened. You had known how important you regaining your memory had been to Sylvia, so for her to give in to despair and give up on it like that had come as a surprise."
        
        "Confused and completely out of your depth, you text Raymond for advice. The retired doctor probably knows your partner well enough to help you with how you should proceed with her."
        
        scene bridge with dissolve
        
        "As you cross the bridge leading away from your childhood home, you get a reply back. It says, 'Give her time and space. The years without you have been tough for her. She'll come around.'"
        
        "Another text comes a while afterwards, 'In the meantime, if you have the time, stop by once I've come back home. I'll see what I can do to help you regain your memory.'"
        
        "You send Raymond a quick 'Thank you' and keep walking. Perhaps there is still hope for you and Sylvia."
        
        "At least you want to hold onto that hope."
        
    return
    
label sixguilty:
    y "I'm sorry that I don't remember anything. I can see that it's important to you."
    
    "Sylvia falls silent and wipes her tears."
    
    stop music fadeout 4.0
    
    n "I'm sorry too. I shouldn't have broken down like that."
    
    n "*sigh*"
    
    n "Come on, let's head to the greenhouse."
    
    jump sixguilty2

label sixguilty2:
    
    scene greenhouse with dissolve
    
    play music "Friday Afternoon Loop.ogg" volume 0.7 #PLACEHOLDER
    #PLAY SOME SAD MUSIC HERE?
    
    show natsumi casual frown at center:
        zoom 0.6
    
    n "Your parents used to grow vegetables here."
    
    y "It seems that Raymond is continuing their work."
    
    n "Yeah, or he's having someone else do it for him."
    
    stop music fadeout 2.0
    
    "You're both quiet for a while."
    
    play music "Try and Solve This Loop.ogg" fadein 1.0
    
    #FADEIN Try and Solve This
    
    y "Are you ok?"
    
    n "Not really."
    
    show natsumi casual closed frown
    
    n "*sigh*"
    
    n "I'm sorry about the outburst earlier. I really shouldn't have done that, especially since I should be grateful that you're here with me, memories or no memories."
    
    y "It's okay. I can only imagine how hard all of this has been for you."
    
    show natsumi casual frown
    
    "Sylvia nods."
    
    n "Still. I should've kept my cool..."
    
    n "*sigh*"
    
    n "Could we please call it a day and resume this tour some other day? Maybe talk with Raymond too, if he's here then."
    
    n "I'm feeling a bit drained after all that, and I could probably use some time to think by myself about all of this."
    
    y "Of course. You only need to ask."
    
    show natsumi casual smile
    
    n "Thank you, Jake. It's good to see that that golden heart of yours is still there."
    
    jump guiltyend
    
label guiltyend:
    
    scene bridge with dissolve
    
    "You leave your childhood home mostly in silence. You both have a lot to unpack, and you'd be lying if you said that you didn't need some time to think and unwind too."
    
    "You and Sylvia promise to meet at work the following day and talk more then."
    
    "Even though you didn't recover memories, you figure that the tour was worth the effort. Perhaps now that the toughest part was over, you'll begin to recover your memories..."
    
    return

label sixgood:
    y "I'm sure I will remember sooner or later. It's just going to take more time than either of us expected."
    
    if lied:
        n "How can I believe you after you lied about recovering memories earlier?"
        
        "You look for an answer. Fortunately, she gives you the time you need to find one while she apparently forces herself to stop crying."
        
        y "I'm sorry I lied. I know that this is important to you and I... I wanted to give you hope that I can recover my memories. I didn't expect it to backfire like that."
        
        n "*sigh*"
        
        "Sylvia wipes her tears and turns to face you."
        
        show natsumi casual frown at center:
            zoom 0.6
        
        n "Don't do that. Lies never work out in the end, and if I can't trust that you're telling the truth, we won't get anywhere with this. Do you understand that?"
        
        "You nod."
        
        y "I'm sorry. I meant well, I swear I did."
        
        stop music fadeout 3.0
        
        n "I believe you."
        
        show natsumi casual smile
        #END TRACK HERE
        
    else:
        n "Are you... are you sure?"
        
        y "Yeah, I am."
        
        stop music fadeout 2.5
        
        "Sylvia stops crying."
        
        #END TRACK HERE
        
        n "Okay then. Okay. Everything's gonna be alright, right?"
        
        y "Yes. Everything will be alright in time."
        
        "Sylvia nods a few times, wipes her tears away and turns to you."
        
        show natsumi casual smile at center:
            zoom 0.6
        
        n "Yeah, you're right. Thanks, Jake."
    
    play music "Monday Morning Loop.ogg" volume 0.5 fadein 1.5
    
    n "And you did mention that you had a gut feeling about what happened to your brothers. I guess that's something, right?"
        
    "You smile. Progress!"
        
    y "Yeah. Yeah, it is something. Not much, but it's better than nothing."
        
    n "I thought so too."
    
    stop music fadeout 4.0
    n "Let's continue. The greenhouse is next."
    
    jump greenhouse
    
label greenhouse:
    scene greenhouse with dissolve
    
    play music "Friday Afternoon Loop.ogg" #OR SOMETHING ELSE?!
    
    show natsumi casual smile at center:
        zoom 0.6
    
    n "Your parents used to grow vegetables here. You'd be surprised by just how much they were able to output in one year with just one greenhouse like that."
    
    n "If I didn't know any better, I'd think your father was a magician in a gardener's disguise."
    
    y "But he was simply that good?"
    
    n "Yeah. He was a professional, after all."
    
    y "Huh. That's must have come in handy..."
    
    n "It did, believe me."
    
    y "Is Raymond continuing their work?"
    
    n "That, or he's having someone else do it for him. I haven't followed what's been going on here aside from things I had to know about as the owner."
    
    y "I see."
    
    show natsumi casual frown
    
    n "Um..."
    
    n "I'm sorry about the outburst earlier. I should've kept my cool better."
    
    show natsumi casual closed frown
    
    n "And I guess I've been fixating on helping you recover your memories too much when I should've focused more on being grateful that you're here with me again, memories or no memories."
    
    y "It's okay. I can only imagine how hard all of this has been for you."
    
    show natsumi casual smile
    
    n "Thank you, Jake."
    
    show natsumi casual closed smile
    
    n "I'm glad that you still have that golden heart of yours."
    
    show natsumi casual smile
    
    n "And even though we haven't gotten much progress today, I am grateful for what we have. We just need to keep going."
    
    y "Do you have more to show me?"
    
    n "I think we could head back to the house to rest a while before heading out. What do you say?"
    
    y "Sounds good to me."
    
    n "Let's go then. This way, please."
    
    jump goodend
    
label goodend:
    
    scene bridge with dissolve
    
    "Some time later, you leave your childhood home. There is a lot to unpack and you know that you are going to need some time to mull over everything you have seen and heard today."
    
    stop music fadeout 5.0
    
    "You stop at the bridge. Sylvia leans against the railing and gestures you to do the same. You oblige and look over the river flowing underneath."
    
    play music "Quantum Loop.ogg" fadein 15.0
    #PLAY Monday Morning?
    
    show natsumi casual smile at center:
        zoom 0.6
    
    n "What a day, huh?"
    
    y "Yup. What a day."
    
    n "How do you feel?"
    
    y "Pretty fine. I've got a lot to think about, though. You?"
    
    n "Same. Revisiting this place with you and reminiscing everything..."
    
    show natsumi casual frown
    
    n "I think I needed all this, even the breakdown I had. It was a reminder that I should be grateful for what I already have even though I very much still do want you to recover your memories."
    
    n "I want you to remember what we went through together, no matter what it takes."
    
    show natsumi casual closed smile
    
    n "There's so much I want to share with you again."
    
    show natsumi casual closed smile blush
    
    n "And a lot of things I want to experience with you again."
    
    y "I want to remember it all too."
    
    show natsumi casual smile
    
    n "Then let's keep working on it together, shall we?"
    
    y "Absolutely."
    
    #stop music fadeout 7.0
    
    n "Then there's nothing in this universe that's going to stop us from achieving that."
    
    hide natsumi casual smile
    
    #play music "Quantum Loop.ogg" fadein 1.0
    
    #Quantum might fit here?
    
    "You leave the bridge and head back to your current home. The work towards recovering your memories has only begun, but you are feeling hopeful."
    
    "With Sylvia, who has survived so much, by your side, recovering your memories is going to be a success, no matter how much time and effort it would take."
    
    scene black with fade
    
    "You are certain of it that night when you lie down by your partner's side and look into her loving eyes."
    
    "Someday, you would remember how it felt to hear her say 'I love you' for the first time ever and more."
    
    "You cannot wait for that day."
    

    # This ends the game.

    return

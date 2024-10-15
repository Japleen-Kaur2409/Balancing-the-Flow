define me = Character('Me', color="#c8c8ff")
define reporter = Character('Reporter', color="#c8c8ff")
define s = Character('Dr. Evelyn Reed', color="#c8ffc8")
define first_nation = Character('Nodin', color="#c8c8ff")
define politician = Character('Politican NPC', color="#c8c8ff")
define friend = Character('Ami')

label start:

    play sound newsbroadcast
    scene black
    pause 2.0

    "I woke up to the blaring sound of the TV. A reporter's voice filtered through the morning haze."
    
    scene tv

    reporter "\"...a hydroelectric dam on the nearby river could bring significant changes to the community...\""

    stop sound
    "I rubbed my eyes and sat up, trying to shake off the remnants of sleep."

    "The reporter's words hung in the air. This dam was a big deal."

    play sound vibratingphone

    "My phone buzzed on the nightstand. It was a message from a friend about the proposal."
    
    play music intersteller

    "I knew I had to get more details. This was just the beginning."
    
    "With the TV still on, I quickly got ready to head out and start my investigation."

    menu:
        "Visit the river":
            jump river
        
        "Reasearch online":
            jump lab 

    
    # Inset label and mini game here    


    label river:
    scene unariver
    with fade
    pause 2.0
    play sound coldwind

    "It’s so peaceful here... Like I’m in a different world, far away from all the chaos, from the never-ending noise of the city."
    
    "I’ve missed this place... The river never changes. It’s the one place that stays still, no matter how fast everything else spins around me."
    
    friend "I knew it... I knew you’d be here. You always come to this spot when something’s weighing on your heart, don’t you?"

    scene trees 
    with dissolve
    show ami 

    me "Yeah... You know me too well."

    me "It’s just... everything’s changing so fast, Ami. This place... it’s the only thing that still feels right. I don’t know what I’ll do if it’s gone."

    me "I need to understand... is it for the greater good, or are we just sacrificing something precious?"

    friend "I get it... It’s hard to imagine losing this place. It means so much to both of us."

    friend "But we also have to think about the bigger picture. If the dam could bring power and jobs to the community, it might help a lot of people. But that doesn’t mean it’s easy to accept... or that we should lose this spot without a fight."

    friend "I think we need to gather more information, talk to others, and see what’s really at stake. We can’t just let this happen without knowing all the facts."

    me "So let’s figure this out together. We’ll talk to people, gather information, and see what options we have. I won’t let this happen without a fight."

    label lab:
    scene lab

    "After a short while, we enter the laboratory, filled with the hum of equipment 
    and the scent of rich soil samples."

    me "Hey..."

    show environmentalist_1 at Position(xpos=0.7, ypos=0.99)
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    me "Ummm... Will you..."

    me "Will you help me explore the benefits of building a new hydro-electric dam?"
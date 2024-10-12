define me = Character('Me', color="#c8c8ff")
define reporter = Character('Reporter', color="#c8c8ff")
define s = Character('Dr. Evelyn Reed', color="#c8ffc8")
define first_nation = Character('Nodin', color="#c8c8ff")
define politician = Character('Politican NPC', color="#c8c8ff")

label start:

    play sound newsbroadcast
    scene black
    pause 2.0

    "I woke up to the muffled sound of the TV. A reporter's voice filtered through the morning haze."
    
    scene tv

    reporter "\"...a hydroelectric dam on the nearby lake could bring significant changes to the community...\""

    stop sound
    "I rubbed my eyes and sat up, trying to shake off the remnants of sleep."

    "The reporter's words hung in the air. This dam was a big deal."

    play sound vibratingphone

    "My phone buzzed on the nightstand. It was a message from a friend about the proposal."
    
    play music intersteller

    "I knew I had to get more details. This was just the beginning."
    
    "With the TV still on, I quickly got ready to head out and start my investigation."

    menu:
        "Visit the Lake":
            jump lab
        
        "Reasearch online":
            jump lab 

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
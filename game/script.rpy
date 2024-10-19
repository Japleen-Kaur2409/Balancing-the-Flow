define me = Character('Me', color="#c8c8ff")
define reporter = Character('Reporter', color="#c8c8ff")
define s = Character('Dr. Evelyn Reed', color="#c8ffc8")
define first_nation = Character('Community Member', color="#c8c8ff")
define elder = Character('Elder', color="#c8c8ff")
define politician = Character('Politican NPC', color="#c8c8ff")
define ami = Character('Ami')

label start:

    play sound newsbroadcast
    scene black
    pause 2.0

    "I woke up to the blaring sound of the TV. A reporter's voice filtered through the morning haze."
    
    scene tv

    reporter "\"...a hydroelectric dam on the nearby river could bring significant changes to the community...\""

    stop sound

    play music intersteller

    "I rubbed my eyes and sat up, trying to shake off the remnants of sleep."

    "The reporter's words hung in the air. This dam was a big deal, that is a beautiful river."

    scene livingroom 
    with dissolve

    show ami
    with dissolve

    show key at Position(xpos=0.1, ypos=0.69)
    with dissolve 

    ami "I can't believe they're going through with the dam. Remember all those times we went canoeing at the river, hanging out with friends?"

    me "I love that place! Canoeing, swimming... I even go there alone sometimes just to think and clear my mind."

    ami "You have a significant role at town hall. I heard on TV earlier that a vote is coming up about the dam's construction. You could really make a difference."

    me "But I don't know enough about dams to have a solid opinion on whether they should be built."

    ami "The First Nations communities are protesting this project. Their reserve is just on the other side of the river. Why not talk to some of them? It could give you a clearer understanding."

    me "I really care about this river. It's crucial for me to find out whether this dam should be built."

    ami "Alright, I have to go now. Bye!"

    hide ami
    with fade

    "I'll head to the First Nation's reserve right now."

    # Open the door. 
    stop music

    show unariver
    with dissolve
    play sound coldwind
    play music naturemusic

    "This is the spot! It's so beautiful here, isn't it?"

    "I've got to hurry and find the First Nations!"

    show reserve
    with dissolve

    "At last, I arrive at the reserve. Sacred cultural symbols, and the smell of cedar and sage fill the air."

    show ami
    with dissolve 

    me "Hey there! I can see your heart's really in this. I'm curious, can you share what this protest stands for and why it means so much to you?"

    elder "We gather here to honor the sacred bond between our people and the land. This protest is our stand against the hydroelectric dam."

    elder "Our ancestors have lived here for thousands of years. This river is our lifeblood. It is not just water; it is our spirit, our heritage."

    elder "These dams are seen as progress by some. But to us, they mean destruction. They drown our lands, erasing our history and our future."

    menu:
        "Powering our communities with diesel fuel can cause even more harm.":
            jump elderresponse1
        
        "The land sustains us, and in return, we safeguard it. Destroying these lands for energy disregards our way of life and our right to preserve our culture.":
            jump elderresponse1

    label elderresponse1:

    elder "We lose more than land; we lose our identity. The spirits of our ancestors cry out as their resting places are submerged."
    
    elder "We lose our hunting grounds for fish and deer, our source of food and income. The floods destroy vegetation, stripping the land of its natural resources."

    menu:
        "While there are other places where you can fish and hunt, the increasing energy demands of our communities necessitate the construction of more dams to foster economic prosperity.":
            elder "Leave here at once!"
       
        "You're right, with the current global crisis the fish population is already diminishing significantly, forests are getting torn apart for corporate profits, the ocean is polluted with plastic and most importantly, a hydro electric dam is going perpetuate environmental degradation.":
            elder "Exactly, we need to stop this dam from killing our identity."
            me "Thank you for speaking with me, bye now."

    show reservehome 
    with dissolve

    show politician at Position(xpos=0.6)
    with dissolve

    first_nation "I heard you were talking to our community Elder."

    me "Yea."

    first_nation "We seek a balance, a way to harness energy without destroying what makes us who we are. Respect for the land is respect for life itself."

    first_nation "Building this hydroelectric dam will create jobs for our people and provide contracts to First Nation developers. We can boost our economy and strengthen our community"

    me "we must also consider the severity of the problems with our ecosystems. They are being destroyed, not just by reckless diesel power use but by interference with nature and the mindset that humans are more important than non-human living things."

    first_nation "Exactly. The dam provides a cleaner, more sustainable energy source. It will reduce our reliance on diesel, and with it, the environmental risks. It's a step forward for our community."

    me "But we also need to consider the long-term impacts on our land and culture. This is more than just a project; it's our way of life at stake."

    first_nation "That is true, which is why we need a solution that respects both our heritage and our future. The dam is a chance to bridge that gap, if we manage it right."

    me "Let's ensure any development plan honors our traditions and safeguards our environment. We need to find a balance where progress doesn't come at the expense of our identity."

    first_nation "Agreed. It's a delicate balance, but it's one we have to strive for—together."

    menu: 
        "Well thank you for letting me know, it seems like building a dam could really benefit the first nation community.":
            first_nation "I am glad you agree with me, even tho some of the others of the community do not."
        
        "Yeah, but you're not considering the severity of the problem with our eco systems, they are being destroyed, not just because of the reckless use of diesel power but by the interference with nature and the mindset that we are more important than these non human living things.":
            first_nation "I AM TO THINKING ABOUT THE ENVIRONMENT!"

    hide politician

    "I should go speak with an environmentalist now, they should help me understand more about the dam."

    show unariver
    with dissolve

    "I should gather my thought, that was alot of information, I have not yet decided on what to vote for."

    "This place is just magnificinet."

    "I should go to see the environmentalist now."

    scene lab

    "After a short while, we enter the laboratory, filled with the hum of equipment 
    and the scent of rich soil samples."

    me "Hey..."

    show environmentalist_1 at Position(xpos=0.7, ypos=0.99)
    with dissolve

    "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    "I'll ask her...!"

    me "Ummm...  Will you..."

    me "Will you help me explore the benefits of building a new hydro-electric dam?"






    




 















    # play sound vibratingphone

    # "My phone buzzed on the nightstand. It was a message from a friend about the proposal."
    
    # play music intersteller

    # "I knew I had to get more details. This was just the beginning."
    
    # "With the TV still on, I quickly got ready to head out and start my investigation."

    # menu:
    #     "Visit the river":
    #         jump river
        
    #     "Reasearch online":
    #         jump lab 

    
    # Inset label and mini game here    


    # label river:
    # scene unariver
    # with fade
    # pause 2.0
    # play sound coldwind

    # "It's so peaceful here... Like I'm in a different world, far away from all the chaos, from the never-ending noise of the city."
    
    # "I've missed this place... The river never changes. It's the one place that stays still, no matter how fast everything else spins around me."
    
    # friend "I knew it... I knew you'd be here. You always come to this spot when something's weighing on your heart, don't you?"

    # scene trees 
    # with dissolve
    # show ami 

    # me "Yeah... You know me too well."

    # me "It's just... everything's changing so fast, Ami. This place... it's the only thing that still feels right. I don't know what I'll do if it's gone."

    # me "I need to understand... is it for the greater good, or are we just sacrificing something precious?"

    # friend "I get it... It's hard to imagine losing this place. It means so much to both of us."

    # friend "But we also have to think about the bigger picture. If the dam could bring power and jobs to the community, it might help a lot of people. But that doesn't mean it's easy to accept... or that we should lose this spot without a fight."

    # friend "I think we need to gather more information, talk to others, and see what's really at stake. We can't just let this happen without knowing all the facts."

    # me "So let's figure this out together. We'll talk to people, gather information, and see what options we have. I won't let this happen without a fight."


    # menu:
    #     "Visit the First Nation Community":
    #         jump first_nation_community
    #     "Visit the Lab":
    #         jump lab
    #     "Visit the Politican":
    #         jump politician
    
    # label first_nation_community:
    
    

    # label lab:
    # scene lab

    # "After a short while, we enter the laboratory, filled with the hum of equipment 
    # and the scent of rich soil samples."

    # me "Hey..."

    # show environmentalist_1 at Position(xpos=0.7, ypos=0.99)
    # with dissolve

    # "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

    # "I'll ask her...!"

    # me "Ummm...  Will you..."

    # me "Will you help me explore the benefits of building a new hydro-electric dam?"


    # label politician:


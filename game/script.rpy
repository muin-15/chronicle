define e = Character("Hikari")
define m = Character("Taiju")
define r = Character("Daifuko")
define t = Character("Teacher")
define s = Character("Shiba")
define n = Character(None)
define y = Character("Yagamishi")

define Duo_main =Character("Taiju & Hikari")
image street="images/Scenes/Backstreet_Spring_Day.png"

image street2="images/Scenes/Street_Autumn_Day.png"

image shrine ="images/Scenes/Temple_Spring_Day.png"

image inside_shrine = "images/Scenes/Old_TempleDay.png"

image schoolgate = "images/Scenes/11.png"

image staffroom ="images/Scenes/staffroom.png"

image mask = "images/accessories/mask.png"

image hallway ="images/scenes/03.png"

image sportsroom ="images/Scenes/sportsroom.png"

image book = "images/greenbook.png"

default ans1=False
default evidence=0

default solve_case=False
label start:

    play music "bg_hiphop.mp3" volume 0.25 fadein 4.0

    scene black with fade

    n "March 31st"

    n "The last day of school"

    n "Those Three years were the best years of life"

    scene street with fade

    show Hikari school bangs_normal sclera_norm eyes_Sorrow brows_angry iris_large mouth_angry at left with move

    e "You are late!!!."

    e "Atleast you could have came early for the graduation ceremony"

    show Taiju school bangs_normal eyes_Sorrow brows_angry iris_large mouth_Open at right with move

    m "Common, I'm in time."

    show Hikari school bangs_normal sclera_norm eyes_Spread brows_norm iris_medium mouth_Grin at left

    e "Anyways"

    e "I'm Excited"

    show Taiju school bangs_normal sclera_norm eyes_Spread brows_norm iris_medium mouth_Grin at right

    m "me too"

    show Taiju at right

    e "The day to end as a child and become an Adult."

    m "I'm gonna miss this days"

    e "Yaa "

    m "I'm Excited too.."

    hide Taiju
    hide Hikari 
    with Dissolve(1.5)

    n "both walks over the street upto school."

    n "footsteps arroaching......"

    show Hikari mouth_Open at left

    e "Look who is here"

    hide Hikari with Dissolve(0.5)

    show Shiba at left
    show Daifuko iris_medium mouth_Uninterested at right 
    with move

    r "Nerds..."

    hide Hikari

    show Shiba mouth_angry at left with dissolve

    s "Shut Up!"

    r "hoiiiii"

    show Shiba mouth_Open at left
    s "You are late we have been waiting for you"
    show Shiba at left

    hide Daifuko

    show Taiju mouth_Open at right with dissolve

    m "For us ?"

    m "Why ?"

    show Taiju at right

    s "It's not like i wanted to be with you,sensei told me to bring you two with me."

    menu:
        "Go with Shiba":
            $ ans1=True

            m "Ok we will come with you."

        "Don't go with Shiba":
            
            m "We will not come."

            s "Please come its urgent{p}I can't tell you why but its important."

            m "Fine{p}Let's go Hikari."

    call gathering_at_shrine

    call inSchool
    if evidence == 2 or evidence == 3:
        call end

    return

label gathering_at_shrine:

    hide Taiju 
    hide Shiba 
    with Dissolve(1.0)

    scene street2 with fade

    n "All of them started walking"

    n "\"Hikari Stops at the corner\""

    show Hikari mouth_angry at left with dissolve

    e "Isn't the School is the other way."

    show Hikari mouth_normal

    show Shiba mouth_Open at right with dissolve

    s "Come with Us.{p}Sensei asked us to bring you two to the shrine."

    show Hikari mouth_Uninterested

    e "Seems like we don't have other option."

    hide Shiba
    hide Hikari
    with Dissolve(0.2)

    scene shrine with fade

    show Shiba

    s "We are here. Sensei !!!"

    hide Shiba

    show Teacher mouth_Uninterested at center with dissolve

    t "It looks like everyone is here."

    show Teacher mouth_Open at center

    t "Shiba you did good.{p}Let me talk to these two in private."

    hide Teacher with Dissolve(0.2)

    s "We will get going to school."

    n "Shiba and Daifuko Leaves the Shrine"

    show Hikari mouth_scared at left
    show Taiju mouth_scared at right
    with dissolve

    m "Sensei whats the matter{p}Why did you called us suddenlly{p}We didn't did anything wrong!"
    e "We were just getting to school for the Graduation Ceremony."

    hide Hikari
    hide Taiju
    show Teacher at center
    t "You didn't did anything wrong{p}Theres a specific problem I need to discuss with you."
    hide Teacher
    show Taiju mouth_Open at right

    m "Us{p}but Why?"

    t "You will get it soon{p}come with me."

    n "All of them walk inside the shrine."

    hide Taiju

    call In_Shrine

    scene street2 with fade

    show Taiju at left
    show Hikari at right
    with dissolve

    e "Where should we start from?"

    m "The awards and aritifacts were been kept at the responsible teacher's desk.{p}So I guess we should first check out for staff room for evidences."

    e "Nice Idea."

    hide Hikari
    hide Taiju
    with Dissolve(0.2)

    n "Going to school"

    return


label In_Shrine:

    scene inside_shrine with fade

    show Teacher

    t "Now I guess no one can here us"

    Duo_main  "What's the matter Sir"

    show Teacher mouth_scared

    t "Actually{p}As you know today is the Graduation Ceremony{p}And at the end of the Ceremony a student gets the Academic award for its excellence throughout the three years."

    t "Every year one teacher gets in charge of the graduation Ceremony.{p}This year its my turn."
    
    t "but the problem is the Academic award trophy got stolen last night from the school.{p}I don't know what to do?"

    t "From some students I've heard that you were in charge of the Detective club and you've solved some astonishing cases."

    t "So I want you two to Fund it out before it gets too late.{p}It's not an order it's a request."

    hide Teacher
    show Hikari at left
    show Taiju at right
    with dissolve

    menu:
        "help Sensei":

            Duo_main "Sure we will help out."

            t "You have an hour to bring the award."


        "Don't Help Sensei":

            m "Why?{p}The school is over and it's not our problem"

            t "I get it.{p}I can't force you."

            e "Stop it Taiju!{p}We will help you out Sir."

            t "Thanks{p}But don't Forget you just have one hour."

            Duo_main "We will do our Best."

    hide Hikari
    hide Taiju with Dissolve(0.5) 
    
    n "Teacher goes to school."

    return
label inSchool:

    scene schoolgate with fade
    show Taiju mouth_scared
    m "10 minutes got away.{p}I guess we need to hurry up."
    hide Taiju with Dissolve(0.5)

    scene staffroom with fade

    show Taiju mouth_Open at left
    show Hikari at right
    with dissolve

    m "Let's takeout a look."

    e "I'll check the other side."

    hide Taiju
    hide Hikari

    m "It seems like they didn't cleaned the staff room since we've joined in."

    e "Yaa its dusty."

    m "I guess I've found something..."

    show Taiju at left
    show Hikari mouth_Open at right

    e "what did you get?"

    show Hikari mouth_normal
    show Taiju mouth_Open

    m "A Rat trap."
    show Hikari mouth_angry brows_angry

    e "Taiju Are you kidding,We don't have time!"

    show Taiju mouth_laugh
    m "Sorry Sorry Just kidding."

    e "Be serious.{p}We don't have time."

    show Taiju  mouth_Open

    m "Okay."

    show Hikari mouth_normal

    e "I guess there is nothing here let's try to find a clue somewhere else."

    menu:
        "leave Staff room":
            e "Let's search it in Sports room.{p}"

            hide Hikari
            hide Taiju
            call sportsroom
            call library
        "Stay for some time":
            hide Hikari
            hide Taiju
            e "Just 5 more minutes!!"

            m "okay"

            n "After sometime"

            show Taiju mouth_Open at left
            show Hikari at right
            m "I guess I got something."
            show Hikari mouth_Open
            e "What's it?"
            show mask
            show Taiju mouth_Open
            m "It's a mask."
            show Hikari mouth_Open
            e "Mask?"
            m "I don't know what it is doing here.{p}But I guess we need to check out for Drama club."

            e "Yaa we could find something there."

            hide Taiju
            hide Hikari
            with Dissolve(0.5)
            $ evidence+=1
            
            call dramaclub

        
    return
label sportsroom:
    scene sportsroom with fade
    show Yamagishi mouth_Open 
    y "Hello{p}Why are you here?{p}The graduation Ceremony is in 30 minutes."
    hide Yamagishi
    show Yamagishi mouth_scared at left
    show Taiju at right
    m "We will catch up with you later."
    y "First that yellow haired boy and now you both are confusing me."
    m "Yellow haired boy? Who are you talking about?"
    y "It's someone from our class I didn't remember his name."
    m "Why was he here?"
    y "I don't know,he had some package in his hands."
    m "package!?"
    y "Something Like an award."
    e "This is lot of evidence ,let'search for the yellow haired guy."
    m "Yaa{p}Thanks Yagamishi."
    y "No problem.{p}But what's the issue?"
    m "We will tell you later."
    hide Taiju
    hide Yamagishi
    scene hallway with fade
    show Hikari
    e "There are many people with yellow hairs in our class."
    m "Yaa"
    hide Hikari
    show Daifuko
    r "Nerds"
    hide Daifuko
    show Hikari mouth_Open at right
    show Taiju at left
    e "He have yellow hairs."
    show Taiju mouth_Open
    m "Yaa he could be one."
    e "He have something in his hands"
    hide Hikari
    hide Taiju
    r "What do you want?{p}I'm late{p}I need to give this frame to Sensei in the Auditorium."
    m "Its not an award it's a frame."
    n "Keeps frame away."
    hide Taiju
    hide Hikari
    show Daifuko with dissolve
    r "Do you two need something?"
    Duo_main "No{p}You can do your Job."
    r "Weird"
    n "Daifuko leaves."
    hide Daifuko
    show Taiju at left
    show Hikari at right
    e "We are back to zero and we don't have much time."
    m "I don't know what to do?{p}but we can't just sit."
    hide Taiju
    hide Hikari
    n "Both Wanders through the hallway."
    show Taiju at left
    show Hikari at right
    e "Taiju come here."
    m "What is it?"
    e "I found a book behind the door of chemistry class."
    m "Where is it?"
    e "Here,look!!"
    show book
    hide Taiju
    hide Hikari
    n "Hikari opened the book"
    e "It's a diary."
    n "Hikari reads the book."
    e "On 30th march - I got up my dream,the Academic award."
    show Taiju sclera_Surprised eyes_Surprised iris_large mouth_happy
    m "That's what we want!"
    hide Taiju
    show Taiju
    m "Check for the Name."
    e "It doesn't have any name."
    m "We are this much close."
    e "Let's give this to Sensei and ask if they know anything about it."
    scene black with fade
    scene classroom with fade
    show Teacher
    t "Did you got anything?"
    hide Teacher with Dissolve(0.2)
    show Taiju
    m "Sir we got this."
    hide Taiju
    show Teacher
    t "Diary?"
    hide Teacher with Dissolve(0.2)
    show Hikari
    e "It has written that someone stole the Award on 30th of march."
    hide Hikari
    show Teacher sclera_Surprised eyes_Surprised iris_large mouth_happy
    t "What??"
    hide Teacher
    show Taiju mouth_scared
    m "But there is not any name on the diary still"
    hide Taiju
    show Teacher mouth_Open
    t "But we still have a chance ,I'll make a false annoucement the culprit will show unexpected expression."
    Duo_main "We will gather everyone."
    t "hurry up we don't have much time."
    hide Teacher
    n "Hikari and Taiju gather up the students."
    n "15 minutes to the Graduation Ceremony."
    show Teacher mouth_Open
    t "Students Listen up to me!{p}Some students found a lost diary in school.If someones diary is missing please contact me."
    hide Teacher
    show Hikari at left 
    show Taiju at right
    e "Do you got anything suspicious?"
    m "I don't think so."
    t "Did you got anything?"
    Duo_main "We don't think so"
    show Taiju mouth_scared
    m "what now sensei?"
    hide Taiju
    hide Hikari
    show Teacher mouth_scared
    t "I don't think we could do anything now.{p}I guess I'll be expelled now."
    hide Teacher
    n "Teacher leaves the classroom."
    show Taiju
    m "I guess we should do something or sensei would be expelled."
    hide Taiju
    show Hikari
    e "You are right."
    e "But what can we do?"
    e "I didn't told you one thing earlier the diary had a school badge on it just like the library books."
    hide Hikari
    show Taiju
    m "Let's get to library.we could definitly get something there."
    hide Taiju
    show Hikari
    e "You are right"
    hide Hikari
    $ evidence+=1

return

label dramaclub:
    scene dramaclub with fade
    n "Drama Club"
    $ evidence+=1
return


label library:
    scene library with fade
    show Taiju at left
    show Hikari at right
    with dissolve
    
    m "let's checkout the registered books."
    $ renpy.pause(2.0,hard=True)
    e "Look the same diary is here."
    show Taiju mouth_Open
    m "Here the name is Kakashi."
    e "Isn't kakashi is the second name of our sports teacher."
    m "Look there are more here."
    m "Like 20 diaries."
    e "Let's check up all of them."
    hide Taiju
    scene black with fade
    scene library with fade
    show Taiju mouth_Open at left 
    show Hikari at right
    m "So among 22 teachers we have got diaries for 21 teachers."
    show Hikari mouth_Open
    e "So we have got the culprit."
    m "Yes."
    hide Taiju
    hide Hikari
    $ evidence +=1

return

label end:
    scene auditorium
    n "The Graduation Ceremony Begins."
    n "Principal's speech starts."
    show Taiju at left
    show Hikari at right
    with dissolve
    m "Hikari look sensei's face got pale."
    e "Let's get the culprit and make him pay for everything he did."
    m "Wait sensei is coming our way."
    hide Hikari
    hide Taiju
    show Teacher mouth_scared brows_sad
    t "I guess I'm gonna get insulted in front of everyone and expelled from the school."
    hide Teacher
    show Taiju mouth_Open at left
    show Teacher at right
    m "Don't worry sensei I guess we have found the culprit."
    hide Taiju
    show Teacher mouth_happy
    t "Really! who is it?{p}I'll suspend him right now."
    hide Teacher
    menu:
        "Teacher":
            n "Sensei is innocent"
            jump TragicEnd
        "Daifuko":
            if evidence == 2:
                n "The culprit is Daifuko"
            else:
                jump TragicEnd
        "Yagamishi":
            if evidence == 3:
                n "The culprit is Yagamishi"
            else:
                jump TragicEnd
        "Shiba":
            n "Shiba is innocent"
            jump TragicEnd
            
    if evidence == 2 or evidence ==3:
        m "The clues we got are:"
        show Taiju mouth_Open
        if evidence==2:
            m "1.Daifuko was in sports room before the ceremony, stated by Yagamishi."
            m "2.When you were in class he was taking some frame like thing to Ground floor,and he was saying that sensei asked me to bring it out."
            m "3.When we found out the diary,Daifuko was there, before sometime."
            m "4.He knew Sensei will assign us the job to get the culprit so he came up to pick up us today with shiba knowing shiba is your favourite student.Having minimal risk."
            m "5.He knew that we are trying to get the culprit so distract us from him he stoled the diary and teared up the first page of it and put it on purpose at back of chemistry class's door."
            m "So I think Daifuko is the culprit behind this."
            hide Taiju
            show Teacher mouth_Open
            t "I didn't ask him to bring anything found.That's great."
            show Teacher mouth_laugh
            t "You guys gonna have a treat after the ceremony."
            Duo_main "Yaay! Thanks."
            hide Teacher
            scene black with fade
            n "Daifuko get caught"
            n "He said he did this because sensei didn't gave high score in the Finals."

        else:
            m "1.What he was doing in the sports room in sports uniform before the Graduation Ceremony."
        jump Graduation_Ceremony
return

label Graduation_Ceremony:
    scene auditorium
    n "Princpal : And know the movement everyone is waiting for - The Academic award.The Academic award is used to given to some other student based on it's studies but now it is used to be given to an unexpecited student."
    n "Taiju Karuma"
    n "Applause from the crowd"
    show Taiju mouth_laugh
    m "Me but how"
    hide Taiju
    n "It's was suggested on a special request from the whole staff."
    n "taiju gets up on the stage"
    n "Principal whispers in ear : You saved the reputation of our school."
    n "Everyone celebrates the graduation ceremony."
    n "Students got emotional and started to wish good luck to each other for future carrier."
    n "Graduation Ceremony Ends."
    n "Daifuko got problems dealing with the teacher for getting a good college."
    scene black with fade
return
label TragicEnd:
    scene black with fade
    n "You messed up!!!"
    show Teacher mouth_scared brows_sad eyes_Spread sclera_Spread iris_small
    n "Sensei got fired!!!"
return
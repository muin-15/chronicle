define e = Character("Hikari")
define m = Character("Taiju")
define r = Character("Daifuko")
define t = Character("Teacher")
define s = Character("Shiba")
define n = Character(None)
image street="images/Scenes/Backstreet_Spring_Day.png"
image street2="images/Scenes/Street_Autumn_Day.png"

image shrine ="images/Scenes/Temple_Spring_Day.png"

label start:

    play music "bg_hiphop.mp3" volume 0.25 fadein 4.0

    scene black

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

    s "It's not like i wanted to be with you,sensei told me to bring you two with me"

    hide Taiju 
    hide Shiba 
    with Dissolve(1.0)

    scene street2

    n "\"Hikari Stops at the corner\""

    show Hikari mouth_angry at left with dissolve

    e "The School is the other way"

    show Hikari mouth_normal

    show Shiba mouth_Open at right with dissolve

    s "Come with Us.{p}Sensei asked us to bring you to the shrine"

    hide Shiba
    hide Hikari
    with Dissolve(0.2)

    scene shrine with fade

    show Shiba

    s "We are here"

    hide Shiba

    show Teacher mouth_Uninterested at center with dissolve

    t "It looks like everyone is here"

    return

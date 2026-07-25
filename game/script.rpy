define e = Character("Hikari")
define m = Character("Taiju")
define r = Character("Daifuko")
image street="images/Scenes/Backstreet_Spring_Day.png"
label start:

    play music "bg_hiphop.mp3" volume 0.25 fadein 4.0
    scene street with fade

    show Hikari school bangs_normal sclera_norm eyes_Sorrow brows_angry iris_large mouth_angry

    e "You are late!!!."

    e "Atleast you could have came early for the exam."

    show Hikari school bangs_normal sclera_Surprised eyes_Sorrow brows_norm iris_small mouth_normal

    e "Common..."

    e "Didn't you forgot about the exams."

    hide Hikari

    show Taiju school bangs_normal sclera_Spread eyes_Spread brows_angry iris_large mouth_Open

    m "I'm not fool"

    hide Taiju

    show Hikari school bangs_normal sclera_norm eyes_Spread brows_norm iris_medium mouth_Grin

    e "Anyways"

    e "The day to end as a child and become an Adult."

    e "The Last Exam."

    hide Hikari

    show Taiju school bangs_normal sclera_norm eyes_Spread brows_norm iris_medium mouth_Grin

    m "I'm Excited too.."

    hide Taiju

    "both walks over the street upto school."

    "footsteps arroaching......"

    e "Look who is here"

    show Daifuko mouth_Uninterested

    r "Nerds..."
    return
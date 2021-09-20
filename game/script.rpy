# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define miku = Character("miku")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg kyoto
    play music "audio/miku ost.mp3"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    image miku meet = Image("miku meet.png", xalign=0.5, yalign=0.02) 
    show miku meet
    with dissolve
    # These display lines of dialogue.

    miku "Selamat Pagi"
    
    miku "Kamu siapa ya?"

    miku "Sepertinya kamu bukan asal sini deh "
    
    "Bilek""Ehhh!!!!!"
    "Bilek""(Anjir ni cewek mantap battt dah, duh kok gw sange ya anjirr lah)/Boy berhanlah"
    
    "Bilek""Namaku hmmm ano hmmm aduh, kamu bisa memanggilku bilek aja, salam kenal, namamu siapa ya? :)"
    
    "Bilek""Kamu cantik deh"
    
    image miku shy:
        "miku shy.png"
        zoom 2
        xalign -5.0
    
    show miku shy
    miku "."
    miku ".."
    miku "..."
    
    # image miku shy  = im.FactorScale("miku shy.png",1.5)
    # show miku shy at right
    # with dissolve
    
    # miku "."
    # image miku shy:
    #     "miku shy.png"
    #     zoom 2
    #     xalign -5.0
    # show miku shy
    # miku ".."
    # image miku shy:
    #     "miku shy.png"
    #     zoom 3
    #     xalign 5.0
    # show miku shy
    

    # This ends the game.

    return

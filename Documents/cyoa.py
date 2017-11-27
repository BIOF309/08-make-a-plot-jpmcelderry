print("You wake up in an unfamiliar room. You can't remember what happened last night, or why you ended up where you are now")
input("--ENTER--")
print("You look around and see that the room is medium sized. Big enough for you to walk around in but by no stretch a master bedroom.")
print("You're laying on a small bed with a steel frame. The bed has sheets but no blankets. Though an overhead light hangs nearby, the only light comes from the crack underneath the only door in the room.")
print("As you look around the room you discover that the walls are a pristine white, and the room itself is impeccably neat.")
print("Though the room betrays nothing sinister to the eyes, you feel a sense of unease about the uncertainty of your position. Where are you, and why?")
print("As you look around you also see a small closet, a wooden chest of drawers, and a large piece of plywood nailed to the wall.")

lockpick=False
WD40=False
hammer=False

while True :
    print("What would you like to do")
    print("1:investigate door")
    print("2:investigate closet")
    print("3:investigate chest of drawers")
    print("4:investigate plywood")
    print("5:investigate lamp")
    print("6:quit game")
    answer=str(input())

    if ("1" or "door") in answer.lower():
        if lockpick == False :
            print("You walk over to the door and attempt to turn the knob but it won't budge. It must be locked. Looking under the door, you see the walls of a hallway outside and a couple other doors, all closed.")
            print("The door is sturdy, really sturdy. You took firefighting 101 in college, but you can tell that this door wouldn't break if you tried.")
            input("--ENTER--")
            continue
        elif lockpick == True :
            print("You take the makeshift lockpick to the door, but you're surprised to find the door is actually unlocked, despite the fact that you can't turn the doorknob.")
            if WD40 == True :
                    print("You use the WD-40 on the doorknob, and now when you turn it the knob turns freely!")
                    input("--ENTER--")
                    break


    elif ("2" or "closet") in answer.lower():
        while True:
            print("You open the closet and find no clothes hanging but a few wire coat hangers. There is a shelf in the closet.")
            print("What would you like to do?")
            print("1:investigate shelf")
            print("2:investigate coat hangers")
            print("3:investigate walls of closet")
            print("4:leave closet")
            closet_answer=str(input())
            if ("1" or "shelf") in closet_answer.lower() :
                print("You check the shelf and find a hammer!")
                hammer=True
                input("--ENTER--")
                continue
            elif ("2" or "hangers") in closet_answer.lower() :
                print("You remember what you learned in your locksmith 101 class in college and fashion a lockpick from the wire hanger!")
                lockpick=True
                input("--ENTER--")
                continue
            elif ("3" or "walls") in closet_answer.lower() :
                print("Investigating the walls shows nothing out of the ordinary, no hidden panels.")
                input("--ENTER--")
                continue
            elif ("4" or "leave") in closet_answer.lower() :
                break

    elif ("3" or "chest" or "drawers" or "wardrobe") in answer.lower() :
        while True:
            print("You check the drawers of the wardrobe but they're all empty.")
            print("1:Look around some more")
            print("2:Leave")
            wardrobe_answer=str(input())
            if ("1" or "look") in wardrobe_answer.lower():
                print("You look around and pull out the drawers of the chest. Behind one of the drawers you see a rat! It's standing on its haunches and looks dangerous.")
                print("1:Attack rat")
                print("2:Put drawers back")
                rat_answer=str(input())
                if ("1" or "attack" or "rat") in rat_answer.lower() :
                    print("You go to attack the rat and find it's actually a can of WD-40! You knew you should have seen the optometrist...")
                    WD40 = True
                    input("--ENTER--")
                if ("2" or "drawers" or "back") in rat_answer.lower() :
                    print("You replace the drawers and breathe a sigh of relief as the rat stays put.")
                    input("--ENTER--")
                continue
            if ("2" or "leave") in wardrobe_answer.lower():
                break
        continue

    elif ("4" or "plywood") in answer.lower() :
        while True :
            print("You investigate the plywood. The plywood is nailed to the wall by many nails, neatly nailed around the edges of the panel.")
            print("There is a faint whistling sound on the other side of the plywood. Maybe it's an exit.")
            print("1:Investigate nails")
            print("2:Kick and break plywood")
            print("3:Leave window")
            plywood_answer=str(input())
            if ("1" or "nails") in plywood_answer.lower() :
                if hammer==True :
                    print("You carefully pry the nails off of the plywood with the reverse side of the hammer. Doing so reveals a window to the outside!")
                    print("Said window has a small break in it at the corner. Looking out it seems as though you are in the woods. You're on the second story of a house, and there's a large bush with thorns underneath the window.")
                    print("1:Open the window and jump.")
                    print("2:Leave the window as is. And put the plywood back up, it's cold outside.")
                    window_answer=str(input())
                    if ("1" or "jump" or "open") in window_answer.lower():
                        print("You jump out the window, but unfortunately you land strangely and break your leg.")
                        print("Hurting all over, you see your friend run out of the house from which you jumped. He rushes you to the hospital.")
                        print("Turns out you had crashed at your friend's house after a heavy night of drinking the night before. The door and the plywood over the window were simply because your friend's guest room had fallen into disrepair. You now have a huge medical bill to pay off. That sucks.")
                        input("-The End-")
                        break
                    elif ("2" or "leave" or "plywood" or "close") in window_answer.lower():
                         break
                if hammer==False :
                    print("There's nothing weird about the nails, but they're big. They're never gonna budge by hand.")
                    input("--ENTER--")
                    continue
            elif ("2" or "kick" or "break") in plywood_answer.lower() :
                print("Using the knowledge from your firefighting 101 class in college you kick and break the plywood.")
                print("Unfortunately, that's not the only thing you break. You skipped a couple classes and it cost you. Your leg is now broken from kicking incorrectly.")
                print("Even worse, there was a window behind the plywood. Kicking it broke the window and cut your leg very badly. Feeling desperate, you jump out the window, but fall in a big bush of thorns.")
                print("Hurting all over, you see your friend run out of the house from which you jumped. He rushes you to the hospital, but from the fall and your injuries the doctors have to amputate your leg.")
                print("Turns out you had crashed at your friend's house after a heavy night of drinking the night before. The door and the plywood over the window were simply because your friend's guest room had fallen into disrepair. And now you have one leg. Sad.")
                input("-The End-")
                break
            elif ("3" or "leave") in plywood_answer.lower() :
                break
            continue

    elif("5" or "lamp") in answer.lower() :
        print("You look around the lamp but there's nothing suspicious about it. There's a light switch on the wall, but flipping it does nothing.")
        input("--ENTER--")
        continue

    elif("6" or "quit") in answer.lower() :
        break

if ("6" or "quit") in answer.lower() :
    pass
else:
    print("You walk out the door and follow the hallway. You find you're in a well lit house that looks nothing like the room from which you came.")
    print("You cautiously walk down the stairs and find your friend in the kitchen cooking breakfast. Turns out the two of your had gone out drinking the night before and you had crashed at his house.")
    print("He's rather ashamed when acknowledging the state of the guest room in which you awoke. The window is broken, hence the plywood. The doorknob is old and kind of hard to turn, and the lamp in your room must have gone out recently.")
    print("Regardless, you thank your friend and enjoy breakfast. Afterward he gives you a lift home. Life is good :)")
    input("-The End-")

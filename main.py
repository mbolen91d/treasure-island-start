print('''

                        ._
                          |~
                        uuuuu
                        |_#-|
                        | _#|
                        |_ -|
   ________ .$$. ______ | - | _____________
           .#$$$. __    |-  | ....__
     _.--' $$$$$$    ` -[__N]        `--a:f-
           $$$$$$    -.
      -.    `:/'    _.))        .--.
             ||   .'.-'     _..-.. _.-.
      ._.-.  '"  /  (     .'      `.
    -'     `.   .    `. -'
             `. .      `--..
                 `.
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print("You find yourself standing at a crossroads with a choice.  Left or Right? You can not see anything in either direction, but your intuition says something good lies this way.  Which way is it? ")
left_or_right = input('''Left or Right? ''')
left_or_right.lower()
if left_or_right == "left" :
  print("After days of walking you come to a shore with a dock, but nothing in sight.  Do you wait for a boat to return or attempt to swim?")
  swim_or_wait = input('Choose "swim" or "wait". ')
  swim_or_wait.lower()
  if swim_or_wait == "wait":
    print('''As the sun sets, you see a ship appear on the horizon. When the ship arrives the ship's captian greets you like an old friend.  He invites you aboard and you set sail to shores unkown.  When you awake the next morning you find yourself in a distant land with scenery that you have never seen before, but feels like home.  Off in the distance you see a grand tower and start walking to it. Along the way you encounter a young child who aks for your help.  Do you help the child or continue on your quest?''')
    help_or_continue = input('''Choose "help" or "continue". ''')
    help_or_continue.lower()
    if help_or_continue == "continue":
      print('''Racked with guilt you continue your journey.  When you arrive at the tower you see a single door with stairs that lead up and stairs that lead down.  Which way do you go? ''')
      climb_or_descend = input('''Up or down? ''')
      climb_or_descend.lower()
      if climb_or_descend == "up":
        print('''As you begin to ascend you feel your pulse quicken and you race faster and faster up the stairs until your sprinting up them.  You finally reach the top of steps and see a golden door.  Winded with your pulse echoing in your ears, you open the door.  Standing before you like some crazy dream is the crossroads.  Panicing you turn to run, but millions of hands spring from the door pulling you in. As you turn to meet your fate, you are struck with the realization that this is not the first time you have been here.  You step out of the door feeling that this time it will be different.  This time you will claim what is rightfully yours.  As you walk towards the crossroads the memories from the last few days begin to fade. You no longer remember how you got here.  Only that you have a choice. Left or Right?''')
      else:
        print('''You travel down in to the descending darkness.  You lose your footing, slip and tumble down the steps.  You think to yourself this is it.  You manage to stick your hand out and grab something rope like, but it's hard to tell in the dark.  You pull yourself up only to feel the rope move.  You panic and try to drop it, but its to late.  The snake bites you injecting you with a deadly poison.  As you slowly fade away you think to yourself; I was so close.  I was sure this would be the time I broke free.''')
    else:
        print('''The boy leads you to a well where he says his puppy fell.  As you peer over the edge, you hear a metallic click.  Your heart stops as you realize what is about to happen.  *BANG* The world begins to fade away as you think, no good deed goes unpunished.''')
  else:
    print('''Feeling strong you set out.  After swimming for awhile you stop to check your surroundings.  All you see is water and storm clouds on the horizon.  Thinking you bit off more than you can chew you turn around.  As you begin to swim back to shore you can feel the water pulling you backwards. You turn to see a massive swell.  You swim harder and harder, but it's no use.  The wave breaks over top of you sending you down to the inky black depths.''')
else:
  print('''You begin walking as the sun climbs higher and higher. You continue for days as the sun continues to get hotter and hotter.  On the 5th day, you see some trees off in the distance. You get excited because you finished the last of your water last night.  Your pace quickens just a little at the prospect of water. As the sun climbs to it highest peak, you collapse. You lift your head to see the trees shimmering in the distance.  No closer than they were when you first spotted them.  A breeze tickles your face. You see the trees sway and then blow away in the dust.  You fade out wondering why you ever went this way.''')





















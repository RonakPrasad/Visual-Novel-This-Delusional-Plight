﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("James",color="#eba134")
define n = Character("[name]",color="#2789e6")
define s = Character("Stella",color="#2de35b")
define r = Character("Ruby",color="#d34fff")
define m = Character("Me",color="#2789e6")
define w = Character("Waiter",color="#2712f4")
define mystery = Character("???",color="#2712f4")

image alpha_control:
    "spotlight.png"

    anchor (.5, .5)

    parallel:
        zoom 0
        linear .5 zoom .75
        pause 2
        linear 1.0 zoom 4.0
        time 4.0
        
    parallel:
        xpos 0.0 ypos .6
        linear 1.5 xpos 1.0
        linear 1.0 xpos .5 ypos .2
        time 7.0
    pause .5
    repeat

define alpha_example = AlphaDissolve("alpha_control", delay=3.5)

$ rubydec

image ilya alekseevanim1:
    "ilya alekseev 1.png" with Dissolve(2.0)
    pause 1.9   
    "ilya alekseev1 (1).png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev6 (1).png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev2 (1).png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev3 (1).png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev4 (1).png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev7 (1).png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev5 (1).png" with Dissolve(2.0)
    pause 1.9
    repeat

image ilya alekseevanim:
    "ilya alekseev.png" with Dissolve(2.0)
    pause 1.9   
    "ilya alekseev1.png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev6.png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev2.png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev3.png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev4.png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev7.png" with Dissolve(2.0)
    pause 1.9
    "ilya alekseev5.png" with Dissolve(2.0)
    pause 1.9
    repeat

    
image the end:
    "Screenshot (575).png"
    pause .11
    "Screenshot (576).png"
    pause .11
    "Screenshot (577).png"
    pause .11
    "Screenshot (578).png"
    pause .11
    repeat

image ruby zoomed:
    zoom 1.2
    "ruby smile1"
    
image arcade anime:
    "Screenshot (442).png"
    pause .11
    "Screenshot (444).png"
    pause .11
    "Screenshot (443).png"
    pause .11
    repeat

image cafe anim:
    "Screenshot (445).png"
    pause .12
    "Screenshot (446).png"
    pause .12
    "Screenshot (447).png"
    pause .12
    repeat

image crowd anim:
    "Screenshot (452).png"
    pause .24
    "Screenshot (453).png"
    pause .24
    "Screenshot (454).png"
    pause .24
    repeat
    
image lady anim:
    zoom 1.1
    xalign .5
    yalign .5
    "Screenshot (460).png"
    pause .15
    "Screenshot (461).png"
    pause .15
    "Screenshot (463).png"
    pause .15
    "Screenshot (470).png"
    pause .15
    "Screenshot (465).png"
    pause .15
    "Screenshot (469).png"
    pause .15
    "Screenshot (464).png"
    pause .15
    "Screenshot (468).png"
    pause .15
    "Screenshot (464).png"
    pause .15
    "Screenshot (467).png"
    pause .15
    "Screenshot (471).png"
    pause .15
    "Screenshot (472).png"
    pause .15
    "Screenshot (471).png"
    pause .15
    "Screenshot (472).png"
    pause .15
    "Screenshot (471).png"
    pause .15
    "Screenshot (461).png"
    pause .15
    "Screenshot (471).png"
    pause .15
    "Screenshot (472).png"
    pause .15
    "Screenshot (471).png"
    pause .15
    "Screenshot (461).png"
    pause .15
    repeat
    
image gasstation anim:
    "Screenshot (484).png"
    pause .15
    "Screenshot (485).png"
    pause .15
    "Screenshot (489).png"
    pause .15
    "Screenshot (486).png"
    pause .15
    repeat
    
# The game starts here.

label start:



scene black
with Dissolve(1.0)

$ name = renpy.input("What would you like to be called in the visual novel? \n (By default you'll be called Sam)")
$ name = name.strip()
   
if name=="":
       $ name = "Sam"

pause 1.0

play sound "alarm clock.mp3" fadeout 1.0 fadein 1.0

stop music fadeout 1.0

"{i}alarm clock rings{/i}"

m ".......... {i}yawns{/i}"

m "Wow! Is it morning already??? \nNo matter how long I sleep it feels like I need more sleep these days."

m "And what was that dream?? I see some weird dreams these days, it's really unusual."

m "Maybe I should stop watching thriller movies......I'm not certain....\nNightcrawler was a good movie though."

m "Well... anyways, I've got to get up now."

play music "music/vntrack04.mp3" fadein 1.0 fadeout 1.0

scene my home
with Dissolve(2.0)
pause 4.0

m "It's holidays and I've gotta meet my friends today. \nWe're gonna go... uh... I don't know where actually. We haven't really decided."

m "They are gonna come to my house first, then we'll go out together. \nI live alone in this rented independent house, I came to this city to complete my secondary education."
   
m "My parents stay at my hometown. They used to come visit me once every semester, \nbut things have changed over the years because now I'm in college. 
   I've got to take my own responsibilities. "   
   
m "Things weren't like this before, I mean I used to be alone most of the time during my holidays."

m "But now I have these friends that I hangout with. It feels good, to be honest.\nOhh... I should get ready... they'll be here in an hour."

scene black
with Dissolve(1.0)

scene my home 
with Dissolve(1.0)
pause .5

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
m "I'm all set. They should be reaching now."

play sound "door knock.mp3"


show james smile1
with dissolve
    # These display lines of dialogue.



j "Hey [n]." 

m "Hey, James! You are here.... great."

j "Stella told me she'll be here in some time."

m "Well, okay then. You want some snacks?"

j "No, I'm good."

play sound "door knock.mp3"

show stella smile1 at left
with dissolve

s "Hey guys I'm here."

j "Woah! That was quick. You just texted me 5 minutes ago." 

s "I've got supernatural powers [j], I told you."

show james smile2
with dissolve

j "Yeah,sure! but I still reached early and without super powers."

show stella angry1
with dissolve

m "Haha! He's not wrong you know."

s "Don't lie james we both know you have super powers. The power to annoy people is one."

m "Come on, [s]! He's just messing around. I'm glad you are here! "

show james smile1
show stella annoyed1
with dissolve

s "Obviously I'd come. But don't support this idiot."

show stella neutral1
with dissolve

m "Ok, fine. \nYou guys have anything in mind for today?"

s "Well, we could go to a restaurant. I know a place, it's really good."

show james smile2
with dissolve

j "Yeah! We can do that, and then I have a surprise for you guys."

m "Woahh! Seriously??"

show stella smile2
with dissolve

s "Well, I hope your surprise isn't as bad as your jokes."

show james annoyed
with dissolve

j "It won't be! And my jokes are not bad, you just don't get them."

s "Huh! I'm sure they are."

show james smile1
with dissolve

m "Let's hope for the best."

show stella smile1
with dissolve

m "Ohh!! I just forgot.... Ruby is not here. Did she tell you guys when she'll be here?"

show james neutral
show stella neutral2
with dissolve

j "No, mate... she didn't. She doesn't talk to us a lot and I don't know why."

s "Yeah really! She didn't tell me either."

m "She's been acting weird these days. I don't get it."

m "({i}Ruby's my oldest friend! I've known her for some time now.{/i})"

show stella sad2
with dissolve

s "I just hope everything is fine with her. I really worry about her, but she doesn't open up to me."

show james apologize
with dissolve

j "Yeah! She's your close friend [n], just make sure everything is ok with her. We really do care about her."

m "I guess I have to now..... You guys are worried about her and she is just staying away. I hope she tells me what's wrong."

show james concerned
show stella sad1
with dissolve

m "Ok... I'll just call her."
    

play sound "<to 7.5>phone call.mp3"

"{i}.....calling Ruby{/i}"

stop sound

r "Hello [n]"

m "Hey [r], where are you?"

r "I'm at home. I can't come today."

m "Why? Is everything alright?"

r "Yep. I just don't feel like it."

m " Hey, come on [r], you told me you'll come. You can't back out now. Everyone is waiting for you."

r "I don't know [n], I'm not sure if I'll be comfortable around [j] and [s]."

m "What are you talking about? They are waiting for you to come. I want you to come. We'll have fun." 
   
r "Ok... if you want me to. \nI'll be there in 15 mins."

m "Great! We'll wait. Don't rush, take your time."

r "Ok [n], see ya."

m "Bye."

play sound "call end.mp3"

"{i}calls ends{/i}"

m "She's coming."

show james smile2
show stella smile2
with dissolve

j "Great!"

scene black
with Dissolve(1.0)

scene my home 
with Dissolve(1.0)
pause .5

show stella smile1 at left
show james smile1 
show ruby neutral1 at right
with dissolve

j "Ruby! You are finally here.... so good to see you."

show stella smile2
with dissolve

s "Yeah!! Ruby is here... we can finally head out."

r "{i}(silently){/i}.....Hey everyone."

show stella smile1
with dissolve

m "What's with that low energy? Come on! Cheer up... we are heading out."

r "Yeah! Whatever."

j "Let's go then!!!"


######TRAVELLING OPTION MENU#######

menu:
    
    s "You wanna go by train or bus?"

    "Train would be adventurous":
      jump train_travel

    "We can take a bus, the bus stop is close by":
      jump bus_travel

    "Let's walk to the main road and then decide":
      jump street_travel
 
###### 
####################################STREET TRAVEL############################################# 
###### 

label street_travel:

m "Let's walk to the main road and then decide"

j "Ok cool"


scene black
with dissolve
scene road outside
with dissolve

m "You guys go ahead, I'll talk to ruby."

s "Ok"

m "Ruby.... I'll ask you right away. Is everything ok?"

show ruby neutral2
with dissolve

r "Everything is fine."

m "Then why don't you get along with them?"

show ruby annoyed2
with dissolve

r "I told you I don't like them. They don't seem right to me."

m "Well, I've been with them for a while now. They've always been kind to me... and ever since they've come along... you are distancing from us."

show ruby annoyed1
with dissolve

r "I don't know [n]. I told you what I feel. I'm not the kind of person who likes explaining stuff."

m "You weren't like this before [r]. I don't know if they are wrong or you."

r "Think of it what you may. You are the decision-maker."

m "Have you been smoking weed lately?"

show ruby angry
with dissolve

r "Yo!! What the hell?? Noo."

m "Then calm down... and give them a chance! They care about you. Be normal around them today... maybe you'll feel better about them."

show ruby neutral1
with dissolve

r "Ok... kiddo.... stop nagging! I'll be normal."

m "Yeah! This kiddo has to advice a weed-smoker. Lol"

show ruby smile1
with dissolve

r "You're the one who has always needed advice kiddo... You can't sustain without me."

m "Oh! I can. For sure. Well, atleast you are back to normal. Now let's catch up with those guys."

scene road morning:
    zoom 1.05
with dissolve

pause

hide ruby
show james smile1
with dissolve

j "Dude, what were you guys talking about? Global warming?"

hide james
show stella smile1
with dissolve

s "Yeah! What took you so long?"

m "Little Missie here needed a therapy session."

hide stella
show ruby smile1
with dissolve

r "Well Well... [n] comes to me to get advice almost all the time ... so you should know who actually was conducting the session."

m "{i}( Is she dissing? ){/i}"

hide ruby
show stella smile2
with dissolve

s "Haha... that's cool! Now [n] comes to me for advice... but I do suggest to talk to you."

m "Well... she's been running away... so I need advice from someone though."

show ruby annoyed2 at left
with dissolve

r "Yeah, yeah. Why not?"

s "It's nice to see you are fine with this."

m "{i}( She does not seem fine. ){/i}" 

hide stella
hide ruby
show james smile1
with dissolve

j "Yo, therapists... you might want to walk a little faster."

m "Yeah, long legs."

scene main road
with dissolve

pause

show james smile1
with dissolve

j "Ok Stella you can stop checking the map, we are on the main road."

show stella angry1 at right
with dissolve

s "I wasn't looking at the map, I was looking at the menu online, idiot."

show james concerned
with dissolve

j "I'm pretty sure they provide menus in the restaurant [s], you're weird."

show stella annoyed1
with dissolve

s "I like to decide what I want before reaching the place. It saves time and I get my food while you decide what you want... so that I don't have to share."

show stella smile1
show james smile1
with dissolve

m "Wow! That's a pro-gamer move."

s "Yes, it is."

j "I don't know... sounds lame to me."

m "Yeah! little bit."

show stella annoyed1
with dissolve

s "You too [n]?"

show ruby neutral2 at left
with dissolve

r "It's not wierd at all."

show stella neutral2
with dissolve

s "Woah! Did you just support me?? Seriously??"

r "Now I feel stupid."

s "For the first time. High Five."

play sound "high five.mp3"

r "Ok."
                
show stella smile1
with dissolve

menu:
   s "Now that we are here, bus or train?"
   
   "Train would be fun":
    jump train_travel
   
   "Bus would be cool":
    jump bus_travel

######
######BUS TRAVEL#######################################
######
label bus_travel:
    
m "We can take a bus, the bus stop is close by"

s "Ok"

scene black
with dissolve

play music "music/vntrack05.mp3" fadein 1.0 fadeout 1.0

scene busstop 1
with Dissolve(1.0)

s "We are here."


show james neutral
with dissolve

j "You do know which bus to take right?"

m "What am I in kindergarten? Of course I do."

show james smile1
with dissolve

m "Let's wait for the bus."


scene busstop closeup:
  zoom 1.1
with dissolve 

show stella smile1
with dissolve

m "How is this restaurant that you told us about?"

s "It's really good actually, they have a great menu."

m "Sounds good right, [r]?"

show ruby neutral1 at right
with dissolve

r "Yes, I guess."

m "{i}( why can't she respond normally? ){/i}"

#play sound bus horn 
play sound "horn.mp3"


"{i}bus honks{/i}"

 
m "Ok the bus is here. Let's go"


hide stella
hide ruby
with dissolve

show busstop bus:
    zoom 1.3
    xalign 1.0
    yalign 0.4
with dissolve

m "Come on, get in [j] and stop texting for one second."

j "Geez...  [n], ok."

m "And we are off."

scene black
with dissolve
pause 1.0

scene bus inside:
 zoom 1.04
with Dissolve(1.0)


show james smile1
with dissolve

j "Yeah! You guys sit together... I'll go sit with the driver then."

hide james
show stella smile2
with dissolve

s "Haha... that will be great though."
hide stella
show james angry
with dissolve

j "Shut up! And move over [s]."

m "Lol! Come on, sit next to Ruby."

show james smile1
with dissolve

j "What's up miss 'Sad'ie Hawkins? What can I do to cheer you up?"

hide james
show ruby annoyed2
with dissolve

r "You can stay away from me. That'll help."

j "Woah! Woah! What am I Freddy Krueger?"
  
show ruby annoyed1 
with dissolve

m "[r], he's trying to talk to you and you are just being mean now."

show ruby neutral3
with dissolve

r "I don't want to mingle with him. I just want be by myself."

hide ruby
show stella neutral2
with dissolve

s "[r], you need to chill. We are here to help if you have any problems."
   
r "{i}*mumbles to herself* You are the problem.{/i}"

m "See, they are trying to be friends with you and also trying to help you."

hide stella
show ruby sad1
with dissolve

r "Ok... Ok... I'm sorry! I'll do my best to be normal."

m "That's more like it."

hide ruby
show james smile1
with dissolve

j "Phew.... finally."

hide james
show stella smile1
with dissolve

s "Dude, the houses in this area are so beautiful."

m "I know right."

s "Look at that one."
 
hide stella
scene house stella
with dissolve

s "It looks so great and I think no one lives there."

j "May be they closed the windows because they saw you looking."

s "Ok, that is not funny."

m "We are reaching guys."


jump reach_restaurant

#######
#######TRAIN TRAVEL#######################################################
#######

label train_travel:

m "Train would be adventurous"

s "Ok"



scene black
with dissolve

play music "music/vntrack05.mp3" fadein 1.0 fadeout 1.0

scene train station
with Dissolve(1.0)


show stella smile1 at right
with dissolve

s "We are here."

m "Great! Right on time. The train will be here for another 2 minutes."

show james neutral
with dissolve

j "You do know that it takes us where we want to go right?"

m "What am I in kindergarten? Of course I do."

show james smile1
with dissolve

m "We'll get in when the train honks."

show stella smile1
with dissolve

m "How is this restaurant that you told us about?"

s "It's really good actually, they have a great menu. You'll love this place."

m "Sounds good right, [r]?"

hide james
show ruby neutral1
with dissolve

r "Yes, I guess."

m "{i}( why can't she respond normally? ){/i}"

#play sound bus horn 
play sound "train horn.mp3"


"{i}train honks{/i}"

 
m "Ok it's time. Let's go"


hide stella
hide ruby
with dissolve



m "Come on, get in [j] and stop texting for one second."

j "Geez...  [n], ok."

scene black
with dissolve
scene train leaving
with dissolve

m "And we are off."

s "Travelling in train is the best."

j "Yeah! It sure is."

m "Well, let's get to our seats then."

scene black
with dissolve
pause 1.0

scene train morning:
 zoom 1.04
with Dissolve(1.0)

pause

show james smile1
with dissolve

j "Yeah! You guys sit together... I'll go sit with the driver then."

hide james
show stella smile2
with dissolve

s "Haha... that will be great though."
hide stella
show james angry
with dissolve

j "Shut up! And move over [s]."

m "Lol! Come on, sit next to Ruby."

show james smile1
with dissolve

j "What's up miss 'Sad'ie Hawkins? What can I do to cheer you up?"

hide james
show ruby annoyed2
with dissolve

r "You can stay away from me. That'll help."

j "Woah! Woah! What am I Freddy Krueger?"
  
show ruby annoyed1 
with dissolve

m "[r], he's trying to talk to you and you are just being mean now."

show ruby neutral3
with dissolve

r "I don't want to mingle with him. I just want be by myself."

hide ruby
show stella neutral2
with dissolve

s "[r], you need to chill. We are here to help if you have any problems."
   
r "{i}*mumbles to herself* You are the problem.{/i}"

m "See, they are trying to be friends with you and also trying to help you."

hide stella
show ruby sad1
with dissolve

r "Ok... Ok... I'm sorry! I'll do my best to be normal."

m "That's more like it."

hide ruby
show james smile1
with dissolve

j "Phew.... finally."

hide james
show stella smile1
with dissolve

s "Dude, the houses in this area are so beautiful."

m "I know right."

s "Look at that one."
 
hide stella
scene house stella1
with dissolve

s "It looks so great and I think no one lives there."

j "May be they closed the windows because they saw you looking."

s "Ok, that is not funny."

m "We are reaching guys."


jump reach_restaurant



#######
#######REACH RESTAURANT######################################################
#######

label reach_restaurant:
    
scene black
with Dissolve(1.0)
scene restaurant outside
with dissolve

pause

j "We are here nigg...(paused)"

m "No. No, [j]. Just don't."

show james neutral
with dissolve

j "Mmm Ok, mate."

show stella smile1 at right
show ruby smile1 at left
with dissolve

m "Let's go in."

scene black
with Dissolve(1.0)
scene restaurant inside
with dissolve

pause

j "Yo.... this place looks so cool."

show saki normal
with dissolve

w "Welcome."

m "Hi. Table for 4, please."

w "Sure. You can take the front table."

s "This is good."

w "I'll bring the menu."

hide saki
with dissolve

j "Nice choice [s]."

m "I hope the food is as good as the ambience."
   
j "Yeah."
         
show saki normal
with dissolve

w "Here you go."

hide saki
show james smile1
with dissolve

j "It'll take me some time to decide, dude."

m "Yeah! Everything looks great."

hide james
show stella smile1
with dissolve

s "Now you know why I come prepared."

hide stella
show james smile1
with dissolve

j "Do you serve some extra toppings in this?"

hide james
show saki surprised
with dissolve

w "Oh, I'm sorry we don't."

w "You can check some other items in the menu that have different combinations that you'd like."

hide saki
show stella neutral2
with dissolve

s "What are you here to eat pizza?"

hide stella
show james neutral
with dissolve

j "What's wrong with a pizza? But no I'm not."

m "Did you decide what you want [r]?"

hide james
show ruby neutral1
with dissolve

r "Yup."

m "Ok. So, let's give the order."

hide ruby
show saki normal
with dissolve

w "Your food will be here in few minutes. Meanwhile, would you like any beverages?"

m "Yeah, 4 beverages."

hide saki
show james smile1
with dissolve
j "So, Stella how are the holidays going?"

hide james
show stella smile1
with dissolve

s "Going great actually, but my house rent has increased. I don't know if I can manage."

hide stella 
show james concerned
with dissolve

j "Rent in your area is already high. What do they want? Gold?"

hide james
show stella sad1
with dissolve

s "I don't know I'll have to do something about this."

m "Yes, you should."

m "James, what's new?"

hide stella
show james smile1
with dissolve

j "I've reduced smoking. I don't smoke that often now."

menu:
    
    "That's great.":
        show james smile1
        j "I know right. It doesn't get easy though."
        
    
    "Oh really? I don't believe you. I saw you smoking yesterday.":
        show james annoyed
        j "Yes! I was, but that was just once that whole day. I said I've reduced not stopped."
       
hide james
show ruby neutral1
with dissolve
r "Another reason to stay away from this guy."

hide ruby
show stella smile1
with dissolve
s "Lol, Yeah."

hide stella
show james sad
with dissolve

j "Hey, I can't help it. It's really addictive. But I'm trying."

m "I know you are  [j]."

hide james
show stella smile1
with dissolve

s "Ruby, are you doing character arts in these holidays?"

hide stella
show ruby annoyed1
with dissolve

r "How do you know I do character arts?"

hide ruby
show stella smile2
with dissolve

s "Your buddy [n] told me. I've seen some of your work, they look great."

hide stella
show ruby annoyed2
with dissolve

r "Oh, he did? Well, thank you."   

hide ruby
show saki happy
with dissolve
   
w "Here's your order. Enjoy your meal."

m "Thank you."

hide saki
show ruby angry
with dissolve

r "You showed her my artworks without asking me?"

m "She just wanted to see them."

show ruby annoyed2
with dissolve

r "Or wanted to know me."

m "What? What are you talking about?"

show ruby annoyed1
with dissolve

r "Nothing forget it."

hide ruby
show james smile1
with dissolve

j "Oh... man the food is so good."

hide james
show stella smile2
with dissolve

s "Let me have a taste."

hide stella
show james smile1
with dissolve

m "Hey [j], we are going to the arcade tomorrow right?"

j "Yes, we are."

m "And Ruby is going to come with us."

hide james
show ruby neutral2
with dissolve

r "No, I'm not. Take Stella with you."

hide ruby
show stella smile2
with dissolve

s "I don't like arcade. Maybe you and I can go somewhere together. I've been wanting to go out with you."
hide stella
show ruby neutral1
with dissolve

r "I don't thi... (paused)"

m "She will.... (whispers) Listen to me, go out with her to a place you like. You'll know she is a good person when you meet her personally."

show ruby annoyed2
with dissolve

r "Ok... whatever. And if I don't then I'll distance myself from her."


menu:
   m "What do I do?"

   "Ok, fine. Whatever you say.":
       m "Ok, fine. Whatever you say."
       $ rubydec = 1
     
   "Forget it. Stella, you and I will go out together.":
       m "Forget it. Stella, you and I will go out together."
       $ rubydec = 0
   

hide ruby
show james smile1
with dissolve

j "Do you remember when you said to me, \"My friend, hope is a prison\"?"

m "Yoo... what?"

hide james
show stella smile2
with dissolve

s "Did your beverage have something different in it?"

hide stella
show james smile2
with dissolve

j "It's a song lyric, people... I have this song stuck in my head."

hide james
show stella smile3
with dissolve

s "He has no hope of dating anyone. He sings this to remind himself."
hide stella 
show ruby smile2
with dissolve
r "Lol."

m "That's sad."

hide ruby
show james angry
with dissolve

j "Shut up, I have. This song has nothing to do with that."

m "Ok chill [j]."

hide james
show stella smile1
with dissolve

s "Oh... I'm full."

show ruby smile1 at right
with dissolve

r "Me too."

m "Yeah... let's pay the bill and leave."

show stella neutral1
with dissolve

s "Yeah... we've been here for 3 hours."

show james smile1 at left
with dissolve

j "Now it's my turn to take you guys somewhere, and it's a surprise."

show stella smile1
with dissolve
m "Hell yeah!!!" 

hide ruby 
hide james 
hide stella

show saki normal
with dissolve

w "Hope you enjoyed your meal."

m "Yes, we did. Thank you."

m "It's evening already. Let's head out guys"

scene outside restaurant:
    zoom 1.08
with dissolve

pause


show stella smile1
with dissolve

s "Ok. Where are we going now [j]?"

hide stella
show james sly2
with dissolve

j "Just follow my lead."

hide james
show ruby annoyed1
with dissolve
r "What's with that evil grin?"

hide ruby
show james concerned
with dissolve

j "Read my mind Ruby. I'm about to do something evil is what you can think I know, so don't think."

m "Oh... Burn."

show ruby neutral2 at right
with dissolve

r "Yeah I'm gonna need some burnol."


show stella smile2 at left
with dissolve

s "Haha... are we reaching?"

show james smile1
with dissolve

j "Yup. Just a few steps from here."

#####
#####Resto  Bar Scene#############################################
#####

scene black
with Dissolve(1.0)
scene openmic club
with Dissolve(1.0)

pause

m "Yooo this is a.."

show james smile1
with dissolve

j "Restobar yes."

hide james
show stella smile2
with dissolve

s "Hey there's an open mic. Ok wait, you are not here for what I think you are."

hide stella
show james smile2
with dissolve
j "Yes I am, Stella. I'm gonna sing for you guys today."

m "Oh My God!! James that's awesome."

hide james 
show ruby smile1
with dissolve

r "Woah! I didn't know, this guy sings. I've gotta listen."

hide ruby
show james smile1
with dissolve

j "And we are right on time, after this guy finishes his stand-up I'll be next. So, just grab a drink and come closer to the stage. "

hide james
with dissolve

"[j] goes back stage."

show stella smile4
with dissolve

s "Heck Yeah!!! What a surprise dude. Did you expect this [n]? He's gonna play his guitar too."

m "No, I didn't. This guy is full of surprises."

hide stella
with dissolve

stop music fadeout 1.0

pause

play sound "<to 5.0>mic squeak.mp3" fadein 1.0 fadeout 1.0



j "(On the mic) Good evening ladies and gentlemen... Hope everyone's having a dope evening. I'm gonna perform a song for you guys. It's a song that my friend here loves. 
   The song is called 'This Town' by Niall Horan. And I hope you guys like it." 

play sound "audience cheer.mp3"

play music "music/this town.mp3" fadein 1.0 fadeout 1.0 noloop

"Audience Cheer"

pause

m "I love this song. It's one of my favourites. He knew. And he did this for me."

s "Really?? OMG [j]... this is so cool. I feel like I'm gonna cry."

r "His voice is so soothing, like it's not his real voice."

m "I can't believe this. This is brilliant."

s "He's a complete idiot but a great friend. I wish someone sang for me."

r "[n], you are spacing out."

m "This song reminds me of the dream that I've been seeing for a few days."

scene black
with Dissolve(1.0)
show lady anim
with Dissolve(1.0)

m "I see this beautiful girl with an umbrella."

m "It's raining... she turns around and just stares at me."

m "She says - 'Two. Evening. Road. Alone. You.'"

m "I don't understand a thing she says."

m "I just admire the beauty. But this seems really wierd."

s "[n]??"

r "[n], you here??"

scene black
with dissolve

scene openmic club
show stella sad2:
    xalign 0.7
    yalign 1.0
show ruby sad1:
    xalign 0.3
    yalign 1.0
with alpha_example
 
m "Hey, what happened?"

r "Are you alright?"

m "I guess. I don't know, I just had this flash back."

show ruby smile1
show stella smile1
with dissolve

s "Well, now that you are back. Let's listen to his song."

hide stella
hide ruby
with dissolve

m "Yes, I was listening the whole time I was in the other world. This song is what took me there."   

s "Yes it really is mesmerizing."

"Click to end the song or wait till it ends."

pause 74.0

stop music fadeout 2.0

play sound "audience applaude.mp3" fadeout 3.0

pause

j "Thank you so much. Cheers."

play music "music/vntrack05.mp3" fadein 1.0 fadeout 1.0

show james smile1
with dissolve

s "Woooo [j]!! That was amazing."

m "You killed it."

r "Pretty good [j]."

j "Thanks guys."

m "You sang one of my favourite songs. This was such a pleasant surprise."

show james smile2
with dissolve

j "Haha.... this was for you mate."

s "You do open mics frequently idiot. Don't try to flatter [n]."

show james neutral
with dissolve

j "I know I do, but not this song."

m "Thanks, my friend. I loved it."

show james smile1
with dissolve

j "Ok... let's grab a final drink then we'll head back home."

scene black 
with dissolve
scene road night:
    zoom 1.03
with dissolve

show stella smile1
with dissolve

s "We had such a great time today."

m "Yeah!!"

show ruby smile1 at right
with dissolve

r "It's getting late. We should probably head home." 

m "Alright, then I'll see you tomorrow [j]."

show james smile1 at left
with dissolve

j "Yeah! Don't be late."

s "Bye guys."

r "Bye everyone."




if  rubydec == 1 :
    
    label lasun:
        
      m "lasun"

if rubydec == 0:

    label lasun1:
        
        m "lasun1"
 
call phone_start from _call_phone_start
 
call message_start("nadia", "hey, this is a phone texting thingy") from _call_message_start

call reply_message("oh really? what does it do lol") from _call_reply_message

call message_img("nadia", "it works with images too!","pic1") from _call_message_img


call message_img("nadia", "receive cute pics from your friend","pic2") from _call_message_img_1

call message("nadia", "the text box changes depending on how much content there is. dont put too big images or its gonna look weeeeiiiird") from _call_message

call message("nadia", "you can also do menus here") from _call_message_1

call phone_end from _call_phone_end

pause

label jamesending:
  
play music "music/vntrack17.mp3" fadein 1.0 fadeout 1.0

show gasstation anim
with dissolve

pause
 
m "Another crazy day. I feel like I'm falling apart."

m "I don't even see people around me anymore. Even the Gas Station is empty."

m "I've got to walk home now."

scene black
with Dissolve(1.5)

m "When I'm away from my friends, I feel so lonely and miserable."

m "Well, they are there to help me when I need them. So, I've just gotta take a good nap and meet them tomorrow."



scene scary house2
with dissolve
pause

m "Oh! I didn't even know where I was going while I was deep in my thoughts."

scene scary house1
with Dissolve(1.0)
  
pause

m "Woah!"

m "Oh my God"

m "That's the girl I've been seeing in my dreams."

m "And the other girl... uh... I met her at the bus stop few days ago."

m "How are they... why is this.... what are they doing together?"

scene scary house2
with vpunch

pause

m "Where did they go?? They were right here."

scene scary house2:
    zoom 1.4
    xalign .2
    yalign .8
with dissolve

m "Did they go inside?"

m "I need to know what is happening. This can't be real."

menu:
    
  "Should I go inside?"
  
  "Yes. I need to know what this is about.":
    jump jamesend1
  
  "No. I don't think this is a great idea.":
    jump jamesend2


label jamesend1:
    
m "Yes. I need to know what this is about."

m "I want to know why is this happening to me."

m "I'll go inside."

scene last room
with dissolve

pause

stop music fadeout 1.0


play sound "door close.mp3"

scene black
with vpunch

"door closes suddenly"

m "What?? Who closed the door?"

play sound "banging door.mp3"

"*Banging*"

m "Open the door!!! Who's there?? "

mystery "Oh! I so wish I could open the door."

m "Who are you?? What do you want from me??"

mystery "{i}*silence*{/i}"
         
m "LET ME OUT!!!"
               
mystery "You chose wrong [n]."

m "What???"

mystery "One can never be sure what's real."

m "What are you talking about??"

mystery "This is what happens when you go in the wrong direction."

mystery "You can scream for help.... try to break the door.... but no one will help you [n]. You can't undo this now."

mystery "You came too close. You brought this upon yourself."

mystery "One would like to think this isn't real. It isn't right? Or is it?"

mystery "I'm a part of you now."

mystery "Because you let things be this way."

mystery "Loneliness attracts incompetence."

mystery "Especially when you stop thinking."

m "Why don't you just let me go??"

mystery "Do you remember when you said to me, \"My friend, hope is a prison\"?"

play music "music/paranoid android.mp3"  fadeout 1.0 noloop

scene black
pause 1.0

show blood stain:
 zoom 1.8
 xalign .5
 yalign .5
with Dissolve(2.0)
    # This ends the game.
pause 6.0

scene black
with dissolve
scene ilya alekseevanim
with Dissolve(2.0)

pause 15.0

scene ilya alekseevanim1
with Dissolve(2.0)


pause 385.0

pause

return


label jamesend2:
    
m "No. I don't think this is a great idea."

m "I need to get out of here. I don't know what's happening."

m "Am I still dreaming?"



show the end:
    zoom 1.3
    xalign 0.5
    yalign 0.5
with fade

pause

show arcade anime
with dissolve
pause

show cafe anim
with dissolve
pause

show stella smile1 at left
pause .5
show stella smile2
pause

show lady anim
with dissolve
pause

show gasstation anim
with dissolve
pause

scene black
with dissolve
pause 1.0
show blood stain:
 zoom 1.8
 xalign .5
 yalign .5
with Dissolve(2.0)
    # This ends the game.
pause


"{b}BAD ENDING{/b}"

return
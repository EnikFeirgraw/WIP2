label chapter_1:

scene black with fade
show text "Chapter 1: Cheesy subtitle maybe" at truecenter with dissolve
pause 2.5
hide text with dissolve
pause 1

#[Scene: Daytime, in a public square. A festival is on]
show ferris_wheel with fade:
    subpixel True
    yalign 0.0

Nemyu "Am I... Alone?"
"This sun..."

show ferris_wheel:
    subpixel True
    yalign 0.0
    linear 3.0 yalign 1.0
play music carnival_crowd fadein 5.0 loop
$ renpy.pause(3.0)

"These crowds..."
"Too bright. Too loud."
"Why did I come here? Why alone?"

show text "{color=#000}A cloudless sky. The heat beats down on NEET and athlete alike{/color}" at top with dissolve
$ renpy.pause()
hide text with dissolve

"Shade, where art thou."
show text "{color=#000}The energetic crowds pay no heed to the young girl who looks on the verge of collapse.{/color}" at top with dissolve
$ renpy.pause()
#[Scene: To the shade of an alley between two buildings]
scene alley with fade

"Ahh, much better."
"I had been spaced out in the crowds moving to and fro between the stalls lined up throughout the square."
"It feels almost like I had been dozing off. Heat exhaustion?"
"Could be. The weather is fiercely tranquil today."
"While I'm here, I suppose I could get some ice-cream. I'm sure one of these stalls will have it."
"I check my pockets for my wallet -- I can't even recall whether I left the house with it."
"Fortunately it's indeed there."
"So thirsty..."
"I now notice just how dry my throat is. I regret coming here, knowing well how terribly I handle the sun."

stop music fadeout 1.5

UK "Ah, Nemyu! There you are!"
"Someone calls my name. Ah, right--"

play music ely_tryagain fadein 3 loop
#$ renpy.music.queue("./bgms/carnival_crowd.ogg", channel='music', loop=True, clear_queue=True, fadein=3.0, tight=None)
show Ely at center with moveinright

Nemyu "Sorry, I didn't mean to just disappear like that."
UK "Disappear? Now that'd be troublesome. But running off is no problem for me!"
"She hands me an cone, stacked high with vanilla ice-cream."
"My favorite."
Nemyu "Ah, thank you."
"Of course, I wasn't here alone. In my daze, I guess it slipped my mind that she was just getting ice-cream."
UK "Are you feeling alright? Is it too hot after all?"
Nemyu "I should be fine. Just need a moment in the shade."
UK "Sure. Let me know if you want to go home though, I don't mind."
Nemyu "Yeah. Thanks... Ely."
"Ely smiles brightly and begins eating."
"With a bite of my own, I immediately begin to feel better. The world becomes more vivid and the heat less torturous."
"Today's festival is to celebrate the launch of a new satellite."
"Why such a large celebration? I don't know the specifics, but I heard that it's a pretty important technological achievement. Not to mention that its launch coincides with the 20th anniversary of this city's creation."
"A city built for the advancement of several fields of research and technology. Most families here have at least one member who has been working towards this very day in their own way."
Nemyu "Is your father not here? I thought he'd be a big part of the celebrations."
Ely "Ahah, I'm sure he wanted to, but he still has to manage operations at the office."
Nemyu "Seems tough."
Ely "But it's all thanks to him that everything was ready in time for today. He sure did well, right?"
Nemyu "Yeah. I'm sure he worked hard."
Ely "You feeling better now?"
"She asks with a concerned look. Ely has always been especially conscious of her friends' feelings."
"I'm always thankful for that."
Nemyu "A little. Why don't we go for a walk?"
"I nod my head down the alley; at the other end another crowd bustles. Events are happening everywhere, so there's no need to hang around at one place."
Ely "Sure!"
"We head down the deserted alley, lined with doors that lead to who knows where."
Ely "By the way, doesn't this remind you of when we were kids?"
"I think about in what way that would be, but Ely continues first."
Ely "I'd always find you wandering around in places like this."
Nemyu "Ah yeah, I remember well. I guess I just loved to explore forgotten parts of the city."
Nemyu "Even here near the city center, there are places only few people ever step into. I've always felt drawn to places like this."
Ely "It's strange, isn't it? Everybody here is so set in their routine, they basically only know their workplace and where to buy what they need."
Nemyu "Everybody is always busy, after all... I hear that our city is fairly unusual in that regard."
Ely "Ah, but it was always exciting back then."
Nemyu "How so?"
Ely "Whenever I was bored I'd go looking around, wondering if I'd bump into you..."
Ely "And I did almost every time! It seemed natural to me back then, but now I realize how coincidental it all was... Right?"
"I recall those days."
"Ely's referring to a time when we were only 8 or 9."
"With crime being almost non-existent in our city, it wasn't strange for even children to be outside late at night."
"Either to run to the convenience store on an errand for the parents, or to walk or play in the parks."
"I remember that Ely was out for the former when I first met her."
"And as she said, we indeed ran into each other over and over after that. As if I could forget how I made my first friend."
Nemyu "So I had a stalker that far back, huh. This city's scarier than I thought."
"Ely chokes on her ice-cream as I say that."
Nemyu "Aha, just kidding, just kidding."
"She may actually feel bad, so I smile to relieve her."
Nemyu "If you did keep searching for me, I'm glad for that."
"Since I was too shy to ask her to be my friend even if I wanted company..."
Ely "Hehe, well I'm glad too..."
"Rather than leaving the coolness of the alley, we had made a few turns while walking, bringing up more memories of those days."
"Through the gaps between the tall concrete buildings the sky could still be seen, but the heat of the summer day couldn't reach here."
"Refreshing and comfortable, and a little exciting."
"The external components of A/C units hummed from all around; the only indication of life in the stillness of these narrow streets."
"The crowds couldn't even be heard from here, their sound blocked by the tall structures."
"This wasn't a place I'd ever been to before. It felt as though there were infinitely many such places, growing faster than I ever could've explored them all."
Ely "It's actually a bit cold here, isn't it?"
Nemyu "Yeah, sorry, do you want to head back?"
Ely "Oh, no no, don't worry about me!"
"As considerate as ever."
"I decide that we should return to the outside, but..."
stop music fadeout 2
Nemyu "?"
Ely "Is something wrong?"
$ renpy.music.set_volume(0.3, delay=0, channel='music')
play music ac_unit fadein 2
Nemyu "Not really, just..."
"I strain my ears and try to block out the white noise of the A/C units, but fail to discern the vague sense of change that I felt."
"Perhaps not something I heard, but just something I arbitrarily sensed."
Ely "Ah! Hey, was that door open before?"
"Ely, looking down a perpendicular path, points to a door on the second floor of a building, with stairs leading up to it."
"It's not like I had taken particular notice of it earlier, but it's certain that an open door would've stood out to me if I had seen one."
"Everything thus far was closed, so it was unusual. It seems like it really was just opened."
Nemyu "I don't think so."
"I hesitate for a second, but I feel a compulsion;"
Nemyu "Do you want to check it out?"
"Ely looks a little scared, but she doesn't shake her head."
Ely "If you want to..."
Ely "It does feel strangely exciting, right?"
"As expected of the girl who would always come to talk to me in the most obscure corners of this city."
"But, I shouldn't make her come along with me when I may be doing something silly."

#[CHOICE: "Enter the door" -> 2.txt | "Retreat to the outside" -> 3.txt]
menu:
    "Enter the door":
        jump chapter_2
    "Retreat to the outside":
        stop music
        $ renpy.music.set_volume(1.0, delay=0, channel='music')
        "You die a horrific death for no reason! Game Over"
        return

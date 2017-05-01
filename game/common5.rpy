#[Scene: Main city train station]
label common5:

scene black with fade
show text "Chapter 2: Or whatever chapter number we are actually on" at truecenter with dissolve
pause 2.5
hide text with dissolve
pause 1
scene platform_day

Ely "Have a good day! Bye!"
"I wave to Ely as we part outside the train station, having arrived back in the city center."
"Unlike Ely who attends high school, I have to work to be able to continue affording a place to stay."
"I have no relatives to take care of me, so this is simply how it is."
"Even if I have the time to spend some of my week at school, I can't afford the tuition of the high class establishments that monopolize the area."
"Would I enjoy high school? Would I have fun, carefree days like other teenagers?"
"I don't really care, since it's only wishful thinking..."
"When Ely's out of sight, I turn around and begin walking in the opposite direction."

#[Scene: Store]
scene storefront with dissolve

"My current job is doing food deliveries."
"I only started here recently. I change jobs often because, frankly, they get boring."
Boss "Nemyu!"
Nemyu "Yes!"
Boss "This one's going out to 53 Kallwark! He's a long-time customer, so make it snappy!"
Nemyu "Yes sir."
"I take a shortcut I know."

scene alley with dissolve
Old_Woman "Ohh, good morning dearie."
Nemyu "Morning!"
"I often get greeted when I'm moving around."
"Mostly by the elderly, who never fail to recognize me and unanimously seem drawn to striking up conversations."
"*Knock, knock*"
Man "Whoa, already? Ah, you're new, aren't you? What's your name?"
Nemyu "I'm Nemyu."
Man "I could get used to things being this quick! Thanks kid, see you around."
Nemyu "Good day."
"I'll forgive him for calling me kid only because he's old."
scene storefront with dissolve
Nemyu "Back, sir."
Boss "Wha--"
Nemyu "?"
Boss "Seriously? That was like 3 minutes..."
"I'm pretty popular in the business because of my speed."
"I don't have to worry about jumping between jobs, as long as my recommendations are encouraging."
"Like this, my days are spent uneventfully and with ample time for wandering thoughts."
"..."
"I wonder what Ely's up to..."

#The same afternoon, at a nearby high school...
scene school with dissolve
Ely "The umbrella did {b}{i}what{/b}{/i} to her? Haha!"
Girl "Hey Ely, why were you so late today? You missed out on soooo much fun."
Ely "I sense some sarcasm there..."
Ely "Well, I'll let you know. I slept the night at a friend's house, and thought it too much a bother to leave early in the morning."
Girl "Hey hey, don't let the teachers hear that."
Girl_2 "Yeah, they assume you miss a lot for good reason... You could get suspended if they knew you were just lazy."
Ely "I can't deny my own nature! Daytime isn't good for me..."
Girl "Hah, here it is, the classic excuse!"
Girl_2 "Remember when you wrote that whole essay in middle school about how you couldn't do PE because of the toxic rays?"
Ely "Geh--"
Ely "{color=#804000}{i}I should've learned how to limit myself back then...{/color}{/i}"
Ely "Well, it worked, didn't it?"
Girl_2 "Only because you had to go talk to counseling instead..."
Girl "Say say, was that friend the one you always talk about?"
Ely "Huh? Ah, yeah..."
Girl_2 "Oh yeah, I want to finally met her! I'm not gonna let her hide from us forever, fufufu."
Ely "Are you that interested?"
Girl "You do talk about her a lot you know, Ely. Her name was like, Nep or something, right?"
Ely "Ahh, no! Nem!"
Ely "... Well, I suppose we could go surprise her?"
Ely "{color=#804000}{i}Nem isn't exactly opposed to making new friends...{/color}{/i}"
Girl "Yeah, yeah! After school, then! Yeah!"
Ely "Ah, sure! *nervous*"
UK "..."

#[Scene: Back at store]
scene storefront with dissolve
Boss "Nemyu! Got another order."
Nemyu "Ah, sure. Where to?"
Boss "*****"
Nemyu "--"
Boss "? Everything alright?"
Nemyu "U-um... I did mention that I can't go that area when I applied, right?"
Boss "What? I don't recall that."
Boss "It's not far. Get going."
Nemyu "But--"
Boss "We're busy, there's no time."
"He walks away."
"Great, this old guy's mood is fickle... Maybe I'll find somewhere else to work."
"But I need the money for this week."
"So I have no choice but to try..."
#[Scene: Walking outside]
scene alley with dissolve
"There's one place in this city that I cannot go."
"Maybe there are more, but there's one place I know I must avoid."
"This is undoubtedly a normal city. The people are friendly, the officials are transparent and all for the betterment of the community."
"Any corruption is quickly snuffed out, and there are no suspicious facilities or anything like that."
scene alley2 with dissolve
"Yet when I come here..."
Nemyu "..."
"As expected, I begin to feel myself shivering."
"The air is still warm, but it's as though my skin will no longer absorb the heat."
"I continue putting one foot in front of the other."
"But my strength is gradually disappearing."
Nemyu "Crap..."
Nemyu "As I thought, it's still impossible..."
"I don't care why."
"Life raises questions whether it intends to answer them or not."
"It's best to simply ignore the things you can do nothing about, and focus on what you can do."
"So I don't care. I just want to avoid this place forever."
"Yet I'm forced here whether I want it or not."
Nemyu "Gh--"
Nemyu "Stupid work."
"My gait strengthens as I grow angry."
"It's pointless. I'm still not even close to where I need to go."
"I thought I was managing well, but I'm getting looks from everyone who passes by..."
"My vision is starting to fade. I mustn't look very good."
"I finally reach an underpass."
"It's the only way forward. Before me are several railway tracks, with no crossing over them."
"To get to the neighboring part of town, I either have to take a large detour, or walk through this passage."
"It's unnaturally dark. This isn't a well-used part of town."
Nemyu "Heh. I don't like to think of myself as easily scared, but this is straight out of a horror movie."
"If I go on, I doubt anything will jump out of the shadows at me."
"But collapsing is a real possibility..."
#[CHOICE: "Go ahead" -> TBD | "Leave" -> common6.txt]
menu:
    "Go ahead":
        "Nemyu encounters the reason she can't go to this part of town... Unicorns roam here!"
        "Taking a deep breath, Nemyu continues."
        "Slowly walking, hoping they don't notice her, Nemyu steps on a twig"
        Nemyu "Fuck!! They see me! They remember I've eaten their young to survive!"
        "Nemyu is promptly gored by a Unicorn in rage."
        "..."
        "Game... Fucking... Over"
        return
    "Retreat to the outside":
        jump common6
        return

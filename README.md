# kjv
This is a command line based browser for the KJV Bible.

    Usage: [./kjv] [options] [search words] ...

      -r  omit verse references
      -w  word search
      -s  word-wrap to terminal size (automatic if output to terminal)
      -p  partial word match (don't search word in any part of a word)
      -0  zero verses context during search
                echo  -1 .. -9 more verses context
      -t  use tr1550 greek text
      -a  use af1953 afrikaans text
      -o  don't pipe to less, just to stdout

    Shows extracts having all the terms in the adjoining context
    With no options, display the text with highlighted verses using less

       kjv
       kjv liberty spy
       kjv -t Matthew

## Word search

Suppose you are looking for a verse related to this:

James 3:18 And the **fruit** of **righteousness** is sown in peace of them that make peace.

You can run

    kjv -0 fruit righteousness

and get all verses that speak of both fruit and righteousness (including words that start with "fruit" like "fruitful"):

Isaiah 32:16 Then judgment shall dwell in the wilderness, and **righteousness** remain in the **fruit**ful field.  
Amos 6:12 Shall horses run upon the rock? will one plow there with oxen?  for ye have turned judgment into gall, and the **fruit** of **righteousness** into hemlock: 
2 Corinthians 9:10 Now he that ministereth seed to the sower both minister bread for your food, and multiply your seed sown, and increase the **fruit**s of your **righteousness**;) 
Ephesians 5:9 (For the **fruit** of the Spirit is in all goodness and **righteousness** and truth;) 
Philippians 1:11 Being filled with the **fruit**s of **righteousness**, which are by Jesus Christ, unto the glory and praise of God.  
Hebrews 12:11 Now no chastening for the present seemeth to be joyous, but grievous: nevertheless afterward it yieldeth the peaceable **fruit** of **righteousness** unto them which are exercised thereby.  
James 3:18 And the **fruit** of **righteousness** is sown in peace of them that make peace.  

## Contextual word search

The default (without ```-0```) is to search and display  with ```-5``` lines of context before and after:

    kjv fruit righteousness

And get this - all the verses that say "fruit" and "**righteousness**" in close proximity:

Deuteronomy 33:14 And for the precious **fruits** brought forth by the sun, and for the precious things put forth by the moon, 
Deuteronomy 33:15 And for the chief things of the ancient mountains, and for the precious things of the lasting hills, 
Deuteronomy 33:16 And for the precious things of the earth and fulness thereof, and for the good will of him that dwelt in the bush: let the blessing come upon the head of Joseph, and upon the top of the head of him that was separated from his brethren.  
Deuteronomy 33:17 His glory is like the firstling of his bullock, and his horns are like the horns of unicorns: with them he shall push the people together to the ends of the earth: and they are the ten thousands of Ephraim, and they are the thousands of Manasseh.  
Deuteronomy 33:18 And of Zebulun he said, Rejoice, Zebulun, in thy going out; and, Issachar, in thy tents.  
Deuteronomy 33:19 They shall call the people unto the mountain; there they shall offer sacrifices of **righteousness**: for they shall suck of the abundance of the seas, and of treasures hid in the sand.  
    ``--``
Joshua 5:7 And their children, whom he raised up in their stead, them Joshua circumcised: for they were uncircumcised, because they had not circumcised them by the way.  
Joshua 5:8 And it came to pass, when they had done circumcising all the people, that they abode in their places in the camp, till they were whole.  
Joshua 5:9 And the LORD said unto Joshua, This day have I rolled away the reproach of Egypt from off you. Wherefore the name of the place is called Gilgal unto this day.  
Joshua 5:10 And the children of Israel encamped in Gilgal, and kept the passover on the fourteenth day of the month at even in the plains of Jericho.  
    ``--``
Psalms 129:2 Many a time have they afflicted me from my youth: yet they have not prevailed against me.  
    ``--``
Psalms 132:6 Lo, we heard of it at Ephratah: we found it in the fields of the wood.  
Psalms 132:7 We will go into his tabernacles: we will worship at his footstool.  
Psalms 132:8 Arise, O LORD, into thy rest; thou, and the ark of thy strength.  
Psalms 132:9 Let thy priests be clothed with **righteousness**; and let thy saints shout for joy.  
Psalms 132:10 For thy servant David's sake turn not away the face of thine anointed.  
Psalms 132:11 The LORD hath sworn in truth unto David; he will not turn from it; Of the **fruit** of thy body will I set upon thy throne.  
Psalms 132:12 If thy children will keep my covenant and my testimony that I shall teach them, their children shall also sit upon thy throne for evermore.  
Psalms 132:13 For the LORD hath chosen Zion; he hath desired it for his habitation.  
Psalms 132:14 This is my rest for ever: here will I dwell; for I have desired it.  
    ``--``
    ``--``
Proverbs 8:14 Counsel is mine, and sound wisdom: I am understanding; I have strength.  
Proverbs 8:15 By me kings reign, and princes decree justice.  
Proverbs 8:16 By me princes rule, and nobles, even all the judges of the earth.  
Proverbs 8:17 I love them that love me; and those that seek me early shall find me.  
Proverbs 8:18 Riches and honour are with me; yea, durable riches and **righteousness**.  
Proverbs 8:19 My **fruit** is better than gold, yea, than fine gold; and my revenue than choice silver.  
Proverbs 8:20 I lead in the way of **righteousness**, in the midst of the paths of judgment: 
Proverbs 8:21 That I may cause those that love me to inherit substance; and I will fill their treasures.  
Proverbs 8:22 The LORD possessed me in the beginning of his way, before his works of old.  
Proverbs 8:23 I was set up from everlasting, from the beginning, or ever the earth was.  
Proverbs 8:24 When there were no depths, I was brought forth; when there were no fountains abounding with water.  
    ``--``
    ``--``
Proverbs 12:12 The wicked desireth the net of evil men: but the root of the righteous yieldeth **fruit**.  
Proverbs 12:13 The wicked is snared by the transgression of his lips: but the just shall come out of trouble.  
Proverbs 12:14 A man shall be satisfied with good by the **fruit** of his mouth: and the recompence of a man's hands shall be rendered unto him.  
Proverbs 12:15 The way of a fool is right in his own eyes: but he that hearkeneth unto counsel is wise.  
Proverbs 12:16 A fool's wrath is presently known: but a prudent man covereth shame.  
Proverbs 12:17 He that speaketh truth sheweth forth **righteousness**: but a false witness deceit.  
Proverbs 12:18 There is that speaketh like the piercings of a sword: but the tongue of the wise is health.  
Proverbs 12:19 The lip of truth shall be established for ever: but a lying tongue is but for a moment.  
    ``--``
Proverbs 12:25 Heaviness in the heart of man maketh it stoop: but a good word maketh it glad.  
Proverbs 12:26 The righteous is more excellent than his neighbour: but the way of the wicked seduceth them.  
Proverbs 12:27 The slothful man roasteth not that which he took in hunting: but the substance of a diligent man is precious.  
Proverbs 12:28 In the way of **righteousness** is life: and in the pathway thereof there is no death.  
Proverbs 13:1 A wise son heareth his father's instruction: but a scorner heareth not rebuke.  
Proverbs 13:2 A man shall eat good by the **fruit** of his mouth: but the soul of the transgressors shall eat violence.  
Proverbs 13:3 He that keepeth his mouth keepeth his life: but he that openeth wide his lips shall have destruction.  
Proverbs 13:4 The soul of the sluggard desireth, and hath nothing: but the soul of the diligent shall be made fat.  
Proverbs 13:5 A righteous man hateth lying: but a wicked man is loathsome, and cometh to shame.  
Proverbs 13:6 **Righteousness** keepeth him that is upright in the way: but wickedness overthroweth the sinner.  
Proverbs 13:7 There is that maketh himself rich, yet hath nothing: there is that maketh himself poor, yet hath great riches.  
    ``--``
Proverbs 18:15 The heart of the prudent getteth knowledge; and the ear of the wise seeketh knowledge.  
Proverbs 18:16 A man's gift maketh room for him, and bringeth him before great men.  
Proverbs 18:17 He that is first in his own cause seemeth just; but his neighbour cometh and searcheth him.  
    ``--``
Isaiah 10:17 And the light of Israel shall be for a fire, and his Holy One for a flame: and it shall burn and devour his thorns and his briers in one day; 
Isaiah 10:18 And shall consume the glory of his forest, and of his **fruit**ful field, both soul and body: and they shall be as when a standard-bearer fainteth.  
Isaiah 10:19 And the rest of the trees of his forest shall be few, that a child may write them.  
Isaiah 10:20 And it shall come to pass in that day, that the remnant of Israel, and such as are escaped of the house of Jacob, shall no more again stay upon him that smote them; but shall stay upon the LORD, the Holy One of Israel, in truth.  
Isaiah 10:21 The remnant shall return, even the remnant of Jacob, unto the mighty God.  
Isaiah 10:22 For though thy people Israel be as the sand of the sea, yet a remnant of them shall return: the consumption decreed shall overflow with **righteousness**.  
Isaiah 10:23 For the Lord GOD of hosts shall make a consumption, even determined, in the midst of all the land.  
    ``--``
Isaiah 13:13 Therefore I will shake the heavens, and the earth shall remove out of her place, in the wrath of the LORD of hosts, and in the day of his fierce anger.  
Isaiah 13:14 And it shall be as the chased roe, and as a sheep that no man taketh up: they shall every man turn to his own people, and flee every one into his own land.  
Isaiah 13:15 Every one that is found shall be thrust through; and every one that is joined unto them shall fall by the sword.  
    ``--``
Isaiah 14:32 What shall one then answer the messengers of the nation? That the LORD hath founded Zion, and the poor of his people shall trust in it.  
Isaiah 15:1 The burden of Moab. Because in the night Ar of Moab is laid waste, and brought to silence; because in the night Kir of Moab is laid waste, and brought to silence; 
Isaiah 15:2 He is gone up to Bajith, and to Dibon, the high places, to weep: Moab shall howl over Nebo, and over Medeba: on all their heads shall be baldness, and every beard cut off.  
    ``--``
Isaiah 16:4 Let mine outcasts dwell with thee, Moab; be thou a covert to them from the face of the spoiler: for the extortioner is at an end, the spoiler ceaseth, the oppressors are consumed out of the land.  
Isaiah 16:5 And in mercy shall the throne be established: and he shall sit upon it in truth in the tabernacle of David, judging, and seeking judgment, and hasting **righteousness**.  
Isaiah 16:6 We have heard of the pride of Moab; he is very proud: even of his haughtiness, and his pride, and his wrath: but his lies shall not be so.  
Isaiah 16:7 Therefore shall Moab howl for Moab, every one shall howl: for the foundations of Kirhareseth shall ye mourn; surely they are stricken.  
Isaiah 16:8 For the fields of Heshbon languish, and the vine of Sibmah: the lords of the heathen have broken down the principal plants thereof, they are come even unto Jazer, they wandered through the wilderness: her branches are stretched out, they are gone over the sea.  
Isaiah 16:9 Therefore I will bewail with the weeping of Jazer the vine of Sibmah: I will water thee with my tears, O Heshbon, and Elealeh: for the shouting for thy summer **fruit**s and for thy harvest is fallen.  
Isaiah 16:10 And gladness is taken away, and joy out of the plentiful field; and in the vineyards there shall be no singing, neither shall there be shouting: the treaders shall tread out no wine in their presses; I have made their vintage shouting to cease.  
    ``--``
Isaiah 32:11 Tremble, ye women that are at ease; be troubled, ye careless ones: strip you, and make you bare, and gird sackcloth upon your loins.  
Isaiah 32:12 They shall lament for the teats, for the pleasant fields, for the **fruit**ful vine.  
Isaiah 32:13 Upon the land of my people shall come up thorns and briers; yea, upon all the houses of joy in the joyous city: 
Isaiah 32:14 Because the palaces shall be forsaken; the multitude of the city shall be left; the forts and towers shall be for dens for ever, a joy of wild asses, a pasture of flocks; 
Isaiah 32:15 Until the spirit be poured upon us from on high, and the wilderness be a **fruit**ful field, and the **fruit**ful field be counted for a forest.  
Isaiah 32:16 Then judgment shall dwell in the wilderness, and **righteousness** remain in the **fruit**ful field.  
Isaiah 32:17 And the work of **righteousness** shall be peace; and the effect of **righteousness** quietness and assurance for ever.  
Isaiah 32:18 And my people shall dwell in a peaceable habitation, and in sure dwellings, and in quiet resting places; 
Isaiah 32:19 When it shall hail, coming down on the forest; and the city shall be low in a low place.  
Isaiah 32:20 Blessed are ye that sow beside all waters, that send forth thither the feet of the ox and the ass.  
Isaiah 33:1 Woe to thee that spoilest, and thou wast not spoiled; and dealest treacherously, and they dealt not treacherously with thee! when thou shalt cease to spoil, thou shalt be spoiled; and when thou shalt make an end to deal treacherously, they shall deal treacherously with thee.  
    ``--``
Isaiah 33:4 And your spoil shall be gathered like the gathering of the caterpiller: as the running to and fro of locusts shall he run upon them.  
Isaiah 33:5 The LORD is exalted; for he dwelleth on high: he hath filled Zion with judgment and **righteousness**.  
Isaiah 33:6 And wisdom and knowledge shall be the stability of thy times, and strength of salvation: the fear of the LORD is his treasure.  
Isaiah 33:7 Behold, their valiant ones shall cry without: the ambassadors of peace shall weep bitterly.  
Isaiah 33:8 The highways lie waste, the wayfaring man ceaseth: he hath broken the covenant, he hath despised the cities, he regardeth no man.  
Isaiah 33:9 The earth mourneth and languisheth: Lebanon is ashamed and hewn down: Sharon is like a wilderness; and Bashan and Carmel shake off their **fruit**s.  
Isaiah 33:10 Now will I rise, saith the LORD; now will I be exalted; now will I lift up myself.  
    ``--``
Isaiah 57:18 I have seen his ways, and will heal him: I will lead him also, and restore comforts unto him and to his mourners.  
Isaiah 57:19 I create the **fruit** of the lips; Peace, peace to him that is far off, and to him that is near, saith the LORD; and I will heal him.  
Isaiah 57:20 But the wicked are like the troubled sea, when it cannot rest, whose waters cast up mire and dirt.  
Isaiah 57:21 There is no peace, saith my God, to the wicked.  
Isaiah 58:1 Cry aloud, spare not, lift up thy voice like a trumpet, and shew my people their transgression, and the house of Jacob their sins.  
Isaiah 58:2 Yet they seek me daily, and delight to know my ways, as a nation that did **righteousness****, and forsook not the ordinance of their God: they ask of me the ordinances of justice; they take delight in approaching to God.  
Isaiah 58:3 Wherefore have we fasted, say they, and thou seest not?  wherefore have we afflicted our soul, and thou takest no knowledge? Behold, in the day of your fast ye find pleasure, and exact all your labours.  
    ``--``
Isaiah 65:16 That he who blesseth himself in the earth shall bless himself in the God of truth; and he that sweareth in the earth shall swear by the God of truth; because the former troubles are forgotten, and because they are hid from mine eyes.  
Isaiah 65:17 For, behold, I create new heavens and a new earth: and the former shall not be remembered, nor come into mind.  
Isaiah 65:18 But be ye glad and rejoice for ever in that which I create: for, behold, I create Jerusalem a rejoicing, and her people a joy.  
    ``--``
Jeremiah 21:12 O house of David, thus saith the LORD; Execute judgment in the morning, and deliver him that is spoiled out of the hand of the oppressor, lest my fury go out like fire, and burn that none can quench it, because of the evil of your doings.  
Jeremiah 21:13 Behold, I am against thee, O inhabitant of the valley, and rock of the plain, saith the LORD; which say, Who shall come down against us? or who shall enter into our habitations?  
Jeremiah 21:14 But I will punish you according to the **fruit** of your doings, saith the LORD: and I will kindle a fire in the forest thereof, and it shall devour all things round about it.  
Jeremiah 22:1 Thus saith the LORD; Go down to the house of the king of Judah, and speak there this word, 
Jeremiah 22:2 And say, Hear the word of the LORD, O king of Judah, that sittest upon the throne of David, thou, and thy servants, and thy people that enter in by these gates: 
Jeremiah 22:3 Thus saith the LORD; Execute ye judgment and **righteousness**, and deliver the spoiled out of the hand of the oppressor: and do no wrong, do no violence to the stranger, the fatherless, nor the widow, neither shed innocent blood in this place.  
Jeremiah 22:4 For if ye do this thing indeed, then shall there enter in by the gates of this house kings sitting upon the throne of David, riding in chariots and on horses, he, and his servants, and his people.  
Jeremiah 22:5 But if ye will not hear these words, I swear by myself, saith the LORD, that this house shall become a desolation.  
    ``--``
Jeremiah 22:28 Is this man Coniah a despised broken idol? is he a vessel wherein is no pleasure? wherefore are they cast out, he and his seed, and are cast into a land which they know not?  
Jeremiah 22:29 O earth, earth, earth, hear the word of the LORD.  
    ``--``
Jeremiah 23:1 Woe be unto the pastors that destroy and scatter the sheep of my pasture! saith the LORD.  
Jeremiah 23:2 Therefore thus saith the LORD God of Israel against the pastors that feed my people; Ye have scattered my flock, and driven them away, and have not visited them: behold, I will visit upon you the evil of your doings, saith the LORD.  
Jeremiah 23:3 And I will gather the remnant of my flock out of all countries whither I have driven them, and will bring them again to their folds; and they shall be **fruit**ful and increase.  
Jeremiah 23:4 And I will set up shepherds over them which shall feed them: and they shall fear no more, nor be dismayed, neither shall they be lacking, saith the LORD.  
Jeremiah 23:5 Behold, the days come, saith the LORD, that I will raise unto David a righteous Branch, and a King shall reign and prosper, and shall execute judgment and justice in the earth.  
Jeremiah 23:6 In his days Judah shall be saved, and Israel shall dwell safely: and this is his name whereby he shall be called, THE LORD OUR **RIGHTEOUSNESS**.  
Jeremiah 23:7 Therefore, behold, the days come, saith the LORD, that they shall no more say, The LORD liveth, which brought up the children of Israel out of the land of Egypt; 
Jeremiah 23:8 But, The LORD liveth, which brought up and which led the seed of the house of Israel out of the north country, and from all countries whither I had driven them; and they shall dwell in their own land.  
    ``--``
Jeremiah 28:17 So Hananiah the prophet died the same year in the seventh month.  
Jeremiah 29:1 Now these are the words of the letter that Jeremiah the prophet sent from Jerusalem unto the residue of the elders which were carried away captives, and to the priests, and to the prophets, and to all the people whom Nebuchadnezzar had carried away captive from Jerusalem to Babylon; 
    ``--``
    ``--``
Hosea 10:8 The high places also of Aven, the sin of Israel, shall be destroyed: the thorn and the thistle shall come up on their altars; and they shall say to the mountains, Cover us; and to the hills, Fall on us.  
Hosea 10:9 O Israel, thou hast sinned from the days of Gibeah: there they stood: the battle in Gibeah against the children of iniquity did not overtake them.  
Hosea 10:10 It is in my desire that I should chastise them; and the people shall be gathered against them, when they shall bind themselves in their two furrows.  
Hosea 10:11 And Ephraim is as an heifer that is taught, and loveth to tread out the corn; but I passed over upon her fair neck: I will make Ephraim to ride; Judah shall plow, and Jacob shall break his clods.  
Hosea 10:12 Sow to yourselves in **righteousness**, reap in mercy; break up your fallow ground: for it is time to seek the LORD, till he come and rain **righteousness** upon you.  
Hosea 10:13 Ye have plowed wickedness, ye have reaped iniquity; ye have eaten the **fruit** of lies: because thou didst trust in thy way, in the multitude of thy mighty men.  
Hosea 10:14 Therefore shall a tumult arise among thy people, and all thy fortresses shall be spoiled, as Shalman spoiled Betharbel in the day of battle: the mother was dashed in pieces upon her children.  
Hosea 10:15 So shall Bethel do unto you because of your great wickedness: in a morning shall the king of Israel utterly be cut off.  
Hosea 11:1 When Israel was a child, then I loved him, and called my son out of Egypt.  
Hosea 11:2 As they called them, so they went from them: they sacrificed unto Baalim, and burned incense to graven images.  
    ``--``
Amos 6:7 Therefore now shall they go captive with the first that go captive, and the banquet of them that stretched themselves shall be removed.  
Amos 6:8 The Lord GOD hath sworn by himself, saith the LORD the God of hosts, I abhor the excellency of Jacob, and hate his palaces: therefore will I deliver up the city with all that is therein.  
Amos 6:9 And it shall come to pass, if there remain ten men in one house, that they shall die.  
Amos 6:10 And a man's uncle shall take him up, and he that burneth him, to bring out the bones out of the house, and shall say unto him that is by the sides of the house, Is there yet any with thee? and he shall say, No. Then shall he say, Hold thy tongue: for we may not make mention of the name of the LORD.  
Amos 6:11 For, behold, the LORD commandeth, and he will smite the great house with breaches, and the little house with clefts.  
Amos 6:12 Shall horses run upon the rock? will one plow there with oxen?  for ye have turned judgment into gall, and the **fruit** of **righteousness** into hemlock: 
Amos 6:13 Ye which rejoice in a thing of nought, which say, Have we not taken to us horns by our own strength?  
Amos 6:14 But, behold, I will raise up against you a nation, O house of Israel, saith the LORD the God of hosts; and they shall afflict you from the entering in of Hemath unto the river of the wilderness.  
Amos 7:1 Thus hath the Lord GOD shewed unto me; and, behold, he formed grasshoppers in the beginning of the shooting up of the latter growth; and, lo, it was the latter growth after the king's mowings.  
Amos 7:2 And it came to pass, that when they had made an end of eating the grass of the land, then I said, O Lord GOD, forgive, I beseech thee: by whom shall Jacob arise? for he is small.  
Amos 7:3 The LORD repented for this: It shall not be, saith the LORD.  
    ``--``
Obadiah 1:4 Though thou exalt thyself as the eagle, and though thou set thy nest among the stars, thence will I bring thee down, saith the LORD.  
    ``--``
Micah 6:2 Hear ye, O mountains, the LORD's controversy, and ye strong foundations of the earth: for the LORD hath a controversy with his people, and he will plead with Israel.  
Micah 6:3 O my people, what have I done unto thee? and wherein have I wearied thee? testify against me.  
Micah 6:4 For I brought thee up out of the land of Egypt, and redeemed thee out of the house of servants; and I sent before thee Moses, Aaron, and Miriam.  
Micah 6:5 O my people, remember now what Balak king of Moab consulted, and what Balaam the son of Beor answered him from Shittim unto Gilgal; that ye may know the **righteousness** of the LORD.  
Micah 6:6 Wherewith shall I come before the LORD, and bow myself before the high God? shall I come before him with burnt offerings, with calves of a year old?  
Micah 6:7 Will the LORD be pleased with thousands of rams, or with ten thousands of rivers of oil? shall I give my firstborn for my transgression, the **fruit** of my body for the sin of my soul?  
Micah 6:8 He hath shewed thee, O man, what is good; and what doth the LORD require of thee, but to do justly, and to love mercy, and to walk humbly with thy God?  
Micah 6:9 The LORD's voice crieth unto the city, and the man of wisdom shall see thy name: hear ye the rod, and who hath appointed it.  
Micah 6:10 Are there yet the treasures of wickedness in the house of the wicked, and the scant measure that is abominable?  
    ``--`` 
Micah 7:4 The best of them is as a brier: the most upright is sharper than a thorn hedge: the day of thy watchmen and thy visitation cometh; now shall be their perplexity.  
Micah 7:5 Trust ye not in a friend, put ye not confidence in a guide: keep the doors of thy mouth from her that lieth in thy bosom.  
Micah 7:6 For the son dishonoureth the father, the daughter riseth up against her mother, the daughter in law against her mother in law; a man's enemies are the men of his own house.  
    ``--`` 
Micah 7:8 Rejoice not against me, O mine enemy: when I fall, I shall arise; when I sit in darkness, the LORD shall be a light unto me.  
Micah 7:9 I will bear the indignation of the LORD, because I have sinned against him, until he plead my cause, and execute judgment for me: he will bring me forth to the light, and I shall behold his **righteousness**.  
Micah 7:10 Then she that is mine enemy shall see it, and shame shall cover her which said unto me, Where is the LORD thy God? mine eyes shall behold her: now shall she be trodden down as the mire of the streets.  
Micah 7:11 In the day that thy walls are to be built, in that day shall the decree be far removed.  
Micah 7:12 In that day also he shall come even to thee from Assyria, and from the fortified cities, and from the fortress even to the river, and from sea to sea, and from mountain to mountain.  
Micah 7:13 Notwithstanding the land shall be desolate because of them that dwell therein, for the **fruit** of their doings.  
Micah 7:14 Feed thy people with thy rod, the flock of thine heritage, which dwell solitarily in the wood, in the midst of Carmel: let them feed in Bashan and Gilead, as in the days of old.  
    ``--`` 
Haggai 1:13 Then spake Haggai the LORD's messenger in the LORD's message unto the people, saying, I am with you, saith the LORD.  
Haggai 1:14 And the LORD stirred up the spirit of Zerubbabel the son of Shealtiel, governor of Judah, and the spirit of Joshua the son of Josedech, the high priest, and the spirit of all the remnant of the people; and they came and did work in the house of the LORD of hosts, their God, 
Haggai 1:15 In the four and twentieth day of the sixth month, in the second year of Darius the king.  
    ``--`` 
Zechariah 8:7 Thus saith the LORD of hosts; Behold, I will save my people from the east country, and from the west country; 
Zechariah 8:8 And I will bring them, and they shall dwell in the midst of Jerusalem: and they shall be my people, and I will be their God, in truth and in **righteousness**.  
Zechariah 8:9 Thus saith the LORD of hosts; Let your hands be strong, ye that hear in these days these words by the mouth of the prophets, which were in the day that the foundation of the house of the LORD of hosts was laid, that the temple might be built.  
Zechariah 8:10 For before these days there was no hire for man, nor any hire for beast; neither was there any peace to him that went out or came in because of the affliction: for I set all men every one against his neighbour.  
Zechariah 8:11 But now I will not be unto the residue of this people as in the former days, saith the LORD of hosts.  
Zechariah 8:12 For the seed shall be prosperous; the vine shall give her **fruit**, and the ground shall give her increase, and the heavens shall give their dew; and I will cause the remnant of this people to possess all these things.  
Zechariah 8:13 And it shall come to pass, that as ye were a curse among the heathen, O house of Judah, and house of Israel; so will I save you, and ye shall be a blessing: fear not, but let your hands be strong.  
    ``--`` 
Matthew 3:10 And now also the axe is laid unto the root of the trees: therefore every tree which bringeth not forth good **fruit** is hewn down, and cast into the fire.  
Matthew 3:11 I indeed baptize you with water unto repentance: but he that cometh after me is mightier than I, whose shoes I am not worthy to bear: he shall baptize you with the Holy Ghost, and with fire: 
Matthew 3:12 Whose fan is in his hand, and he will throughly purge his floor, and gather his wheat into the garner; but he will burn up the chaff with unquenchable fire.  
Matthew 3:13 Then cometh Jesus from Galilee to Jordan unto John, to be baptized of him.  
Matthew 3:14 But John forbad him, saying, I have need to be baptized of thee, and comest thou to me?  
Matthew 3:15 And Jesus answering said unto him, Suffer it to be so now: for thus it becometh us to fulfil all **righteousness**. Then he suffered him.  
    ``--`` 
Matthew 7:11 If ye then, being evil, know how to give good gifts unto your children, how much more shall your Father which is in heaven give good things to them that ask him?  
Matthew 7:12 Therefore all things whatsoever ye would that men should do to you, do ye even so to them: for this is the law and the prophets.  
Matthew 7:13 Enter ye in at the strait gate: for wide is the gate, and broad is the way, that leadeth to destruction, and many there be which go in thereat: 
Matthew 7:14 Because strait is the gate, and narrow is the way, which leadeth unto life, and few there be that find it.  
    ``--``
Matthew 21:24 And Jesus answered and said unto them, I also will ask you one thing, which if ye tell me, I in like wise will tell you by what authority I do these things.  
    ``--``
Matthew 21:29 He answered and said, I will not: but afterward he repented, and went.  
Matthew 21:30 And he came to the second, and said likewise. And he answered and said, I go, sir: and went not.  
Matthew 21:31 Whether of them twain did the will of his father? They say unto him, The first. Jesus saith unto them, Verily I say unto you, That the publicans and the harlots go into the kingdom of God before you.  
Matthew 21:32 For John came unto you in the way of **righteousness**, and ye believed him not: but the publicans and the harlots believed him: and ye, when ye had seen it, repented not afterward, that ye might believe him.  
Matthew 21:33 Hear another parable: There was a certain householder, which planted a vineyard, and hedged it round about, and digged a winepress in it, and built a tower, and let it out to husbandmen, and went into a far country: 
Matthew 21:34 And when the time of the **fruit** drew near, he sent his servants to the husbandmen, that they might receive the **fruit**s of it.  
Matthew 21:35 And the husbandmen took his servants, and beat one, and killed another, and stoned another.  
Matthew 21:36 Again, he sent other servants more than the first: and they did unto them likewise.  
Matthew 21:37 But last of all he sent unto them his son, saying, They will reverence my son.  
    ``--`` 
Romans 1:12 That is, that I may be comforted together with you by the mutual faith both of you and me.  
Romans 1:13 Now I would not have you ignorant, brethren, that oftentimes I purposed to come unto you, (but was let hitherto,) that I might have some **fruit** among you also, even as among other Gentiles.  
Romans 1:14 I am debtor both to the Greeks, and to the Barbarians; both to the wise, and to the unwise.  
Romans 1:15 So, as much as in me is, I am ready to preach the gospel to you that are at Rome also.  
Romans 1:16 For I am not ashamed of the gospel of Christ: for it is the power of God unto salvation to every one that believeth; to the Jew first, and also to the Greek.  
Romans 1:17 For therein is the **righteousness** of God revealed from faith to faith: as it is written, The just shall live by faith.  
Romans 1:18 For the wrath of God is revealed from heaven against all ungodliness and un**righteousness** of men, who hold the truth in unrighteousness; 
    ``--`` 
Romans 6:16 Know ye not, that to whom ye yield yourselves servants to obey, his servants ye are to whom ye obey; whether of sin unto death, or of obedience unto **righteousness**?  
Romans 6:17 But God be thanked, that ye were the servants of sin, but ye have obeyed from the heart that form of doctrine which was delivered you.  
Romans 6:18 Being then made free from sin, ye became the servants of **righteousness**.  
Romans 6:19 I speak after the manner of men because of the infirmity of your flesh: for as ye have yielded your members servants to uncleanness and to iniquity unto iniquity; even so now yield your members servants to **righteousness** unto holiness.  
Romans 6:20 For when ye were the servants of sin, ye were free from **righteousness**.  
Romans 6:21 What **fruit** had ye then in those things whereof ye are now ashamed? for the end of those things is death.  
Romans 6:22 But now being made free from sin, and become servants to God, ye have your **fruit** unto holiness, and the end everlasting life.  
Romans 6:23 For the wages of sin is death; but the gift of God is eternal life through Jesus Christ our Lord.  
Romans 7:1 Know ye not, brethren, (for I speak to them that know the law,) how that the law hath dominion over a man as long as he liveth?  
Romans 7:2 For the woman which hath an husband is bound by the law to her husband so long as he liveth; but if the husband be dead, she is loosed from the law of her husband.  
    ``--`` 
    ``--`` 
2 Corinthians 9:5 Therefore I thought it necessary to exhort the brethren, that they would go before unto you, and make up beforehand your bounty, whereof ye had notice before, that the same might be ready, as a matter of bounty, and not as of covetousness.  
2 Corinthians 9:6 But this I say, He which soweth sparingly shall reap also sparingly; and he which soweth bountifully shall reap also bountifully.  
2 Corinthians 9:7 Every man according as he purposeth in his heart, so let him give; not grudgingly, or of necessity: for God loveth a cheerful giver.  
2 Corinthians 9:8 And God is able to make all grace abound toward you; that ye, always having all sufficiency in all things, may abound to every good work: 
2 Corinthians 9:9 (As it is written, He hath dispersed abroad; he hath given to the poor: his **righteousness** remaineth for ever.  
2 Corinthians 9:10 Now he that ministereth seed to the sower both minister bread for your food, and multiply your seed sown, and increase the **fruit**s of your **righteousness**;) 
2 Corinthians 9:11 Being enriched in every thing to all bountifulness, which causeth through us thanksgiving to God.  
2 Corinthians 9:12 For the administration of this service not only supplieth the want of the saints, but is abundant also by many thanksgivings unto God; 
2 Corinthians 9:13 Whiles by the experiment of this ministration they glorify God for your professed subjection unto the gospel of Christ, and for your liberal distribution unto them, and unto all men; 
2 Corinthians 9:14 And by their prayer for you, which long after you for the exceeding grace of God in you.  
2 Corinthians 9:15 Thanks be unto God for his unspeakable gift.  
    ``--`` 
Ephesians 5:4 Neither filthiness, nor foolish talking, nor jesting, which are not convenient: but rather giving of thanks.  
Ephesians 5:5 For this ye know, that no whoremonger, nor unclean person, nor covetous man, who is an idolater, hath any inheritance in the kingdom of Christ and of God.  
Ephesians 5:6 Let no man deceive you with vain words: for because of these things cometh the wrath of God upon the children of disobedience.  
Ephesians 5:7 Be not ye therefore partakers with them.  
Ephesians 5:8 For ye were sometimes darkness, but now are ye light in the Lord: walk as children of light: 
Ephesians 5:9 (For the **fruit** of the Spirit is in all goodness and **righteousness** and truth;) 
Ephesians 5:10 Proving what is acceptable unto the Lord.  
Ephesians 5:11 And have no fellowship with the un**fruit**ful works of darkness, but rather reprove them.  
Ephesians 5:12 For it is a shame even to speak of those things which are done of them in secret.  
Ephesians 5:13 But all things that are reproved are made manifest by the light: for whatsoever doth make manifest is light.  
Ephesians 5:14 Wherefore he saith, Awake thou that sleepest, and arise from the dead, and Christ shall give thee light.  
    ``--`` 
Philippians 1:6 Being confident of this very thing, that he which hath begun a good work in you will perform it until the day of Jesus Christ: 
Philippians 1:7 Even as it is meet for me to think this of you all, because I have you in my heart; inasmuch as both in my bonds, and in the defence and confirmation of the gospel, ye all are partakers of my grace.  
Philippians 1:8 For God is my record, how greatly I long after you all in the bowels of Jesus Christ.  
Philippians 1:9 And this I pray, that your love may abound yet more and more in knowledge and in all judgment; 
Philippians 1:10 That ye may approve things that are excellent; that ye may be sincere and without offence till the day of Christ.  
Philippians 1:11 Being filled with the **fruit**s of **righteousness**, which are by Jesus Christ, unto the glory and praise of God.  
Philippians 1:12 But I would ye should understand, brethren, that the things which happened unto me have fallen out rather unto the furtherance of the gospel; 
Philippians 1:13 So that my bonds in Christ are manifest in all the palace, and in all other places; 
Philippians 1:14 And many of the brethren in the Lord, waxing confident by my bonds, are much more bold to speak the word without fear.  
Philippians 1:15 Some indeed preach Christ even of envy and strife; and some also of good will: 
Philippians 1:16 The one preach Christ of contention, not sincerely, supposing to add affliction to my bonds: 
    ``--`` 
Hebrews 12:6 For whom the Lord loveth he chasteneth, and scourgeth every son whom he receiveth.  
Hebrews 12:7 If ye endure chastening, God dealeth with you as with sons; for what son is he whom the father chasteneth not?  
Hebrews 12:8 But if ye be without chastisement, whereof all are partakers, then are ye bastards, and not sons.  
Hebrews 12:9 Furthermore we have had fathers of our flesh which corrected us, and we gave them reverence: shall we not much rather be in subjection unto the Father of spirits, and live?  
Hebrews 12:10 For they verily for a few days chastened us after their own pleasure; but he for our profit, that we might be partakers of his holiness.  
Hebrews 12:11 Now no chastening for the present seemeth to be joyous, but grievous: nevertheless afterward it yieldeth the peaceable **fruit** of **righteousness** unto them which are exercised thereby.  
Hebrews 12:12 Wherefore lift up the hands which hang down, and the feeble knees; 
Hebrews 12:13 And make straight paths for your feet, lest that which is lame be turned out of the way; but let it rather be healed.  
Hebrews 12:14 Follow peace with all men, and holiness, without which no man shall see the Lord: 
Hebrews 12:15 Looking diligently lest any man fail of the grace of God; lest any root of bitterness springing up trouble you, and thereby many be defiled; 
Hebrews 12:16 Lest there be any fornicator, or profane person, as Esau, who for one morsel of meat sold his birthright.  
    ``--`` 
James 3:13 Who is a wise man and endued with knowledge among you? let him shew out of a good conversation his works with meekness of wisdom.  
James 3:14 But if ye have bitter envying and strife in your hearts, glory not, and lie not against the truth.  
James 3:15 This wisdom descendeth not from above, but is earthly, sensual, devilish.  
James 3:16 For where envying and strife is, there is confusion and every evil work.  
James 3:17 But the wisdom that is from above is first pure, then peaceable, gentle, and easy to be intreated, full of mercy and good **fruit**s, without partiality, and without hypocrisy.  
James 3:18 And the **fruit** of **righteousness** is sown in peace of them that make peace.  
James 4:1 From whence come wars and fightings among you? come they not hence, even of your lusts that war in your members?  
James 4:2 Ye lust, and have not: ye kill, and desire to have, and cannot obtain: ye fight and war, yet ye have not, because ye ask not.  
James 4:3 Ye ask, and receive not, because ye ask amiss, that ye may consume it upon your lusts.  
James 4:4 Ye adulterers and adulteresses, know ye not that the friendship of the world is enmity with God? whosoever therefore will be a friend of the world is the enemy of God.  
James 4:5 Do ye think that the scripture saith in vain, The spirit that dwelleth in us lusteth to envy?  

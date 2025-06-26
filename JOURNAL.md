---
title: "glyph"
author: "@hex4"
description: "[ a custom split keyboard for portably and comfortably interfacing with computer systems ] "
created_at: "2025-05-23"
---

# [ JOURNAL_ ]

## [ MAY 27: IDEA ]

![20250527_163805](https://github.com/user-attachments/assets/579e4fdf-607c-4d9c-a123-cc6cfc335620)

![20250527_163744](https://github.com/user-attachments/assets/a831da7a-0973-4c5f-93ca-46ca8e02de78)


Hello world! I'm working on Glyph, a fun, portable, and comfortable split keyboard. It's the logical next step after designing and fixing the Hexapad. In this session I mostly just worked on the layout and gimmick of the keyboard. The key assignment isn't done yet but I want to start on the PCB now so I'll save that for later. Glyph has a finger-staggered main matrix of 6x3, and a key and joystick for each thumb. The joystick is the main gimmick of the board - you'll use it to switch layers and navigate documents. I started designing in FigJam but realized it would be hard to match up with my hands so I moved to using my notebook instead. While the keymap isn't complete, I'd like to have a layer for symbols, specials, and metas. Symbols include the number row and misc symbols like +, - and =. Specials - accessible with the right thumb - are brackets, quotation marks, /, and other common programming symbols. Meta keys are keys that adjust the keyboard, like RGB.

**[hours worked this session: 1]**

**[total: 1]**

## [ MAY 29: BASICS ]

Hey again! Today I'm going to be working on the basic skeleton of the left half of the keyboard. In my spare time I've been trying to find a suitable joystick - first googling around for one I found on Adafruit ([this one](https://www.adafruit.com/product/512)), then realizing SnapMagic exists and searching there. I eventually settled on the [COM-09032](https://www.snapeda.com/parts/COM-09032/SparkFun%20Electronics/view-part/). I then spent a LONG time trying to figure out how to get the symbol and footprint into KiCad from SnapMagic. After trying a bunch of different things (turns out there IS a kicad plugin but it's for an ancient version) I figured out how to import a footprint and started on design.

![image](https://github.com/user-attachments/assets/a510623c-de91-4f6f-8261-4786f6660957)

For glyph I'm going to be using a Raspberry Pi Pico - I have a bunch of them and they have plenty of I/O and are easy to work with. After spending a fair bit finding a reference for the matrix (ended up taking a screenshot of the Hexapad's matrix and using that) I got to work popping the switches down!

![image](https://github.com/user-attachments/assets/c47320f6-371b-49a2-820f-e2081a21fcd0)

This was mostly just copying and pasting. Then I researched how to use a joystick with Pico, and after tracking down a broken link on SparkFun's product page, arrived at this wiring:

![image](https://github.com/user-attachments/assets/171e84b0-5b02-46cd-bfeb-33cb3db54e79)

_(side note: the sparkfun product page included [an explanation of how the joystick worked](https://learn.sparkfun.com/tutorials/thumb-joystick-hookup-guide/how-does-an-analog-thumb-joystick-work), which i found super neat)_

And to finish today off, I quickly added the thumb button:

![image](https://github.com/user-attachments/assets/d809ff7c-a0ac-4345-90a4-d4d2b0ab3b0e)

Tomorrow (which is friday :yay:) I'll add the RGB and start on the PCB design - hopefully I can knock out the entire PCB this weekend and only need to finish the case and firmware!

**[hours worked this session: 2]**

**[total: 3]**

## [ MAY 31 // GLOW ]

_[note: I forgot to save while writing this so I'm rewriting this entry from memory on Jun 2]_

Hai :3! Today I'll add the RGB and start on the case design. I started researching different NeoPixel-style LEDs - I wanted something small but still reasonably hand-solderable. Instead of doing perkey RGB, which takes a lot of resources and a lot of soldering, I'm going to do something like an "underglow" with 6 RGB LEDs on each side. However, the Adafruit docs say you need a 0.1uF capacitor for each neopixel, which was pretty annoying for the Hexapad. But the docs also say in some cases you can do 1 cap to 2 LEDs, knocking it down to 3 caps per side, which I'm comfortable with. I googled around ([these ones](https://www.adafruit.com/product/2758) were pretty common but looked hard to solder), and eventually found [these](https://www.adafruit.com/product/4960) NeoPixels with nice, long legs that should be good for hand-soldering. Turns out these are actually the reverse-mount LEDs people were using for their hackpads! After debugging a weird KiCad crash (and it magically working again 🙄) I imported the ScottoKeebs library and had a slight struggle wiring up the neopixels with 1 cap per pair. Some digging made why the cap was needed "click" and I found that I was doing it all wrong. Here's the final, corrected wiring I ended up with:

![image](https://github.com/user-attachments/assets/a585ffe0-121e-4046-a948-f50af4775701)

To finish off today I assigned all the footprints (using hotswaps for the switches) and moved to the PCB editor.

![image](https://github.com/user-attachments/assets/0a349d16-92f6-4973-8ba7-0d8c728a92b8)

**[hours worked this session: 1]**

**[total: 4]**

## [ JUN 4 // ARRANGEMENTS ]

_[ done in the Highway Roadtrip call! ]_

I was just about to start laying out the PCB, when I realized... the PCB needs a way to talk to the other half of the keyboard. After some googling around I came across a Reddit thread suggesting UART, which doesn't need pullup resistors. Nice! This also fits perfectly with a TRRS jack (power, tx, rx, and gnd), so I used the ScottoKeebs TRRS symbol.

![image](https://github.com/user-attachments/assets/fbc98ec0-6ab6-4993-9a33-705b93becb5e)

I put it in to the Kicad PCB editor and struggled to setup the grid properly so I could lay out the keyswitches. After (eventually) fixing the snapping settings to make it work I started laying down the switches:

![image](https://github.com/user-attachments/assets/4386d854-1c2b-44bf-94e6-5f3575548d47)


... and promptly realized I wasn't doing them in the correct order. Quickly fixing them (it was actually quite relaxing), here it is:
![image](https://github.com/user-attachments/assets/60ebe14c-8a90-415d-9319-d805d605a58c)

I then added the diodes (KiCad crashed while doing this! Scary! But luckily it autosaved my work and I didn't lose much), and arranged the other parts. The RGB is in three corners and I found a lovely spot for the Pico and TRRS jack.

![image](https://github.com/user-attachments/assets/cd76b518-9355-4777-a5f6-0ea955392d28)

That's all for today! Tomorrow I'll route the whole thing (!!), print it out to test for fit, and get to work on the right side.


**[hours worked this session: 1.5]**

**[total: 5.5]**

## [ JUN 9 // ROUTING ]

Hello!

I booted up Kicad and started getting ready for routing. First, I noticed that the hotswap sockets... were on the back of the PCB? That didn't look right. But after some googling I found that these actually _were_ supposed to go on the back of the board. As well during my research, I found that millmax 0305s were a pretty popular hotswap option, but ended up deciding against them because it would mean a lot more soldering. Flipping all the components to the sides they were supposed to be on, I assigned 3D models to some of the parts:

![image](https://github.com/user-attachments/assets/fcf09a51-1cdb-4a97-b598-17eb52382bb5)

On to routing! This time for Glyph I'm going to manually route everything because when I used an autorouter for the Hexapad it produced some... interesting results. Some searching around on Reddit produced [this thread](https://www.reddit.com/r/MechanicalKeyboards/comments/fxupwp/need_help_with_pcb_design/) which suggested some track widths I'm comfortable with. I'm also going to try a ground pour with Glyph, which should make routing a little less painful.

I also edited some footprints to make them easier to solder:
![image](https://github.com/user-attachments/assets/fc846092-306c-4b48-bada-08bbe5d6c4bb)

When I started routing I realized I still needed to print out the PCB to check for fit. But my printer was out of ink, so I did what any normal person would do, and taped a piece of paper to my screen and traced out all the keys.

After painstakingly replicating my layout, I checked it against my hand and it was pretty comfy! So I switched back to routing.

There isn't really much to say about this other than that it was very relaxing.

![image](https://github.com/user-attachments/assets/b69d1f64-893e-480a-993c-9aec1bce5a2b)

Chonky 3v3 lines for the LEDs:
![image](https://github.com/user-attachments/assets/6c9b8912-edc8-4920-a9cd-2e32e22de975)

With only a few routes left, I ran DRC and got this strange hole clearance error. The ScottoKeebs footprint put a NPTH REALLY close to the pin hole. Weird. I spent a lot of time trying a lot of different things and ended up removing the board-wide clearance for copper-to-hole. The netclass still has a 0.2mm clearance and this allows the footprint's clearance override (which I'm assuming is to fix this problem) to take effect.

There were a few more DRC track clearance errors, so I fixed those up. Some clearance-fixing and routing later, Glyph[Left] v0 is done! Apart from the PCB art and outline, of course.

**[hours worked this session: 2]**

**[total: 7.5]**

## [ JUN 14 // REPLICATION ]

Today I'm going to finish both sides of the PCB! This includes the PCB art, and then completely duplicating and flipping the design.

I started up Figma and did some light finagling to get to this:
![image](https://github.com/user-attachments/assets/1a642241-3d32-46e4-9e7c-2482bd0f924e)

On the PCB:

![image](https://github.com/user-attachments/assets/29cfb4ac-02ac-4980-a31d-ff5f875d0a4a)

I then duplicated the left folder and renamed everything, and started rearranging the right side PCB to match my sketch. During a quick break, it occured to me that I should make sure that my keyboard switches match a 1u grid. I know I tried to do this back when I was laying them out, but KiCad grids are hard.

Checking each switch with the Ruler tool, I noticed one particular one that was a teensy bit off. I spent WAY too long fiddling with KiCad's snapping settings trying to get this to move, but eventually I lined it back up again.

![image](https://github.com/user-attachments/assets/5d2fc1a4-8c20-4f5f-afa7-7fa665ae75df)

Turns out this was a VERY good idea! A lot of other switches were off by a little bit. I also made the thumb switch match the grid. I duplicated the left project once again, and started my rearrangement. 
![image](https://github.com/user-attachments/assets/2bc90569-8d0e-4d28-ad8e-fdbbe38fdcd5)

Now, to reroute the whole right side. Luckily I had a pretty good idea of what to do here (what order, trace widths, etc) so it went quicker than last time.

I used a LOT of vias, but after a bunch of routing, I got to 0 DRC errors. Amazing!

Updating the silkscreen art, here's the full right side:

![image](https://github.com/user-attachments/assets/b71dd5f9-0208-4481-a270-c39127b31893)

That concludes the PCB section of this journal! Now onto the case. I use OnShape for CAD, so I started a new project (with tabs for the left and right sides). I then hopped into Keyboard Layout Editor to try and replicate my design. Here it is for the left side :3

![image](https://github.com/user-attachments/assets/88f9a788-7897-4054-b1f6-b03bdb039744)

That's all for today! Glyph is getting closer to fruition. All that's left is the case and firmware. See you then!

**[hours worked this session: 2.5]**

**[total: 10]**

## [ JUN 20 // MICRO ]

Hey again! Today i'm going to try to finish both cases. Then I'll be ready for firmware tomorrow and submission the day after. 

To start this session off, I exported the left-side PCB and tried to put it into OnShape. The file was really complex and slowed down the website a lot, so I had to re-export in KiCad with some settings disabled. A lot of settings-tweaking later, I ended up compositing the PCB model in its own tab and deriving that in my main tab.

![image](https://github.com/user-attachments/assets/d4f484ba-3fba-4d10-acf0-ef3a9e62bf35)

I got a plate from the ai03 plate generator and dropped it into an Assembly with the PCB. Checking for fit, I noticed that I had messed up some of the switch positions in KLE! I edited that, reimported, and got here: ![image](https://github.com/user-attachments/assets/9ef30ea6-457b-463e-a93c-c5d8ff4ac3eb)

In the cross-section view you can see that there's no spot for the joystick, which isn't good! Like the Hexapad, I'm doing a sandwich mount minus the top frame, which means I need to make a hole for the joystick. I quickly added that and spent a while fighting OnShape about which point to move after editing a dimension, I managed to make the plate a little smaller:

![image](https://github.com/user-attachments/assets/1eb81983-3a64-4a7a-9343-96d425418442)

Some more dimensioning and cutting brought me to this. I also made the cutout for the joystick a hexagon, which I think looks really cool. I'll probably have that hexagon extend into the full case. However, I have to think about how I'm going to fit everything else - namely the Pico, RGB and TRRS jack, into the case.

![image](https://github.com/user-attachments/assets/172db701-fc59-497d-bc91-0fd94df11d00)

Alright, so due to a lot of interruptions I didn't have much time today, but I think I'll be able to finish the case tomorrow, firmware on Sunday, and submit on Monday. Let's see how that goes. You can find my OnShape design [here](https://cad.onshape.com/documents/a309a43e7ab9d98fd3e56af4/w/ec765f4ff1bc21db4a251eb8/e/584204243a6751a6ad9ca171?renderMode=0&uiState=68562695e7134e26808a7204), I'll add it to the readme later.

**[hours worked this session: 0.5]**

**[total: 10.5]**


## [ JUN 21 // MODEL ]

I was thinking about Glyph last night, and remembered that I needed to change the power circuitry for the right side. Right now power goes to VBUS, which can work but will explode if ever connected to USB. Not good! I booted up kicad once more to update that schematic and PCB. Luckily this was a fairly easy change since the VBUS and VSYS pins are right next to each other on the Pico. I then switched back to OnShape to continue on the case. Extending the hexagon shape and outlining the case, I started to build up the other parts and sides:

![image](https://github.com/user-attachments/assets/db7761dd-faac-443a-a23c-63dbf8ca480a)

When making the walls, I needed to check how tall they should be to fit the Pico. For some reason KiCad didn't include a 3D model of the Pi Pico, so I set out to find one on GrabCAD, and got [this one](https://grabcad.com/library/raspberry-pi-pico-w-pins-1). I had to sign up for an account to download (why the hack do you need my phone number????), but eventually got it into my main assembly in OnShape. Some light translation got me here:

![image](https://github.com/user-attachments/assets/d0e305cc-75e7-431c-ac44-764d42179067)

I then quickly added the bottom of the case, and then set my sights on the USB hole and TRRS hole. Sadly, the TRRS hole will have to go through the hexagon cutout (which looks ugly) because the jack is too tall. My CAD software produced some... unique results:

![image](https://github.com/user-attachments/assets/1ae38c97-780d-4555-a60f-48d78b8dcb99)

To finish up today, I cleaned up the case a little and made the bottom side smaller so the hexagon pattern could stick out more.

That's all! I didn't get as much as I wanted to done, but I *think* I'll be able to get the case and basic firmware done on Sunday.

**[hours worked this session: 1.5]**

**[total: 12]**

## [ JUN 22 // ALMOST ]

Screw holes!

I was missing screw holes in my case. But before I fixed that, I tweaked some dimensions in the sketch to make the hexagon more prounounced. I then turned to the screw holes. I already have some M4 nuts and bolts from the Hexapad, so I tried to find their specs. The hole itself was quite easy - M4 means 4mm. But I had to do a lot more digging to find the specs for my nut, and ended up on [this ISO specs page](https://www.engineersedge.com/hardware/standard_metric_hex_nuts_13728.htm)
![image](https://github.com/user-attachments/assets/2f932869-a7ce-42d3-96e8-f9e70826113e)

Holding the nuts up to a ruler (because i don't have callipers :noo:), it looked like they were 3mm tall and 7mm from flat-to-flat, which matches up with the min/maxes on the table. I fought OnShape to expand the walls (it's probably just my terrible sketching skills) and sketch the holes:

![image](https://github.com/user-attachments/assets/0b801dda-6234-439d-ae29-df96812431ff)

I also split the case into two and connected them together with OnShape's very nice mate system. Next up is the USB hole. I did this the same way I did for the Hexapad - creating a new sketch with a rectangle, and using a remove extrude to cut out a hole. It felt quite refreshing to work in a sketch that wasn't the absolute mess of my plate!

![image](https://github.com/user-attachments/assets/9780194d-43d2-4296-90ec-3b85758a614a)

Originally I was going do to something similar to the Hexapad, with outset text on top:
![image](https://github.com/user-attachments/assets/2190a8a7-7c40-44a7-acc1-78b49d3380ae)

But I think this time I'll put the text on the sides. It looks way cooler and sleeker:

![image](https://github.com/user-attachments/assets/e22d9e20-ae09-4b40-87cb-0e4bcc0589ed)

While I was doing this I had to figure out how to flip a sketch (I was drawing on the left side and my plane was the right plane.), and learnt that sketches could use mate connectors as planes. I flipped a mateconnector until the sketch was correctly oriented, and ended up with this really nice effect!

Now onto filleting. While filleting the top plate I misclicked and selected a face instead of an edge, producing a "pillowy" effect I'm quite fond of. However, when I tried to apply this to the entire thing, I ran into a fillet error on one of the sides. This side, for whatever reason during my terrible sketching, was two faces split by an edge. Some research led me to the "delete face" tool, which worked perfectly and allowed me to finish this really neat touch:

![image](https://github.com/user-attachments/assets/56ccead8-42f8-41a2-8362-ca2ac5691177)

I then filleted out everything else, and the left-side case is done!

![image](https://github.com/user-attachments/assets/552d3e6a-8c22-45f1-96d0-72c55c6efd26)

Onto the right case. I wanted to see if I could be lazy and just flip my left design and tweak a few positions, so I imported the right PCB and duplicated my Part Studio, deleting everything except the sketch and mirroring it. If this flip works, and there are no major changes that need to be made, it would save me hours.

It frickin' worked.

I re-extruded and tweaked some sizes to fit the slightly different part locations on the new PCB, then tried to add more clearance for the top and right sides, which the board was clipping into. The top side worked easily but I had to (yet again) fight my CAD software to let me re-dimension the right side. It was very annoying but I did learn about driven (like a ruler) and driving (forces the sketch to change) dimensions. No need for a USB port on this side, so I skipped to the text inset:

![image](https://github.com/user-attachments/assets/aee28c9c-c982-4158-9032-d97239cee12e)

To finish up the case, I filleted everything up:

![image](https://github.com/user-attachments/assets/dfc7e81b-9b31-403f-b535-e836526512d0)

And that's it for the Glyph case!

This was a huge entry, but Glyph is almost done. I can see the light at the end of the tunnel.

Firmware's up next.


**[hours worked this session: 3]**

**[total: 15]**

## [ JUN 25 // FINALITY (?) ]

School's out!

I'm hoping to submit today. Flights to Undercity are getting expensive and review takes 3-4 days, so I need to lock in. Before the firmware, though, I needed a basic layout. After cleaning my hideous (🫣) desk, I opened my notebook back up and tweaked the layout from the first entry.

Now onto which firmware to use. Joysticks aren't very common on keyboards so I need something that's either really extensible or has lots of support. QMK has lots of features but hurts my brain, and ZMK doesn't have wired support. KMK it is then! It has a split keyboard module (w/ UART over TRRS which is great) and I can just write (or copy :3) some circuitpython to get joystick support. I hopped over to their [guide](https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/Getting_Started.md), made two folders for the two halves, and scaffolded each one. I then opened up my schematic to have available as I mapped, and imported the HoldTap module for my space-shift key. Here's the main keymap:

![image](https://github.com/user-attachments/assets/e710345e-b550-43fc-8b7c-f351f1a51038)

Next up is RGB. This was quite easy, I just pasted in the RGB code from the docs and set `rgb.animation_mode = "rainbow"` which is a nice default. Now, I need to figure out how to get my thumb key working. I don't think KMK has support for some switches being directly wired, so I searched their Zulip and found nothing except rewriting the pin-scanning class, which I did not want to do. However, KMK has encoder support, and I have unused pins on my Pico. What if I did an epic hack and pretended an encoder was there, but it actually was just a switch? I added an encoder and I don't see any problems with using HoldTap with it, so I guess this hack would work. Now, all that's left is the joystick and split config, then copying it over to the second half.

I searched around and found this [thumbstick module](https://github.com/Ben0981/kmk_firmware/blob/module_thumbstick/kmk/modules/thumbstick.py), which I downloaded and put into both my folders. I changed the pin definitions to suit me and it was done! Finally for this side's firmware, I imported the Split module and set it up.

I then duplicated the file for the right-side firmware, edited the keymap to match my notebook, and just like that, **[glyph] is - somehow - done!!!**

Tomorrow will be getting everything ready for submission and finding part sources.

See you then!

**[hours worked this session: 2]**

**[total: 17]**




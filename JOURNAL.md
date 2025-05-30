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



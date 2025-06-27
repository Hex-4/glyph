# [ GLYPH_ ]
[ a custom split keyboard ]

[ for portably and comfortably interfacing with computing systems ]

Glyph is the keyboard I wish I had. It's a finger-staggered split mechanical keyboard with hotswap support, powered by the Raspberry Pi Pico and KMK firmware. The main gimmick is a joystick next to each thumb switch that acts as a novel way to switch layers, run macros, and navigate documents.

I had made the Hexapad (a macropad) before, but I wanted something to replace my Keychron. It was a pretty nice board, but it had a boring standard layout, non-customizable firmware, and no extra features apart from a per-key white backlight. I saw a video on youtube about someone making their own custom split keyboard, and that planted the seed in my head. When Highway was announced I was sure that this would be my first project. Glyph has a 6x3 main grid on each side, and instead of a vanilla thumb cluster, it has one thumb button and a joystick.

[{ visit the journal }](JOURNAL.md)

[{ left pcb }](https://kicanvas.org/?github=https://github.com/Hex-4/glyph/tree/main/PCB/left)

[{ right pcb }](https://kicanvas.org/?github=https://github.com/Hex-4/glyph/tree/main/PCB/right)

[{ case }](https://cad.onshape.com/documents/a309a43e7ab9d98fd3e56af4/w/ec765f4ff1bc21db4a251eb8/e/62d9ee1d9fa6e5db3ba2bbb2?renderMode=0&uiState=685db91bc2e0c400d63d1642)

[ made with [Hack Club's](https://hack.club) [Highway](https://highway.hackclub.com/?ref=recNHETbc0csFrnMW), a hardware grant program for teen hackers ]

![Right Side PCB](https://github.com/user-attachments/assets/392e3c7f-0a96-42b0-aee1-6e3a2e86b603)


![Left Side PCB](https://github.com/user-attachments/assets/f55ab95c-e5f7-46ac-9f1a-36541b27a230)


![Right Side Case](https://github.com/user-attachments/assets/1bc45ad9-49ce-4f24-9420-0ca8a3af6835)

![Left Side Case](https://github.com/user-attachments/assets/2385b14f-4012-491f-b49b-93beddf2a483)

## [ BOM ]

| prices in CAD | ITEM                                | INFO                                                                     | COST PER ONE | QUANTITY                         | TOTAL COST | SOURCE                                                                                                                  |   |   |   |   |
|---------------|-------------------------------------|--------------------------------------------------------------------------|--------------|----------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------|---|---|---|---|
| COMPONENTS    | MX switches                         | It's a keyboard                                                          | $0           | 38                               | $0         | Already own                                                                                                             |   |   |   |   |
|               | Hotswap sockets                     | To swap out switches if needed                                           | $0\.15       | 40 \(comes in packs of 20\)      | $10\.68    | https://www\.aliexpress\.com/item/1005008954571807\.html?mp=1                                                           |   |   |   |   |
|               | Raspberry Pi Pico \(or equivalent\) | So that the fifteen minutes I spent writing firmware doesn't go to waste | $0           | 2                                | $0         | Already own                                                                                                             |   |   |   |   |
|               | COM\-09032 joystick                 | \[glyph\]'s gimmick                                                      | $0           | 2                                | $0         | Already own                                                                                                             |   |   |   |   |
|               | Diodes                              | The Matrix                                                               | $0\.04       | 36 \(thumbs are directly wired\) | $3\.91     | https://www\.aliexpress\.com/item/1005007131309837\.html?mp=1                                                           |   |   |   |   |
|               | TRRS jack                           | for communication with the other side                                    | $0\.29       | 10 \(will use 2\)                | $2\.89     | https://www\.aliexpress\.com/item/33029465106\.html?mp=1                                                                |   |   |   |   |
|               | Capacitors                          | for RGB                                                                  | $0\.33       | 10 \(will use 6\)                | $3\.33     | https://www\.aliexpress\.com/item/1005007842990856\.html?pdp\_ext\_f=%7B%22order%22%3A%221%22%2C%22eval%22%3A%221%22%7D |   |   |   |   |
|               | RGB LEDs                            | glowy :3                                                                 | $0\.16       | 20 \(will use 12\)               | $3\.15     | https://www\.aliexpress\.com/item/1005005193716172\.html                                                                |   |   |   |   |
|               | Components total                    |                                                                          |              |                                  | $23\.96    | AliExpress                                                                                                              |   |   |   |   |
|               |                                     |                                                                          |              |                                  |            |                                                                                                                         |   |   |   |   |
| PCB           | Left\-side PCB                      | Handwiring is hard                                                       | $12\.59      | 1                                | $12\.59    | JLCPCB                                                                                                                  |   |   |   |   |
|               | Right\-side PCB                     |                                                                          | $12\.87      | 1                                | $12\.87    | JLCPCB                                                                                                                  |   |   |   |   |
|               | Estimated shipping                  | Cheapest option                                                          | $14\.84      | 1                                | $14\.84    | JLCPCB                                                                                                                  |   |   |   |   |
|               | PCB total                           |                                                                          |              |                                  | $40\.30    |                                                                                                                         |   |   |   |   |
|               |                                     |                                                                          |              |                                  |            |                                                                                                                         |   |   |   |   |
| MISC          | M4 nuts and bolts                   |                                                                          | $0           | 16                               | $0         | Already own                                                                                                             |   |   |   |   |
|               | Keycaps                             | MOA profile for my nonstandard layout                                    | $22\.99      | 1                                | $22\.99    | https://www\.aliexpress\.com/item/1005009118477177\.html                                                                |   |   |   |   |
|               |                                     |                                                                          |              |                                  |            |                                                                                                                         |   |   |   |   |
| TOTAL         | Subtotal                            |                                                                          |              |                                  | $87\.25    |                                                                                                                         |   |   |   |   |
|               | Tax \(5% GST\)                      |                                                                          |              |                                  | $91\.61    |                                                                                                                         |   |   |   |   |
|               | Buffer                              | in case of e\.g extra taxes                                              | etc          |                                  |            | $100                                                                                                                    |   |   |   |   |


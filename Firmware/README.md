# [ GLYPH :: FIRMWARE ]

This folder stores [glyph]'s QMK firmware. Once you've [installed QMK](https://docs.qmk.fm/newbs_getting_started), simply drop this `glyph` folder into your `qmk-firmware/keyboards`. Then flash:

```
hold down the BOOT button on the left pico while plugging in. mount the drive, then:

qmk flash -kb glyph -km default -bl uf2-split-left

do the same for the right side. make sure to unplug the other side first!

qmk flash -kb glyph -km default -bl uf2-split-right
```
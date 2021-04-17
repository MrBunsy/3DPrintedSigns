# 3D Printable Multi-Colour UK Road Signs

The generate.py Python script will use generate.scad to produce a configurable list of multi-material signs. If you want to add a new sign, modify generate.py and add one to the signs list.

To make rather fetching coasters/cup mats I've scaled the round signs to 9cm diameter, keeping the 4mm thickness, and added felt to the bottom with double sided tape. Printing them in PETG should mean they're fine for hot drinks.

Since I don't own a multi-material printer I've used a variation on a technique I found on a [blog post](http://schlosshan.eu/blog/2019/03/02/prusa-i3-mk3-real-multicolour-prints-without-mmu/):
 - I added a new printer to prusa slicer, and configured it with multiple extruders.
 - I then added the custom G-code for "Tool change G-code" to be M600. This tells the printer to request the user to change the filament.
 - When exporting gcode, I manually edit the file to remove the first M600 call - otherwise the printer asks you to change the filament immediately.
 - I print the signs upside down, so the manual filament changes are over fairly quickly, and the rest of the sign can print without intervention.
 
Printing in PETG on the textured bed, with the 'front' of the sign facing down results in a very neat and tidy front surface. If you tweak the elephant's foot settings right (I found about 0.1mm worked for me) then there will be no gaps and very little colour blurring at the boundaries between colours.

Sign graphics are licenced under the [Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) and available in their original vector format from [here](https://www.gov.uk/guidance/traffic-sign-images)
include<generic_sign.scad>

BASE_FILE = "771_background.svg";
DETAIL_FILES = ["771_inner.svg","771_outline.svg"];
//[background, details...]
COLOURS = ["white","black","red"];
HEIGHT = 4;
LAYER_HEIGHT = 0.2;
MMU = true;
//only valid if MMU
GEN_ITEM = 0;
BASE_COLOUR = "white";

echo(COLOURS);

if(MMU){
	mmu_sign(GEN_ITEM, BASE_FILE, DETAIL_FILES, COLOURS, HEIGHT, LAYER_HEIGHT, BASE_COLOUR );
}else{
	layered_sign(BASE_FILE, DETAIL_FILES, COLOURS, HEIGHT, LAYER_HEIGHT);
}

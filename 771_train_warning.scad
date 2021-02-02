//include <constants.scad>


layer_height = 0.2;

background_height = 0.6;
detail_height = background_height + layer_height*1;
border_height = background_height + layer_height*2;

//somehow 0.1 of the original is about OO version of the largest version of the sign (1200mm)
scale([0.1,0.1,1]){
color("white")linear_extrude(height=background_height)hull()import("771_outline.svg");

color("black")linear_extrude(height=detail_height)import("771_inner.svg");

color("red")linear_extrude(height=border_height)import("771_outline.svg");

}

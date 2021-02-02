include <constants.scad>



color("grey")linear_extrude(height=background_height)hull()import("771_outline.svg");

color("black")linear_extrude(height=detail_height)import("771_inner.svg");

color("red")linear_extrude(height=border_height)import("771_outline.svg");



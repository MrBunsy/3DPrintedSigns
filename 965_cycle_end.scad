include <constants.scad>



color("blue")linear_extrude(height=background_height)hull()import("965.svg");

color("white")linear_extrude(height=detail_height)import("965_inner.svg");



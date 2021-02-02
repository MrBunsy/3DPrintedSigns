
module layered_sign(base_file, detail_files,colours=["white","black","red"] ,base_height = 3, colour_layer_height = 0.4){
	
	color(colours[0])linear_extrude(height=base_height)import(base_file);
	
	for(i = [0:len(detail_files)-1]){
		layer_height = base_height + (i+1)*colour_layer_height;
		
		
		color(colours[(i+1)%len(colours)])linear_extrude(height=layer_height)import(detail_files[i]);
	}
}


module mmu_sign(gen_colour,base_file, detail_files,colours=["white","black","red"] ,base_height = 3, colour_layer_height = 0.2){
	
	if(gen_colour == 0){
		//base layer
		difference(){
			color(colours[0])linear_extrude(height=base_height)import(base_file);
			//subtract all the other colours
			union(){
				for(i = [0:len(detail_files)-1]){				
					
					translate([0,0,base_height-colour_layer_height])linear_extrude(height=colour_layer_height+1)import(detail_files[i]);
				}
			}
		}
	}
	else{
		color(colours[gen_colour])translate([0,0,base_height-colour_layer_height])linear_extrude(height=colour_layer_height)import(detail_files[gen_colour-1]);
	}
	
}



//layered_sign("771_background.svg",["771_inner.svg","771_outline.svg"]);

//layered_sign("965.svg",["965_inner.svg"],["blue","white"]);


//mmu_sign(0,"771_background.svg",["771_inner.svg","771_outline.svg"]);

//mmu_sign(1,"771_background.svg",["771_inner.svg","771_outline.svg"]);
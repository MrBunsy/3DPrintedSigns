
module layered_sign(base_file, detail_files,colours=["white","black","red"] ,base_height = 3, colour_layer_height = 0.4){
	
	color(colours[0])linear_extrude(height=base_height)import(base_file);
	
	for(i = [0:len(detail_files)-1]){
		layer_height = base_height + (i+1)*colour_layer_height;
		
		
		color(colours[(i+1)%len(colours)])linear_extrude(height=layer_height)import(detail_files[i]);
	}
}

module all_details(detail_files,height, except=-1){
	union(){
		for(i = [0:len(detail_files)-1]){				
			if(i != except){
				linear_extrude(height=height)import(detail_files[i]);
			}
		}
	}
}

module get_background(base_file,detail_files,height){
	difference(){
		linear_extrude(height=height)import(base_file);
		translate([0,0,-0.5])all_details(detail_files,height+1);
	}
}

//if background_is_part_of_base is false, then the base will be the same colour as the detail
module mmu_sign(gen_colour,base_file, detail_files,colours=["white","black","red"] ,base_height = 3, colour_layer_height = 0.2, base_colour="white"){
	
	searchableList = [for(i=[0:len(colours)-1]) [colours[i], i]];
	base_colour_index = search([base_colour],searchableList)[0];
	echo("base_colour_index",base_colour_index);
	
	if(gen_colour == base_colour_index){

		//base layer
		color(colours[base_colour_index])linear_extrude(height=base_height-colour_layer_height)import(base_file);
			
	if(base_colour_index == 0){
		//background
			color(colours[base_colour_index])translate([0,0,base_height-colour_layer_height])get_background(base_file,detail_files,colour_layer_height);
				
	}else{
			//include a detail layer in the base
			color(colours[base_colour_index])translate([0,0,base_height-colour_layer_height])linear_extrude(height=colour_layer_height)import(detail_files[base_colour_index-1]);
		}

	}
	else{
		
		if(gen_colour == 0){
			//background, if it isn't the same colour as teh base
			color(colours[gen_colour])translate([0,0,base_height-colour_layer_height])get_background(base_file,detail_files,colour_layer_height);
			
		}else{
		//detail layer
			color(colours[gen_colour])translate([0,0,base_height-colour_layer_height])linear_extrude(height=colour_layer_height)import(detail_files[gen_colour-1]);
		}
	}
	
}



//layered_sign("771_background.svg",["771_inner.svg","771_outline.svg"]);

//layered_sign("965.svg",["965_inner.svg"],["blue","white"]);


//mmu_sign(0,"771_background.svg",["771_inner.svg","771_outline.svg"]);

//mmu_sign(1,"771_background.svg",["771_inner.svg","771_outline.svg"]);
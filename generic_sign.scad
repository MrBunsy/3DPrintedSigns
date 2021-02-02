;


module generic_layered_sign(base_file, detail_files,colours=["white","black","red"] ,base_height = 3,colour_layer_height = 0.4){
	
	color(colours[0])linear_extrude(height=base_height)import(base_file);
	
	for(i = [0:len(detail_files)-1]){
		echo("i",i);
		layer_height = base_height + (i+1)*colour_layer_height;
		
		translate_height = 0;
		
		color(colours[(i+1)%len(colours)])translate([0,0,translate_height])linear_extrude(height=layer_height)import(detail_files[i]);
	}
}



//generic_layered_sign("771_background.svg",["771_inner.svg","771_outline.svg"]);

generic_layered_sign("965.svg",["965_inner.svg"],["blue","white"]);

Possible idea: Effect of human preference vs. intended use. Specifically, wear and tear in a public area.  
Sites: Vincent Massey park or random trails  
areas to look at: trail paths, picnic tables, litter, structural damage, placement of structures for intended use, signs of moved architecture  
additional conditions (leaf paths, grass damage, intended paths)  
Sections: picnic table area, 2 high-quality picnic areas, gazebos, also reffered to as zone 1, 2, 3, 4 as seen in Vincent MasseyMap.jpg  

Observations  
Zone 1 contained the most travelling perople in it, bikes walkers no signs of staying for a while    
Zone 2 and 3 had more people staying in the area with fires lit    
Zone 4 large parties clear litter left behind  

Notes:  
Picnic tables near the edge of the forest had less pines despite same quantity of pine needles on the ground nearby   
the path between Zone 3-4 had the most damaged amount of grass    
The images were taken October 3rd 15:00 however are not currently in Github due to it being around 15 photos meant for data gathering.
The ovals represent how big, it is a literal piece of architectural design
The geese are more active in zone 5 activities, more in that area

Zone 4 more debris on tables (19/23) in the top half left (closer to edges). 1 desire path from main path by washroom to far zone 5

Zone 4 has smoke remains and debris on inner tables; outer are clear; some tire tracks along area 4 main path (bikes)
Zone 3 has significantly more families

Zone 1 has debris but a significant amount for being such a clear area +moss on one's further from path. Also, desire paths between tables; not much diversion outside. No trash whatsoever. 1 Table missing half a plank. Also, a large quantity of kickable rocks present in no other area. Only desire path is connected directly to the path and is more like the first step
 Zone 4 also has the long stretches of tables beside the path and edge

Zone 4 and 5 had cracks in picnic table bases

4 kickable rocks in zone 1 (not present in other areas) (supporting rest stop area where a kid would leave behind the rock they have been kicking)
Edges and side path. Pretty much a lot of desire path from 4 to 5

All generally have the equally spaced layout besides 4. Zone 4 also just has much more significant ground damage (no grass)

Zone 1 grass good, all except 4



Code attempt 1:  
Currently, there are issues regarding creating a PDF result and the locations still need to be plotted onto the park map jpg. This was later resolved after remembering to include the file type in the file call, resulting in MapGrid.pdf, which will help with plotting points when the GIS application is found.

Brainstorming:                  
Might be better to just plot the points in SQL then use the GIS workshop application to format a map to identify any additional ideas  
Thesis could be about classification on which areas are best for which event, taking into consideration how busy somthing is, intention, current usage, and access proximity (parking lot, road access, trail access)  
https://library.carleton.ca/guides/help/gis-software = Carleton GIS local
It would probably be best to create expected circles over areas to show leaf density and then an actual version showing clearer tables indicating signs of use, which can be overlaid to see a pattern.
 
dataset:  
the feature variable is to allow flexibility beyond picnic tables for areas like the general path, desire paths, or on a area thats not declared (grass between areas)

possible resources
https://opcug.ca/wp-content/uploads/Vincent-Massey-Park_Map_v2020.pdf

________________________________________________________Nov 13 notes
In turns out it is very difficult to create coordinates in a dataset to then put into a GIS
instead I am opting to abandon the mapping method previously deployed and dierctly apply points through the GIS software
this is the current link
https://fieldmaps.arcgis.app/?itemID=74f7ca36b04f43d89716e76413dcd812&referenceContext=open&portalURL=https%3A%2F%2Fcarleton-u.maps.arcgis.com
Currently : sections made, data needs to be added, Add high leaf zones to all areas, add clear tables as points, add rock entries at points, add trash nodes with descriptions of what it is, Also possible outline the paths as a layer

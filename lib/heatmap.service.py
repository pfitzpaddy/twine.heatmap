#!/usr/bin/env python

import sys, shutil, json, time, heatmap
sys.path.insert(0, 'path_to_my_modules')

# Load the data that PHP sent us
try:
    data=json.loads(sys.argv[1])
except:
    print '{"success": "false"}'
    sys.exit(1)

if __name__ == "__main__":
    pts=[];
    epoch=int(time.time());
    # py heatmap
    dotsize=int(data[0][0]);
    opacity=int(data[0][1]); 
    scheme='fire'; # str(data[0][2]); #one of ["classic", "fire", "omg", "pbj", "pgaitch"]
    size=[data[1][0],data[1][1]]; # pixel size of map
    bounds=[[data[2][0][0],data[2][0][1]],[data[2][1][0],data[2][1][1]]]; # geographic extents
    
    # Currently reading in TopoJson for testing purposes
    # Can use PostGIS bounding box query to fetch points
        #http://postgis.refractions.net/documentation/manual-2.0/ST_Contains.html

    # Read TopoJson and determine bounds
    with open('ww2_thor_pt.min.json') as f:
        data = json.load(f)

    for feature in data['features']:
        if bounds[0][0] <= feature['geometry']['coordinates'][1] <= bounds[1][0] and bounds[0][1] <= feature['geometry']['coordinates'][0] <= bounds[1][1]:
            pts.append(feature['geometry']['coordinates'])

    #print "Processing %d points..." % len(pts)

    hm = heatmap.Heatmap()
    # classic
    # hm.heatmap(pts,dotsize=dotsize,size=(size[0], size[1]),scheme=scheme)
    # hm.saveKML('../imgs/'+str(epoch)+'.kml')
    img=hm.heatmap(pts,dotsize=dotsize,opacity=opacity,size=(size[0], size[1]),scheme=scheme)
    img.save('../imgs/'+str(epoch)+'.png')
    # scaled bounding coords
    ((east, south), (west, north)) = hm._ranges(hm.points)
    print '{"success": "true", "filename": "'+str(epoch)+'", "dotSize": "'+str(dotsize)+'", "opacity": "'+str(opacity)+'", "scheme": "'+str(scheme)+'", "imgSize": "'+str(size)+'", "bounds": "[['+str(south)+','+str(east)+'],['+str(north)+','+str(west)+']]" }'
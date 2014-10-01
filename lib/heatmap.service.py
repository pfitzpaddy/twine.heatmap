#!/usr/bin/env python

import sys, json, time, heatmap
sys.path.insert(0, 'path_to_my_modules')

# Load the data that PHP sent us
try:
    data=json.loads(sys.argv[1])
except:
    print '{"success": "false"}'
    sys.exit(1)

if __name__ == "__main__":
    pts=[];
    dotsize=56;
    scheme='fire';
    epoch=int(time.time());
    # pixel size of map
    size=[data[0][0],data[0][1]]; #size=[1653,600];
    # geographic extents
    bounds=[[data[1][0][0],data[1][0][1]],[data[1][1][0],data[1][1][1]]]; #bounds=[[-7.0354756524330115,90.593261718751],[6.118707747190857,126.91406249999999]];
    
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
    #hm.heatmap(pts,dotsize=dotsize,size=(size[0], size[1]),scheme=scheme)
    #hm.saveKML("../classic.kml")
    img=hm.heatmap(pts,dotsize=dotsize,size=(size[0], size[1]),scheme=scheme)
    img.save('../imgs/'+str(epoch)+'.png')
    print '{"success": "true", "filename": "'+str(epoch)+'", "size": "'+str(size)+'", "bounds": "'+str(bounds)+'" }'
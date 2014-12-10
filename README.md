## Twine Heatmap (twine.heatmap)

Python server side heatmap library demo

- [http://jjguy.com/heatmap/](http://jjguy.com/heatmap/)

#### Setup

- install heatmap

		$ cd heatmap-2.2.1
		$ python setup.py install
		
- install PIL
	
		$ sudo easy_install Pillow
	
#### Test heatmaps py install

	$ python lib/python-heatmap/test.py
	
- This script takes a series of points from a JSON file.

#### Application

 - From Apache web server navigate to 
	 
		http://<your.host>>/twine-heatmap/index.html

- If no heatmap is visible, check permissions (enable shell_exec and r/w "imgs" folder)

#### Heatmap Service

 - Currently the twine.heatmap.py service is not a Rest API, it uses twine.heatmap.php to accept requests and run the twine.heatmap.py script.


 - The script accepts the following params;

		 - png: (boolean) - determines wether or not to generate a python PNG heatmap or return an array of [lat, lon] coords to the client.
		 - dotSize: (int) - the dot size of each cluster based on the Python server side heatmap library.
		 - opacity: (int) - the opacity to set the generated heatmap layer.
		 - imgSize: ([width, height]) - image size of PNG to generate.
		 - bounds: ([width, height]) - bounds of image to generate.   

 - The script returns either;

	- filename of the image located on the server (filename is unix timestamp), added to Leaflet map using L.imageOverlay;
	
			L.imageOverlay('imgs/' + response.filename + '.png', [[bounds[0][0],bounds[0][1]],[bounds[1][0],bounds[1][1]]]).addTo(map);

	- [lat, lon] points to display on the client;

			var heatmapLayer = L.heatLayer(response.data, options).addTo(map);

#### Improvements

-Several improvements are required to make this proof of concept a reliable service.

1. Implement Python script as Rest API with default set of options.
2. Run cleanup script to remove generated PNG heatmap images from server. 
3. Request point data from PostGIS indexed db using [ST_Contains](http://postgis.refractions.net/documentation/manual-2.0/ST_Contains.html) query.
4. Provide the "scheme" as an option for the generated PNG heatmap image (available options from Python heatmap library as below include one of ["fire", "classic", "omg", "pbj", "pgaitch"].

	![classic](http://jjguy.com/heatmap/fire.png) ![fire](http://jjguy.com/heatmap/classic.png) ![omg](http://jjguy.com/heatmap/omg.png) ![pbj](http://jjguy.com/heatmap/schemes/pbj.png) ![pgaitch](http://jjguy.com/heatmap/pgaitch.png)

## Demo (results)
- At zoom levels greater than 7 (where the world is at full extents as zoom level 0), the client transitions from displaying server side PNG generated heatmap to [leaflet.heat](https://github.com/Leaflet/Leaflet.heat) client generated heatmap.

#### Zoom scale 6, server side generated heatmap

![server side heatmap](https://dl.dropboxusercontent.com/u/67905790/heatmap-small-scale-v1.PNG)

#### Zoom scale 7, transition to client side generated heatmap

![client side heatmap](https://dl.dropboxusercontent.com/u/67905790/heatmap-mid-scale-v1.PNG)

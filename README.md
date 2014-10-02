##twine.heatmap

Python server side heatmap library demo

- http://jjguy.com/heatmap/

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

- If no heatmap is visible, check permissions (enable shell_exec and r/w folder)

#### Known issues

 - since the generated PNG needs to be aligned to the map projection, at small scales (when the map is zoomed in) the map may not display correctly. 

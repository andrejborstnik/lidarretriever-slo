# Lidar retriever

## Usage

Visit ARSO lidar GIS for obtaining coordinates of the lidar tiles: [link](http://gis.arso.gov.si/evode/profile.aspx?id=atlas_voda_Lidar@Arso)

Use D48GK projection and remember the coordinates of the tiles. Let's make an example

    468_85 and 470_83

These tile labels are in the format `(x_y)`. First tile should be north-west, last tile should be south-east. Now, we will extract parameters `x1`, `y1`, `x2` and `y2`.

* `x1` - NW x (smallest) (e. g. 486)
* `y1` - SE y (smallest) (e. g. 83)
* `x2` - SE x (largest) (e. g. 470)
* `y2` - NW y (largest) (e. g. 85)

Now we run the program:

`python lidar-evode.py --x1 468 --y1 83 --x2 470 --y2 85`

Use `lidar-evode-dem.py` for DEM files.

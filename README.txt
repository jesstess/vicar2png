vicar2png
=========

`vicar2png` converts VICAR image files to PNGs. The VICAR (Video Image
Communication and Retrieval) format is commonly used by NASA, JPL, and
various universities. Read more about the format specification at
http://www-mipl.jpl.nasa.gov/external/VICAR_file_fmt.pdf.

We wrote and packaged `vicar2png` so that anyone can view, enjoy, and
remix NASA's mission image data easily by converting VICAR files to
the popular PNG image format.

Sample usage:

    # Use the input filename to generate a default output filename.
    vicar2png cassini01.IMG

    # Specify an output filename.
    vicar2png cassini01.IMG test_image.png


Installing vicar2png
--------------------

You can get and install `vicar2png` from PyPI:
http://pypi.python.org/pypi/Vicar2Png

You'll need to install the setuptools packages before installing
`vicar2png`: http://pypi.python.org/pypi/setuptools


vicar2png demo
--------------

Once you've installed `vicar2png`, try converting the following files:

*  An image of Jupiter from an Earth-Jupiter cruise during the Cassini mission:

   1. Download http://pdsimg.jpl.nasa.gov/data/cassini/cassini_orbiter/coiss_1004/data/1355070805_1355176231/N1355070913_1.IMG
   2. Convert from VICAR to PNG with `vicar2png N1355070913_1.IMG`
   3. Open `N1355070913_1.png` in an image viewer (`open N1355070913_1.png` will do the trick on OS X and many Linuxes)

*  An encounter with Saturn's moon Phoebe from the Cassini-Huygens mission:

   1. Download http://pdsimg.jpl.nasa.gov/data/cassini/cassini_orbiter/coiss_2004/data/1465674475_1465709620/N1465674502_2.IMG
   2. Convert from VICAR to PNG with `vicar2png N1465674502_2.IMG`
   3. Open `N1465674502_2.png` in an image viewer (e.g. `open N1465674502_2.png`)

You can find many more images to test at http://pdsimg.jpl.nasa.gov/data/cassini/cassini_orbiter/.

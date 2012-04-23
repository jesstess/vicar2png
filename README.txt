=========
Vicar2Png
=========

Vicar2Png converts VICAR image files to PNGs. The VICAR (Video Image
Communication and Retrieval) format is commonly used by NASA, JPL, and
various universities. Read more about the format specification at
http://www-mipl.jpl.nasa.gov/external/VICAR_file_fmt.pdf.

Sample usage::

    # Use the input filename to generate a default output filename.
    vicar2png cassini01.IMG

    # Specify an output filename.
    vicar2png cassini01.IMG test_image.png

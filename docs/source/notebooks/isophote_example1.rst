:orphan:


Basic example on how to run the 'ellipse' fitting tool
======================================================

The 'isphote' package does not provide support for input/output
operations. The basic input for the 'ellipse' fitting tool is a numpy
2-D array. In this example, we use the astropy.fits package to read an
image and deliver the required pixel array. The basic output is an
instance of class IsophoteList. See code documentation for details.

The image of galaxy M51 formerly distributed with the IRAF software as
dev$pix was used extensively before as a regression test for the old
STSDAS 'ellipse' task. We re-use it here for the sake of consistency.

Note that the M51 galaxy, with its proeminent spiral arms and giant HII
regions, is not the best subject for science analysis by the 'ellipse'
algorithm, since this algorithm assumes that isophotes are mainly
elliptical in shape. On the other hand, the M51 image is ideal for
checking the resilience of the algorithm against image contamination by
non-elliptical features.

See notebook 'example3.ipynb', in which we apply the 'ellipse' tool to
an image of a "true" elliptical galaxy.

Note: notebooks will only run when the 'jupyter notebook' command is
issued from directory stak/docs/source/notebooks

.. code:: ipython3

    from astropy.io import fits
    image = fits.open("../../../stak/isophote/test/data/M51.fits")
    pixel_data = image[0].data

Next, we create an instance of the Ellipse class, passing the numpy 2-D
array with the pixel data as argument to the constructor:

.. code:: ipython3

    from stak.isophote.ellipse.ellipse import Ellipse
    
    ellipse = Ellipse(pixel_data)


.. parsed-literal::

    Centering on object....   Done. Found x0 = 257.0, y0 = 258.0


Finally, we run the 'fit\_image' method on the instance, getting as
result an instance of class IsophoteList.

This may take a while. Wait until all the output prints out, down to the
SMA = 0 central intensity value. This interpreted version of the
algorithm is significantly slower than the old, compiled code in the
IRAF system. In this implementation, we trade speed for flexibility.

.. code:: ipython3

    isolist = ellipse.fit_image()


.. parsed-literal::

    #
    # Semi-      Isophote         Ellipticity    Position     Grad.   Data  Flag Iter. Stop
    # major        mean                           Angle        rel.                    code
    # axis       intensity                                    error
    #(pixel)                                     (degree)
    #
      10.00     1070.76 ( 8.38)  0.049 (0.006)  51.18 ( 3.8)  0.190    62     0   50     2
      11.00     1043.49 ( 7.66)  0.129 (0.005)  72.75 ( 1.1)  0.154    65     0   10     0
      12.10      987.31 ( 7.29)  0.154 (0.004)  67.97 ( 0.8)  0.156    70     0   10     0
      13.31      924.67 ( 8.30)  0.154 (0.006)  52.56 ( 1.3)  0.242    77     0   50     2
      14.64      875.32 ( 8.61)  0.154 (0.003)  52.56 ( 0.6)  None     85     0    3     5
      16.11      913.07 ( 8.38)  0.321 (0.005)  52.56 ( 0.5)  0.236    83     0   50     2
      17.72      888.62 ( 8.25)  0.359 (0.003)  50.56 ( 0.3)  0.141    89     0   10     0
      19.49      756.00 ( 7.54)  0.178 (0.002)  35.74 ( 0.4)  0.111   111     0   10     0
      21.44      682.93 ( 7.59)  0.212 (0.003)  35.17 ( 0.4)  0.154   120     0   10     0
      23.58      668.46 ( 9.53)  0.285 (0.002)  38.53 ( 0.3)  0.113   125     0   10     0
      25.94      528.48 ( 6.49)  0.230 (0.002)  41.01 ( 0.2)  0.095   143     0   10     0
      28.53      536.36 ( 7.37)  0.306 (0.002)  51.36 ( 0.2)  0.103   149     0   18     0
      31.38      366.26 ( 5.92)  0.076 (0.003)  59.60 ( 1.1)  0.142   190     0   50     2
      34.52      311.41 ( 5.08)  0.076 (0.004)  59.60 ( 1.5)  0.221   209     0    5     5
      37.97      277.50 ( 5.51)  0.076 (0.005)  59.60 ( 2.0)  0.153   230     0    3     5
       9.09     1115.25 ( 9.01)  0.045 (0.009)  59.60 ( 5.7)  0.232    56     0   14     0
       8.26     1151.01 ( 8.29)  0.066 (0.008) 105.23 ( 3.5)  0.223    51     0   10     0
       7.51     1219.53 ( 8.46)  0.075 (0.006) 115.20 ( 2.5)  0.165    46     0   10     0
       6.83     1304.29 ( 8.19)  0.073 (0.005) 120.72 ( 2.2)  0.135    42     0   10     0
       6.21     1404.53 ( 8.03)  0.080 (0.005) 125.44 ( 1.8)  0.117    38     0   10     0
       5.64     1513.05 ( 7.85)  0.093 (0.005) 128.91 ( 1.5)  0.109    34     0   10     0
       5.13     1633.12 ( 7.19)  0.106 (0.004) 131.43 ( 1.2)  0.096    31     0   10     0
       4.67     1759.91 ( 6.51)  0.111 (0.003) 128.93 ( 1.0)  0.081    28     0   10     0
       4.24     1899.53 ( 6.50)  0.109 (0.003) 125.88 ( 0.9)  0.070    26     0   10     0
       3.86     2060.44 ( 7.13)  0.102 (0.003) 123.71 ( 0.9)  0.059    23     0   10     0
       3.50     2247.73 ( 7.27)  0.099 (0.003) 120.34 ( 0.9)  0.053    21     0   10     0
       3.19     2485.58 (11.70)  0.099 (0.004) 117.51 ( 1.2)  0.060    19     0   50     2
       2.90     2761.16 (12.73)  0.094 (0.004) 119.51 ( 1.3)  0.062    18     0   10     0
       2.63     3068.65 (10.33)  0.095 (0.003) 117.41 ( 1.0)  0.055    16     0   10     0
       2.39     3396.38 ( 8.75)  0.095 (0.002) 113.32 ( 0.8)  0.049    15     0   50     0
       2.18     3713.23 (13.53)  0.084 (0.004) 120.79 ( 1.5)  0.061    14     0   10     0
       1.98     4073.83 (17.83)  0.081 (0.005) 118.90 ( 1.9)  0.062    13     0   50     2
       1.80     4463.16 (17.72)  0.085 (0.005) 119.29 ( 1.7)  0.066    13     0   10     0
       1.64     4834.80 (19.75)  0.092 (0.005) 120.12 ( 1.9)  0.076    13     0   10     0
       1.49     5157.80 (18.69)  0.093 (0.005) 120.23 ( 2.0)  0.085    13     0   10     0
       1.35     5439.23 (18.23)  0.090 (0.006) 119.37 ( 2.2)  0.093    13     0   10     0
       1.23     5703.82 (21.42)  0.093 (0.008) 119.03 ( 2.8)  0.112    13     0   10     0
       1.12     5935.08 (24.06)  0.098 (0.010) 117.37 ( 3.3)  0.135    13     0   10     0
       1.02     6119.23 (30.27)  0.083 (0.015) 119.87 ( 5.8)  0.205    13     0   10     0
       0.92     6242.94 (32.39)  0.043 (0.020) 119.87 (14.3)  0.267    13     0   50     2
       0.84     6393.17 (30.60)  0.070 (0.022) 139.56 ( 9.9)  0.298    13     0   10     0
       0.76     6505.07 (27.86)  0.065 (0.024) 133.86 (11.7)  0.353    13     0   10     0
       0.69     6605.62 (26.91)  0.054 (0.025) 140.17 (14.3)  0.352    13     0   10     0
       0.63     6706.67 (26.54)  0.054 (0.027) 144.13 (15.4)  0.378    13     0   10     0
       0.57     6787.73 (23.70)  0.040 (0.026) 136.91 (20.1)  0.367    13     0   10     0
       0.52     6872.32 (21.73)  0.040 (0.027) 151.38 (20.7)  0.389    13     0   10     0
       0.00     7599.76


Check the result's type, it should be an instance of the IsophoteList
class:

.. code:: ipython3

    type(isolist)




.. parsed-literal::

    stak.isophote.ellipse.isophote.IsophoteList



Note that the Ellipse constructor runs an object centering algorithm.
See the Ellipse class documentation for details.

Running 'ellipse' in a finer-grained way:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can fit individual ellipses as well, by just calling the
'fit\_isophote' method in the same Ellipse instance (passing the
semi-major axis length to the method):

.. code:: ipython3

    isophote = ellipse.fit_isophote(20.)
    
    from stak.isophote.ellipse.isophote import print_header
    print_header(verbose=True)
    isophote.print(verbose=True)


.. parsed-literal::

    #
    # Semi-      Isophote         Ellipticity    Position     Grad.   Data  Flag Iter. Stop
    # major        mean                           Angle        rel.                    code
    # axis       intensity                                    error
    #(pixel)                                     (degree)
    #
      20.00      740.53 ( 7.23)  0.192 (0.002)  36.07 ( 0.4)  0.113   113     0   14     0


Note that in this case we get an instance of class Isophote, not
IsophoteList as before:

.. code:: ipython3

    type(isophote)




.. parsed-literal::

    stak.isophote.ellipse.isophote.Isophote



Regarding the example above, by calling the 'fit\_isophote' method in a
simple 'for' loop with successive values for the semi-major axis length,
one may be lead to think that it will emulate the behavior of the
'fit\_image' method. However, that would not in general be the case. The
algorithm will probably stop prematurely, and/or will not result in the
best fit. The fitting algorithm is quite sensitive to the initial
guesses (the starting ellipse geometry) and other fitting parameters
such as the step used to move from a given ellipse to the next, the area
integration method, finding the maximum acceptable semi-major axis
length, and such. The 'fit\_image' method takes care of handling these
details in a transparent way for the user.

In the 'isophote' package, the class constructors and method calls
accept a variety of parameters that can be used to customize and
fine-tune the fit process. Here we give a few eaxamples; please see the
code documentation for a complete description.

For instance, the fit algorithm is quite sensitive to the initial
guesses for the X and Y position of the center of the galaxy on the
frame. When using default values as in the examples above, the methods
assume that the galaxy is exactly centered in the frame. The fit
algorithm can also fail to properly converge if either the ellipticiy or
the position angle of the semi-major axis are too way off the true
values. To override the default values, we initialize the Ellipse
constructor with an instance of class Geometry. This class encapsulates
all data and behavior associated with a given ellipse's geometry.

.. code:: ipython3

    import numpy as np
    from stak.isophote.ellipse.geometry import Geometry
    
    # user defines here the geometry parameters that will be used as first guess.
    x0 = 256.    # center position
    y0 = 256.    # center porsition
    sma = 20.    # semi-major axis length in pixels
    eps = 0.2    # ellipticity
    
    # positon angle is defined in radians, counterclockwise from the
    # +X axis (rotating towards the +Y axis). Here we use 35 degrees 
    # as a first guess.
    pa = 35. / 180. / np.pi
    
    # note that the Geometry constructor has additional parameters with
    # default values. Please see the class documentation for details.
    g = Geometry(x0, y0, sma, eps, pa)
    
    # the custom geometry is passed to the Ellipse constructor.
    ellipse = Ellipse(pixel_data, geometry=g)
    
    # the fit proceeds as usual.
    isophote = ellipse.fit_isophote(20.)
    
    isophote.print(verbose=True)


.. parsed-literal::

    Centering on object....   Done. Found x0 = 257.0, y0 = 258.0
      20.00      732.58 ( 7.25)  0.183 (0.002)  35.40 ( 0.4)  0.116   114     0   10     0


To further break down the fit process, one could explictly work with the
Sample and Fitter classes, as exemplified below.

.. code:: ipython3

    from stak.isophote.ellipse.sample import Sample
    from stak.isophote.ellipse.fitter import Fitter
    
    sample = Sample(pixel_data, 7., geometry=g)
    fitter = Fitter(sample)
    isophote = fitter.fit()
    
    isophote.print(verbose=True)


.. parsed-literal::

       7.00     1281.23 ( 8.19)  0.073 (0.005) 120.25 ( 2.2)  0.142    43     0   10     0


In here, we initially create an instance of the Sample class. This
instance encapsulates everything associated with a given elliptical path
over the image. This includes not only the geometry information, but
also the raw intensity samples extracted from the image (intensity as a
function of polar angle and radius), as well as associated statistical
quantities.

Note that the Sample constructor allows for overriding the semi-major
axis length initially used to create the Geometry instance. That way,
one can propagate a given geometry configuration to other Samples taken
at other values of semi-major axis length.

The Sample instance is used to initialize an instance of the Fitter
class. This class has a number of controls to help in tweaking the fit.
The final result of the 'fit' method is an instance of class Isophote
with the final, fitted values of the geometry parameters.

Raw values extracted from the image can be accessed via the 'values'
attribute of a Sample instance. This attribute stores a 2-D numpy array.
The first element is of length 3, and each one of those has as many
elements as there are individual extracted values from the image.

.. code:: ipython3

    isophote.sample.values.shape




.. parsed-literal::

    (3, 43)



The 3 top-level elements contain respectively the position angles, the
polar radii, and the intensity values extracted at each position along
the elliptical path on the image:

.. code:: ipython3

    # angles in radians
    isophote.sample.values[0]




.. parsed-literal::

    array([ 0.05      ,  0.19288644,  0.3361739 ,  0.48030165,  0.62564106,
            0.7724653 ,  0.92092505,  1.07103245,  1.22265551,  1.37552507,
            1.52925515,  1.68337627,  1.83737888,  1.99076254,  2.14308465,
            2.29400291,  2.44330627,  2.59093146,  2.7369644 ,  2.88162779,
            3.02525777,  3.16827284,  3.31113832,  3.454329  ,  3.59829202,
            3.74341204,  3.88998011,  4.03816824,  4.18801188,  4.33940244,
            4.49209213,  4.64571207,  4.79980367,  4.95386066,  5.10737768,
            5.25989957,  5.41106517,  5.56064049,  5.70853764,  5.85481868,
            5.99968535,  6.14345721,  6.28654166])



.. code:: ipython3

    # polar radii in pixels
    isophote.sample.values[1]




.. parsed-literal::

    array([ 6.99856493,  6.97897768,  6.93828898,  6.8804462 ,  6.81086458,
            6.73583242,  6.66189686,  6.59530262,  6.54152474,  6.50490772,
            6.48840375,  6.49339629,  6.51959943,  6.56503502,  6.6261035 ,
            6.697773  ,  6.7739114 ,  6.84777004,  6.91259898,  6.96233506,
            6.99227017,  6.99959105,  6.98369509,  6.94622817,  6.89084786,
            6.82276863,  6.7481787 ,  6.67362337,  6.60543142,  6.54923099,
            6.50957146,  6.48964647,  6.49110439,  6.51393557,  6.55643606,
            6.6152615 ,  6.68559519,  6.76145555,  6.83615551,  6.90289931,
            6.95546419,  6.98887927,  6.99999353])



.. code:: ipython3

    # intensities
    isophote.sample.values[2]




.. parsed-literal::

    array([ 1276.92000884,  1320.60642806,  1337.23605124,  1310.00501376,
            1261.24978973,  1201.54150935,  1162.78485047,  1196.56451538,
            1291.07392577,  1375.52220458,  1409.31442191,  1379.59276368,
            1303.24192573,  1213.4425464 ,  1167.76949733,  1221.93190567,
            1317.10332738,  1336.89856224,  1287.60975105,  1243.15358231,
            1241.53068837,  1275.35792608,  1303.97088288,  1302.67476376,
            1306.29345628,  1271.74844061,  1266.6792211 ,  1271.85831046,
            1285.05966689,  1299.42608522,  1313.89313382,  1307.40961991,
            1276.82117095,  1231.13416971,  1199.11815248,  1230.30523959,
            1291.87760854,  1336.31845105,  1345.3695319 ,  1325.89988559,
            1277.76792777,  1249.15817313,  1269.79706802])



Note that, in the example above, we cannot use the original Sample
instance that was originally used to initialize the fitter. Once the
fitter does its bidding, that instance becomes invalid and we need to
look for a new Sample instance inside the Isophote instance just created
by the fitter.

Plotting results:
-----------------

Import packages necessary for plotting:

.. code:: ipython3

    import matplotlib.pyplot as plt
    %matplotlib inline

The attributes of an Isophote instance are also attributes of an
IsophoteList instance. The difference is, while the individual isophotes
have scalar attributes, the same attributes in an IsophoteList are numpy
arrays that store the given attribute across all isophotes in the list.
Thus, attributes in a IsophoteList can be directly used as parameters
for matplotlib calls.

To ease transition to this new implementation, attribute names were
chosen whenever possible to match the names used in the old STSDAS task
and its parameter sets.

As an example, a basic plot of magnitude as a function of (semi-major
axis length)^1/4 can be done simply as:

.. code:: ipython3

    plt.figure(figsize=(8, 4))
    
    plt.scatter(isolist.sma**0.25, -2.5*np.log10(isolist.intens))
    
    plt.xlabel('sma**1/4')
    plt.ylabel('Magnitude')
    plt.gca().invert_yaxis()
    plt.title("M51 brightness profile")




.. parsed-literal::

    <matplotlib.text.Text at 0x110433080>




.. image:: isophote_example1_files/isophote_example1_33_1.png


Next, a multiple plot depicting ellipse geometry as a function of
semi-major axis length:

.. code:: ipython3

    plt.figure(figsize=(10, 5))
    plt.figure(1)
    
    plt.subplot(221)
    plt.errorbar(isolist.sma, isolist.eps, yerr=isolist.ellip_err, fmt='o', markersize=4)
    plt.title('EPS')
    
    plt.subplot(222)
    plt.errorbar(isolist.sma, isolist.pa/np.pi*180., yerr=isolist.pa_err/np.pi* 80., fmt='o', markersize=4)
    plt.title('PA (deg.)')
    
    plt.subplot(223)
    plt.errorbar(isolist.sma, isolist.x0, yerr=isolist.x0_err, fmt='o', markersize=4)
    plt.title('X0')
    
    plt.subplot(224)
    plt.errorbar(isolist.sma, isolist.y0, yerr=isolist.y0_err, fmt='o', markersize=4)
    plt.title('Y0')
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)



.. image:: isophote_example1_files/isophote_example1_35_0.png


Ellipses can be overplotted on the image display:

.. code:: ipython3

    import matplotlib.cm as cm
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(pixel_data, cmap=cm.gnuplot, vmin=0, vmax=1000)
    plt.axis([0,511,0,511])
    
    # this method on an IsophoteList instance will retrieve the isophote 
    # that has the closest 'sma' from the passed argument.
    iso = isolist.get_closest(40.)
    print("Closest SMA = %f" % iso.sma)
    
    # this method on an Isophote instance returns the X-Y coordinates of 
    # the sampled points in the image.
    x, y, = iso.sampled_coordinates()
    
    plt.plot(x, y, color='white')


.. parsed-literal::

    Closest SMA = 37.974983




.. parsed-literal::

    [<matplotlib.lines.Line2D at 0x1106fc6a0>]




.. image:: isophote_example1_files/isophote_example1_37_2.png


The "isophote" doesn't look quite isophotal. This is to be expected in
this image though. The fitting algorithm assumes that a smooth surface
brightness distribution will dominate the image, and this is hardly the
case of M51 with its proeminent spiral arms and lots of clumpy star
formation regions.

We can examine the elliptical brightness sample associated with the
ellipse depicted above to get an idea of what is going on. The plot
below shows large contamination from those bright HII regions.

.. code:: ipython3

    plt.figure(figsize=(10, 3))
    plt.plot(iso.sample.values[0]/np.pi*180., iso.sample.values[2])
    plt.ylabel("Intensity")
    plt.xlabel("Angle (deg.)")




.. parsed-literal::

    <matplotlib.text.Text at 0x1106f26a0>




.. image:: isophote_example1_files/isophote_example1_39_1.png


We can use sigma-clipping to try to get around them. Please see the next
notebook 'example2.ipynb' for a demo of the sigma-clip feature.

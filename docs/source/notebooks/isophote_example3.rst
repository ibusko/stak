:orphan:


Building an image model from results obtained by fitting
========================================================

M51 test image
--------------

Initially we fit the M51 test image; then, from the fit results we build
a model, and finally we subtract the model from the original image.

Note: notebooks will only run when the 'jupyter notebook' command is
issued from directory stak/docs/source/notebooks

We start in the same way as we did in notebook 'example2.ipynb':

.. code:: ipython3

    from astropy.io import fits
    image = fits.open("../../../stak/isophote/test/data/M51.fits")
    pixel_data = image[0].data
    
    from stak.isophote.ellipse.ellipse import Ellipse
    ellipse = Ellipse(pixel_data)
    isolist = ellipse.fit_image(sclip=2., nclip=3)


.. parsed-literal::

    Centering on object....   Done. Found x0 = 257.0, y0 = 258.0
    #
    # Semi-      Isophote         Ellipticity    Position     Grad.   Data  Flag Iter. Stop
    # major        mean                           Angle        rel.                    code
    # axis       intensity                                    error
    #(pixel)                                     (degree)
    #
      10.00     1089.59 ( 8.44)  0.102 (0.006)  65.93 ( 2.0)  0.191    60     0   20     0
      11.00     1044.70 ( 7.70)  0.132 (0.005)  72.93 ( 1.1)  0.150    65     0   10     0
      12.10      983.21 ( 5.88)  0.157 (0.003)  70.03 ( 0.6)  0.122    61     9   10     0
      13.31      916.06 ( 7.32)  0.157 (0.006)  49.90 ( 1.3)  0.216    70     7   50     2
      14.64      895.94 ( 6.87)  0.223 (0.004)  55.85 ( 0.7)  0.160    77     4   19     0
      16.11      868.99 ( 5.41)  0.282 (0.003)  51.85 ( 0.5)  0.152    76    10   12     0
      17.72      851.25 ( 5.75)  0.282 (0.003)  43.00 ( 0.3)  0.119    79    15   12     0
      19.49      731.82 ( 4.44)  0.154 (0.002)  32.80 ( 0.3)  0.082    88    25   11     0
      21.44      689.18 ( 5.18)  0.239 (0.002)  36.47 ( 0.3)  0.112   102    15   10     0
      23.58      634.82 ( 7.00)  0.285 (0.002)  36.47 ( 0.2)  0.102   111    14   10     0
      25.94      533.36 ( 5.05)  0.264 (0.001)  40.23 ( 0.2)  0.086   123    16   11     0
      28.53      556.56 ( 5.04)  0.348 (0.001)  47.71 ( 0.1)  0.072   123    21   21     0
      31.38      367.35 ( 4.80)  0.116 (0.002)  71.99 ( 0.6)  0.095   161    25   10     0
      34.52      294.35 ( 3.72)  0.110 (0.002)  71.99 ( 0.5)  0.087   182    23   10     0
      37.97      283.46 ( 3.59)  0.114 (0.002)  12.67 ( 0.6)  0.121   193    32   15     0
      41.77      242.09 ( 2.87)  0.114 (0.002)  25.08 ( 0.6)  0.118   219    29   10     0
      45.95      210.63 ( 2.34)  0.114 (0.002)  25.08 ( 0.6)  0.111   236    37   50     2
      50.54      208.59 ( 1.66)  0.195 (0.002) 170.04 ( 0.3)  0.096   247    39   10     0
      55.60      201.83 ( 1.05)  0.249 (0.001) 163.12 ( 0.1)  0.043   259    44   10     0
      61.16      166.77 ( 1.08)  0.249 (0.001) 163.12 ( 0.1)  0.096   308    25    3     5
      67.27      168.57 ( 1.01)  0.298 (0.001)  60.51 ( 0.1)  0.074   297    57   15     0
      74.00      149.81 ( 0.97)  0.298 (0.001)  60.51 ( 0.2)  None    332    57    9     5
      81.40      152.51 ( 0.75)  0.258 (0.001)  69.92 ( 0.1)  0.094   381    60   50     2
      89.54      140.31 ( 0.87)  0.258 (0.004)  69.92 ( 0.5)  0.469   454    31   11     5
      98.50      156.94 ( 0.85)  0.425 (0.001)  76.16 ( 0.1)  0.099   370    93   50     2
     108.35      136.89 ( 0.82)  0.305 (0.001)  65.58 ( 0.1)  0.082   480    86   10     0
     119.18      123.87 ( 0.69)  0.305 (0.001)  65.58 ( 0.2)  0.196   531    91    3     1
       9.09     1113.98 ( 9.01)  0.048 (0.010)  65.58 ( 6.0)  0.259    56     0   10     0
       8.26     1147.75 ( 6.87)  0.029 (0.006) 105.67 ( 6.6)  0.169    47     5   10     0
       7.51     1223.46 ( 5.70)  0.040 (0.004) 115.22 ( 4.0)  0.114    39     8   10     0
       6.83     1315.90 ( 5.70)  0.099 (0.005) 122.56 ( 1.4)  0.121    35     6   10     0
       6.21     1420.23 ( 3.82)  0.136 (0.003) 120.69 ( 0.6)  0.077    30     7   10     0
       5.64     1553.17 ( 4.06)  0.171 (0.004) 120.72 ( 0.5)  0.069    25     8   11     0
       5.13     1640.73 ( 5.51)  0.132 (0.004) 125.20 ( 0.8)  0.077    27     3   10     0
       4.67     1765.74 ( 5.76)  0.126 (0.003) 126.18 ( 0.7)  0.067    26     2   10     0
       4.24     1904.59 ( 6.06)  0.110 (0.003) 127.73 ( 0.8)  0.058    25     1   10     0
       3.86     2059.54 ( 7.09)  0.102 (0.003) 123.41 ( 0.9)  0.059    23     0   10     0
       3.50     2249.78 ( 6.43)  0.097 (0.003) 122.36 ( 0.9)  0.048    20     1   10     0
       3.19     2496.95 ( 6.36)  0.092 (0.002) 121.92 ( 0.9)  0.040    16     4   10     0
       2.90     2763.14 (11.28)  0.099 (0.003) 121.22 ( 1.2)  0.059    17     1   10     0
       2.63     3078.39 ( 9.40)  0.067 (0.004) 109.89 ( 1.8)  0.047    13     3   20     0
       2.39     3417.54 ( 4.59)  0.099 (0.001) 111.95 ( 0.5)  0.046    13     2   50     2
       2.18     3706.63 (12.93)  0.089 (0.004) 123.22 ( 1.5)  0.062    13     1   10     0
       1.98     4082.37 (15.63)  0.089 (0.004) 121.55 ( 1.7)  0.053    12     1   19     0
       1.80     4453.36 (14.93)  0.089 (0.005) 121.55 ( 1.5)  0.058    11     2   50     2
       1.64     4831.54 (14.93)  0.090 (0.005) 119.00 ( 1.3)  0.052    11     2   10     0
       1.49     5119.69 (16.64)  0.078 (0.006) 119.00 ( 2.0)  0.076    12     1   50     2
       1.35     5438.31 (18.15)  0.089 (0.006) 119.29 ( 2.2)  0.092    13     0   10     0
       1.23     5703.88 (21.42)  0.093 (0.008) 119.04 ( 2.8)  0.112    13     0   10     0
       1.12     5922.34 (18.08)  0.098 (0.007) 125.09 ( 2.8)  0.092    12     1   10     0
       1.02     6038.60 ( 8.79)  0.036 (0.006) 134.43 ( 5.6)  0.090    10     3    9     1
       0.92     6268.40 (23.03)  0.110 (0.015) 147.73 ( 4.3)  0.196    12     1   10     0
       0.84     6341.55 (11.83)  0.057 (0.010) 146.98 ( 6.4)  0.146     9     4    8     1
       0.76     6449.35 (13.03)  0.063 (0.012) 143.75 ( 8.1)  0.169    10     3   21     0
       0.69     6609.65 (25.92)  0.063 (0.024) 132.73 (12.0)  0.359    13     0   20     0
       0.63     6656.85 (12.02)  0.053 (0.013) 146.08 (10.4)  0.181    10     3   12     0
       0.57     6787.21 (23.22)  0.042 (0.025) 138.63 (19.1)  0.360    13     0   28     0
       0.52     6875.62 (20.50)  0.049 (0.025) 157.23 (16.1)  0.371    13     0   27     0
       0.00     7607.99


Now we build a model image.

Note that we use as fill value a background estimate taken from the data
array itself. This works OK for this particular image; users should
tailor the procedure according to their data and science goal.

.. code:: ipython3

    import numpy as np
    from stak.isophote.model import build_model
    
    model_image = build_model(pixel_data, isolist, fill=np.mean(pixel_data[0:10,0:10]))


.. parsed-literal::

    Interpolating....Done
    SMA=119.1
    Done


.. code:: ipython3

    print(pixel_data.shape)
    print(model_image.shape)


.. parsed-literal::

    (512, 512)
    (512, 512)


Display (just the central, modeled region):

.. code:: ipython3

    import matplotlib
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    %matplotlib inline
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
    
    limits = [128,384]
    
    ax1.imshow(model_image, cmap=cm.gnuplot, vmin=0, vmax=1000)
    ax1.set_xlim(limits)
    ax1.set_ylim(limits)
    ax1.set_title("Model")
    ax2.imshow(pixel_data, cmap=cm.gnuplot, vmin=0, vmax=1000)
    ax2.set_xlim(limits)
    ax2.set_ylim(limits)
    ax2.set_title("Data")




.. parsed-literal::

    <matplotlib.text.Text at 0x110c4bda0>




.. image:: isophote_example3_files/isophote_example3_8_1.png


Finally, subtract model from data:

.. code:: ipython3

    residual = pixel_data - model_image
    
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(residual, cmap=cm.gnuplot, vmin=-200, vmax=200)
    limits = [128,384]
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    ax.set_title("Residual")




.. parsed-literal::

    <matplotlib.text.Text at 0x110cfde10>




.. image:: isophote_example3_files/isophote_example3_10_1.png


Elliptical galaxy test image
----------------------------

Of course, M51 is not the best object to test this procedure, since the
non-elliptical contamination is so significant.

Better results for demo purposes can be obtained from a "true"
elliptical galaxy. We chose a public-domain image of M105 as published
at asd.gsfc.nasa.gov

We repeat the procedure above but this time passing a Geometry instance
to the Ellipse constructor, since the galaxy center does not coincide
with the image frame center. We also pass first guess values for the
ellipticity and position angle parameters, gleaned from visually
inspecting the image.

(We name variables here with "\_e" and "\_s" suffixes to tell them apart
from similar variables defined in the code above).

.. code:: ipython3

    image = fits.open("../../../stak/isophote/test/data/M105-S001-RGB.fits")
    pixel_data_e = image[0].data[0]
    
    from stak.isophote.ellipse.geometry import Geometry
    g = Geometry(530., 511, 10., 0.1, 10./180.*np.pi)
    
    ellipse_e = Ellipse(pixel_data_e, geometry=g)
    isolist_e = ellipse_e.fit_image()
    
    model_image_e = build_model(pixel_data_e, isolist_e, fill=np.mean(pixel_data_e[20:120,20:120]))
    residual_e = pixel_data_e - model_image_e


.. parsed-literal::

    Centering on object....   Done. Found x0 = 530.0, y0 = 512.0
    #
    # Semi-      Isophote         Ellipticity    Position     Grad.   Data  Flag Iter. Stop
    # major        mean                           Angle        rel.                    code
    # axis       intensity                                    error
    #(pixel)                                     (degree)
    #
      10.00     1512.34 ( 0.06)  0.066 (0.000)  12.19 ( 0.2)  0.013    61     0   20     0
      11.00     1505.58 ( 0.06)  0.074 (0.000)  13.00 ( 0.2)  0.015    67     0   10     0
      12.10     1499.54 ( 0.07)  0.077 (0.001)  12.89 ( 0.2)  0.016    74     0   10     0
      13.31     1494.16 ( 0.05)  0.082 (0.000)  12.69 ( 0.2)  0.016    81     0   10     0
      14.64     1489.53 ( 0.05)  0.083 (0.001)  12.11 ( 0.2)  0.019    89     0   10     0
      16.11     1485.90 ( 0.05)  0.088 (0.001)  10.68 ( 0.2)  0.023    97     0   10     0
      17.72     1483.12 ( 0.05)  0.097 (0.001)  11.79 ( 0.2)  0.027   106     0   10     0
      19.49     1480.81 ( 0.04)  0.105 (0.001)  11.44 ( 0.2)  0.038   116     0   10     0
      21.44     1479.20 ( 0.06)  0.136 (0.001)  10.65 ( 0.2)  0.036   126     0   10     0
      23.58     1477.36 ( 0.04)  0.142 (0.001)  10.65 ( 0.2)  0.032   137     0   10     0
      25.94     1475.94 ( 0.03)  0.152 (0.001)   9.02 ( 0.1)  0.030   150     0   10     0
      28.53     1474.56 ( 0.02)  0.145 (0.000)   5.86 ( 0.1)  0.027   166     0   10     0
      31.38     1473.30 ( 0.02)  0.142 (0.000)   9.74 ( 0.1)  0.028   183     0   10     0
      34.52     1472.18 ( 0.02)  0.149 (0.000)   8.22 ( 0.1)  0.029   201     0   10     0
      37.97     1470.99 ( 0.02)  0.149 (0.001)   8.49 ( 0.1)  0.033   221     0   10     0
      41.77     1469.88 ( 0.02)  0.136 (0.000)   5.39 ( 0.1)  0.028   245     0   10     0
      45.95     1469.01 ( 0.01)  0.144 (0.000)   9.73 ( 0.1)  0.029   268     0   10     0
      50.54     1468.29 ( 0.01)  0.144 (0.001)   9.73 ( 0.2)  0.485   295     0    3     5
      55.60     1467.73 ( 0.02)  0.144 (0.001)   9.73 ( 0.1)  0.047   324     0   50     2
      61.16     1467.14 ( 0.01)  0.144 (0.000)   9.73 ( 0.1)  0.036   357     0   50     2
      67.27     1466.70 ( 0.01)  0.139 (0.001)   9.73 ( 0.1)  0.044   394     0   10     0
      74.00     1466.23 ( 0.01)  0.109 (0.001)  13.46 ( 0.2)  0.045   441     0   10     0
      81.40     1465.88 ( 0.01)  0.109 (0.001)  13.46 ( 0.2)  0.064   485     0   10     0
      89.54     1465.64 ( 0.01)  0.109 (0.001)  13.46 ( 0.2)  0.082   533     0   50     2
      98.50     1465.47 ( 0.01)  0.109 (0.001)  13.46 ( 0.3)  0.084   587     0    1     5
     108.35     1465.31 ( 0.01)  0.109 (0.000)  13.46 ( 0.1)  None    645     0    1     5
       9.09     1520.53 ( 0.07)  0.066 (0.000)  12.70 ( 0.2)  0.013    56     0   12     0
       8.26     1529.50 ( 0.11)  0.063 (0.001)  18.18 ( 0.3)  0.015    51     0   10     0
       7.51     1538.91 ( 0.10)  0.053 (0.001)  22.38 ( 0.3)  0.017    46     0   10     0
       6.83     1549.62 ( 0.10)  0.040 (0.001)  26.42 ( 0.4)  0.015    43     0   10     0
       6.21     1562.60 ( 0.14)  0.039 (0.001)  26.62 ( 0.5)  0.014    39     0   10     0
       5.64     1577.08 ( 0.14)  0.033 (0.001)  39.76 ( 0.5)  0.015    35     0   10     0
       5.13     1593.26 ( 0.14)  0.033 (0.001)  48.99 ( 0.5)  0.013    32     0   10     0
       4.67     1611.89 ( 0.14)  0.038 (0.001)  62.87 ( 0.4)  0.017    29     0   10     0
       4.24     1630.72 ( 0.17)  0.034 (0.001)  67.66 ( 0.6)  0.013    27     0   50     2
       3.86     1653.00 ( 0.24)  0.048 (0.001)  76.63 ( 0.6)  0.016    24     0   10     0
       3.50     1675.90 ( 0.34)  0.058 (0.001)  81.07 ( 0.7)  0.024    22     0   10     0
       3.19     1697.24 ( 0.36)  0.054 (0.001)  82.28 ( 0.8)  0.023    20     0   10     0
       2.90     1718.63 ( 0.31)  0.060 (0.001)  83.84 ( 0.7)  0.023    18     0   10     0
       2.63     1738.51 ( 0.49)  0.051 (0.002)  85.08 ( 1.3)  0.030    17     0   10     0
       2.39     1755.57 ( 0.35)  0.036 (0.002)  79.75 ( 1.5)  0.035    15     0   50     2
       2.18     1772.65 ( 0.44)  0.031 (0.003)  84.57 ( 2.6)  0.041    14     0   10     0
       1.98     1788.92 ( 0.69)  0.014 (0.004)  71.73 ( 9.6)  0.069    13     0   34     0
       1.80     1805.67 ( 0.41)  0.024 (0.003)  91.49 ( 3.6)  0.042    13     0   50     2
       1.64     1819.13 ( 0.51)  0.025 (0.004)  82.93 ( 4.6)  0.049    13     0   50     2
       1.49     1831.88 ( 0.70)  0.021 (0.006)  73.98 ( 8.5)  0.081    13     0   11     0
       1.35     1843.27 ( 0.57)  0.028 (0.005)  80.81 ( 5.6)  0.066    13     0   50     2
       1.23     1853.54 ( 0.65)  0.045 (0.007)  81.99 ( 4.9)  0.097    13     0   10     0
       1.12     1862.29 ( 0.63)  0.059 (0.008)  85.40 ( 4.1)  0.112    13     0   11     0
       1.02     1869.33 ( 0.67)  0.060 (0.010)  84.89 ( 5.0)  0.133    13     0   10     0
       0.92     1874.21 ( 0.98)  0.042 (0.019)  78.03 (13.7)  0.255    13     0   10     0
       0.84     1879.25 ( 0.74)  0.072 (0.015)   9.39 ( 6.9)  0.217    13     0   11     0
       0.76     1885.59 ( 0.93)  0.178 (0.021)   1.13 ( 3.9)  0.314    13     0   10     0
       0.69     1889.50 ( 0.97)  0.219 (0.026)   1.13 ( 4.2)  0.446    13     0   50     2
       0.63     1891.89 ( 0.89)  0.219 (0.028)   1.13 ( 4.4)  0.494    13     0   50     2
       0.57     1894.08 ( 0.81)  0.219 (0.028)   1.13 ( 4.4)  0.495    13     0   50     2
       0.52     1896.01 ( 0.73)  0.219 (0.028)   1.13 ( 4.4)  0.497    13     0   50     2
       0.00     1912.16
    Interpolating....Done
    SMA=108.3
    Done


.. code:: ipython3

    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(15, 10))
    limits = [512-120,512+150]
    ax1.imshow(pixel_data_e, cmap=cm.gnuplot, vmin=1464., vmax=1480.)
    ax1.set_xlim(limits)
    ax1.set_ylim(limits)
    ax1.set_title("Data")
    ax2.imshow(model_image_e, cmap=cm.gnuplot, vmin=1464., vmax=1480.)
    ax2.set_xlim(limits)
    ax2.set_ylim(limits)
    ax2.set_title("Model")
    ax3.imshow(residual_e, cmap=cm.gnuplot, vmin=-3, vmax=3)
    ax3.set_xlim(limits)
    ax3.set_ylim(limits)
    ax3.set_title("Residual")
    ax4.imshow(residual_e, cmap=cm.gnuplot, vmin=-3, vmax=3)
    ax4.set_xlim(limits)
    ax4.set_ylim(limits)
    ax4.set_title("Residual")
    
    # overplot a few isophotes on the residual map
    iso1 = isolist_e.get_closest(10.)
    iso2 = isolist_e.get_closest(40.)
    iso3 = isolist_e.get_closest(100.)
    
    plt.axis([512-120,512+150,512-120,512+150])
    x, y, = iso1.sampled_coordinates()
    plt.plot(x, y, color='white')
    x, y, = iso2.sampled_coordinates()
    plt.plot(x, y, color='white')
    x, y, = iso3.sampled_coordinates()
    plt.plot(x, y, color='white')




.. parsed-literal::

    [<matplotlib.lines.Line2D at 0x1130a8278>]




.. image:: isophote_example3_files/isophote_example3_15_1.png


The residuals in more detail.

.. code:: ipython3

    fig, ax = plt.subplots(figsize=(6, 6))
    plt.axis([512-120,512+150,512-120,512+120])
    ax.imshow(residual_e, cmap=cm.gnuplot, vmin=-2, vmax=2)




.. parsed-literal::

    <matplotlib.image.AxesImage at 0x11c69d9b0>




.. image:: isophote_example3_files/isophote_example3_17_1.png


Note how the residuals are affected by the bright star image about 50
pixels to the right of the nucleus. The "isophote" that intercepts that
star image contains a significant non-elliptical component caused by the
inclusion of the bright star in the intensity sample extracted from the
image. This is a good candidate to be processed by sigma-clipping, as
explained in script 'example2.ipynb' (see below).

Out of curiosity, lets see how the radial profiles look like.

.. code:: ipython3

    plt.figure(figsize=(8, 4))
    
    plt.scatter(isolist_e.sma**0.25, -2.5*np.log10(isolist_e.intens))
    
    plt.xlabel('sma**1/4')
    plt.ylabel('Magnitude')
    plt.gca().invert_yaxis()
    plt.title("M105 brightness profile")




.. parsed-literal::

    <matplotlib.text.Text at 0x11c850668>




.. image:: isophote_example3_files/isophote_example3_20_1.png


.. code:: ipython3

    plt.figure(figsize=(10, 5))
    plt.figure(1)
    
    plt.subplot(221)
    plt.errorbar(isolist_e.sma, isolist_e.eps, yerr=isolist_e.ellip_err, fmt='o', markersize=4)
    plt.title('EPS')
    
    plt.subplot(222)
    plt.errorbar(isolist_e.sma, isolist_e.pa/np.pi*180., yerr=isolist_e.pa_err/np.pi* 80., fmt='o', markersize=4)
    plt.title('PA (deg.)')
    
    plt.subplot(223)
    plt.errorbar(isolist_e.sma, isolist_e.x0, yerr=isolist_e.x0_err, fmt='o', markersize=4)
    plt.title('X0')
    
    plt.subplot(224)
    plt.errorbar(isolist_e.sma, isolist_e.y0, yerr=isolist_e.y0_err, fmt='o', markersize=4)
    plt.title('Y0')
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)



.. image:: isophote_example3_files/isophote_example3_21_0.png


.. code:: ipython3

    plt.figure(figsize=(10, 5))
    plt.figure(1)
    limits = [0., 100., -0.2, 0.2]
    
    plt.subplot(221)
    plt.axis(limits)
    plt.errorbar(isolist_e.sma, isolist_e.a3, yerr=isolist_e.a3_err, fmt='o', markersize=4)
    plt.title('A3')
    
    plt.subplot(222)
    plt.axis(limits)
    plt.errorbar(isolist_e.sma, isolist_e.b3, yerr=isolist_e.b3_err, fmt='o', markersize=4)
    plt.title('B3')
    
    plt.subplot(223)
    plt.axis(limits)
    plt.errorbar(isolist_e.sma, isolist_e.a4, yerr=isolist_e.a4_err, fmt='o', markersize=4)
    plt.title('A4')
    
    plt.subplot(224)
    plt.axis(limits)
    plt.errorbar(isolist_e.sma, isolist_e.b4, fmt='o', yerr=isolist_e.b4_err, markersize=4)
    plt.title('B4')
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)



.. image:: isophote_example3_files/isophote_example3_22_0.png


Note how the presence of the bright star causes a significant
non-elliptical component to appear around SMA=50 pixels.

Lets repeat the procedure with sigma-clipping enabled to remove the star
and see the effect on the residuals map.

Note that there is no need to create a new Ellipse instance, since
nothing changed in either the input pixel map nor the input geometry.

.. code:: ipython3

    isolist_s = ellipse_e.fit_image(sclip=3., nclip=3, verbose=False)
    
    model_image_s = build_model(pixel_data_e, isolist_s, fill=np.mean(pixel_data_e[20:120,20:120]))
    residual_s = pixel_data_e - model_image_s


.. parsed-literal::

    Interpolating....Done
    SMA=108.3
    Done


Plot residuals using a very narrow range for the pixel values.

.. code:: ipython3

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))
    limits = [512-120,512+150]
    ax1.imshow(residual_s, cmap=cm.gnuplot, vmin=-0.5, vmax=0.5)
    ax1.set_xlim(limits)
    ax1.set_ylim(limits)
    ax1.set_title('With sigma-clip')
    ax2.imshow(residual_e, cmap=cm.gnuplot, vmin=-0.5, vmax=0.5)
    ax2.set_xlim(limits)
    ax2.set_ylim(limits)
    ax2.set_title('Without sigma-clip')




.. parsed-literal::

    <matplotlib.text.Text at 0x11e6ad940>




.. image:: isophote_example3_files/isophote_example3_27_1.png


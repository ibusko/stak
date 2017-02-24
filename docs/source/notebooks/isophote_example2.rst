:orphan:


Running 'ellipse' with sigma-clipping
=====================================

In this example, we execute the basic fitting demonstrated in the
'example1.ipynb' notebook, with the main difference that the fit is
performed with sigma-clipping.

Note: notebooks will only run when the 'jupyter notebook' command is
issued from directory stak/docs/source/notebooks

We start in the same way:

.. code:: ipython3

    from astropy.io import fits
    image = fits.open("../../../stak/isophote/test/data/M51.fits")
    pixel_data = image[0].data
    
    from stak.isophote.ellipse.ellipse import Ellipse
    ellipse = Ellipse(pixel_data)


.. parsed-literal::

    Centering on object....   Done. Found x0 = 257.0, y0 = 258.0


Sigma-clipping is implemented via parameters on the 'fit\_image' method.
In this example, due to the significant contamination of the image by
non-elliptical features, we apply quite aggressive clipping.

.. code:: ipython3

    isophote_list = ellipse.fit_image(sclip=2., nclip=3)


.. parsed-literal::

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


Note how the added stability provided by sigma-clipping allows the fit
to proceed further outwards before sensing a too low signal-to-noise
condition.

Plotting results
----------------

Similar to what we did before in notebook 'example1.ipynb':

.. code:: ipython3

    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline
    plt.rcParams['image.origin'] = 'lower'

.. code:: ipython3

    plt.figure(figsize=(8, 4))
    
    plt.scatter(isophote_list.sma**0.25, -2.5*np.log10(isophote_list.intens))
    
    plt.xlabel('sma**1/4')
    plt.ylabel('Magnitude')
    plt.gca().invert_yaxis()
    plt.title("M51 profile with sigma-clip")




.. parsed-literal::

    <matplotlib.text.Text at 0x11033a438>




.. image:: isophote_example2_files/isophote_example2_9_1.png


.. code:: ipython3

    plt.figure(figsize=(10, 5))
    plt.figure(1)
    
    plt.subplot(221)
    plt.errorbar(isophote_list.sma, isophote_list.eps, yerr=isophote_list.ellip_err, fmt='o', markersize=4)
    plt.title('EPS')
    
    plt.subplot(222)
    plt.errorbar(isophote_list.sma, isophote_list.pa/np.pi*180., yerr=isophote_list.pa_err/np.pi* 80., fmt='o', markersize=4)
    plt.title('PA (deg.)')
    
    plt.subplot(223)
    plt.errorbar(isophote_list.sma, isophote_list.x0, yerr=isophote_list.x0_err, fmt='o', markersize=4)
    plt.title('X0')
    
    plt.subplot(224)
    plt.errorbar(isophote_list.sma, isophote_list.y0, yerr=isophote_list.y0_err, fmt='o', markersize=4)
    plt.title('Y0')
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)



.. image:: isophote_example2_files/isophote_example2_10_0.png


Overplot a few "isophotes" on the image display:

.. code:: ipython3

    import matplotlib.cm as cm
    
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(pixel_data, cmap=cm.gnuplot, vmin=0, vmax=1000)
    plt.axis([0,511,0,511])
    
    iso1 = isophote_list.get_closest(20.)
    iso2 = isophote_list.get_closest(50.)
    iso3 = isophote_list.get_closest(90.)
    
    x, y, = iso1.sampled_coordinates()
    plt.plot(x, y, color='white')
    x, y, = iso2.sampled_coordinates()
    plt.plot(x, y, color='white')
    x, y, = iso3.sampled_coordinates()
    plt.plot(x, y, color='white')




.. parsed-literal::

    [<matplotlib.lines.Line2D at 0x110f99f28>]




.. image:: isophote_example2_files/isophote_example2_12_1.png


Brightness samples associated with the three isophotes above are plotted
next.

Note that the angles in the raw sample arrays are defined w.r.t the
semi-major axis position angle. To plot everything in the same
coordinate system, we have to offset each isophote's angles array by the
corresponding position angle.

.. code:: ipython3

    plt.figure(figsize=(10, 3))
    
    plt.scatter((iso1.sample.values[0]+iso1.sample.geometry.pa)/np.pi*180., iso1.sample.values[2], color='red')
    plt.scatter((iso2.sample.values[0]+iso2.sample.geometry.pa)/np.pi*180., iso2.sample.values[2], color='black')
    plt.scatter((iso3.sample.values[0]+iso3.sample.geometry.pa)/np.pi*180., iso3.sample.values[2], color='blue')
    
    plt.ylabel("Intensity")
    plt.xlabel("Angle (deg.)")




.. parsed-literal::

    <matplotlib.text.Text at 0x110f5ab38>




.. image:: isophote_example2_files/isophote_example2_14_1.png


Parameters that measure deviations from a perfect ellipse can be plotted
like this:

.. code:: ipython3

    plt.figure(figsize=(10, 5))
    plt.figure(1)
    limits = [0., 100., -0.1, 0.1]
    
    plt.subplot(221)
    plt.axis(limits)
    plt.errorbar(isophote_list.sma, isophote_list.a3, yerr=isophote_list.a3_err, fmt='o', markersize=4)
    plt.title('A3')
    
    plt.subplot(222)
    plt.axis(limits)
    plt.errorbar(isophote_list.sma, isophote_list.b3, yerr=isophote_list.b3_err, fmt='o', markersize=4)
    plt.title('B3')
    
    plt.subplot(223)
    plt.axis(limits)
    plt.errorbar(isophote_list.sma, isophote_list.a4, yerr=isophote_list.a4_err, fmt='o', markersize=4)
    plt.title('A4')
    
    plt.subplot(224)
    plt.axis(limits)
    plt.errorbar(isophote_list.sma, isophote_list.b4, fmt='o', yerr=isophote_list.b4_err, markersize=4)
    plt.title('B4')
    
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.35, wspace=0.35)



.. image:: isophote_example2_files/isophote_example2_16_0.png



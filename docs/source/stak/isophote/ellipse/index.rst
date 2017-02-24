.. image:: /images/stsci_pri_combo_mark_white_bkgd.png
   :align: center
   :scale: 8


===================================
Isophote package
===================================
The `isophote` package in the Space Telescope Astronomy Kit (STAK) replaces the
analysis/isophote package formerly found in the STSDAS software.

The core of the package is the `ellipse` analysis algorithm. It is designed to
fit elliptical isophotes to galaxy images.

The image is measured using an iterative method described in [CIT1]_. Each isophote
is fitted at a pre-defined, fixed semi-major axis length. The algorithm starts from
a first guess ellipse. The image is sampled along that elliptical path, producing a
1-dimensional function that describes the dependency of the intensity (pixel value)
with the polar angle. The harmonic content of this function is decomposed by
least-squares fitting to an harmonic function that includes first and second harmonics.

Each one of the harmonic amplitudes that result from this fit is related to a specific
ellipse geometric parameter, in the sense that it conveys information regarding how
much the current parameter value deviates from the "true" one. At each iteration,
the largest amplitude among the fitted values is selected and used to compute the
corresponding increment in the associated ellipse parameter. That parameter is updated,
and the image is resampled. The process is repeated until certain criteria are met.

See the documentation for the Ellipse class for details.

Refer to the examples in the notebooks for how to start using the package.

Refer to the API documentation below for the detailed description of each class,
method, and parameter.


Reference/API
=============

.. automodapi:: stak.isophote.ellipse


Frequently Asked Questions
==========================

.. include:: faq.rst










1 - What are the basic equations relating harmonic amplitudes to geometrical parameter updates?

The basic elliptical isophote fitting algorithm, as described in reference [1], computes
corrections for the current ellipse's geometrical parameters by essentially "projecting"
the fitted harmonic amplitudes onto the image plane:

.. math::

    {\delta}_{X0} = \frac {-B_{1}} {I'}

.. math::

    {\delta}_{Y0} = \frac {-A_{1} (1 - {\epsilon})} {I'}

.. math::

    {\delta}_{\epsilon} = \frac {-2 B_{2} (1 - {\epsilon})} {I' a}

.. math::

    {\delta}_{\Theta} = \frac {2 A_{2} (1 - {\epsilon})} {I' a [(1 - {\epsilon}) ^ 2 - 1 ]}



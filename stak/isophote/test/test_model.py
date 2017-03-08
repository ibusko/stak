from __future__ import (absolute_import, division, print_function, unicode_literals)

import unittest

import numpy as np
from astropy.io import fits

from stak.isophote.ellipse.geometry import Geometry
from stak.isophote.ellipse.ellipse import Ellipse
from stak.isophote.model import build_model
from stak.isophote.util.build_test_data import build

TEST_DATA = "data/"


class TestModel(unittest.TestCase):

    def test_model(self):
        name = "M105-S001-RGB"
        test_data = fits.open(TEST_DATA + name + ".fits")
        image = test_data[0].data[0]

        g = Geometry(530., 511, 10., 0.1, 10./180.*np.pi)
        ellipse = Ellipse(image, geometry=g, verbose=False, threshold=1.e5)
        isophote_list = ellipse.fit_image(verbose=False)
        model = build_model(image, isophote_list, fill=np.mean(image[10:100,10:100]), verbose=False)

        self.assertEqual(image.shape, model.shape)

        residual = image - model

        self.assertLessEqual(np.mean(residual),  5.0)
        self.assertGreaterEqual(np.mean(residual), -5.0)

    def test_2(self):
        image = build(eps=0.5, pa=np.pi/3., noise=1.e-2)

        g = Geometry(256., 256., 10., 0.5, np.pi/3.)
        ellipse = Ellipse(image, geometry=g, verbose=False, threshold=1.e5)
        isophote_list = ellipse.fit_image(verbose=False)
        model = build_model(image, isophote_list, fill=np.mean(image[0:50,0:50]), verbose=False)

        self.assertEqual(image.shape, model.shape)

        residual = image - model

        self.assertLessEqual(np.mean(residual),  5.0)
        self.assertGreaterEqual(np.mean(residual), -5.0)



import unittest
import os
import cv2

import bibtagger.bodydetector as bd
import bibtagger.bibtagger as bt

class testbibtagger(unittest.TestCase):

    photodir = ""

    #called before every test
    def setUp(self):
        #self.widget = Widget('The widget')
        self.basedir = os.path.dirname(os.path.abspath(os.curdir))
        self.photodir = os.path.join(self.basedir,"photos")
        self.photooutdir = os.path.join(self.basedir, "photos-out")
        print "setup"

    def tearDown(self):
        #self.widget.dispose()
        print "teardown"

    def test_findBibs(self):

        print self.photodir

        #image = cv2.imread(os.path.join(self.photodir,"Frosty5k","1.jpg"))
        #image = cv2.imread(os.path.join(self.photodir,"abba.png"))
        image = cv2.imread(os.path.join(self.photodir,"GloryDays","4.jpg"))

        print image.shape
        #bd.getbodyboxes(image)
        bt.findBibs(image,os.path.join(self.photooutdir,"test_one_image"))

    def test_nullImage(self):
        #self.assertEqual('foo'.upper(), 'FOO')
        #self.assertTrue('FOO'.isupper())
        bt.findBibs(None)

if __name__ == '__main__':
    unittest.main()
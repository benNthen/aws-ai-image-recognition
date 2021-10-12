import unittest
import image_helpers
import vehicle_detect
import wordsearch
import pathlib as pl
import tracemalloc

tracemalloc.start()

class TestDet(unittest.TestCase):

    def test_file_valid(self):

        # Assume : image is valid/found
        # re-write line of code - that's bound to pass
        img_path = pl.Path('images/car.jpg')

        # Action : checks for the output
        imgbytes = image_helpers.get_image_from_file(img_path)

        # Assert :
        self.assertTrue(imgbytes)

    def test_file_invalid(self):

        # Assume : image is invalid/not found
        # re-write line of code - that's bound to fail
        img_path = pl.Path('images/nothere.jpg')

        # Action :
        if img_path.is_file():
            # Assert :
            self.assertFalse(img_path)

    # def test_output(self): #suppose to compare output_disp to actual JSON code - if they match
    #                     # then test should pass. Eg. Sedan in Labels == Sedan mentioned in output
    #
    #     photo = 'images/car.jpg'
    #
    #     a = vehicle_detect.detect_labels_local_file(photo) # this returns array from JSON data
    #
    #     b = vehicle_detect.output_display(0) # this returns output word from image (eg. car, truck)
    #
    #     word_similarity = wordsearch.Solution() # calls the wordsearch function for comparison between
    #                                 # a and b
    #
    #     if word_similarity.exist(a, b): # condition - pass test if JSON data matches output
    #         self.assertTrue(self)

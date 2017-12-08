import unittest
from prelims import *
from constraints import *


class TestNote(unittest.TestCase):
    def test_eq(self):
        self.assertTrue(Note('A', 2) == Note('A', 2))
        self.assertTrue(Note('C', 4) == Note('C', 4))
        self.assertFalse(Note('D', 3) == Note('D', 4))
        self.assertFalse(Note('C', 2) == Note('E', 2))
    def test_lt(self):
        self.assertTrue(Note('C', 2) < Note('D', 2))
        self.assertTrue(Note('C', 2) < Note('C', 3))
        self.assertFalse(Note('C', 2) < Note('C', 2))
        self.assertFalse(Note('C', 2) < Note('C', 1))
    def test_sub(self):
        self.assertEqual(Note('E', 2) - Note('C', 2), 3)
        self.assertEqual(Note('C', 3) - Note('C', 2), 8)
        self.assertEqual(Note('D', 2) - Note('D', 2), 1)
    def test_str(self):
        self.assertEqual(str(Note('C', 3)), 'C3')

class TestAllAboutBass(unittest.TestCase):
    def test_invert_0(self):
        self.assertEquals(all_about_that_bass(1, 0), [[1, 3, 5], [3, 5, 5],
                          [3, 3, 5]])
        self.assertEquals(all_about_that_bass(2, 0), [[4, 4, 6], [2, 4, 6]])
        self.assertEquals(all_about_that_bass(3, 0), [[5, 5, 7], [3, 5, 7]])
        self.assertEquals(all_about_that_bass(4, 0), [[4, 6, 1], [6, 1, 1],
                          [6, 6, 1]])
        self.assertEquals(all_about_that_bass(5, 0), [[5, 7, 2], [5, 2, 2]])
        self.assertEquals(all_about_that_bass(6, 0), [[1, 1, 3], [6, 1, 3]])
        self.assertEquals(all_about_that_bass(7, 0), [[2, 2, 4]])
    def test_invert_1(self):
        self.assertEquals(all_about_that_bass(1, 1), [[6, 1, 3], [6, 6, 3]])
        self.assertEquals(all_about_that_bass(2, 1), [[7, 2, 4]])
        self.assertEquals(all_about_that_bass(3, 1), [[1, 1, 5], [1, 5, 5],
                          [1, 3, 5]])
        self.assertEquals(all_about_that_bass(4, 1), [[2, 4, 6], [2, 2, 6]])
        self.assertEquals(all_about_that_bass(5, 1), [[3, 5, 7], [3, 3, 7]])
        self.assertEquals(all_about_that_bass(6, 1), [[4, 4, 1], [4, 1, 1],
                          [4, 6, 1]])
        self.assertEquals(all_about_that_bass(7, 1), [[5, 5, 2], [5, 2, 2]])
    def test_invert_2(self):
        self.assertEquals(all_about_that_bass(1, 2), [[4, 6, 1]])
        self.assertEquals(all_about_that_bass(2, 2), [[5, 7, 2]])
        self.assertEquals(all_about_that_bass(3, 2), [[6, 1, 3]])
        self.assertEquals(all_about_that_bass(4, 2), [[7, 2, 2]])
        self.assertEquals(all_about_that_bass(5, 2), [[1, 3, 5]])
        self.assertEquals(all_about_that_bass(6, 2), [[2, 4, 6]])
        self.assertEquals(all_about_that_bass(7, 2), [[3, 5, 7]])

class TestConstraints(unittest.TestCase):
    def test_crossvoice(self):
       chord_1 = [Note('G', 4), Note('C', 4), Note('G', 3), Note('C', 3)]
       chord_2 = [Note('G', 4), Note('C', 5), Note('G', 3), Note('C', 3)]
       chord_3 = [Note('G', 4), Note('C', 4), Note('E', 4), Note('C', 3)]
       chord_4 = [Note('G', 4), Note('C', 4), Note('G', 3), Note('C', 4)]
       self.assertTrue(crossvoice(chord_1))
       self.assertFalse(crossvoice(chord_2))
       self.assertFalse(crossvoice(chord_3))
       self.assertFalse(crossvoice(chord_4))
    def test_spacing(self):
       chord_b1 = [Note('G', 7), Note('C', 5), Note('G', 4), Note('C', 4)]
       chord_b2 = [Note('G', 5), Note('C', 5), Note('E', 3), Note('C', 3)]
       chord_good = [Note('G', 4), Note('E', 4), Note('C', 4), Note('C', 2)]
       self.assertFalse(spacing(chord_b1))
       self.assertFalse(spacing(chord_b2))
       self.assertTrue(spacing(chord_good))
    def test_parallel(self):
       octaves = parallel(1)
       fifths = parallel(5)
       voice_1 = (Note('C', 5), Note('E', 5))
       voice_2 = (Note('C', 4), Note('E', 4))
       voice_3 = (Note('C', 5), Note('D', 5))
       voice_4 = (Note('F', 4), Note('G', 4))
       self.assertFalse(octaves(voice_1, voice_2))
       self.assertFalse(fifths(voice_3, voice_4))
       self.assertTrue(octaves(voice_3, voice_4))
       self.assertTrue(fifths(voice_1, voice_2))
    def test_jump(self):
       jump_bad = jump(5)
       self.assertFalse(jump_bad(Note('C', 5), Note('A', 5)))
       self.assertTrue(jump_bad(Note('C', 5), Note('E', 5)))

if __name__ == '__main__':
    unittest.main()

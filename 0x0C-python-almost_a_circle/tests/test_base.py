#!/use/bin/python

import unittest

class TestBase(unittest.TestCase):
  def test_instantiation(self):
    instance_1 = Base()
    instance_2 = Base()
    instance_3 = Base()
    instance_4 = Base(None)
    instance_5 = Base(500)
    instance_6 = Base()
    
    self.assertEqual(instance_1.id, 1)
    self.assertEqual(instance_2.id, 2)
    self.assertEqual(instance_3.id, 3)
    self.assertEqual(instance_4.id, 4)
    self.assertEqual(instance_5.id, 500)
    self.assertEqual(instance_6.id, 5)

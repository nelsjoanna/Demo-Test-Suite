"""Demo Test Suite: purpose of a test suite is to
run every single test file you want together at the same time
using the test suite concept"""

import unittest
#import the test cases you want that you created
from unittestpackage.test_class1 import TestClass1
from unittestpackage.test_class2 import TestClass2

# get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestClass1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestClass2)

# create a Test Suite combining these two classes
smoke_test = unittest.TestSuite([tc1, tc2])

# trigger the run
unittest.TextTestRunner(verbosity=2).run(smoke_test)

import unittest

import PolinomTests

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(PolinomTests.PolinomSetAndGetTest))
calcTestSuite.addTest(unittest.makeSuite(PolinomTests.PolinomCallTest))
#такі собі тести

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)

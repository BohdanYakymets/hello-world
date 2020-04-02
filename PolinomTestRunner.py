import unittest

import PolinomTests

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(PolinomTests.PolinomSetAndGetTest))
calcTestSuite.addTest(unittest.makeSuite(PolinomTests.PolinomCallTest))
calcTestSuite.addTest(unittest.makeSuite(PolinomTests.PolinomStrTest))
calcTestSuite.addTest(unittest.makeSuite(PolinomTests.PolinomAddTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)

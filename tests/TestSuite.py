# import files
import unittest
from tests.LoginTest import LoginTest


# create object of the class using unitTest
loginTest = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

# create TestSuite
regressionTest = unittest.TestSuite(loginTest)

# call the test runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)

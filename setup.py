# -*- coding: utf-8 -*-
from setuptools import setup
import sys
import unittest

import yahoo_jtextapi
from yahoo_jtextapi import __version__, __license__, __author__

if __name__ == '__main__':
#   from jcconv import jcconv_test
#   # run module test
#   loader = unittest.TestLoader()
#   result = unittest.TestResult()
#   suite  = loader.loadTestsFromModule(jcconv_test)
#   suite.run(result)
#   if not result.wasSuccessful():
#     print "unit tests have failed!"
#     print "aborted to make a source distribution"
#     sys.exit(1)

  # build distribution package
  setup(
    packages         = ('yahoo_jtextapi',),
    name             = 'yahoo_jtextapi',
    version          = __version__,
    py_modules       = ['yahoo_jtextapi'], 
    description      = "Easy-to-use Interface for Yahoo! Japan's text analysis services",
    long_description = yahoo_jtextapi.__doc__,
    author           = __author__,
    author_email     = 'taichino@gmail.com',
    url              = 'http://github.com/taichino/yahoo_jtextapi',
    keywords         = 'yahoo japan, text analysis',
    license          = __license__,
    classifiers      = ["Development Status :: 3 - Alpha",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: POSIX",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Libraries :: Python Modules"]
    )

#! /usr/bin/env python
# -*- coding: utf-8 -*-


########################################################################################
#   Created on Nov 30, 2012                                                            #
#   Author: Bertrand Neron,                                                            #
#   Organization:'Projects and Developments in Bioinformatic' Group,                   #
#                 Institut Pasteur, Paris.                                             #  
#   Distributed under BSD3 Clause. Please refer to the COPYING document.               #
#                                                                                      #
########################################################################################

import os
import sys
import unittest


def run(lib, tests, verbosity = 0):
    """
    run the unit tests and print the results on stderr
    
    :param lib: the path where is the txsscanlib
    :type lib: string
    :param tests: the name of test to run. if tests is empty list, discover recursively tests form this directory.
                  a test is python module with the test_*.py pattern
    :type tests: list of string
    :param verbosity: the verbosity of the output
    :type verbosity: int
    """
    if lib not in sys.path:
        sys.path.insert(0, lib)
    if not tests:
        suite = unittest.TestLoader().discover(os.path.dirname(__file__), pattern="test_*.py" ) 
    else:
        suite = unittest.TestSuite()
        for test in tests: 
            if os.path.exists(test):
                if os.path.isfile(test):
                    fpath, fname =  os.path.split( test )
                    suite.addTests(unittest.TestLoader().discover(fpath , pattern = fname )) 
                elif os.path.isdir(test):  
                    suite.addTests(unittest.TestLoader().discover(test)) 
            else:
                sys.stderr.write(  "%s : no such file or directory\n" % test) 

    res = unittest.TextTestRunner(verbosity = verbosity).run(suite)
    return res



if __name__ == '__main__':

    from argparse import ArgumentParser    
    parser = ArgumentParser()
    parser.add_argument("tests",
                        nargs = '*',
                        default = [],
                        help = "name of test to execute")

    parser.add_argument("-v", "--verbose" , 
                        dest= "verbosity" , 
                        action="count" , 
                        help= "set the verbosity level of output",
                        default = 0
                        )

    args = parser.parse_args()
   
    src_path = os.path.abspath( os.path.join( os.path.dirname( __file__ ) , '..', 'src') )
    script_path = os.path.join( src_path , 'blast2seqids')
    os.symlink( script_path , script_path + ".py" )
    res = run(src_path, args.tests, args.verbosity)
    os.unlink( script_path + ".py" )
    sys.exit( not res.wasSuccessful())


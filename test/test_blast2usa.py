########################################################################################
#                                                                                      #
#   Author: Bertrand Neron                                                               #
#   Organization:'Biological Software and Databases' Group, Institut Pasteur, Paris.   #
#   Distributed under BSD3 Licence. Please refer to the COPYING.LIB document.         #
#                                                                                      #
########################################################################################


import unittest
import os.path
import sys

data_path = os.path.abspath( os.path.join( os.path.dirname( __file__ ) , 'data') )
from blast2usa import _searchBegining , parseSummary , format2usa


class Test(unittest.TestCase):


    def setUp(self):
        self.report_path = os.path.join(data_path, 'blast2_report.txt' )
        self.ids = [('sp', 'Q61285'), ('sp', 'Q9QY44'), ('sp', 'Q9UBJ2'), ('sp', 'P33897'), 
                    ('sp', 'P48410'), ('sp', 'P28288'), ('sp', 'P16970'), ('sp', 'P55096'), 
                    ('sp', 'Q8T8P3'), ('sp', 'P41909'), ('sp', 'P34230'), ('sp', 'Q94FB9'), 
                    ('sp', 'Q55774'), ('sp', 'O89016'), ('sp', 'O14678'), ('sp', 'Q54W20'), 
                    ('sp', 'Q54W19'), ('sp', 'Q6NLC1'), ('sp', 'Q50614'), ('sp', 'Q57335')]

        
    def tearDown(self):
        pass


    def testSearchBegining(self):
        report = open( self.report_path ,'r' )
        report = _searchBegining( report )
        first_summary_line = report.next()
        report.close()
        self.assertEqual(first_summary_line, "sp|Q61285|ABCD2_MOUSE RecName: Full=ATP-binding cassette sub-fam...  1508   0.0  \n")
        
    def testParseSummary(self):
        report = open( self.report_path ,'r' )
        ids = parseSummary( report )
        report.close()
        self.assertEqual( ids , self.ids )
        
        report = open( self.report_path ,'r' )
        ids = parseSummary( report , From = 5 )
        report.close()
        self.assertEqual( ids , self.ids[4: ] )
        
        report = open( self.report_path ,'r' )
        ids = parseSummary( report , To = 10 )
        report.close()
        self.assertEqual( ids , self.ids[: 10 ] )
       
        report = open( self.report_path ,'r' )
        ids = parseSummary( report , From = 10 , To = 15 )
        report.close()
        self.assertEqual( ids , self.ids[9: 15] )
        
    def testFormat2usa(self):
        ids= [ ( "sp" , "P33311" ) , ( "gb", "Q5F364") , ( "embl" , "O89016" ) ]
        usa = "sp:P33311\ngb:Q5F364\nembl:O89016\n"
        self.assertEqual( usa , format2usa(ids) )

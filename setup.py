#!/usr/bin/env python

from distutils.core import setup

setup(name        = 'blast2usa',
      version     = '1.1',
      author      = "Neron B",
      author_email = "bneron@pasteur.fr" ,
      license      = "GPLv2" ,
      description  = " parse a blast2 report ( text format -m 0 ) and return a list of hits identifier in usa format.",
      classifiers = [
	             'License :: GPLv2' ,
                     'Operating System :: POSIX' ,
                     'Programming Language :: Python' ,
                     'Topic :: Bioinformatics' ,
                    ] ,
      scripts     = [ 'src/blast2usa' ] ,
      )


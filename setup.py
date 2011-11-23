#!/usr/bin/env python

from distutils.core import setup
from distutils.command.install_egg_info import install_egg_info 
import time

class nohup_egg_info(install_egg_info):
  def run(self):
    #there is nothing to install in sites-package
    #so I don't put any eggs in it
    pass



setup(name        = 'blast2usa',
      version     = time.strftime("%Y%m%d"),
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
      cmdclass = { 'install_egg_info': nohup_egg_info }
      )


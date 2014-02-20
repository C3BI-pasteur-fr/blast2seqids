blast2seqid
===========


DESCRIPTION
-----------
  
  Parse a blast2 report ( text format -m 0 ) and return a list of hits identifier
  in usa format.
  Beware the output of blast can change according of options used to index your
  databanks (formatdb). In these conditions blast2seqids can fail to parse blast output.

Download distribution
---------------------

 [ ![Download](https://api.bintray.com/packages/bneron/generic/blast2seqids/images/download.png) ](https://bintray.com/bneron/generic/blast2seqids/view)


INSTALLATION from distribution
-------------------------------

 1. Uncompress and untar the package:

   tar -xzf blast2seqids-x.x.tar.gz

 2. go to blast2seqids directory
 
    cd blast2seqids-1.0

3. build and install

    python setup.py build
    python setup.py test -vv
    python setup.py install

    to see all installation options "python setup.py --help"

INSTALLATION from repository
----------------------------
 
  1. clone this github repository
  
     git clone https://github.com/bneron/blast2seqids/      

  2. got to INSTALLATION from distribution set 2.

LICENCE
-------

    blast2usa was developped at the "Institut Pasteur" in the
    "Projects and Developpemnt in Bioinformatics" group and is distributed under 
    BSD 3-Clause
    Please refer to the LICENSE document.

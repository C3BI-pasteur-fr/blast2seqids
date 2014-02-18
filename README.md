blast2seqid
===========


DESCRIPTION
-----------
  
  Parse a blast2 report ( text format -m 0 ) and return a list of hits identifier
  in usa format.
  Beware the output of blast can change according of options used to index your
  databanks (formatdb). In these conditions blast2usa can fail to parse blast output.

INSTALLATION
------------

 1. Uncompress and untar the package:

   tar -xzf blast2usa1.0.tar.gz

 2. go to blast2usa directory
 
    cd blast2usa1.0

3. build and install

    python setup.py build
		python setup.py test -vv
    python setup.py install

    to see all installation options "python setup.py --help"


LICENCE
-------

    blast2usa was developped at the "Institut Pasteur" in the
    "Projects and Developpemnt in Bioinformatics" group and is distributed under 
    BSD 3-Clause
    Please refer to the LICENSE document.

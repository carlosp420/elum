elum
====

.. image:: https://pypip.in/v/elum/badge.png
    :target: https://pypi.python.org/pypi/elum
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/carlosp420/elum.png
   :target: https://travis-ci.org/carlosp420/elum
   :alt: Latest Travis CI build status

Take a blast output file and complete it with metadata if the subject sequences are found in NCBI genbank.

It requires a CSV file as input file:

.. code:: shell

    query   subject pident  length  mismatch        gaps    qstart  qend    sstart  send    evalue  bitscore
    TR348|c0_g1_i1  gi|768429225|ref|XM_011557484.1|        69.03   2218    657     14      1766    3974    789     2985    0       866
    TR291|c0_g1_i2  gi|57506561|dbj|AB126052.1|     69.84   2261    627     29      2       2235    2494    4726    0       931
    TR365|c0_g5_i2  gi|910316988|ref|XM_013305788.1|        74.82   2518    617     7       56      2564    68      2577    0       1667

Usage
-----
.. code:: python

    python elum.py blast_out.csv > blast_out_completed.csv

Installation
------------

Requirements
^^^^^^^^^^^^

Compatibility
-------------

Licence
-------

Authors
-------

`elum` was written by `Carlos Pena <mycalesis@gmail.com>`_.

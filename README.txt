This package aims to provide much of the IDL "astron" functionality that
pertains to coordinate manipulations in an OO framework. Our target user is
a typical astronomer who needs to analyze data, work with catalogs, prepare
observing proposals, and prepare for observing runs.

It depends on numpy, which must already be installed on your
system.

It incorporates the TPM library, graciously contributed by Jeff
Percival, to perform coordinate system transformations. This will be
installed as part of the package installation.

Install this package in the usual way:

python setup.py install

After installation, you can test the package as follows:

>>> import coords as C
>>> C._test()

A successful test run will produce no output from this command.

If you have questions about this module, send mail to
help@stsci.edu and it will get to the appropriate
person.

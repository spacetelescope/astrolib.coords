These test files are intended to be usable with pandokia, nose, or
by importing the file and calling the functions directly.

If you add more test files, be sure to add them to:
    __init__.py
    the stsci_python coords.snout file in the nightly regtests

--

nosetests notes:

You can run these directly from the source directory, but they
require an installed copy of coords.

--

pandokia notes:

Use pdkrun on one of the test*.py files or use this in the file
coords.snout :

    coords.test_angsep
    coords.test_astrodate
    coords.test_tpm
    coords.test_pos

--

running directly:

    import coords
    coords.test()

--

developer:

Each test file has a function run() that calls each of the test
functions without using any test framework.  This works stand-alone,
but the first failing test terminates your test run.

The test functions can be called individually.


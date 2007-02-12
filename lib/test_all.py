"""Developer-use convenience module to run all unit tests."""

import testpos, test_angsep, test_tpm, test_astrodate, test_snapshot
def run():
    import coords
    coords._test() #snapshot test
    testpos.run()
    test_angsep.run()
    test_tpm.run()
    test_astrodate.run()


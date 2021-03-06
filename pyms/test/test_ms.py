import unittest
import pyms.ms as ms
import tempfile
import os
import shutil

class TestMs(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_one_section(self):
        with ms.MsSimu(nsamp=20,nreps=1,tau=200,
                    rho=200,nbsegsites=501) as mssimu :
            mssimu.run()
            (G,H) = mssimu.process_output()

        self.assertEqual(len(G),1)
        self.assertEqual(len(H),1)
        self.assertEqual(H[0].shape[0],20)
        
if __name__ == '__main__':
    unittest.main()

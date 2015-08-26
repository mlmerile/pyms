import unittest
import pyms.msparser as msparser
import tempfile
import os
import shutil

class TestMsparser(unittest.TestCase):

    def setUp(self):
        pass

    def test_empty_file(self):
        try:
            tmp_dir = tempfile.mkdtemp(prefix="TestMsparser")
            filename = os.path.join(tmp_dir,"test.txt")
            open(filename,'w').close()

            with open(filename,'r') as f:
                (eof,nbsegsites,res_ms_simu) = msparser.parse_section(f)

            self.assertEqual(eof, True)
        finally:
            try:
                shutil.rmtree(tmp_dir)
            except OSError as exc:
                if exc.errno != errno.ENOENT:
                    raise

    def test_one_section(self):
        try:
            tmp_dir = tempfile.mkdtemp(prefix="TestMsparser")
            filename = os.path.join(tmp_dir,"test.txt")
            with open(filename,'w') as f:
                f.write('//\n')
                f.write('segsites: 2\n')
                f.write('positions: 0.2 0.9\n')
                f.write('01\n')
                f.write('10\n')
                f.write('10\n')
                f.write('01\n')

            with open(filename,'r') as f:
                (eof,nbsegsites,res_ms_simu) = msparser.parse_section(f)

            self.assertEqual(eof, False)
            self.assertEqual(nbsegsites, 2)
            self.assertEqual(res_ms_simu.shape, (4,2))
        
        finally:
            try:
                shutil.rmtree(tmp_dir)
            except OSError as exc:
                if exc.errno != errno.ENOENT:
                    raise

if __name__ == '__main__':
    unittest.main()

# Lib
import numpy as np
import subprocess
import tempfile
import logging
import sys
import os
import shutil

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# Local Lib
import pyms.msparser as msparser

class MsSimu(object):
    """
    Ms simulation

    Run and store the output of an ms simu.
    """

    def __init__(self,nsamp,nreps,tau,rho,nbsegsites):
        self.nsamp = nsamp
        self.nreps = nreps
        self.tau = tau
        self.rho = rho
        self.nbsegsites = nbsegsites

        # File for output
        self.tmp_dir = tempfile.mkdtemp(prefix="OutputPyMs")
        self.outputfilename = os.path.join(self.tmp_dir,"res_ms_simu.txt")

        # results list of G and H
        self.G = []
        self.H = []
            
    def __enter__(self):
        return self

    def __exit__(self,type,value,traceback):
        try:
            shutil.rmtree(self.tmp_dir)
        except OSError as exc:
            if exc.errno != errno.ENOENT:
                raise

    def run(self):
        cmdline = "ms {0} {1} -t {2} -r {3} {4}".format(self.nsamp,
                                                        self.nreps,
                                                        self.tau,
                                                        self.rho,
                                                        self.nbsegsites)
        cmdline = cmdline + " > {0}".format(self.outputfilename)
        subprocess.call(cmdline,shell=True)

    def process_output(self):
        with open(self.outputfilename,'r') as f:
            line = f.readline() # CMD LINE
            line = f.readline() # SEEDS
            line = f.readline() # New line

            eof = False
            res = []
            while not eof:
                (eof,nbsegsites,output_ms) = msparser.parse_section(f)
                if not eof:
                    res.append(output_ms)

        self.H = res
        self.G = MsSimu.compute_G(res)
        
        return (self.G,self.H)

    @staticmethod
    def compute_G(lH):
        lG = []
        for H in lH:
            G = H[::2,:] + H[1::2,:]
            lG.append(G)

        return lG

                
def main():
    print("Main empty")
    return

if __name__ == '__main__':
    main()

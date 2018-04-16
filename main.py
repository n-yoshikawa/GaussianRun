import os, sys
import GaussianRunPack
				
usage ='Usage; %s infile' % sys.argv[0]

try:
    infilename = sys.argv[1]
except:
    print (usage); sys.exit()

test_sdf = GaussianRunPack.GaussianDFTRun('B3LYP', '3-21g*',12, 'OPT energy dipole nmr uv',infilename,0)

#test_sdf.read_sdf()	
outdic = test_sdf.run_gaussian()
print (outdic)
#gap = test_sdf.Extract_values(infilename,1,0,1,1,0)

#print (gap)

#print(Energy[-1])



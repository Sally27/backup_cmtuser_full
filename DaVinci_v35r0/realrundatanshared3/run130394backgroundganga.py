import sys

print sys.argv

job_name = 'StrippingB23MuNuBackground'

sandbox = []

dv = DaVinci(version="v35r0", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v35r0/realrundatanshared2/run130394background.py' ])
#dv = DaVinci( version = 'v32r2p15', setupProjectOptions = '--nightly lhcb-branches Tue', platform = 'x86_64-slc5-gcc46-opt') #to run nightlies on LSF

opts = []

f = open("run130394background.py")
opts = f.read()
f.close()

print opts

#dv.extraopts = opts
dv.user_release_area = '/afs/cern.ch/user/s/slstefko/cmtuser/'

t = JobTemplate(application = dv)

print "Now reading the data"
#ds = dv.readInputData("/afs/cern.ch/user/s/slstefko/cmtuser/DaVinci_v35r0/Phys/StrippingSelections/tests/data/Reco14_Run125113.py")

#bk_down = BKQuery(type="Run",i"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/RealData/Reco14/90000000/FULL.DST")

bk_down = BKQuery (
    dqflag=['OK'],
    path = '/130394/Real Data/Reco14/90000000/FULL.DST' ,
    type = 'Run' 
    ) 
data = bk_down.getDataset()

mySplitter = SplitByFiles()
mySplitter.filesPerJob = 1
#mySplitter.maxFiles = -1


j = Job(t, 
  name = job_name, 
  backend = Dirac(), 
  inputdata = data, 
  outputfiles = [ DiracFile( '*.root') ],
  splitter = mySplitter
)

j.backend.settings['BannedSites'] = ['LCG.CERN.ch']
j.inputfiles =[ LocalFile( "/home/hep/ss4314/cmtuser/DaVinci_v35r0/realrundatanshared2/weights_110614_Lc_pX.xml") ]


print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id

#j.submit()

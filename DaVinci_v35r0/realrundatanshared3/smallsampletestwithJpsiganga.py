import sys

print sys.argv

myjobname = 'SmallDataMISIDStrip'

#sandbox = []

#dv = DaVinci(version="v36r4p1", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/afs/cern.ch/user/s/slstefko/cmtuser/DaVinci_v35r0/Phys/StrippingSelections/tests/run130393signal.py' ])

myapplication = DaVinci(version="v35r0")
myapplication.optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v35r0/realrundatanshared3/smallsampletestwithJpsi.py' ]

#dv = DaVinci(version="v35r0", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/afs/cern.ch/user/s/slstefko/cmtuser/DaVinci_v35r0/realdatarunnshared/run130392background.py' ])
#dv = DaVinci( version = 'v32r2p15', setupProjectOptions = '--nightly lhcb-branches Tue', platform = 'x86_64-slc5-gcc46-opt') #to run nightlies on LSF

#opts = []

#f = open("run130392background.py")
#opts = f.read()
#f.close()

#print opts

#dv.extraopts = opts
#dv.user_release_area = '/afs/cern.ch/user/s/slstefko/cmtuser/'

#t = JobTemplate(application = dv)

print "Now reading the data"
#ds = dv.readInputData("/afs/cern.ch/user/s/slstefko/cmtuser/DaVinci_v35r0/Phys/StrippingSelections/tests/data/Reco14_Run125113.py")

#bk_down = BKQuery(type="Run",i"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/RealData/Reco14/90000000/FULL.DST")

DATA_FILES = ['Reco14_Run130390.py',
              'Reco14_Run130391.py',
              'Reco14_Run130392.py',
              'Reco14_Run130393.py',
              'Reco14_Run130394.py',
              'Reco14_Run130395.py',
              'Reco14_Run130396.py']
DATALIST = []
for INPUT in DATA_FILES:
    DATALIST += myapplication.readInputData(INPUT)
data = LHCbDataset(DATALIST)



mySplitter = SplitByFiles()
mySplitter.filesPerJob = 1
#mySplitter.maxFiles = -1


j = Job( 
  name = myjobname,
  application = myapplication, 
  backend = Dirac(), 
  inputdata = data, 
  outputfiles = [ '*.root' ] ,
  splitter = mySplitter
)

#j.inputfiles =[ LocalFile( "/home/hep/ss4314/cmtuser/DaVinci_v35r0/realrundatanshared3/weights_110614_Lc_pX.xml") ]
j.inputsandbox =["/home/hep/ss4314/cmtuser/DaVinci_v35r0/realrundatanshared3/weights_110614_Lc_pX.xml"]

j.backend.settings['BannedSites'] = ['LCG.NIPNE-07.ro']

print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id


#j.submit()

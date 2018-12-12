import sys

print sys.argv

job_name = 'MisIDSSrestrip'

dv = DaVinci(version="v36r1p3", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/misidSSdata/runssmisidrestripping2011.py' ])

t = JobTemplate(application = dv)

print "Now reading the data"

bk_down = BKQuery(path="/LHCb/Collision11/Beam3500GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r1p1a/90000000/SEMILEPTONIC.DST",dqflag="OK")
data = bk_down.getDataset()

bk_up = BKQuery(path="/LHCb/Collision11/Beam3500GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r1p1a/90000000/SEMILEPTONIC.DST",dqflag="OK")
data.extend(bk_up.getDataset())



mySplitter = SplitByFiles()
mySplitter.filesPerJob = 10
mySplitter.maxFiles = -1

myMerger = RootMerger()
myMerger.files = ['B23MuNuFakeSS.root']
myMerger.overwrite = True     #False by default
myMerger.ignorefailed = True  #False by default
myMerger.args = '-f2'

j = Job(t, 
  name = job_name, 
  backend = Dirac(), 
  inputdata = data, 
#  postprocessors = myMerger,
  outputfiles = [ '*.root' ],
  splitter = mySplitter
)

j.inputfiles =[ LocalFile("/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/misidSSdata/weights_110614_Lc_pX.xml")]

print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id

#j.submit()

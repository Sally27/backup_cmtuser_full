import sys

print sys.argv

job_name = 'MisIDOS12restrip'


dv = DaVinci(version="v36r1p3", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/misidOSdata/runosmisidrestripping2012.py' ])


t = JobTemplate(application = dv)

print "Now reading the data"

bk_down = BKQuery(path="/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21r0p1a/90000000/SEMILEPTONIC.DST",dqflag="OK")
data = bk_down.getDataset()

bk_up = BKQuery(path="/LHCb/Collision12/Beam4000GeV-VeloClosed-MagUp/Real Data/Reco14/Stripping21r0p1a/90000000/SEMILEPTONIC.DST",dqflag="OK")
data.extend(bk_up.getDataset())



mySplitter = SplitByFiles()
mySplitter.filesPerJob = 10
mySplitter.maxFiles = -1

myMerger = RootMerger()
myMerger.files = ['B23MuNuFakeOS.root']
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

j.inputfiles =[ LocalFile("/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/misidOSdata/weights_110614_Lc_pX.xml")]
print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id


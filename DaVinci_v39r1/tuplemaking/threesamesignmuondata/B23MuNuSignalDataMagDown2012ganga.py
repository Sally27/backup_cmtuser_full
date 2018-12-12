import sys

print sys.argv

job_name = 'B23SameSignMuDown12'

#sandbox = []

#dv = DaVinci()
dv = DaVinci(version="v39r1", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v39r1/tuplemaking/threesamesignmuondata/B23SameSignMuNuData2012.py' ])
#dv = DaVinci(version="v39r1", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v39r1/tuplemaking/threesamesignmuondata/B23MuNuSignalData.py' ])
#dv = DaVinci( version = 'v32r2p15', setupProjectOptions = '--nightly lhcb-branches Tue', platform = 'x86_64-slc5-gcc46-opt') #to run nightlies on LSF

#opts = []

#f = open("new.py")
#opts = f.read()
#f.close()

#print opts

#dv.extraopts = opts
#dv.user_release_area = '/afs/cern.ch/user/s/slstefko/cmtuser/'

t = JobTemplate(application = dv)

print "Now reading the data"
#ds = dv.readInputData("/afs/cern.ch/user/s/slstefko/cmtuser/DaVinci_v35r0/Phys/StrippingSelections/tests/data/Reco14_Run125113.py")

#bk_down = BKQuery(type="Run",i"/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/RealData/Reco14/90000000/FULL.DST")

bk_down = BKQuery("/LHCb/Collision12/Beam4000GeV-VeloClosed-MagDown/Real Data/Reco14/Stripping21/90000000/SEMILEPTONIC.DST")
data = bk_down.getDataset()
#bk_up = BKQuery("/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12513020/ALLSTREAMS.DST")
#data.extend(bk_up.getDataset())

#bk_down = BKQuery (
#    dqflag=['OK'],
#    path = '/130391/Real Data/Reco14/90000000/FULL.DST' ,
#    type = 'Run' 
#    ) 
#data = bk_down.getDataset()

mySplitter = SplitByFiles()
mySplitter.filesPerJob = 5
mySplitter.maxFiles = -1

myMerger = RootMerger()
myMerger.files = ['DVHistosignal.root','DVTuplesignal.root']
myMerger.overwrite = True     #False by default
myMerger.ignorefailed = True  #False by default
myMerger.args = '-f2'

j = Job(t, 
  name = job_name, 
  backend = Dirac(), 
  inputdata = data, 
  postprocessors = myMerger,
  outputfiles = [ '*.root' ],
  splitter = mySplitter
)

#j.application.args = ["-T"] # Use tcmalloc
j.inputfiles = [ LocalFile ("/home/hep/ss4314/cmtuser/DaVinci_v39r1/tuplemaking/threesamesignmuondata/weights_110614_Lc_pX.xml")]

print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id

#j.submit()

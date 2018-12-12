import sys

print sys.argv


myJobName = '2015DownB2JpsiKMC'
myApplication = DaVinci(version="v39r1",platform = 'x86_64-slc6-gcc48-opt')
#myApplication = DaVinci(version="v36r7p4")
### Define job-options file
myApplication.optsfile = ['/home/hep/ss4314/cmtuser/DaVinci_v39r1/tuplemaking/controlchannel2015diffiso/mc/BuJpsiK_MC_B23Mu_MagDown_2015.py']
#myApplication.optsfile = ['/home/hep/th1011/Documents/B2KmumuAna/controlchannel2015diffiso/reconstruction/b2xmumu_2012.py']

### Input & output data
#data = DaVinci().readInputData('/afs/cern.ch/user/y/yiming/projects/Bc/Bc2Psi2sPi/Psi2mumu/mc/options/mc11a_Bc2Psi2Spi_102k.py')
#bkpath = BKQuery('/LHCb/Collision11/Beam3500GeV-VeloClosed-MagDown/Real Data/Reco12/Stripping17/90000000/DIMUON.DST',dqflag=['OK'])
#bk_down = BKQuery("/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia6/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12143001/ALLSTREAMS.DST")
#data = bk_down.getDataset()
bk_down = BKQuery("/MC/2015/Beam6500GeV-2015-MagDown-Nu1.6-25ns-Pythia8/Sim09a/Trig0x411400a2/Reco15a/Turbo02/Stripping24NoPrescalingFlagged/12143001/ALLSTREAMS.DST") 
data=bk_down.getDataset() 
#bk_down2 = BKQuery("/MC/2011/Beam3500GeV-2011-MagDown-Nu2-Pythia8/Sim08c/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/12143001/ALLSTREAMS.DST")
#data.extend(bk_down2.getDataset()) 
#bk_up2 = BKQuery("/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12143001/ALLSTREAMS.DST")
#data.extend(bk_up2.getDataset())

myOutputdata =['*.root']


### choose Dirac backend and specify CPU time in seconds
#myBackend = Dirac()
myBackend = Dirac()  # for test only!!

### split into subjobs, defining max number of input files & number of input files per subjob

mySplitter = SplitByFiles()
mySplitter.filesPerJob = 1
#mySplitter.maxFiles = -1
#mySplitter.ignoremissing = True
#mySplitter.bulksubmit = False

### define subjob files to be merged
myMerger = RootMerger()
myMerger.files = ['BuKMuMuMC2015.root']
myMerger.overwrite = True     #False by default
myMerger.ignorefailed = True  #False by default

### create and submit job
j = Job (
     name         = myJobName,
      application  = myApplication,
      splitter     = mySplitter,
 #     postprocessors       = myMerger,
      outputfiles   = myOutputdata,
      backend      = myBackend,
      inputdata    = data
     )

j.inputfiles =[ LocalFile("/home/hep/ss4314/cmtuser/DaVinci_v39r1/tuplemaking/controlchannel2015diffiso/mc/weights_110614_Lc_pX.xml")]
#j.inpudata=j.inputdata[:1]

print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id


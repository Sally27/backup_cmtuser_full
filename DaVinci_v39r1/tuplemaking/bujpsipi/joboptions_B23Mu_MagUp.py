
myJobName = 'UpB2JpsiPiMC'
myApplication = DaVinci(version="v39r1",platform = 'x86_64-slc6-gcc48-opt')
#myApplication = DaVinci(version="v36r7p4")
### Define job-options file
myApplication.optsfile = ['/home/hep/ss4314/cmtuser/DaVinci_v39r1/tuplemaking/bujpsipi/BuJpsiK_MC_B23Mu_MagUp.py']
#myApplication.optsfile = ['/home/hep/th1011/Documents/B2KmumuAna/controlchannel/reconstruction/b2xmumu_2012.py']

### Input & output data
#data = DaVinci().readInputData('/afs/cern.ch/user/y/yiming/projects/Bc/Bc2Psi2sPi/Psi2mumu/mc/options/mc11a_Bc2Psi2Spi_102k.py')
#bkpath = BKQuery('/LHCb/Collision11/Beam3500GeV-VeloClosed-MagUp/Real Data/Reco12/Stripping17/90000000/DIMUON.DST',dqflag=['OK'])
#bk_down = BKQuery("/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12143001/ALLSTREAMS.DST")
#data = bk_down.getDataset()
bk_down = BKQuery("/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12143010/ALLSTREAMS.DST") 
data=bk_down.getDataset() 
bk_down2 = BKQuery("/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08a/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12143010/ALLSTREAMS.DST")
data.extend(bk_down2.getDataset()) 
#bk_up2 = BKQuery("/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12143001/ALLSTREAMS.DST")
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
myMerger.files = ['BuKMuMuMC.root']
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

j.inputfiles =[ LocalFile("/home/hep/ss4314/cmtuser/DaVinci_v39r1/tuplemaking/bujpsipi/weights_110614_Lc_pX.xml")]
#j.inpudata=j.inputdata[:1]

print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id



myJobName = 'NewMCtagcorrectUp'
myApplication = DaVinci(version="v36r1p3")
myApplication.optsfile = ['/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/signalmc/B23MuNuSignalSelectionMagUp.py']


#Inputdata

#bk_down = BKQuery("/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia6/Sim08h/Digi13/Trig0x409f0045/Reco14c/Stripping20NoPrescalingFlagged/12513070/ALLSTREAMS.DST")
#data = bk_down.getDataset()
bk_up = BKQuery("/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia6/Sim08h/Digi13/Trig0x409f0045/Reco14c/Stripping20NoPrescalingFlagged/12513070/ALLSTREAMS.DST") 
data = bk_up.getDataset()
#data.extend(bk_up.getDataset()) 
#bk_down2 = BKQuery("/MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08h/Digi13/Trig0x409f0045/Reco14c/Stripping20NoPrescalingFlagged/12513070/ALLSTREAMS.DST")
#data.extend(bk_down2.getDataset()) 
bk_up2 = BKQuery("/MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08h/Digi13/Trig0x409f0045/Reco14c/Stripping20NoPrescalingFlagged/12513070/ALLSTREAMS.DST")
data.extend(bk_up2.getDataset())

myOutputdata =['*.root']

#TupleFile = "Bplus23munu.root"
#extraOptsString = "DaVinci().DDDBtag = 'dddb-20130929-1';""DaVinci().CondDBtag = 'sim-20130522-1-vc-md100';""DaVinci().TupleFile = '"+TupleFile+"';"

myBackend = Dirac()  # for test only!!
mySplitter = SplitByFiles()
mySplitter.filesPerJob = 1

### create and submit job
j = Job (
     name         = myJobName,
      application  = myApplication,
      splitter     = mySplitter,
 #     postprocessors       = myMerger,
      outputfiles   = myOutputdata,
      backend      = myBackend,
      inputdata    = data
#      extraopts = extraOptsString
     )

j.inputfiles = [ LocalFile("/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/signalmc/weights_110614_Lc_pX.xml")]
#j.inpudata=j.inputdata[:1]

print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id


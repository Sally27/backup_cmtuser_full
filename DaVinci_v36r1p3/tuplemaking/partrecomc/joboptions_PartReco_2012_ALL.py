
import sys

print sys.argv


for polarity in ["MagUp", "MagDown"]:
	myJobName = '12'+polarity+'PartReco'
	tuplename = "PartReco_"+polarity+".root"

	myApplication = DaVinci(version="v36r1p3",platform = 'x86_64-slc6-gcc48-opt')
	myApplication.optsfile = ['/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/partrecomc/B23pimu_ALL.py']

	bk_down = BKQuery(path="/MC/2012/Beam4000GeV-2012-"+polarity+"-Nu2.5-Pythia8/Sim08g/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12875540/ALLSTREAMS.DST",dqflag="OK") 
	data=bk_down.getDataset() 
#	bk_down2 = BKQuery(path="/MC/2012/Beam4000GeV-2012-"+polarity+"-Nu2.5-Pythia8/Sim08g/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/12875540/ALLSTREAMS.DST",dqflag="OK")
#	data.extend(bk_down2.getDataset()) 
       
        if polarity == "MagDown":
        	extraOptsString = "DaVinci().DDDBtag  = 'dddb-20130929-1';""DaVinci().CondDBtag = 'sim-20130522-1-vc-md100';""DaVinci().DataType = '2012';""DaVinci().TupleFile = '"+tuplename+"';"

        if polarity == "MagUp":
        	extraOptsString = "DaVinci().DDDBtag  = 'dddb-20130929-1';""DaVinci().CondDBtag = 'sim-20130522-1-vc-mu100';""DaVinci().DataType = '2012';""DaVinci().TupleFile = '"+tuplename+"';"


        if extraOptsString == "":
        	print "No valid option, no job created"


	myOutputdata =['*.root']


	myBackend = Dirac()  # for test only!!


	mySplitter = SplitByFiles()
	mySplitter.filesPerJob = 1

	myMerger = RootMerger()
	myMerger.files = ['BuKMuMuMC2012.root']
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
        j.application.extraopts = extraOptsString
	j.inputfiles =[ LocalFile("/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/partrecomc/weights_110614_Lc_pX.xml")]

	print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id


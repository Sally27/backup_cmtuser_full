
import sys

print sys.argv

for polarity in ["MagUp"]:

	job_name = 'StrippingB2JpsiKstsignal'+polarity+'2016'
	dv = DaVinci(version="v41r2", optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v41r2/tuplemaking/jpsikstdata2016/B2JpsiKst_2016.py' ]) #dv = DaVinci( version = 'v32r2p15', setupProjectOptions = '--nightly lhcb-branches Tue', platform = 'x86_64-slc5-gcc46-opt') #to run nightlies on LSF

	t = JobTemplate(application = dv)

	print "Now reading the data"


	bk_down = BKQuery(path="/LHCb/Collision16/Beam6500GeV-VeloClosed-"+polarity+"/Real Data/Reco16/Stripping26/90000000/LEPTONIC.MDST",dqflag="OK")
	data = bk_down.getDataset()

	mySplitter = SplitByFiles()
	mySplitter.filesPerJob = 10
	mySplitter.maxFiles = -1

	myMerger = RootMerger()
	myMerger.files = ['BuKMuMu.root']
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


	print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id



import sys

print sys.argv

for polarity in ["MagUp", "MagDown"]:

	job_name = 'StrippingB23MuNusignal'+polarity+'2011'

	dv = DaVinci(version="v36r1p3", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/signaldata/B23MuNuSignalData_2011.py' ])

	t = JobTemplate(application = dv)

	print "Now reading the data"

	bk_down = BKQuery(path="/LHCb/Collision11/Beam3500GeV-VeloClosed-"+polarity+"/Real Data/Reco14/Stripping21r1/90000000/SEMILEPTONIC.DST",dqflag="OK")
	data = bk_down.getDataset()

	mySplitter = SplitByFiles()
	mySplitter.filesPerJob = 10
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
	#  postprocessors = myMerger,
			outputfiles = [ '*.root' ],
			splitter = mySplitter
	       )

	j.inputfiles=[LocalFile("/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/signaldata/weights_110614_Lc_pX.xml")]

	print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id


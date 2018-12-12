
import sys

print sys.argv


for polarity in ["MagDown"]:


	job_name = '2012'+polarity+'B2XmumuDATA'

	dv = DaVinci(version="v36r1p3", platform = 'x86_64-slc6-gcc48-opt', optsfile = [ '/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/normalisationdata/BuJpsiK_data_2012_B23Mu.py' ]) #dv = DaVinci( version = 'v32r2p15', setupProjectOptions = '--nightly lhcb-branches Tue', platform = 'x86_64-slc5-gcc46-opt') #to run nightlies on LSF


	t = JobTemplate(application = dv)

	print "Now reading the data"

	bk_down = BKQuery(path="/LHCb/Collision12/Beam4000GeV-VeloClosed-"+polarity+"/Real Data/Reco14/Stripping21/90000000/DIMUON.DST",dqflag="OK")
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

	j.inputfiles = [ LocalFile ("/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/normalisationdata/weights_110614_Lc_pX.xml")]

	print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id

#j.submit()

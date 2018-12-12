
import sys

print sys.argv


for polarity in ["MagDown"]:
    myJobName = '16'+polarity+'B2JpsiKstMC'
    tuplename = "B2JpsiKstMC_2016_"+polarity+".root"
    myApplication = DaVinci(version="v41r2")#,platform = 'x86_64-slc6-gcc48-opt')
    myApplication.optsfile = ['/home/hep/ss4314/cmtuser/DaVinci_v41r2/tuplemaking/jpsikstmc2016/BuJpsiKst_MC_2016.py']
    
    if polarity == "MagDown":

      extraOptsString = "DaVinci().DDDBtag  = 'dddb-20150724';""DaVinci().CondDBtag = 'sim-20161124-2-vc-md100';""DaVinci().DataType = '2016';""DaVinci().TupleFile = '"+tuplename+"';"
    
    if polarity == "MagUp":

      extraOptsString = "DaVinci().DDDBtag  = 'dddb-20150724';""DaVinci().CondDBtag = 'sim-20161124-2-vc-mu100';""DaVinci().DataType = '2016';""DaVinci().TupleFile = '"+tuplename+"';"

     
    if extraOptsString == "":
       print "No valid option, no job created"


    bk_down = BKQuery(path="/MC/2016/Beam6500GeV-2016-"+polarity+"-Nu1.6-25ns-Pythia8/Sim09b/Trig0x6138160F/Reco16/Turbo03/Stripping26NoPrescalingFlagged/11144001/ALLSTREAMS.DST",dqflag="OK") 
    data=bk_down.getDataset() 
    
    myOutputdata =['*.root']
    
    
    ### choose Dirac backend and specify CPU time in seconds
    myBackend = Dirac()  # for test only!!
    
    ### split into subjobs, defining max number of input files & number of input files per subjob
    
    mySplitter = SplitByFiles()
    mySplitter.filesPerJob = 1
    #mySplitter.maxFiles = -1
    #mySplitter.ignoremissing = True
    #mySplitter.bulksubmit = False
    
    
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
    
    #j.inpudata=j.inputdata[:1]
    
    print "Ok, please read the job options for job number %i then submit if it looks ok." % j.id


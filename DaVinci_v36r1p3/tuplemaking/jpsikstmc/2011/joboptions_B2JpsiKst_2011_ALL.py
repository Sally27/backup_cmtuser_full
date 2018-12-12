
import sys

print sys.argv


for polarity in ["MagDown"]:
    myJobName = '11'+polarity+'B2JpsiKstMC'
    tuplename = "B2JpsiKstMC_2011_"+polarity+".root"
    myApplication = DaVinci(version="v36r1p3",platform = 'x86_64-slc6-gcc48-opt')#,platform = 'x86_64-slc6-gcc48-opt')
    myApplication.optsfile = ['/home/hep/ss4314/cmtuser/DaVinci_v36r1p3/tuplemaking/jpsikstmc/2011/BuJpsiKst_MC_2011_ALL.py']
    
    if polarity == "MagDown":

      extraOptsString = "DaVinci().DDDBtag  = 'dddb-20130929';""DaVinci().CondDBtag = 'sim-20130522-vc-md100';""DaVinci().DataType = '2011';""DaVinci().TupleFile = '"+tuplename+"';"
    
    if polarity == "MagUp":

      extraOptsString = "DaVinci().DDDBtag  = 'dddb-20130929';""DaVinci().CondDBtag = 'sim-20130522-vc-mu100';""DaVinci().DataType = '2011';""DaVinci().TupleFile = '"+tuplename+"';"

     
    if extraOptsString == "":
       print "No valid option, no job created"


    bk_down = BKQuery(path="/MC/2011/Beam3500GeV-2011-"+polarity+"-Nu2-Pythia8/Sim08f/Digi13/Trig0x40760037/Reco14a/Stripping20r1NoPrescalingFlagged/11144001/ALLSTREAMS.DST",dqflag="OK") 
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


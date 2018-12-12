# $Id: $
# Test your line(s) of the stripping
#  
# NOTE: Please make a copy of this file for your testing, and do NOT change this one!
#


#use CommonParticlesArchive
from CommonParticlesArchive import CommonParticlesArchiveConf
CommonParticlesArchiveConf().redirect("stripping21r0p1")

from Gaudi.Configuration import *
from Configurables import DaVinci
from StrippingConf.Configuration import StrippingConf


# Tighten Trk Chi2 to <3
from CommonParticles.Utils import DefaultTrackingCuts
DefaultTrackingCuts().Cuts  = { "Chi2Cut" : [ 0, 3 ],
                                "CloneDistCut" : [5000, 9e+99 ] }

#
#Raw event juggler to split Other/RawEvent into Velo/RawEvent and Tracker/RawEvent
#
from Configurables import RawEventJuggler
juggler = RawEventJuggler( DataOnDemand=True, Input=2.0, Output=4.2 )

#
#Fix for TrackEff lines
#
from Configurables import DecodeRawEvent
DecodeRawEvent().setProp("OverrideInputs",4.2)

# Specify the name of your configuration
confname="B23MuNu" #FOR USERS

# NOTE: this will work only if you inserted correctly the 
# default_config dictionary in the code where your LineBuilder 
# is defined.
from StrippingSelections import buildersConf
confs = buildersConf()

from StrippingSelections.Utils import lineBuilder, buildStreamsFromBuilder
#confs[confname]["CONFIG"]["SigmaPPi0CalPrescale"] = 0.5 ## FOR USERS, YOU ONLY NEED TO QUICKLY MODIFY CutName and NewValue (no need to recompile the package but please update the default_config before committing)
streams = buildStreamsFromBuilder(confs,confname)

#clone lines for CommonParticles overhead-free timing
print "Creating line clones for timing"
for s in streams:
    for l in s.lines:
        if "_TIMING" not in l.name():
            cloned = l.clone(l.name().strip("Stripping")+"_TIMING")
            s.appendLines([cloned])

#define stream names
leptonicMicroDSTname   = 'Leptonic'
charmMicroDSTname      = 'Charm'
pidMicroDSTname        = 'PID'
bhadronMicroDSTname    = 'Bhadron'
mdstStreams = [ leptonicMicroDSTname,charmMicroDSTname,pidMicroDSTname,bhadronMicroDSTname ]
dstStreams  = [ "BhadronCompleteEvent", "CharmCompleteEvent", "CharmToBeSwum", "Dimuon",
                "EW", "Semileptonic", "Calibration", "MiniBias", "Radiative" ]

stripTESPrefix = 'Strip'

from Configurables import ProcStatusCheck

from PhysConf.Filters import LoKi_Filters
flts = LoKi_Filters(VOID_Code = "( TrSource(TrSOURCE('/Event/Rec/Track/Best', TrLONG))"\
                                " >> ( sum( TrPT,TrP < 1 * TeV ) > 1 * TeV ) )" ,
                    VOID_Preambulo = ["from LoKiTracks.decorators import *" ,
                                      "from LoKiCore.functions    import * ",
                                      "from GaudiKernel.SystemOfUnits import *"])
filterBadEvents = GaudiSequencer("BadEventFilter",
                                  ModeOR = True,
                                  Members = [ flts.sequencer("GECFilter"),
                                              ProcStatusCheck() ] )
streamFilter = { 'default'  : filterBadEvents,
                 'MiniBias' : ProcStatusCheck() }


sc = StrippingConf( Streams = streams,
                    MaxCandidates = 2000,
                    AcceptBadEvents = False,
                    BadEventSelection = streamFilter,
                    TESPrefix = stripTESPrefix,
                    ActiveMDSTStream = True,
                    Verbose = True,
                    DSTStreams = dstStreams,
                    MicroDSTStreams = mdstStreams )

#
# Configure the dst writers for the output
#
#
# Add stripping TCK
#
#from Configurables import StrippingTCK
#stck = StrippingTCK(HDRLocation = '/Event/Strip/Phys/DecReports', TCK=0x36112100)

from Configurables import DecayTreeTuple, FilterDesktop,CombineParticles,FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB
from DecayTreeTuple.Configuration import *



tuple2 = DecayTreeTuple("B_Tuple2")


#tuple2.Inputs = ["/Event/Semileptonic/Phys/]
tuple2.Inputs = ["Phys/B23MuNu_TriMuLine/Particles"]

tuple2.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats",
      "TupleToolPid"
]


tuple2.addBranches({  # remove all "^" except where needed.
    "Bplus" :  "^([B+ -> mu+ mu- mu+]CC)",
    "mu1" :  "[B+ ->  ^mu+ mu- mu+]CC",
    "mu2" :  "[B+ ->  mu+ ^mu- mu+]CC ",
    "mu3" :  "[B+ ->  mu+ mu- ^mu+]CC ",
    })


tuple2.Decay = "[B+ -> ^mu+ ^mu- ^mu+]CC" #^J/psi(1S)->
#
#Configure DaVinci
#

# Change the column size of Timing table
from Configurables import TimingAuditor, SequencerTimerTool
TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
TimingAuditor().TIMER.NameSize = 60

from Configurables import AuditorSvc, ChronoAuditor
AuditorSvc().Auditors.append( ChronoAuditor("Chrono") )

from Configurables import StrippingReport
sr = StrippingReport(Selections = sc.selections())

from Configurables import AlgorithmCorrelationsAlg
ac = AlgorithmCorrelationsAlg(Algorithms = list(set(sc.selections())))

#from Configurables import GaudiSequencer
#MySequencer = GaudiSequencer('Sequence')



#Configure DaVinci
from Configurables import DaVinci

DaVinci().TupleFile = "DVTuplesnshared.root"
DaVinci().HistogramFile = 'DVHistosnshared.root'
DaVinci().EvtMax = 5000
DaVinci().PrintFreq = 2000
DaVinci().UserAlgorithms = [ tuple2 ]
DaVinci().appendToMainSequence( [ sc.sequence() ] )
DaVinci().appendToMainSequence( [ sr ] )
DaVinci().appendToMainSequence( [ ac ] )
#DaVinci().appendToMainSequence( [ dstWriter.sequence() ] )
#DaVinci().ProductionType = "Stripping"
DaVinci().DataType  = "2012"
DaVinci().InputType = "DST"
DaVinci().Simulation = False

# change the column size of timing table
from Configurables import TimingAuditor, SequencerTimerTool
TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
TimingAuditor().TIMER.NameSize = 60

MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

# database
DaVinci().DDDBtag  = "dddb-20120831"
DaVinci().CondDBtag = "cond-20121008"

# RedoCalo
#importOptions("$STRIPPINGSELECTIONSROOT/tests/users/DV-RedoCaloPID-Stripping21.py")

# input file
importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco14_Run125113.py")

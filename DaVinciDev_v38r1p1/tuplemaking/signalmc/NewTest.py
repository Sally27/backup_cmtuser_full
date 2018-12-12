
from Configurables import DecayTreeTuple, FilterDesktop,CombineParticles,FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB
from Configurables import MCTupleToolKinematic, MCTupleToolHierarchy, TupleToolMCTruth, TupleToolMCBackgroundInfo

from DecayTreeTuple.Configuration import *

#use CommonParticlesArchive
from CommonParticlesArchive import CommonParticlesArchiveConf
CommonParticlesArchiveConf().redirect("stripping26")
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
confs[confname]["CONFIG"]["Muon_PIDmu"] = -999999
confs[confname]["CONFIG"]["Muon_PIDmuK"] = -999999
 ## FOR USERS, YOU ONLY NEED TO QUICKLY MODIFY CutName and NewValue (no need to recompile the package but please update the default_config before committing)
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
enablePacking = True
from DSTWriters.microdstelements import *
from DSTWriters.Configuration import ( SelDSTWriter,
                                       stripDSTStreamConf,
                                       stripDSTElements,
                                       stripMicroDSTStreamConf,
                                       stripMicroDSTElements,
                                       stripCalibMicroDSTStreamConf )
#
# Configuration of MicroDST
# per-event an per-line selective writing of the raw event is active (selectiveRawEvent=True)
#
mdstStreamConf = stripMicroDSTStreamConf(pack=enablePacking, selectiveRawEvent=True)
mdstElements   = stripMicroDSTElements(pack=enablePacking)
#
# Configuration of SelDSTWriter
# per-event an per-line selective writing of the raw event is active (selectiveRawEvent=True)
#
SelDSTWriterElements = {
    'default'               : stripDSTElements(pack=enablePacking),
    charmMicroDSTname       : mdstElements,
    leptonicMicroDSTname    : mdstElements,
    pidMicroDSTname         : mdstElements,
    bhadronMicroDSTname     : mdstElements
    }
SelDSTWriterConf = {
    'default'                : stripDSTStreamConf(pack=enablePacking, selectiveRawEvent=True),
    charmMicroDSTname        : mdstStreamConf,
    leptonicMicroDSTname     : mdstStreamConf,
    bhadronMicroDSTname      : mdstStreamConf,
    pidMicroDSTname          : stripCalibMicroDSTStreamConf(pack=enablePacking, selectiveRawEvent=True)
    }
# Items that might get lost when running the CALO+PROTO ReProcessing in DV
caloProtoReprocessLocs = [ "/Event/pRec/ProtoP#99", "/Event/pRec/Calo#99" ]
# Make sure they are present on full DST streams
SelDSTWriterConf['default'].extraItems += caloProtoReprocessLocs
dstWriter = SelDSTWriter( "MyDSTWriter",
                          StreamConf = SelDSTWriterConf,
                          MicroDSTElements = SelDSTWriterElements,
                          OutputFileSuffix ='000000',
                          SelectionSequences = sc.activeStreams() )
#
# Add stripping TCK
#
#from Configurables import StrippingTCK
#stck = StrippingTCK(HDRLocation = '/Event/Strip/Phys/DecReports', TCK=0x36112100)
#
#Configure DaVinci


tuple = DecayTreeTuple("B23MuNu_Tuple")

#tuple.Inputs = [location]

tuple.Inputs = ['Phys/B23MuNu_TriMuLine/Particles']
#tuple.Inputs = [stripsel.outputLocation()]
tuple.Decay = "[B+ -> ^mu+ ^mu- ^mu+]CC"
#tuple.Inputs = ["Phys/DecayTreeFitterB"]
tuple.ToolList =  [
      "TupleToolKinematic"
    , "TupleToolEventInfo"
    , "TupleToolRecoStats"
    , "TupleToolMCTruth"
    , "TupleToolMCBackgroundInfo"
    , "TupleToolPid"
    , "TupleToolANNPID"
    , "TupleToolL0Data"
]




tuple.addBranches ({
      "mu1" : "[B+ -> ^mu+ mu- mu+]CC",
      "mu2" : "[B+ -> mu+ ^mu- mu+]CC ",
      "mu3" : "[B+ -> mu+ mu- ^mu+]CC",
      "Bplus" : "[B+ -> mu+ mu- mu+]CC ",
})


MCTruth = TupleToolMCTruth()
MCTruth.ToolList =  ["MCTupleToolKinematic","MCTupleToolHierarchy" ]
tuple.addTool(MCTruth)

tuple.Bplus.ToolList += [ "TupleToolTISTOS" ]
tuple.Bplus.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.Bplus.TupleToolTISTOS.Verbose = True
tuple.Bplus.TupleToolTISTOS.TriggerList = [
      "L0DiMuonDecision"
    , "L0MuonDecision"
    , "L0HadronDecision"
    , "Hlt1TrackAllL0Decision"
    , "Hlt1TrackMuonDecision"
    , "Hlt1DiMuonHighMassDecision"
    , "Hlt1SingleMuonHighPTDecision"
    , "Hlt2TopoMu2BodyBBDTDecision"
    , "Hlt2TopoMu3BodyBBDTDecision"
    , "Hlt2Topo2BodyBBDTDecision"
    , "Hlt2Topo3BodyBBDTDecision"
    , "Hlt2DiMuonDetachedJPsiDecision"
    , "Hlt2DiMuonDetachedDecision"
    , "Hlt2SingleMuonDecision"
    , "Hlt2DiMuonDetachedHeavyDecision"
    , "Hlt2Topo2BodyDecision"
    , "Hlt2Topo3BodyDecision"
    , "Hlt2TopoMu2BodyDecision"
    , "Hlt2TopoMu3BodyDecision"
]


LoKi_All=tuple.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_All")
LoKi_All.Variables = {
        'MINIPCHI2' : "MIPCHI2DV(PRIMARY)",
        'MINIP' : "MIPDV(PRIMARY)",
        'ETA' : 'ETA',
        'PHI' : 'PHI'

}


LoKi_Bplus=tuple.Bplus.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Bplus")
LoKi_Bplus.Variables = {
       'TAU' : "BPVLTIME()",
       'DIRA_OWNPV' : "BPVDIRA",
       'FD_CHI2' : "BPVVDCHI2",
       'ENDVERTEX_CHI2' : "VFASPF(VCHI2/VDOF)",
       'X_travelled' : "VFASPF(VX)-BPV(VX)",
       'Y_travelled' : "VFASPF(VY)-BPV(VY)",
       'Z_travelled' : "VFASPF(VZ)-BPV(VZ)",
       'P_Parallel' : "BPVDIRA*P",
       'P_Perp' : "sin(acos(BPVDIRA))*P",
       'BPVVDZ' : "BPVVDZ",
       'Corrected_Mass' : "BPVCORRM"
}


LoKi_mu1=tuple.mu1.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu1")
LoKi_mu1.Variables = {
       'PIDmuLoki' : "PIDmu",
       'PIDKLoki' : "PIDK",
       'PIDpLoki' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuonLoki' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

LoKi_mu2=tuple.mu2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu2")
LoKi_mu2.Variables = {
       'PIDmuLoki' : "PIDmu",
       'PIDKLoki' : "PIDK",
       'PIDpLoki' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuonLoki' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"

}

LoKi_mu3=tuple.mu3.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu3")
LoKi_mu3.Variables = {
       'PIDmuLoki' : "PIDmu",
       'PIDKLoki' : "PIDK",
       'PIDpLoki' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuonLoki' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"

}

#tuple.Decay = "Bplus -> ^(J/psi(1S) -> ^mu+ ^mu-) ^gamma"
#tuple.Decay = "J/psi(1S) -> ^mu+ ^mu-"
from Configurables import DaVinci



from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexppMuMu
tuple.Bplus.addTool(TupleToolVertexppMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexppMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexpmMuMu
tuple.Bplus.addTool(TupleToolVertexpmMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexpmMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexmpMuMu
tuple.Bplus.addTool(TupleToolVertexmpMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexmpMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexMuMuMu
tuple.Bplus.addTool(TupleToolVertexMuMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexMuMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolSallyvs3
tuple.Bplus.addTool(TupleToolSallyvs3)
tuple.Bplus.ToolList+=["TupleToolSallyvs3"]


from DecayTreeTuple.Configuration import *
from Configurables import TupleToolApplypMuIsolation
tuple.Bplus.addTool(TupleToolApplypMuIsolation)
tuple.Bplus.TupleToolApplypMuIsolation.OutputSuffix="_weights"
tuple.Bplus.TupleToolApplypMuIsolation.WeightsFile="weights_110614_Lc_pX.xml"
tuple.Bplus.ToolList+=["TupleToolApplypMuIsolation"]

#Mysterious things to make isolation work

name="TupleToolApplypMuIsolation"
from Configurables import ChargedProtoParticleMaker
#
veloprotos = ChargedProtoParticleMaker(name+"ProtoPMaker")
veloprotos.Inputs = ["Rec/Track/Best"]
veloprotos.Output = "Rec/ProtoP/myProtoPMaker/ProtoParticles"
#
DaVinci().appendToMainSequence( [ veloprotos ])
#
from Gaudi.Configuration import *
from Configurables       import ProtoParticleCALOFilter, CombinedParticleMaker,NoPIDsParticleMaker
from CommonParticles.Utils import *
#
algorithm = NoPIDsParticleMaker('StdNoPIDsVeloPions',  Particle = 'pion',  )
algorithm.Input = "Rec/ProtoP/myProtoPMaker/ProtoParticles"
selector = trackSelector ( algorithm , trackTypes = ['Velo'] )
#
from Configurables import DaVinci
locations = updateDoD ( algorithm )
DaVinci().appendToMainSequence( [ algorithm ])

#
from Configurables import GaudiSequencer
MySequencer = GaudiSequencer('Sequence')


from Configurables import DaVinci
DaVinci().TupleFile = "Bplus23munu.root"
#DaVinci().EventPreFilters = fltrs.filters ('Filters')
DaVinci().EvtMax = 200
DaVinci().PrintFreq = 100
#DaVinci().EvtMax = -1
DaVinci().DataType = '2016'

DaVinci().Simulation   = True
DaVinci().Lumi = False
DaVinci().DDDBtag  = "dddb-20150724"
DaVinci().CondDBtag = "sim-20160606-vc-md100"


_myseq = GaudiSequencer("myseq")
#_myseq.Members += [ DecayTreeFitterB]
#_myseq.Members += [ eventNodeKiller ]
#_myseq.Members += [ TrackSmearingSeq ]  
_myseq.Members += [ sc.sequence() ] 
#_myseq.Members += [ seq.sequence() ] 
#_myseq.Members += [ dstWriter.sequence() ]
_myseq.Members += [tuple]

DaVinci().UserAlgorithms = [_myseq]

DaVinci().MainOptions  = ""

#from Configurables import CondDB
#CondDB().UseLatestTags =["2012"]
#DaVinci().appendToMainSequence( [sc.sequence()]
#DaVinci().appendToMainSequence( [ tuple ] )
#DaVinci().appendToMainSequence( [ seq.sequence(),tuple])
#DaVinci().MainOptions  = ""

from GaudiConf import IOHelper

IOHelper().inputFiles(['./00056361_00000020_3.AllStreams.dst'], clear=True)



## Change the column size of Timing table
#from Configurables import TimingAuditor, SequencerTimerTool
#TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
#TimingAuditor().TIMER.NameSize = 60
#from Configurables import AuditorSvc, ChronoAuditor
#AuditorSvc().Auditors.append( ChronoAuditor("Chrono") )
#from Configurables import StrippingReport
#sr = StrippingReport(Selections = sc.selections())
#from Configurables import AlgorithmCorrelationsAlg
#ac = AlgorithmCorrelationsAlg(Algorithms = list(set(sc.selections())))
##Configure DaVinci
#
#
#
#
#
#
#DaVinci().HistogramFile = 'DV_stripping_histos.root'
#DaVinci().EvtMax = 10000
#DaVinci().PrintFreq = 2000
#DaVinci().appendToMainSequence( [ sc.sequence() ] )
#DaVinci().appendToMainSequence( [ sr ] )
#DaVinci().appendToMainSequence( [ ac ] )
#DaVinci().appendToMainSequence( [ dstWriter.sequence() ] )
#DaVinci().ProductionType = "Stripping"
#DaVinci().DataType  = "2012"
#DaVinci().InputType = "DST"
## change the column size of timing table
#from Configurables import TimingAuditor, SequencerTimerTool
#TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
#TimingAuditor().TIMER.NameSize = 60
#MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"
## database
#DaVinci().DDDBtag  = "dddb-20120831"
#DaVinci().CondDBtag = "cond-20121008"
## RedoCalo
#importOptions("$STRIPPINGSELECTIONSROOT/tests/users/DV-RedoCaloPID-Stripping21.py")
## input file
#importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco14_Run125113.py")

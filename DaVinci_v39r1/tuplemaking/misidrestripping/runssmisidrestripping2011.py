# $Id: $
# Test your line(s) of the stripping
#  
# NOTE: Please make a copy of this file for your testing, and do NOT change this one!
#


##use CommonParticlesArchive
#from CommonParticlesArchive import CommonParticlesArchiveConf
#CommonParticlesArchiveConf().redirect("stripping21r1p1a")
#
#from Gaudi.Configuration import *
#from Configurables import DaVinci
#from StrippingConf.Configuration import StrippingConf
#
#
## Tighten Trk Chi2 to <3
#from CommonParticles.Utils import DefaultTrackingCuts
#DefaultTrackingCuts().Cuts  = { "Chi2Cut" : [ 0, 3 ],
#                                "CloneDistCut" : [5000, 9e+99 ] }
#
##
##Raw event juggler to split Other/RawEvent into Velo/RawEvent and Tracker/RawEvent
##
#from Configurables import RawEventJuggler
#juggler = RawEventJuggler( DataOnDemand=True, Input=2.0, Output=4.2 )
#
##
##Fix for TrackEff lines
##
#from Configurables import DecodeRawEvent
#DecodeRawEvent().setProp("OverrideInputs",4.2)
#
## Specify the name of your configuration
#confname="B23MuNu" #FOR USERS
#
## NOTE: this will work only if you inserted correctly the 
## default_config dictionary in the code where your LineBuilder 
## is defined.
#from StrippingSelections import buildersConf
#confs = buildersConf()
#
#from StrippingSelections.Utils import lineBuilder, buildStreamsFromBuilder
##confs[confname]["CONFIG"]["SigmaPPi0CalPrescale"] = 0.5 ## FOR USERS, YOU ONLY NEED TO QUICKLY MODIFY CutName and NewValue (no need to recompile the package but please update the default_config before committing)
#streams = buildStreamsFromBuilder(confs,confname)
#
##clone lines for CommonParticles overhead-free timing
#print "Creating line clones for timing"
#for s in streams:
#    for l in s.lines:
#        if "_TIMING" not in l.name():
#            cloned = l.clone(l.name().strip("Stripping")+"_TIMING")
#            s.appendLines([cloned])
#
##define stream names
#leptonicMicroDSTname   = 'Leptonic'
#charmMicroDSTname      = 'Charm'
#pidMicroDSTname        = 'PID'
#bhadronMicroDSTname    = 'Bhadron'
#mdstStreams = [ leptonicMicroDSTname,charmMicroDSTname,pidMicroDSTname,bhadronMicroDSTname ]
#dstStreams  = [ "BhadronCompleteEvent", "CharmCompleteEvent", "CharmToBeSwum", "Dimuon",
#                "EW", "Semileptonic", "Calibration", "MiniBias", "Radiative" ]
#
#stripTESPrefix = 'Strip'
#
#from Configurables import ProcStatusCheck
#
#from PhysConf.Filters import LoKi_Filters
#flts = LoKi_Filters(VOID_Code = "( TrSource(TrSOURCE('/Event/Rec/Track/Best', TrLONG))"\
#                                " >> ( sum( TrPT,TrP < 1 * TeV ) > 1 * TeV ) )" ,
#                    VOID_Preambulo = ["from LoKiTracks.decorators import *" ,
#                                      "from LoKiCore.functions    import * ",
#                                      "from GaudiKernel.SystemOfUnits import *"])
#filterBadEvents = GaudiSequencer("BadEventFilter",
#                                  ModeOR = True,
#                                  Members = [ flts.sequencer("GECFilter"),
#                                              ProcStatusCheck() ] )
#streamFilter = { 'default'  : filterBadEvents,
#                 'MiniBias' : ProcStatusCheck() }
#
#
#sc = StrippingConf( Streams = streams,
#                    MaxCandidates = 2000,
#                    AcceptBadEvents = False,
#                    BadEventSelection = streamFilter,
#                    TESPrefix = stripTESPrefix,
#                    ActiveMDSTStream = True,
#                    Verbose = True,
#                    DSTStreams = dstStreams,
#                    MicroDSTStreams = mdstStreams )
#



from Configurables import DecayTreeTuple, FilterDesktop,CombineParticles,FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB
from DecayTreeTuple.Configuration import *

#ADDED for BDT reason
#from Configurables import LoKi__Hybrid__TupleTool
#from Configurables import LoKi__Hybrid__Tool as MyFactory
#mf = MyFactory("HybridFactory")
#mf.Modules.append( 'LoKiPhysMC.decorators' )


tuple = DecayTreeTuple("B_Tuple")

#tuple.Inputs = [location]
tuple.Inputs = ["/Event/Semileptonic/Phys/B23MuNu_TriFakeMuLine/Particles"]
#tuple.Inputs = ["Phys/DecayTreeFitterB"]
tuple.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats",
 
      "TupleToolANNPID"
]
 
 
tuple.addBranches({  # remove all "^" except where needed.
    "Jpsi" :  "^(J/psi(1S) -> mu+ mu-)",
    "mu1" :  " J/psi(1S) -> ^mu+ mu-",
    "mu2" :  " J/psi(1S) -> mu+ ^mu-"
    })

tuple.Jpsi.ToolList += [ "TupleToolTISTOS" ]
tuple.Jpsi.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.Jpsi.TupleToolTISTOS.Verbose = True
tuple.Jpsi.TupleToolTISTOS.TriggerList = [
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
]


LoKi_All1=tuple.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_All")
LoKi_All1.Variables = {
        'MINIPCHI2' : "MIPCHI2DV(PRIMARY)",
        'MINIP' : "MIPDV(PRIMARY)",
        'ETA' : 'ETA',
        'PHI' : 'PHI'
}


LoKi_Jpsi1=tuple.Jpsi.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Bplus")
LoKi_Jpsi1.Variables = {
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


LoKi_mu11=tuple.mu1.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu1")
LoKi_mu11.Variables = {
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

LoKi_mu22=tuple.mu2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu2")
LoKi_mu22.Variables = {
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




tuple.Decay = "J/psi(1S) -> ^mu+ ^mu-" 

tuple2 = DecayTreeTuple("B_Tuple2")


tuple2.Inputs = ["/Event/Semileptonic/Phys/B23MuNu_TriFakeMuLine/Particles"]

tuple2.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats",
      "TupleToolPid",
      "TupleToolANNPID"
]


tuple2.addBranches({  # remove all "^" except where needed.
    "Bplus" :  "^([B+ -> (J/psi(1S) -> mu+ mu-) mu+]CC)",
    "mu1" :  "[B+ -> (J/psi(1S) -> ^mu+ mu-) mu+]CC",
    "mu2" :  "[B+ -> (J/psi(1S) -> mu+ ^mu-) mu+]CC ",
    "mu3" :  "[B+ -> (J/psi(1S) -> mu+ mu-) ^mu+]CC ",
    })


tuple2.Bplus.ToolList += [ "TupleToolTISTOS" ]
tuple2.Bplus.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple2.Bplus.TupleToolTISTOS.Verbose = True
tuple2.Bplus.TupleToolTISTOS.TriggerList = [
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
]


LoKi_All=tuple2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_All")
LoKi_All.Variables = {
        'MINIPCHI2' : "MIPCHI2DV(PRIMARY)",
        'MINIP' : "MIPDV(PRIMARY)",
        'ETA' : 'ETA',
        'PHI' : 'PHI'
}


LoKi_Bplus=tuple2.Bplus.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Bplus")
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


LoKi_mu1=tuple2.mu1.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu1")
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

LoKi_mu2=tuple2.mu2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu2")
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

LoKi_mu3=tuple2.mu3.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu3")
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

tuple2.Decay = "[B+ -> ^(J/psi(1S) -> ^mu+ ^mu-) ^mu+]CC" #^J/psi(1S)->

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexMisppMuMu
tuple2.Bplus.addTool(TupleToolVertexMisppMuMu)
tuple2.Bplus.ToolList+=["TupleToolVertexMisppMuMu"]


from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexMispmMuMu
tuple2.Bplus.addTool(TupleToolVertexMispmMuMu)
tuple2.Bplus.ToolList+=["TupleToolVertexMispmMuMu"]


from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexMismpMuMu
tuple2.Bplus.addTool(TupleToolVertexMismpMuMu)
tuple2.Bplus.ToolList+=["TupleToolVertexMismpMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexMisMuMuMu
tuple2.Bplus.addTool(TupleToolVertexMisMuMuMu)
tuple2.Bplus.ToolList+=["TupleToolVertexMisMuMuMu"]


from DecayTreeTuple.Configuration import *
from Configurables import TupleToolSallyvs3
tuple2.Bplus.addTool(TupleToolSallyvs3)
tuple2.Bplus.ToolList+=["TupleToolSallyvs3"]


#tuple2.Decay = "[B+ -> ^(J/psi(1S) -> ^mu+ ^mu-) ^mu+]CC" #^J/psi(1S)->
from DecayTreeTuple.Configuration import *
from Configurables import TupleToolApplypMuIsolation
tuple2.Bplus.addTool(TupleToolApplypMuIsolation)
tuple2.Bplus.TupleToolApplypMuIsolation.OutputSuffix="_weights"
tuple2.Bplus.TupleToolApplypMuIsolation.WeightsFile="weights_110614_Lc_pX.xml"
tuple2.Bplus.ToolList+=["TupleToolApplypMuIsolation"]

#Mysterious things to make isolation work

name="TupleToolApplypMuIsolation"
from Configurables import ChargedProtoParticleMaker

veloprotos = ChargedProtoParticleMaker(name+"ProtoPMaker")
veloprotos.Inputs = ["Rec/Track/Best"]
veloprotos.Output = "Rec/ProtoP/myProtoPMaker/ProtoParticles"

from Configurables import DaVinci

DaVinci().appendToMainSequence( [ veloprotos ])

from Gaudi.Configuration import *
from Configurables       import ProtoParticleCALOFilter, CombinedParticleMaker,NoPIDsParticleMaker
from CommonParticles.Utils import *

algorithm = NoPIDsParticleMaker('StdNoPIDsVeloPions',  Particle = 'pion',  )
algorithm.Input = "Rec/ProtoP/myProtoPMaker/ProtoParticles"
selector = trackSelector ( algorithm , trackTypes = ['Velo'] )

locations = updateDoD ( algorithm )
DaVinci().appendToMainSequence( [ algorithm ])


from Configurables import TimingAuditor, SequencerTimerTool
TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
TimingAuditor().TIMER.NameSize = 60

from Configurables import AuditorSvc, ChronoAuditor
AuditorSvc().Auditors.append( ChronoAuditor("Chrono") )

#from Configurables import StrippingReport
#sr = StrippingReport(Selections = sc.selections())

#from Configurables import AlgorithmCorrelationsAlg
#ac = AlgorithmCorrelationsAlg(Algorithms = list(set(sc.selections())))



#DaVinci().HistogramFile = 'DV_stripping_histosnew2.root'
DaVinci().TupleFile = "B23MuNuFakeSS.root"
#DaVinci().HistogramFile = 'DVHistosnshared.root'
#DaVinci().TupleFile = "DVTuplesnshared.root"
#DaVinci().EvtMax = 10000
DaVinci().PrintFreq = 2000
#DaVinci().UserAlgorithms = [ tuple ]
#DaVinci().appendToMainSequence( [ tuple ] )
DaVinci().appendToMainSequence( [ tuple2 ] )


#DaVinci().appendToMainSequence( [ tuple2 ] )
#DaVinci().appendToMainSequence( [ sc.sequence() ] )
#DaVinci().appendToMainSequence( [ tuple] )
#DaVinci().appendToMainSequence( [ tuple2] )
#DaVinci().appendToMainSequence( [ sr ] )
#DaVinci().appendToMainSequence( [ ac ] )
#DaVinci().appendToMainSequence( [ tuple] )
#DaVinci().appendToMainSequence( [ tuple2] )
DaVinci().DataType  = "2011"
DaVinci().InputType = "DST"
DaVinci().Lumi = True
DaVinci().Simulation = False


# change the column size of timing table
from Configurables import TimingAuditor, SequencerTimerTool
TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
TimingAuditor().TIMER.NameSize = 60
#NTupleSvc().Output = ["FILE1 DATAFILE='trythis.root' TYP='ROOT' OPT='NEW'"]
MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

#from GaudiConf import IOHelper

#IOHelper().inputFiles(['./00050733_00021988_1.semileptonic.dst'], clear=True)
# database
#DaVinci().DDDBtag  = "dddb-20120831"
#DaVinci().CondDBtag = "cond-20121008"
#DaVinci().Lumi = True
# input file
#importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco15a_Run164668.py")

#importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco14_Run125113.py")

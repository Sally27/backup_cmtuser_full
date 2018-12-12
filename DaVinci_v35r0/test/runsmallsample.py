# $Id: $
# Test your line(s) of the stripping
#  
# NOTE: Please make a copy of this file for your testing, and do NOT change this one!
#

from Gaudi.Configuration import *
from Configurables import DaVinci
from StrippingConf.Configuration import StrippingConf

# Tighten Trk Chi2 to <3
from CommonParticles.Utils import DefaultTrackingCuts
DefaultTrackingCuts().Cuts  = { "Chi2Cut" : [ 0, 3 ],
                                "CloneDistCut" : [5000, 9e+99 ] }

# Now build the stream
from StrippingConf.StrippingStream import StrippingStream
stream = StrippingStream("Test")

# Append your line.
# NOTE: this will work only if you inserted correctly the 
# default_config dictionary in the code where your LineBuilder 
# is defined. StrippingDiMuonNew.py is a good example to follow
#from StrippingSelections import buildersConf
#confs = buildersConf()
#from StrippingSelections.Utils import lineBuilder
#builder = lineBuilder(confs,'FullDSTDiMuon')
#stream.appendLines( builder.lines() )

#my attempt
#from StrippingSelections.Utils import lineBuilder
#from StrippingSelections import buildersConf


from StrippingSelections.play import B23MuNuConf
from StrippingSelections.play import defaultConfig
#from testsally import B23MuNuConf
#from testsally import defaultConfig



builder = B23MuNuConf(name="B23MuNu",config = defaultConfig)#name="B23MuNu"
stream.appendLines(builder.lines())


# Standard configuration of Stripping, do NOT change them
from Configurables import  ProcStatusCheck
filterBadEvents =  ProcStatusCheck()

from StrippingConf.Configuration import StrippingConf

sc = StrippingConf( Streams = [ stream ],
                    MaxCandidates = 2000,
                    AcceptBadEvents = False,
                    BadEventSelection = filterBadEvents,
                    TESPrefix = 'Strip'
                    )

from Configurables import AuditorSvc, ChronoAuditor
AuditorSvc().Auditors.append( ChronoAuditor("Chrono") )

from Configurables import StrippingReport
sr = StrippingReport(Selections = sc.selections())

from Configurables import AlgorithmCorrelationsAlg
ac = AlgorithmCorrelationsAlg(Algorithms = sc.selections())


# DecayTreeTuple constructor 
#from Configurables import DecayTreeTuple
#from DecayTreeTuple.Configuration import *

#from Configurables import DecayTreeTuple, FitDecayTrees, TupleToolRecoStats, CondDB

from Configurables import DecayTreeTuple, FilterDesktop,CombineParticles,FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB
from DecayTreeTuple.Configuration import *

#ADDED for BDT reason
#from Configurables import LoKi__Hybrid__TupleTool
#from Configurables import LoKi__Hybrid__Tool as MyFactory
#mf = MyFactory("HybridFactory")
#mf.Modules.append( 'LoKiPhysMC.decorators' )


tuple = DecayTreeTuple("B_Tuple_SS")
tuple.Inputs = ["Phys/B23MuNu_JpsiLine/Particles"]
tuple.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats"
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
        'ID' : 'ID'
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
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)", 
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

LoKi_mu22=tuple.mu2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu2")
LoKi_mu22.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}




tuple.Decay = "J/psi(1S) -> ^mu+ ^mu-" 


tupleos = DecayTreeTuple("B_Tuple_OS")
tupleos.Inputs = ["Phys/B23MuNu_JpsiLine/Particles"]
tupleos.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats"
]
 
 
tupleos.addBranches({  # remove all "^" except where needed.
    "Jpsi" :  "^([J/psi(1S) -> mu+ mu+]CC)",
    "mu1" :  "[J/psi(1S) -> ^mu+ mu+]CC",
    "mu2" :  "[J/psi(1S) -> mu+ ^mu+]CC"
    })

tupleos.Jpsi.ToolList += [ "TupleToolTISTOS" ]
tupleos.Jpsi.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tupleos.Jpsi.TupleToolTISTOS.Verbose = True
tupleos.Jpsi.TupleToolTISTOS.TriggerList = [
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


LoKi_All1os=tupleos.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_All")
LoKi_All1os.Variables = {
        'MINIPCHI2' : "MIPCHI2DV(PRIMARY)",
        'MINIP' : "MIPDV(PRIMARY)",
        'ETA' : 'ETA',
        'ID' : 'ID'
}


LoKi_Jpsi1os=tupleos.Jpsi.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Bplus")
LoKi_Jpsi1os.Variables = {
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


LoKi_mu11os=tupleos.mu1.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu1")
LoKi_mu11os.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)", 
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

LoKi_mu22os=tupleos.mu2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu2")
LoKi_mu22os.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}


tupleos.Decay = "[J/psi(1S) -> ^mu+ ^mu+]CC" 




tuple2 = DecayTreeTuple("B_Tuple2_OS")


tuple2.Inputs = ["Phys/B23MuNu_TriMuLine/Particles"]

tuple2.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats"
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
        'ID' : 'ID'
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
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

LoKi_mu2=tuple2.mu2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu2")
LoKi_mu2.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

LoKi_mu3=tuple2.mu3.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu3")
LoKi_mu3.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

tuple2.Decay = "[B+ -> ^(J/psi(1S) -> ^mu+ ^mu-) ^mu+]CC" #^J/psi(1S)->


tuple2ss2 = DecayTreeTuple("B_Tuple2_SS")


tuple2ss2.Inputs = ["Phys/B23MuNu_TriMuLine/Particles"]

tuple2ss2.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats"
]


tuple2ss2.addBranches({  # remove all "^" except where needed.
    "Bplus" :  "^([B+ -> (J/psi(1S) -> mu+ mu+) mu-]CC)",
    "mu1" :  "[B+ -> (J/psi(1S) -> ^mu+ mu+) mu-]CC",
    "mu2" :  "[B+ -> (J/psi(1S) -> mu+ ^mu+) mu-]CC ",
    "mu3" :  "[B+ -> (J/psi(1S) -> mu+ mu+) ^mu-]CC ",
    })


tuple2ss2.Bplus.ToolList += [ "TupleToolTISTOS" ]
tuple2ss2.Bplus.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple2ss2.Bplus.TupleToolTISTOS.Verbose = True
tuple2ss2.Bplus.TupleToolTISTOS.TriggerList = [
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


LoKi_Allss2=tuple2ss2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_All")
LoKi_Allss2.Variables = {
        'MINIPCHI2' : "MIPCHI2DV(PRIMARY)",
        'MINIP' : "MIPDV(PRIMARY)",
        'ETA' : 'ETA',
        'ID' : 'ID'
}


LoKi_Bplusss2=tuple2ss2.Bplus.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Bplus")
LoKi_Bplusss2.Variables = {
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


LoKi_mu1ss2=tuple2ss2.mu1.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu1")
LoKi_mu1ss2.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

LoKi_mu2ss2=tuple2ss2.mu2.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu2")
LoKi_mu2ss2.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

LoKi_mu3ss2=tuple2ss2.mu3.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu3")
LoKi_mu3ss2.Variables = {
       'PIDmu' : "PIDmu",
       'PIDK' : "PIDK",
       'PIDp' : "PIDp",
       'ghost' : "TRGHP",
       'TRACK_CHI2' : "TRCHI2DOF",
       'NNK' : "PPINFO(PROBNNK)",
       'NNpi' : "PPINFO(PROBNNpi)",
       'NNmu' : "PPINFO(PROBNNmu)",
       'isMuonLoose' : "switch(ISMUONLOOSE,1,0)",
       'isMuon' : "switch(ISMUON,1,0)",
       'inMuon' : "switch(INMUON,1,0)",
       'nShared' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
}

tuple2ss2.Decay = "[B+ -> ^(J/psi(1S) -> ^mu+ ^mu+) ^mu-]CC" #^J/psi(1S)->








from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexMisIDmu
tuple2.mu1.addTool(TupleToolVertexMisIDmu)
tuple2.mu1.ToolList+=["TupleToolVertexMisIDmu"]


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

DaVinci().appendToMainSequence( [ veloprotos ])

from Gaudi.Configuration import *
from Configurables       import ProtoParticleCALOFilter, CombinedParticleMaker,NoPIDsParticleMaker
from CommonParticles.Utils import *

algorithm = NoPIDsParticleMaker('StdNoPIDsVeloPions',  Particle = 'pion',  )
algorithm.Input = "Rec/ProtoP/myProtoPMaker/ProtoParticles"
selector = trackSelector ( algorithm , trackTypes = ['Velo'] )

locations = updateDoD ( algorithm )
DaVinci().appendToMainSequence( [ algorithm ])


#DaVinci().HistogramFile = 'DV_stripping_histosnew2.root'
DaVinci().HistogramFile = 'DVHistosnshared.root'
DaVinci().TupleFile = "DVTuplesnshared.root"
DaVinci().EvtMax = 1000
DaVinci().PrintFreq = 2000

DaVinci().appendToMainSequence( [ sc.sequence() ] )
#DaVinci().appendToMainSequence( [ tuple] )
#DaVinci().appendToMainSequence( [ tuple2] )
DaVinci().appendToMainSequence( [ sr ] )
DaVinci().appendToMainSequence( [ ac ] )
DaVinci().appendToMainSequence( [ tuple] )
DaVinci().appendToMainSequence( [ tupleos] )
DaVinci().appendToMainSequence( [ tuple2] )
DaVinci().appendToMainSequence( [ tuple2ss2] )
DaVinci().DataType  = "2012"
DaVinci().InputType = "DST"



# change the column size of timing table
from Configurables import TimingAuditor, SequencerTimerTool
TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
TimingAuditor().TIMER.NameSize = 60
#NTupleSvc().Output = ["FILE1 DATAFILE='trythis.root' TYP='ROOT' OPT='NEW'"]
MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

# database
DaVinci().DDDBtag  = "dddb-20120831"
DaVinci().CondDBtag = "cond-20121008"
DaVinci().Lumi = True
# input file
#importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco14_Run125113.py")

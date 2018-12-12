
from Gaudi.Configuration import *
#from Configurables import DaVinci
from StrippingConf.Configuration import StrippingConf

#from Gaudi.Configuration import *
from PhysSelPython.Wrappers import Selection, SelectionSequence, DataOnDemand, AutomaticData

# Tighten Trk Chi2 to <3
from CommonParticles.Utils import DefaultTrackingCuts
DefaultTrackingCuts().Cuts  = { "Chi2Cut" : [ 0, 3 ],
                                "CloneDistCut" : [5000, 9e+99 ] }

from Configurables import DecayTreeTuple, FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB, SelDSTWriter
from DecayTreeTuple.Configuration import *
# Now build the stream

from StrippingConf.StrippingStream import StrippingStream
stream = StrippingStream("Test")

# Append your line


from StrippingArchive.Stripping20.StrippingB2XMuMu import B2XMuMuConf as builder
from StrippingArchive.Stripping20.StrippingB2XMuMu import defaultConfig as config
from StrippingConf.Configuration import StrippingConf, StrippingStream
#from StrippingSettings.Utils import strippingConfiguration
#from StrippingArchive.Utils import buildStreams, cloneLinesFromStream
#from StrippingArchive import strippingArchive
#config['MuonPID'] = -999999

stripping='stripping20'
#get the configuration dictionary from the database
#config  = strippingConfiguration(stripping)
#config['HLT_FILTER_HMuNu']=""
lb = builder('B2XMuMu',config)
print config
#get the line builders from the archive


#
# Merge into one stream and run in flag mode
#
AllStreams = StrippingStream("Dimuon")

for line in lb.lines():
    if line.name() == 'StrippingB2XMuMu_Line':
        AllStreams.appendLines([line])


sc = StrippingConf( Streams = [ AllStreams ],
                    MaxCandidates = 2000,
                    AcceptBadEvents = False,
                    TESPrefix = 'Strip'
                    )



stripsel = AutomaticData(Location = "/Event/Dimuon/Phys/B2XMuMu_Line/Particles")

name="B2XMuMu"
#_stripfilter = FilterDesktop("stripfilter",
#  		      Preambulo = ["from LoKiPhysMC.decorators import *","from LoKiPhysMC.functions import mcMatch"],
#                      Code = "ALL")

#Bu_Kmumu = Selection ("Sel"+name,
#                     RequiredSelections = [stripsel])
#seq = SelectionSequence("seq",
#                      TopSelection = Bu_Kmumu)
from Configurables import TupleToolDecayTreeFitter

dtf2 = TupleToolDecayTreeFitter("DTFM", Verbose=True,

                                daughtersToConstrain=['J/psi(1S)'],

                                constrainToOriginVertex=True)



tuple = DecayTreeTuple("B2JpsiKst_Tuple")

tuple.Inputs = [stripsel.outputLocation()]

#from Gaudi.Configuration import *
#from PhysSelPython.Wrappers import Selection, SelectionSequence, DataOnDemand
#
#
#
#from Configurables import DecayTreeTuple, FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB
#from DecayTreeTuple.Configuration import *
#
#
#
#
#tuple = DecayTreeTuple("B2JpsiK_Tuple")
#
#tuple.Inputs = ["/Event/Dimuon/Phys/B2XMuMu_Line/Particles"]
#
tuple.ToolList =  [
      "TupleToolKinematic"
    , "TupleToolEventInfo"
    , "TupleToolRecoStats"
    , "TupleToolPid"
    , "TupleToolANNPID"

]


tuple.addBranches ({
      "Pi" :  "[B0 -> (J/psi(1S) -> mu+ mu-) (K*(892)0 -> K+ ^pi-)]CC",
      "K" :  "[B0 -> (J/psi(1S) -> mu+ mu-) (K*(892)0 -> ^K+ pi-)]CC", 
      "Kst" :  "[B0 -> (J/psi(1S) -> mu+ mu-) ^(K*(892)0 -> K+ pi-)]CC",
      "Jpsi" :  "[B0 -> ^(J/psi(1S) -> mu+ mu-) (K*(892)0 -> K+ pi-)]CC",
      "mu1" :  "[B0 -> (J/psi(1S) -> ^mu+ mu-) (K*(892)0 -> K+ pi-)]CC",
      "mu2" :  "[B0 -> (J/psi(1S) -> mu+ ^mu-) (K*(892)0 -> K+ pi-)]CC",
      "B0" : "^([B0 -> J/psi(1S) K*(892)0]CC)",
})



LoKi_All=tuple.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_All")
LoKi_All.Variables = {
        'MINIPCHI2' : "MIPCHI2DV(PRIMARY)", 
        'MINIP' : "MIPDV(PRIMARY)",
        'IPCHI2_OWNPV' : "BPVIPCHI2()", 
        'IP_OWNPV' : "BPVIP()",
        'ETA' : 'ETA',
        'PHI' : 'PHI'

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

LoKi_K=tuple.K.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_K")
LoKi_K.Variables = {
#from Sally
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


LoKi_Pi=tuple.Pi.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Pi")
LoKi_Pi.Variables = {
#from Sally
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



LoKi_B0=tuple.B0.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_B0")
LoKi_B0.Preambulo += [
  "muE = CHILD(E, '[B+ -> (J/psi(1S) -> mu+ ^mu-)  K+]CC' )",
  "muP = CHILD(P, '[B+ -> (J/psi(1S) -> mu+ ^mu-)  K+]CC' )",
  "muE_aspi = sqrt(muP*muP + 139*139)",
  "muPX = CHILD(PX, '[B+ -> (J/psi(1S) -> mu+ ^mu-)  K+]CC' )",
  "muPY = CHILD(PY, '[B+ -> (J/psi(1S) -> mu+ ^mu-)  K+]CC' )",
  "muPZ = CHILD(PZ, '[B+ -> (J/psi(1S) -> mu+ ^mu-)  K+]CC' )",
  "KP = CHILD(P, '[B+ -> J/psi(1S) ^K+]CC' )",
  "KE_asmu = sqrt(KP*KP + 105*105)",
  "KE = sqrt(KP*KP + 497*497)",
  "KPX = CHILD(PX, '[B+ -> J/psi(1S) ^K+]CC' )",
  "KPY = CHILD(PY, '[B+ -> J/psi(1S) ^K+]CC' )",
  "KPZ = CHILD(PZ, '[B+ -> J/psi(1S) ^K+]CC' )",
  "kmuE = muE + KE_asmu",
  "DE = muE_aspi + KE",
  "PX = muPX + KPX",
  "PY = muPY + KPY",
  "PZ = muPZ + KPZ",


]

LoKi_B0.Variables = {
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

tuple.B0.addTool(dtf2)

tuple.B0.ToolList += ["TupleToolDecayTreeFitter/DTFM"]


list = [
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

tuple.B0.ToolList += [ "TupleToolTISTOS" ]
tuple.B0.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.B0.TupleToolTISTOS.Verbose = True
tuple.B0.TupleToolTISTOS.TriggerList = list
tuple.Jpsi.ToolList += [ "TupleToolTISTOS" ]
tuple.Jpsi.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.Jpsi.TupleToolTISTOS.Verbose = True
tuple.Jpsi.TupleToolTISTOS.TriggerList = list
tuple.Kst.ToolList += [ "TupleToolTISTOS" ]
tuple.Kst.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.Kst.TupleToolTISTOS.Verbose = True
tuple.Kst.TupleToolTISTOS.TriggerList = list


tuple.Decay = "[B0 -> ^(J/psi(1S) -> ^mu+ ^mu-)  ^(K*(892)0 -> ^K+ ^pi-)]CC"

#from DecayTreeTuple.Configuration import *
#from Configurables import TupleToolVertexCCMismpMuMu
#tuple.B0.addTool(TupleToolVertexCCMismpMuMu)
#tuple.B0.ToolList+=["TupleToolVertexCCMismpMuMu"]
#
#from DecayTreeTuple.Configuration import *
#from Configurables import TupleToolVertexCCMisppMuMu
#tuple.B0.addTool(TupleToolVertexCCMisppMuMu)
#tuple.B0.ToolList+=["TupleToolVertexCCMisppMuMu"]
#
#from DecayTreeTuple.Configuration import *
#from Configurables import TupleToolVertexCCMispmMuMu
#tuple.B0.addTool(TupleToolVertexCCMispmMuMu)
#tuple.B0.ToolList+=["TupleToolVertexCCMispmMuMu"]
#
#from DecayTreeTuple.Configuration import *
#from Configurables import TupleToolVertexCCMisMuMuMu
#tuple.B0.addTool(TupleToolVertexCCMisMuMuMu)
#tuple.B0.ToolList+=["TupleToolVertexCCMisMuMuMu"]
#
#from DecayTreeTuple.Configuration import *
#from Configurables import TupleToolSallyCCvs5
#tuple.B0.addTool(TupleToolSallyCCvs5)
#tuple.B0.ToolList+=["TupleToolSallyCCvs5"]
#
#
#
#from DecayTreeTuple.Configuration import *
#from Configurables import TupleToolApplyKMuIsolation
#tuple.B0.addTool(TupleToolApplyKMuIsolation)
#tuple.B0.TupleToolApplyKMuIsolation.OutputSuffix="_weights"
#tuple.B0.TupleToolApplyKMuIsolation.WeightsFile="weights_110614_Lc_pX.xml"
#tuple.B0.ToolList+=["TupleToolApplyKMuIsolation"]
#
#
#
##Mysterious things to make isolation work
from Configurables import DaVinci
#name="TupleToolApplyKMuIsolation"
#from Configurables import ChargedProtoParticleMaker
##
#veloprotos = ChargedProtoParticleMaker(name+"ProtoPMaker")
#veloprotos.Inputs = ["Rec/Track/Best"]
#veloprotos.Output = "Rec/ProtoP/myProtoPMaker/ProtoParticles"
##
#DaVinci().appendToMainSequence( [ veloprotos ])
##
#from Gaudi.Configuration import *
#from Configurables       import ProtoParticleCALOFilter, CombinedParticleMaker,NoPIDsParticleMaker
#from CommonParticles.Utils import *
##
#algorithm = NoPIDsParticleMaker('StdNoPIDsVeloPions',  Particle = 'pion',  )
#algorithm.Input = "Rec/ProtoP/myProtoPMaker/ProtoParticles"
#selector = trackSelector ( algorithm , trackTypes = ['Velo'] )
##
#locations = updateDoD ( algorithm )
#DaVinci().appendToMainSequence( [ algorithm ])
##
#from Configurables import GaudiSequencer
#MySequencer = GaudiSequencer('Sequence')


#from Configurables import DaVinci
DaVinci().TupleFile = "BuKstMuMu.root"

#DaVinci().EvtMax = 5000
DaVinci().DataType = '2011'
DaVinci().Simulation   = False
DaVinci().Lumi = True
#CondDB().UseOracle = True
_myseq = GaudiSequencer("myseq")
#_myseq.Members += [ DecayTreeFitterB]
#_myseq.Members += [ sc.sequence() ]
_myseq.Members += [ tuple]

DaVinci().UserAlgorithms = [_myseq]

DaVinci().MainOptions  = ""

#from GaudiConf import IOHelper

#IOHelper().inputFiles(['./00020738_00006713_1.dimuon.dst'], clear=True)


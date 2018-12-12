

from Gaudi.Configuration import *
from PhysSelPython.Wrappers import Selection, SelectionSequence, DataOnDemand, AutomaticData



from Configurables import DecayTreeTuple, FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB, SelDSTWriter, FilterDesktop
from DecayTreeTuple.Configuration import *

#from Configurables import TrackSmearState as SMEAR
#smear = SMEAR("StateSmear")
#from Configurables import TrackScaleState as SCALER
#scaler = SCALER("StateScale")
#scaler.DeltaScale = -3.0e-4
#from Configurables import TrackSmeared
#TrackSmeared("TrackSmearing").smearBest = True
#TrackSmeared("TrackSmearing").Scale = 0.5
#TrackSmearingSeq = GaudiSequencer("TrackSmearingSeq")
#TrackSmearingSeq.Members = [ TrackSmeared("TrackSmearing") ]


# Standard stripping20 
name = 'bukmumu'

"""
Options for building Stripping20,
with tight track chi2 cut (<3)
"""

from Configurables import EventNodeKiller
eventNodeKiller = EventNodeKiller('Stripkiller')
eventNodeKiller.Nodes = ['/Event/AllStreams','/Event/Strip']

from Gaudi.Configuration import *
MessageSvc().Format = "% F%30W%S%7W%R%T %0W%M"

# Tighten Trk Chi2 to <3
from CommonParticles.Utils import DefaultTrackingCuts
DefaultTrackingCuts().Cuts  = { "Chi2Cut" : [ 0, 4 ],
                                "CloneDistCut" : [5000, 9e+99 ] }

#
# Build the streams and stripping object
#
from StrippingArchive.Stripping20.StrippingB2XMuMu import B2XMuMuConf as builder
from StrippingArchive.Stripping20.StrippingB2XMuMu import defaultConfig as config
from StrippingConf.Configuration import StrippingConf, StrippingStream
#from StrippingSettings.Utils import strippingConfiguration
#from StrippingArchive.Utils import buildStreams, cloneLinesFromStream
#from StrippingArchive import strippingArchive
config['MuonPID'] = -999999

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
                    MaxCandidates = 2000
                    )



stripsel = AutomaticData(Location = "Phys/B2XMuMu_Line/Particles")


_stripfilter = FilterDesktop("stripfilter",
  		      Preambulo = ["from LoKiPhysMC.decorators import *","from LoKiPhysMC.functions import mcMatch"],
                      Code = "ALL")

Bu_Kmumu = Selection ("Sel"+name,
                     Algorithm = _stripfilter,
                     RequiredSelections = [stripsel])
seq = SelectionSequence("seq",
                      TopSelection = Bu_Kmumu)

tuple = DecayTreeTuple("B2JpsiK_Tuple")

tuple.Inputs = [stripsel.outputLocation()]

tuple.ToolList =  [
      "TupleToolKinematic"
    , "TupleToolEventInfo"
    , "TupleToolRecoStats"
    , "TupleToolMCTruth"
    , "TupleToolMCBackgroundInfo"
    , "TupleToolPid"
    , "TupleToolANNPID"

]


tuple.addBranches ({         
      "mu3" :  "[B+ -> ^K+ (J/psi(1S) -> mu+ mu-)]CC",
      "Jpsi" :  "[B+ -> K+ ^(J/psi(1S) -> mu+ mu-)]CC",
      "mu1" :  "[B+ -> K+ (J/psi(1S) -> ^mu+ mu-)]CC",
      "mu2" :  "[B+ -> K+ (J/psi(1S) -> mu+ ^mu-)]CC",
      "Bplus" : "^([B+ -> K+ J/psi(1S)]CC)",
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

LoKi_mu3=tuple.mu3.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_mu3")
LoKi_mu3.Preambulo += [
  "from LoKiTracks.decorators import *",
  "nTT=TRFUN(TrIDC ( 'isTT') )"
]
LoKi_mu3.Variables = {
       'NNKpi' : "PPINFO(PROBNNK)-PPINFO(PROBNNpi)",
       'NNKmu' : "PPINFO(PROBNNK)-PPINFO(PROBNNmu)",
       'nTT' : "nTT",
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

LoKi_Bplus=tuple.Bplus.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Bplus")
LoKi_Bplus.Preambulo += [
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

LoKi_Bplus.Variables = {
#       'ID' : "ID",
#       'TAU' : "BPVLTIME()",
#       'DIRA_OWNPV' : "BPVDIRA",
#       'FD_CHI2' : "BPVVDCHI2",
#       'ENDVERTEX_CHI2' : "VFASPF(VCHI2/VDOF)",
       'KMu_Jpsi' : "sqrt(kmuE*kmuE-(PX*PX+PY*PY+PZ*PZ))",
       'KMu_D' : "sqrt(DE*DE-(PX*PX+PY*PY+PZ*PZ))",
       #'DimuM' : "DTF_FUN(CHILD(M,'[B+ -> ^J/psi(1S) K+]CC'),True,'B+')"
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

tuple.Bplus.ToolList += [ "TupleToolTISTOS" ]
tuple.Bplus.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.Bplus.TupleToolTISTOS.Verbose = True
tuple.Bplus.TupleToolTISTOS.TriggerList = list
tuple.Jpsi.ToolList += [ "TupleToolTISTOS" ]
tuple.Jpsi.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.Jpsi.TupleToolTISTOS.Verbose = True
tuple.Jpsi.TupleToolTISTOS.TriggerList = list
tuple.mu3.ToolList += [ "TupleToolTISTOS" ]
tuple.mu3.addTool( TupleToolTISTOS, name = "TupleToolTISTOS" )
tuple.mu3.TupleToolTISTOS.Verbose = True
tuple.mu3.TupleToolTISTOS.TriggerList = list


tuple.Decay = "[B+ -> ^(J/psi(1S) -> ^mu+ ^mu-)  ^K+]CC"

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexCCMismpMuMu
tuple.Bplus.addTool(TupleToolVertexCCMismpMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexCCMismpMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexCCMisppMuMu
tuple.Bplus.addTool(TupleToolVertexCCMisppMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexCCMisppMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexCCMispmMuMu
tuple.Bplus.addTool(TupleToolVertexCCMispmMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexCCMispmMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexCCMisMuMuMu
tuple.Bplus.addTool(TupleToolVertexCCMisMuMuMu)
tuple.Bplus.ToolList+=["TupleToolVertexCCMisMuMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolSallyCCvs5
tuple.Bplus.addTool(TupleToolSallyCCvs5)
tuple.Bplus.ToolList+=["TupleToolSallyCCvs5"]



from DecayTreeTuple.Configuration import *
from Configurables import TupleToolApplyKMuIsolation
tuple.Bplus.addTool(TupleToolApplyKMuIsolation)
tuple.Bplus.TupleToolApplyKMuIsolation.OutputSuffix="_weights"
tuple.Bplus.TupleToolApplyKMuIsolation.WeightsFile="weights_110614_Lc_pX.xml"
tuple.Bplus.ToolList+=["TupleToolApplyKMuIsolation"]



#Mysterious things to make isolation work
from Configurables import DaVinci
name="TupleToolApplyKMuIsolation"
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
locations = updateDoD ( algorithm )
DaVinci().appendToMainSequence( [ algorithm ])
#
from Configurables import GaudiSequencer
MySequencer = GaudiSequencer('Sequence')


dstWriter = SelDSTWriter('BuKmumuDSTWriter',
                   SelectionSequences = sc.activeStreams(),
                   OutputFileSuffix = 'Stripped')

from Configurables import DaVinci
DaVinci().TupleFile = "BuKMuMuMC.root"

DaVinci().EvtMax = -1
DaVinci().DataType = '2012'
DaVinci().Simulation   = True
DaVinci().Lumi = False
#CondDB().UseOracle = True
DaVinci().DDDBtag  = "dddb-20130929-1"
DaVinci().CondDBtag = "sim-20130522-1-vc-md100"
_myseq = GaudiSequencer("myseq")
#_myseq.Members += [ DecayTreeFitterB]
_myseq.Members += [ eventNodeKiller ]
#_myseq.Members += [ TrackSmearingSeq ]  
_myseq.Members += [ sc.sequence() ] 
_myseq.Members += [ seq.sequence() ] 
#_myseq.Members += [ dstWriter.sequence() ]
_myseq.Members += [tuple]

DaVinci().UserAlgorithms = [_myseq]

DaVinci().MainOptions  = ""

#from GaudiConf import IOHelper

#IOHelper().inputFiles(['./00036968_00000003_1.allstreams.dst'], clear=True)

#get stripped data
#make nTuple

from Gaudi.Configuration import *
from PhysSelPython.Wrappers import AutomaticData, Selection, SelectionSequence, DataOnDemand, MergedSelection

#from StrippingConf.Configuration import StrippingConf
#from StrippingSelections.StrippingBd2KstarMuMu import StrippingBd2KstarMuMuConf

#candidateLoc = "/Event/Dimuon/"

from Configurables import DecayTreeTuple, FilterDesktop,CombineParticles,FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB
from Configurables import MCTupleToolKinematic, MCTupleToolHierarchy, TupleToolMCTruth, TupleToolMCBackgroundInfo

from DecayTreeTuple.Configuration import *




# std muon sel
_stdMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

_stdPions = DataOnDemand(Location = "Phys/StdLoosePions/Particles")

#_stdPi0 = DataOnDemand(Location = "Phys/StandardPi0/Particles")

_muonFilter = FilterDesktop('MuonFilter',
                        Code = "(MIPCHI2DV(PRIMARY) > 9.0 ) & (TRCHI2DOF < 3.0) & (TRGHP < 0.35) ") #Apply IP chisq cut on muons


_pionFilter = FilterDesktop('PionFilter',
                        Code = "(MIPCHI2DV(PRIMARY) > 9.0 ) & (TRCHI2DOF < 3.0) & (TRGHP < 0.35) ") 

MuonFilterSel = Selection(name = 'MuonFilterSel',
                        Algorithm = _muonFilter,
                        RequiredSelections = [ _stdMuons ])

PionFilterSel = Selection(name = 'PionFilterSel',
                        Algorithm = _pionFilter,
                        RequiredSelections = [ _stdPions ])

from PhysSelPython.Wrappers import MergedSelection

#B+ => ^mu+ ^mu- ^(H_10 => ^mu+ ^nu_mu))||(B- => ^mu+ ^mu- ^(H_20 => ^mu- ^nu_mu~)


_B = CombineParticles('BFilter',
                        DecayDescriptor = "[B+ -> pi+ pi- mu+]cc",
                        MotherCut = "(BPVDIRA > 0.999) & (PT > 2000) & (BPVVDCHI2 > 50) & (M > 0) & (M < 7500) & (BPVCORRM > 2500) & (BPVCORRM < 10000) & (VFASPF(VCHI2/VDOF)<4)")

BSel = Selection(name = 'BFilterSel',
                        Algorithm = _B,
                        RequiredSelections = [ MuonFilterSel, PionFilterSel ])


seq = SelectionSequence("Seq",
                          TopSelection = BSel)

tuple = DecayTreeTuple("B2D3pimu_Tuple")

#tuple.Inputs = [location]
tuple.Inputs = [seq.outputLocation()]
#tuple.Inputs = ["Phys/DecayTreeFitterB"]
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
      "mu3" : "[B+ -> pi+ pi- ^mu+]CC",
      "mu1" : "[B+ -> ^pi+ pi- mu+]CC ",
      "mu2" : "[B+ -> pi+ ^pi- mu+]CC",
      "Bplus" : "^([B+ -> pi+ pi- mu+]CC)"
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

tuple.Decay = "[B+ -> ^pi+ ^pi- ^mu+]CC"
#tuple.Decay = "Bplus -> ^(J/psi(1S) -> ^mu+ ^mu-) ^gamma"
#tuple.Decay = "J/psi(1S) -> ^mu+ ^mu-"
from Configurables import DaVinci

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexPRppMuMu
tuple.mu1.addTool(TupleToolVertexPRppMuMu)
tuple.mu1.ToolList+=["TupleToolVertexPRppMuMu"]


from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexPRpmMuMu
tuple.mu1.addTool(TupleToolVertexPRpmMuMu)
tuple.mu1.ToolList+=["TupleToolVertexPRpmMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexPRmpMuMu
tuple.mu1.addTool(TupleToolVertexPRmpMuMu)
tuple.mu1.ToolList+=["TupleToolVertexPRmpMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexPRMuMuMu
tuple.mu1.addTool(TupleToolVertexPRMuMuMu)
tuple.mu1.ToolList+=["TupleToolVertexPRMuMuMu"]



from DecayTreeTuple.Configuration import *
from Configurables import TupleToolSallyvs4
tuple.Bplus.addTool(TupleToolSallyvs4)
tuple.Bplus.ToolList+=["TupleToolSallyvs4"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolApplyPiMuIsolation
tuple.Bplus.addTool(TupleToolApplyPiMuIsolation)
tuple.Bplus.TupleToolApplyPiMuIsolation.OutputSuffix="_weights"
tuple.Bplus.TupleToolApplyPiMuIsolation.WeightsFile="weights_110614_Lc_pX.xml"
tuple.Bplus.ToolList+=["TupleToolApplyPiMuIsolation"]

#Mysterious things to make isolation work

name="TupleToolApplyPiMuIsolation"
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
#DaVinci().TupleFile = "Bplus23munu.root"
#DaVinci().EventPreFilters = fltrs.filters ('Filters')
#DaVinci().EvtMax = 1000
DaVinci().PrintFreq = 100
#DaVinci().EvtMax = 750
DaVinci().DataType = '2012'

DaVinci().Simulation   = True
DaVinci().Lumi = False
#DaVinci().DDDBtag  = "dddb-20120831"
#DaVinci().CondDBtag = "sim-20121025-vc-md100"

from Configurables import CondDB
CondDB().UseLatestTags =["2012"]
DaVinci().appendToMainSequence( [ seq.sequence(),tuple])
DaVinci().MainOptions  = ""



from Gaudi.Configuration import *
from PhysSelPython.Wrappers import Selection, SelectionSequence, DataOnDemand, AutomaticData



from Configurables import DecayTreeTuple, FitDecayTrees, CombineParticles, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB, SelDSTWriter, FilterDesktop
from DecayTreeTuple.Configuration import *
from CommonParticles.Utils import *
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


# Standard stripping20r1 
name = 'bukmumu'

"""
Options for building Stripping20r1,
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


_stdMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

_muonFilter = FilterDesktop('MuonFilter',
                        Code = "ALL")

MuonFilterSel = Selection(name = 'MuonFilterSel',
                        Algorithm = _muonFilter,
                        RequiredSelections = [ _stdMuons ])


from PhysSelPython.Wrappers import MergedSelection

_Jpsi = CombineParticles('JpsiFilter',
                        DecayDescriptor = "J/psi(1S) -> mu+ mu-",
                        CombinationCut = "(ADAMASS('J/psi(1S)')<100.*MeV) & (ADOCACHI2CUT(30., ''))",
                        MotherCut = "(VFASPF(VCHI2)<25)" )

JpsiSel = Selection(name = 'JpsiFilterSel',
                        Algorithm = _Jpsi,
                        RequiredSelections = [ MuonFilterSel ])


_JpsiFilter = FilterDesktop('JpsiFilter2',
                        Code = "(ADMASS('J/psi(1S)')<80.*MeV) & (VFASPF(VCHI2)<16.) & (MFIT) & (MINTREE('mu+'==ABSID, PIDmu) > 0)")

JpsiFilterSel = Selection(name = 'JpsiFilterSel2',
                        Algorithm = _JpsiFilter,
                        RequiredSelections = [ JpsiSel ])

_stdKaons = DataOnDemand(Location = "Phys/StdAllLooseKaons/Particles")

_kaonFilter = FilterDesktop('KaonFilter',
                        Code = "(TRCHI2DOF<5) & (PIDK > 0)")

KaonFilterSel = Selection(name = 'KaonFilterSel',
                        Algorithm = _kaonFilter,
                        RequiredSelections = [ _stdKaons ])

_B = CombineParticles('BFilter',
                        DecayDescriptor = "[B+ -> J/psi(1S) K+]cc",
                        CombinationCut = "in_range(5050,AM,5550)" ,
                        DaughtersCuts = {"K+": "(PT > 500.*MeV)" }, 
                        MotherCut = "in_range(5150,M,5450) & (VFASPF(VCHI2PDOF) < 10)",
                        ReFitPVs = True)


BSel = Selection(name = 'BFilterSel',
                        Algorithm = _B,
                        RequiredSelections = [ JpsiFilterSel , KaonFilterSel ])


_BFilter = FilterDesktop('BFilter2',
                        Code = "(CHILD('Beauty -> ^J/psi(1S) X', PFUNA(ADAMASS('J/psi(1S)'))) < 80.*MeV) & (BPVLTIME()>0.2*ps) & (MINTREE('K+'==ABSID, PT) > 500 *MeV)")
#                        )
BSel2 = Selection(name = 'BFilterSel2',
                        Algorithm = _BFilter,
                        RequiredSelections = [ BSel ])



seq = SelectionSequence("Seq",
                          TopSelection = BSel2)





tuple = DecayTreeTuple("B2JpsiK_Tuple")

tuple.Inputs = [seq.outputLocation()]

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
#    , "Hlt2TopoMu2BodyDecision"
#    , "Hlt2TopoMu3BodyDecision"

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


#tuple.Decay = "[B+ -> ^J/psi(1S) ^K+]CC"

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
#MySequencer = GaudiSequencer('Sequence')


#dstWriter = SelDSTWriter('BuKmumuDSTWriter',
#                   SelectionSequences = sc.activeStreams(),
#                   OutputFileSuffix = 'Stripped')

from Configurables import DaVinci
DaVinci().TupleFile = "BuKMuMuMC2011_MyAtt.root"

DaVinci().EvtMax = 500
DaVinci().DataType = '2011'
DaVinci().Simulation   = True
DaVinci().Lumi = False
#CondDB().UseOracle = True

DaVinci().DDDBtag  = "dddb-20130929"
DaVinci().CondDBtag = "sim-20130522-vc-md100"
#DaVinci().appendToMainSequence( [ seq.sequence(),tuple])
#DaVinci().MainOptions  = ""


#DaVinci().appendToMainSequence( [tuple])
#DaVinci().MainOptions  = ""

_myseq = GaudiSequencer("myseq")
_myseq.Members += [ eventNodeKiller ]
_myseq.Members += [ seq.sequence() ] 
_myseq.Members += [tuple]

importOptions("$APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py");

DaVinci().UserAlgorithms = [_myseq]

DaVinci().MainOptions  = ""

from GaudiConf import IOHelper

IOHelper().inputFiles(['./00024657_00000007_1.allstreams.dst'], clear=True)

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
from StrippingArchive.Stripping21.StrippingB23MuNu import B23MuNuConf as builder
from StrippingArchive.Stripping21.StrippingB23MuNu import defaultConfig as config
from StrippingConf.Configuration import StrippingConf, StrippingStream

print config
print "Done"
#from StrippingSettings.Utils import strippingConfiguration
#from StrippingArchive.Utils import buildStreams, cloneLinesFromStream
#from StrippingArchive import strippingArchive
#config1 = config['CONFIG']
config['Muon_PIDmu'] = -999999
config['Muon_PIDmuK'] = -999999


stripping='stripping21'
#get the configuration dictionary from the database
#config  = strippingConfiguration(stripping)
#config['HLT_FILTER_HMuNu']=""
lb = builder('B23MuNu',config)
print config
#get the line builders from the archive


#
# Merge into one stream and run in flag mode
#
AllStreams = StrippingStream("Semileptonic")

for line in lb.lines():
    if line.name() == 'StrippingB23MuNu_TriMuLine':
        AllStreams.appendLines([line])
        print "success"

sc = StrippingConf( Streams = [ AllStreams ],
                    MaxCandidates = 2000
                    )

name="B23MuNu"

#stripsel = AutomaticData(Location = "/Phys/B23MuNu_TriMuLine/Particles")


#_stripfilter = FilterDesktop("stripfilter",
#  		      Preambulo = ["from LoKiPhysMC.decorators import *","from LoKiPhysMC.functions import mcMatch"],
#                      Code = "ALL")

#Bu_3munu = Selection ("Sel"+name,
#                     Algorithm = _stripfilter,
#                     RequiredSelections = [stripsel])
#seq = SelectionSequence("seq",
#                      TopSelection = Bu_3munu)



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
DaVinci().TupleFile = "B_PiMuMu.root"
#DaVinci().EventPreFilters = fltrs.filters ('Filters')
DaVinci().PrintFreq = 100
#DaVinci().EvtMax = -1
DaVinci().DataType = '2012'

DaVinci().Simulation   = True
DaVinci().Lumi = False
DaVinci().DDDBtag  = "dddb-20130929-1"
DaVinci().CondDBtag = "sim-20130522-1-vc-mu100"


_myseq = GaudiSequencer("myseq")
#_myseq.Members += [ DecayTreeFitterB]
_myseq.Members += [ eventNodeKiller ]
#_myseq.Members += [ TrackSmearingSeq ]  
_myseq.Members += [ sc.sequence() ] 
#_myseq.Members += [ seq.sequence() ] 
#_myseq.Members += [ dstWriter.sequence() ]
_myseq.Members += [tuple]

importOptions("$APPCONFIGOPTS/DaVinci/DV-RedoCaloPID-Stripping21.py")

DaVinci().UserAlgorithms = [_myseq]

DaVinci().MainOptions  = ""

#from Configurables import CondDB
#CondDB().UseLatestTags =["2012"]
#DaVinci().appendToMainSequence( [sc.sequence()]
#DaVinci().appendToMainSequence( [ tuple ] )
#DaVinci().appendToMainSequence( [ seq.sequence(),tuple])
#DaVinci().MainOptions  = ""

#from GaudiConf import IOHelper

#IOHelper().inputFiles(['./00045492_00000014_2.AllStreams.dst'], clear=True)


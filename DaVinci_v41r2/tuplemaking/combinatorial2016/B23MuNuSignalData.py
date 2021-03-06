# $Id: $
# Test your line(s) of the stripping
#  
# NOTE: Please make a copy of this file for your testing, and do NOT change this one!
#

from Gaudi.Configuration import *
from Configurables import DaVinci

line = 'B23MuNu_TriMuLine'
location = '/Event/Semileptonic/Phys/B23MuNu_TriMuLine/Particles'

#from Configurables import DaVinci, PrintDecayTree
#pt = PrintDecayTree(Inputs = [ location ])
#DaVinci().appendToMainSequence( [ pt ] )




######### Refining the candidate
# get classes to build the SelectionSequence
from PhysSelPython.Wrappers import AutomaticData, Selection, SelectionSequence
# Get the Candidates from the DST. AutomaticData is for data on the DST
TriMuSel = AutomaticData(Location = location)

TriMuSeq = SelectionSequence('SeqTriMu',
				TopSelection = TriMuSel,
			    )

DaVinci().appendToMainSequence( [ TriMuSeq.sequence() ] )
# DecayTreeTuple constructor 
from Configurables import DecayTreeTuple
#from DecayTreeTuple.Configuration import *

from Configurables import DecayTreeTuple, FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB, SelDSTWriter
#from DecayTreeTuple.Configuration import *

from Configurables import DecayTreeTuple, FilterDesktop,CombineParticles,FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB, TupleToolPid
from DecayTreeTuple.Configuration import *



tuple = DecayTreeTuple("B_Tuple")

#tuple.Inputs = [ TriMuSeq.outputLocation() ]
tuple.Inputs = ["/Event/Semileptonic/Phys/B23MuNu_TriMuLine/Particles"]
#tuple.Inputs = ["Phys/DecayTreeFitterB"]

#tuple.ToolList =  [
#      "TupleToolKinematic"
#    , "TupleToolEventInfo"
#    , "TupleToolRecoStats"
#    , "TupleToolMCTruth"
#    , "TupleToolMCBackgroundInfo"
#]

tuple.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats",
#      "TupleToolPid",
      "TupleToolANNPID",
      "TupleToolL0Data"
]



tuple.addBranches({  # remove all "^" except where needed.
    "Bplus" :  "^([B+ -> mu+ mu- mu+]CC)",
    "mu1" :  "[B+ -> ^mu+ mu- mu+]CC ",
    "mu2" :  "[B+ -> mu+ ^mu- mu+]CC ",
    "mu3" :  "[B+ -> mu+ mu- ^mu+]CC ",
    })

tuple.ToolList += [ "TupleToolPid" ]
tuple.addTool( TupleToolPid, name = "TupleToolPid")
tuple.TupleToolPid.Verbose = True

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
#       "CONE_angle" : "RELINFO('/Event/Semileptonic/Phys/B23MuNu_TriMuLine/ConeIsoInfo','CONEANGLE', -1.)",
#       "CONE_PT" : "RELINFO('/Event/Semileptonic/Phys/B23MuNu_TriMuLine/ConeIsoInfo','CONEPT', -1.)",
#       "BDTIso" : "RELINFO('/Event/Semileptonic/Phys/B23MuNu_TriMuLine/VtxIsoBDTInfo','VTXISOBDTHARDFIRSTVALUE', -1.)",
#       "NormalVtxIso" : "RELINFO('/Event/Semileptonic/Phys/B23MuNu_TriMuLine/VtxIsoInfo','VTXISONUMVTX', -1.)"

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
       'isMuonTight_previous' : "switch(ISMUONTIGHT,1,0)",
       'isMuonLoose_previous' : "switch(ISMUONLOOSE,1,0)",
       'isMuonLoki_previous' : "switch(ISMUON,1,0)",
       'inMuon_previous' : "switch(INMUON,1,0)",
       'nShared_previous' : "PPINFO(LHCb.ProtoParticle.MuonNShared,-1000)"
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
       'isMuonTight_previous' : "switch(ISMUONTIGHT,1,0)",
       'isMuonLoose_previous' : "switch(ISMUONLOOSE,1,0)",
       'isMuonLoki_previous' : "switch(ISMUON,1,0)",
       'inMuon_previous' : "switch(INMUON,1,0)",
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
       'isMuonTight_previous' : "switch(ISMUONTIGHT,1,0)",
       'isMuonLoose_previous' : "switch(ISMUONLOOSE,1,0)",
       'isMuonLoki_previous' : "switch(ISMUON,1,0)",
       'inMuon_previous' : "switch(INMUON,1,0)",
}



tuple.Decay = "[B+ -> ^mu+ ^mu- ^mu+]CC"


from Configurables import DaVinci

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexDatappMuMu
tuple.mu1.addTool(TupleToolVertexDatappMuMu)
tuple.mu1.ToolList+=["TupleToolVertexDatappMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexDatapmMuMu
tuple.mu1.addTool(TupleToolVertexDatapmMuMu)
tuple.mu1.ToolList+=["TupleToolVertexDatapmMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexDatampMuMu
tuple.mu1.addTool(TupleToolVertexDatampMuMu)
tuple.mu1.ToolList+=["TupleToolVertexDatampMuMu"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexDataMuMuMu
tuple.mu1.addTool(TupleToolVertexDataMuMuMu)
tuple.mu1.ToolList+=["TupleToolVertexDataMuMuMu"]

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
locations = updateDoD ( algorithm )
DaVinci().appendToMainSequence( [ algorithm ])
#
from Configurables import GaudiSequencer
MySequencer = GaudiSequencer('Sequence')


#DaVinci().HistogramFile = 'DV_stripping_histosnew2.root'
DaVinci().HistogramFile = 'DVHistosignal.root'
DaVinci().TupleFile = "DVTuplesignal.root"
#DaVinci().EvtMax = 50000
DaVinci().PrintFreq = 2000

#DaVinci().appendToMainSequence( [ MySequencer ] )
DaVinci().appendToMainSequence( [ tuple] )
#DaVinci().appendToMainSequence( [ sr ] )
#DaVinci().appendToMainSequence( [ ac ] )
DaVinci().DataType  = "2016"
DaVinci().InputType = "DST"


# change the column size of timing table
from Configurables import TimingAuditor, SequencerTimerTool
TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
TimingAuditor().TIMER.NameSize = 60
#NTupleSvc().Output = ["FILE1 DATAFILE='trythis.root' TYP='ROOT' OPT='NEW'"]
MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

# database
#DaVinci().DDDBtag  = "dddb-20120831"
#DaVinci().CondDBtag = "cond-20121008"
DaVinci().Lumi = True
# input file
# importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco14_Run125113.py")

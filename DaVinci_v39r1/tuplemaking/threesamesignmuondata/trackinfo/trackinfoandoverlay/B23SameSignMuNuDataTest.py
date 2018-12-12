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

from Configurables import DecayTreeTuple, FilterDesktop,CombineParticles,FitDecayTrees, TupleToolRecoStats, TupleToolTrigger, TupleToolTISTOS, CondDB
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

tuple.Decay = "[B+ -> ^mu+ ^mu+ ^mu+]CC"

tuple.ToolList =  [
      "TupleToolKinematic",
      "TupleToolEventInfo",
      "TupleToolRecoStats",
      "TupleToolPid",
      "TupleToolANNPID"
]



tuple.addBranches({  # remove all "^" except where needed.
#    "Bplus" :  "^([B+ -> mu+ mu+ mu+]CC)",
    "Bplus" :  "[B+ -> mu+ mu+ mu+]CC",
    "mu1" :  "[B+ -> ^mu+ mu+ mu+]CC ",
    "mu2" :  "[B+ -> mu+ ^mu+ mu+]CC ",
    "mu3" :  "[B+ -> mu+ mu+ ^mu+]CC ",
    })

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

#from LoKiPhys.decorators import *
#LoKi_OVERLAP=LoKi__Hybrid__TupleTool("LoKi_OVERLAP")
#LoKi_OVERLAP.Variables =  {
#    "OVERLAP_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.Velo) )"
#                           } 

#from LoKiPhys.decorators import *

#tuple.Bplus.addTupleTool()
#tuple.Bplus.ToolList+=[" LoKi::Hybrid::TupleTool/LoKi_OVERLAP "]
#LoKi_OVERLAP=LoKi__Hybrid__TupleTool("LoKi_OVERLAP")
#LoKi_OVERLAP.Variables =  {
#    "OVERLAP_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.Velo) )"
#                           } 



LoKi_All=tuple.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_All")
LoKi_All.Variables = {
        'MINIPCHI2' : "MIPCHI2DV(PRIMARY)",
        'MINIP' : "MIPDV(PRIMARY)",
        'ETA' : 'ETA',
        'PHI' : 'PHI'
}

###----------WORKING VERSION-------------###
#from DecayTreeTuple.Configuration import * 
#from Configurables import LoKi__Hybrid__EvtTupleTool, LoKi__Hybrid__TupleTool

#LoKi_OVERLAP=LoKi__Hybrid__TupleTool("LoKi_OVERLAP")
#LoKi_OVERLAP.Variables =  {
#    "OVERLAP_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.Velo) )"
#                           } 


#tuple.Bplus.addTool(LoKi_OVERLAP)
#tuple.Bplus.ToolList+=["LoKi::Hybrid::TupleTool/LoKi_OVERLAP"]
###-------------------------------------###

#LoKi_Overlap=tuple.Bplus.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Overlap")
#LoKi_Overlap.Preambulo += ["PFUNA = LoKi.Particles.PFunA" ]
#LoKi_Overlap.Variables =  {
#    "OVERLAP_12" : "LoKi.Particles.PFunA( (AOVERLAP(1,2, LHCb.LHCbID.Velo) )"
#                           } 
from DecayTreeTuple.Configuration import *
from Configurables import LoKi__Hybrid__EvtTupleTool, LoKi__Hybrid__TupleTool

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
       'Corrected_Mass' : "BPVCORRM",
       'OVERLAP_VELO_12' : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.Velo) )"
#       "OVERLAP_VELO_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.Velo) )",
#       "OVERLAP_VELO_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.Velo) )",
#       "OVERLAP_IT_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.IT) )",
#       "OVERLAP_IT_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.IT) )",
#       "OVERLAP_IT_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.IT) )",
#       "OVERLAP_IT_11" : "LoKi.Particles.PFunA( AOVERLAP(1,1, LHCb.LHCbID.IT) )",
#       "OVERLAP_OT_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.OT) )",
#       "OVERLAP_OT_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.OT) )",
#       "OVERLAP_OT_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.OT) )",
#       "OVERLAP_TT_14" : "LoKi.Particles.PFunA( AOVERLAP(1,4, LHCb.LHCbID.TT) )",
#       "OVERLAP_TT_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.TT) )",
#       "OVERLAP_TT_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.TT) )",
#       "OVERLAP_TT_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.TT) )"

}

#from DecayTreeTuple.Configuration import * 
#from Configurables import LoKi__Hybrid__EvtTupleTool, LoKi__Hybrid__TupleTool
#
#LoKi_OVERLAP=tuple.Bplus.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_OVERLAP")
#LoKi_OVERLAP.Variables =  {
#    "OVERLAP_VELO_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.Velo) )",
#    "OVERLAP_VELO_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.Velo) )",
#    "OVERLAP_VELO_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.Velo) )",
#    "OVERLAP_IT_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.IT) )",
#    "OVERLAP_IT_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.IT) )",
#    "OVERLAP_IT_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.IT) )",
#    "OVERLAP_IT_11" : "LoKi.Particles.PFunA( AOVERLAP(1,1, LHCb.LHCbID.IT) )",
#    "OVERLAP_OT_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.OT) )",
#    "OVERLAP_OT_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.OT) )",
#    "OVERLAP_OT_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.OT) )",
#    "OVERLAP_TT_14" : "LoKi.Particles.PFunA( AOVERLAP(1,4, LHCb.LHCbID.TT) )",
#    "OVERLAP_TT_12" : "LoKi.Particles.PFunA( AOVERLAP(1,2, LHCb.LHCbID.TT) )",
#    "OVERLAP_TT_13" : "LoKi.Particles.PFunA( AOVERLAP(1,3, LHCb.LHCbID.TT) )",
#    "OVERLAP_TT_23" : "LoKi.Particles.PFunA( AOVERLAP(2,3, LHCb.LHCbID.TT) )"
#                           } 



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



#tuple.Decay = "[B+ -> ^mu+ ^mu+ ^mu+]CC"


from Configurables import DaVinci

from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexthreeSSmuonDatappMuMu
tuple.mu1.addTool(TupleToolVertexthreeSSmuonDatappMuMu)
tuple.mu1.ToolList+=["TupleToolVertexthreeSSmuonDatappMuMu"]
#
from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexthreeSSmuonDatapmMuMu
tuple.mu1.addTool(TupleToolVertexthreeSSmuonDatapmMuMu)
tuple.mu1.ToolList+=["TupleToolVertexthreeSSmuonDatapmMuMu"]
#
from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexthreeSSmuonDatampMuMu
tuple.mu1.addTool(TupleToolVertexthreeSSmuonDatampMuMu)
tuple.mu1.ToolList+=["TupleToolVertexthreeSSmuonDatampMuMu"]
#
from DecayTreeTuple.Configuration import *
from Configurables import TupleToolVertexDataMuMuMu
tuple.mu1.addTool(TupleToolVertexDataMuMuMu)
tuple.mu1.ToolList+=["TupleToolVertexDataMuMuMu"]
#
from DecayTreeTuple.Configuration import *
from Configurables import TupleToolSallyvs3
tuple.Bplus.addTool(TupleToolSallyvs3)
tuple.Bplus.ToolList+=["TupleToolSallyvs3"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleTTInfo3sta
tuple.mu1.addTool(TupleTTInfo3sta)
tuple.mu1.ToolList+=["TupleTTInfo3sta"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleTTInfo3sta
tuple.mu2.addTool(TupleTTInfo3sta)
tuple.mu2.ToolList+=["TupleTTInfo3sta"]

from DecayTreeTuple.Configuration import *
from Configurables import TupleTTInfo3sta
tuple.mu3.addTool(TupleTTInfo3sta)
tuple.mu3.ToolList+=["TupleTTInfo3sta"]


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
##
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
DaVinci().DataType  = "2011"
DaVinci().InputType = "DST"


# change the column size of timing table
from Configurables import TimingAuditor, SequencerTimerTool
TimingAuditor().addTool(SequencerTimerTool,name="TIMER")
TimingAuditor().TIMER.NameSize = 60
#NTupleSvc().Output = ["FILE1 DATAFILE='trythis.root' TYP='ROOT' OPT='NEW'"]
MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

# database
#DaVinci().DDDBtag  = ""
#DaVinci().CondDBtag = ""
DaVinci().Lumi = True

from GaudiConf import IOHelper

# Use the local input data
IOHelper().inputFiles([
    './00041838_00000631_1.semileptonic.dst'
], clear=True)
# input file
# importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco14_Run125113.py")

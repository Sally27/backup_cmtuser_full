# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/10012005.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 10012005
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DiMuonBothSignP3GeVMassCut.py" )
from Configurables import Generation
Generation().EventType = 10012005
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=DiMuon,Both,p3GeV,m4.7GeV.dec"
Generation().RepeatDecay.Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

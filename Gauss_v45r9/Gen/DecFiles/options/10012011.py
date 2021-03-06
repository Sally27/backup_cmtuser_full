# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/10012011.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 10012011
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DiMuonOppositeSignP3GeVMinMaxMassDocaHighPtProd.py" )
from Configurables import Generation
Generation().EventType = 10012011
Generation().SampleGenerationTool = "RepeatDecay"
from Configurables import RepeatDecay
Generation().addTool( RepeatDecay )
from Configurables import Inclusive
Generation().RepeatDecay.addTool( Inclusive )
Generation().RepeatDecay.Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b=DiMuon,OppositeSign,p3GeV,m4.7GeV,m6GeV,doca0.4mm,HighPtProd.dec"
Generation().RepeatDecay.Inclusive.CutTool = "LHCbAcceptance"
Generation().FullGenEventCutTool = "DiLeptonInAcceptance"
Generation().RepeatDecay.Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

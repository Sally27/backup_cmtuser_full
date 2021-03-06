# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11396010.py generated: Wed, 25 Jan 2017 15:25:35
#
# Event Type: 11396010
#
# ASCII decay Descriptor: [B0-> {(D+ -> K- pi+ pi+) || (D+ -> K- K+ pi+)} {(D- -> K+ pi- pi-) || (D- -> K+ K- pi-)}]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 11396010
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DD,Kpipi,KKpi=CPV,DDALITZ,DecProdCut,pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

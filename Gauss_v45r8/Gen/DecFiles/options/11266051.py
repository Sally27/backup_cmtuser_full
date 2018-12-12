# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11266051.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 11266051
#
# ASCII decay Descriptor: {[[B0]nos -> (D_s- => K+ K- pi-) K+ pi- pi+]cc, [[B0]os -> (D_s+ => K- K+ pi+) K- pi+ pi-]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 11266051
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsKpipi,KKpi=DDalitz,DecProdCut,pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

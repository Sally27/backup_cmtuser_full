# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11266006.py generated: Wed, 25 Jan 2017 15:25:20
#
# Event Type: 11266006
#
# ASCII decay Descriptor: {[[B0]nos -> (D- => K+ pi- pi-) pi+ pi- pi+]cc, [[B0]os -> (D+ => K- pi+ pi+) pi- pi+ pi-]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 11266006
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_D-pipipi+withf2=DecProdCut_pCut1600MeV.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

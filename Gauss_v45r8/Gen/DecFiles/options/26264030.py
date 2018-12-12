# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/26264030.py generated: Fri, 27 Mar 2015 15:48:08
#
# Event Type: 26264030
#
# ASCII decay Descriptor: [Sigma_c*0 -> (Lambda_c+ --> p+ K- pi+) pi-]CC
#
from Configurables import Generation
Generation().EventType = 26264030
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Scst0_Lcpi,pKpi=DecProdCut_pCut1000MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 4114,-4114 ]

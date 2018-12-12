# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/27260210.py generated: Fri, 27 Mar 2015 16:10:17
#
# Event Type: 27260210
#
# ASCII decay Descriptor: This is the decay file for the background study for D*+ -> D0(D0->K- pi+ pi- pi+) pi+
#
from Configurables import Generation
Generation().EventType = 27260210
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Dst0.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 423,-423 ]

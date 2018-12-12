# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/22164121.py generated: Fri, 27 Mar 2015 16:10:12
#
# Event Type: 22164121
#
# ASCII decay Descriptor: {[D0 -> (K*(892)~0 -> K- pi+) (KS0 -> pi+ pi-)]cc ,[D0 -> (K*(892)0 -> K+ pi-) (KS0 -> pi+ pi-)]cc}
#
from Configurables import Generation
Generation().EventType = 22164121
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_KstKS=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]

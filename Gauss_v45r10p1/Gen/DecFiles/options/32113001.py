# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/32113001.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 32113001
#
# ASCII decay Descriptor: [ Sigma+ -> mu+ mu- p+ ]cc
#
from Configurables import Generation
Generation().EventType = 32113001
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Sigma+_pmumu=phsp,DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCb"
Generation().SignalPlain.SignalPIDList = [ 3222,-3222 ]

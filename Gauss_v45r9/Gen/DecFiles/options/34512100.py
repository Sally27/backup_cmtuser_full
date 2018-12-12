# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/34512100.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 34512100
#
# ASCII decay Descriptor: K_S0 -> pi+ mu- nu_mu~
#
from Configurables import Generation
Generation().EventType = 34512100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ks_pimunu.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 310 ]

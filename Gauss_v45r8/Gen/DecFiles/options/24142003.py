# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/24142003.py generated: Fri, 27 Mar 2015 15:48:15
#
# Event Type: 24142003
#
# ASCII decay Descriptor: J/psi(1S) -> mu+ mu- {,gamma} {,gamma}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/JpsiTransverse.py" )
from Configurables import Generation
Generation().EventType = 24142003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_Jpsi,mm=Transverse,NoCut.dec"
Generation().SignalPlain.CutTool = ""
Generation().SignalPlain.SignalPIDList = [ 443 ]

# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11874031.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 11874031
#
# ASCII decay Descriptor: { [ B0 -> (D+ -> pi+ pi+ pi-) mu- anti_nu_mu ]cc }
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAcc.py" )
from Configurables import Generation
Generation().EventType = 11874031
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DX,3body=cocktail,TracksInAcc.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCb"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

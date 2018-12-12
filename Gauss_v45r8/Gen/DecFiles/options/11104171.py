# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104171.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 11104171
#
# ASCII decay Descriptor: [ B0 -> (Lambda0 -> p+ pi-) (anti-Lambda0 -> p~- pi+) ]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2LambdaX.py" )
from Configurables import Generation
Generation().EventType = 11104171
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_LambdaLambdabar=tightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

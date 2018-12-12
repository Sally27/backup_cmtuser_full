# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42900010.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 42900010
#
# ASCII decay Descriptor: pp -> (Z0 -> nu+ nu-) + jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Znunujet.py" )
from Configurables import Generation
Generation().EventType = 42900010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_nunujet.dec"
Generation().Special.CutTool = ""

# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42912002.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 42912002
#
# ASCII decay Descriptor: pp -> (Z0 -> b b~) (Z0 -> b b~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/ZZbbbb.py" )
from Configurables import Generation
Generation().EventType = 42912002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ZZ_bb,bb.dec"
Generation().Special.CutTool = "LHCbAcceptance"

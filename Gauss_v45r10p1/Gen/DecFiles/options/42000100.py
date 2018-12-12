# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42000100.py generated: Wed, 25 Jan 2017 15:25:23
#
# Event Type: 42000100
#
# ASCII decay Descriptor: pp -> gamma + jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/gammajet.py" )
from Configurables import Generation
Generation().EventType = 42000100
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/gammajet.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
Generation().Special.PythiaHiggsType.LeptonIsFromMother = False
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42112020.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 42112020
#
# ASCII decay Descriptor: pp -> (Z0 -> mu+ mu-) + jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zmumujet.py" )
from Configurables import Generation
Generation().EventType = 42112020
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_mumujet.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

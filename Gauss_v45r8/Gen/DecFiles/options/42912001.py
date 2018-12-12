# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42912001.py generated: Fri, 27 Mar 2015 15:48:01
#
# Event Type: 42912001
#
# ASCII decay Descriptor: pp -> (Z0 -> l+ l-) (Z0 -> b b~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/ZZllbb.py" )
from Configurables import Generation
Generation().EventType = 42912001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ZZ_ll,bb.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 10*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = 0
Generation().Special.PythiaHiggsType.MotherOfThebquarks = "Z0"

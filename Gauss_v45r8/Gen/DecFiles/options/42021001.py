# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42021001.py generated: Fri, 27 Mar 2015 15:47:58
#
# Event Type: 42021001
#
# ASCII decay Descriptor: pp -> ([W+ -> ...]cc) (Z0 -> ...) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WZlX=1l15GeV.py" )
from Configurables import Generation
Generation().EventType = 42021001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/WZ_l,X=1l15GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 15*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42112032.py generated: Wed, 25 Jan 2017 15:25:31
#
# Event Type: 42112032
#
# ASCII decay Descriptor: pp -> (Z0/gamma* -> mu+ mu- jet) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DrellYanmumujet5GeV.py" )
from Configurables import Generation
Generation().EventType = 42112032
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/DrellYan_mumujet=5GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 1.0*SystemOfUnits.GeV

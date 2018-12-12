# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42112021.py generated: Fri, 27 Mar 2015 15:48:00
#
# Event Type: 42112021
#
# ASCII decay Descriptor: pp -> (Z0/gamma* -> mu+ mu-) + jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zgmumujet.py" )
from Configurables import Generation
Generation().EventType = 42112021
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zg_mumujet40GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.MotherOfLeptonMinMass = 40*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

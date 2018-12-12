# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42122021.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 42122021
#
# ASCII decay Descriptor: pp -> (Z0/gamma* -> e+ e-) + jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zgeejet.py" )
from Configurables import Generation
Generation().EventType = 42122021
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zg_eejet40GeV.dec"
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

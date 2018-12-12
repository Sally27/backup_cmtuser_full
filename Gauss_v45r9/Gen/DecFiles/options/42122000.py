# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42122000.py generated: Fri, 27 Mar 2015 16:10:04
#
# Event Type: 42122000
#
# ASCII decay Descriptor: pp -> (Z0 -> e+ e-) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zee.py" )
from Configurables import Generation
Generation().EventType = 42122000
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_ee.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

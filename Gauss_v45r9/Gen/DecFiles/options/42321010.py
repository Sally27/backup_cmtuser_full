# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42321010.py generated: Fri, 27 Mar 2015 16:10:03
#
# Event Type: 42321010
#
# ASCII decay Descriptor: pp -> [W+ -> e+ nu_mu]cc +jet ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wenujet.py" )
from Configurables import Generation
Generation().EventType = 42321010
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_enujet.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

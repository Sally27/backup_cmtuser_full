# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42311002.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 42311002
#
# ASCII decay Descriptor: pp -> [W+ -> mu+ nu_mu {,gamma} {,gamma}]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wmunu=PHOTOS.py" )
from Configurables import Generation
Generation().EventType = 42311002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_munumu=PHOTOS.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

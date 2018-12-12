# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42112102.py generated: Fri, 27 Mar 2015 16:10:06
#
# Event Type: 42112102
#
# ASCII decay Descriptor: pp -> (Z0gamma -> e+ e- gamma) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zgammaee.py" )
from Configurables import Generation
Generation().EventType = 42112102
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zgamma_ee.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

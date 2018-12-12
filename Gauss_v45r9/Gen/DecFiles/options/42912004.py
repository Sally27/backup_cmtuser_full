# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42912004.py generated: Fri, 27 Mar 2015 16:10:13
#
# Event Type: 42912004
#
# ASCII decay Descriptor: pp -> (Z0 -> l+ l-) (Z0 -> b b~) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/ZZllbb.py" )
from Configurables import Generation
Generation().EventType = 42912004
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/ZZ_ll,bb=1l,5Gev,1b.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 5*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = 1
Generation().Special.PythiaHiggsType.MotherOfThebquarks = "Z0"

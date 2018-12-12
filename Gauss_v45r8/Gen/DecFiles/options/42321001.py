# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/42321001.py generated: Fri, 27 Mar 2015 15:48:11
#
# Event Type: 42321001
#
# ASCII decay Descriptor: pp -> [W+ -> e+ nu_e {,gamma} {,gamma} ]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wenue=PHOTOS.py" )
from Configurables import Generation
Generation().EventType = 42321001
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_enue=PHOTOS.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 4*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

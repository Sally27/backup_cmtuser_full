# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42923002.py generated: Wed, 25 Jan 2017 15:25:28
#
# Event Type: 42923002
#
# ASCII decay Descriptor: pp -> ([W+ -> l nu_l]cc) (Z0 -> l+ l-) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/WZlnulll=1l15GeV.py" )
from Configurables import Generation
Generation().EventType = 42923002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/WZ_lnul,ll=1l15GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 15*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

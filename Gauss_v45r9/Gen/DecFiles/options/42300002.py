# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42300002.py generated: Fri, 27 Mar 2015 16:10:19
#
# Event Type: 42300002
#
# ASCII decay Descriptor: pp -> [W+ -> tau+ nu_tau -> anti-nu_tau e+ nu_e]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Wtaunu=e.py" )
from Configurables import Generation
Generation().EventType = 42300002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/W_taunutau=e.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 10*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

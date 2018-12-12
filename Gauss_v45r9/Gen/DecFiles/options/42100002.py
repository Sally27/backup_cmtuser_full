# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/42100002.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 42100002
#
# ASCII decay Descriptor: pp -> [Z0/gamma* -> tau+ tau- -> anti-nu_tau e+ nu_e tau-]cc ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Zgtautau=e.py" )
from Configurables import Generation
Generation().EventType = 42100002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Zg_tautau40GeV=e.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 10*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1

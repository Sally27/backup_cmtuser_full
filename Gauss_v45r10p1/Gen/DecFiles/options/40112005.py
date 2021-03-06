# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/40112005.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 40112005
#
# ASCII decay Descriptor: pp -> (A1 -> mu mu {,gamma} {,gamma}) ...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/A1mumu.py" )
from Configurables import Generation
Generation().EventType = 40112005
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/A1_mumu=10GeV.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 2
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 1*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.MotherOfLepton = ["H_30"]
Generation().Special.PythiaHiggsType.NumberOfbquarks = -1
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_30 89 36 0.0 10.0 1.0e-18 A0 36 0.0e+00" ]

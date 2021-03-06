# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/40911011.py generated: Fri, 27 Mar 2015 15:48:14
#
# Event Type: 40911011
#
# ASCII decay Descriptor: pp -> {[W+ -> {mu+ nu_mu, e+ nu_e}]cc, (Z0 -> {mu+ mu-, e+ e-})} (H_10 -> b anti-b)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Higgs.py" )
from Configurables import Generation
Generation().EventType = 40911011
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_bb=mH115GeV,1l,5GeV,1b.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 5*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = 1
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_10 87 25 0.0 115.000 9.400e-026 Higgs0 25 0.000e+000" ]

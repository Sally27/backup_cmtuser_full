# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/40911012.py generated: Fri, 27 Mar 2015 16:10:16
#
# Event Type: 40911012
#
# ASCII decay Descriptor: pp -> {[W+ -> {mu+ nu_mu, e+ nu_e}]cc, (Z0 -> {mu+ mu-, e+ e-})} (H_10 -> b anti-b)
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Higgs.py" )
from Configurables import Generation
Generation().EventType = 40911012
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Higgs_bb=mH120GeV,1l,5GeV,1b.dec"
Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType )
Generation().Special.PythiaHiggsType.NumberOfLepton = 1
from GaudiKernel import SystemOfUnits
Generation().Special.PythiaHiggsType.LeptonPtMin = 5*SystemOfUnits.GeV
Generation().Special.PythiaHiggsType.LeptonIsFromMother = True
Generation().Special.PythiaHiggsType.NumberOfbquarks = 1
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "H_10 87 25 0.0 120.000 9.400e-026 Higgs0 25 0.000e+000" ]

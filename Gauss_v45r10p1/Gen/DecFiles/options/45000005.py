# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/45000005.py generated: Wed, 25 Jan 2017 15:25:22
#
# Event Type: 45000005
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> (u, d, s, c, b) + jet ... )
#
from Configurables import Generation
Generation().EventType = 45000005
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KaplanNeutralino,mN=48GeV,tN=10ps,mH=125GeV.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/Kaplan_mh125mk48.tbl"]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan.py" )
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan_mh125mk48.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHADecayFile = "Kaplan_mh125mk48_10ps.LHdec"
Generation().Special.PythiaProduction.PDecayList = [1000022]

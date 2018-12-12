# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/45000016.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 45000016
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> (u, d, s, c, b) + jet ... )
#
from Configurables import Generation
Generation().EventType = 45000016
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KaplanNeutralino,mN=48GeV,tN=50ps.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/Kaplan_mh114mk48.tbl"]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan.py" )
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan_mh114mk48.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHADecayFile = "Kaplan_mh114mk48_50ps.LHdec"
Generation().Special.PythiaProduction.PDecayList = [1000022]

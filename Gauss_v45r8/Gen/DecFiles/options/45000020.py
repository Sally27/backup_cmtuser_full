# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/45000020.py generated: Fri, 27 Mar 2015 15:48:03
#
# Event Type: 45000020
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> (u, d, s, c, b) + jet ... )
#
from Configurables import Generation
Generation().EventType = 45000020
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/KaplanNeutralino,mN=38GeV,tN=10ps.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/Kaplan_mk38.tbl"]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan.py" )
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Kaplan_mk38.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHADecayFile = "Kaplan_mk38_10ps.LHdec"
Generation().Special.PythiaProduction.PDecayList = [1000022]

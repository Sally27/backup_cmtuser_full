# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/46000030.py generated: Fri, 27 Mar 2015 15:48:10
#
# Event Type: 46000030
#
# ASCII decay Descriptor: pp -> (X -> ~chi_10 -> (l q q, l l l) + jet ... )
#
from Configurables import Generation
Generation().EventType = 46000030
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/BRpVNeutralino_m0600_m12400.dec"
Generation().Special.CutTool = "PythiaLSP"
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().OtherFiles = ["$DECFILESROOT/ppfiles/mSUGRA_m0600_m12400.tbl"]
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/SusyBRpV.py" )
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.SLHASpectrumFile = "mSUGRA_m0600_m12400.LHspc"

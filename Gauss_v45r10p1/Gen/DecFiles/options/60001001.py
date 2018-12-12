# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/60001001.py generated: Wed, 25 Jan 2017 15:25:32
#
# Event Type: 60001001
#
# ASCII decay Descriptor: p H1[0,0] => ?
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Beam1GasVeLo.py" )
from Configurables import Generation
Generation().EventType = 60001001
Generation().SampleGenerationTool = "MinimumBias"
from Configurables import MinimumBias
Generation().addTool( MinimumBias )
Generation().MinimumBias.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/beamGasVelo,1=Hydrogen.dec"
Generation().MinimumBias.CutTool = ""
from Configurables import HijingProduction
Generation().MinimumBias.addTool( HijingProduction )
Generation().MinimumBias.HijingProduction.Commands += [
 "hijinginit frame LAB",
  "hijinginit targ P",
  "hijinginit beam1",
  "hijinginit iat 1",
  "hijinginit izt 1"
]
from Configurables import FlatZSmearVertex
Generation().addTool( FlatZSmearVertex )
Generation().FlatZSmearVertex.BeamDirection = 1
from Configurables import UniformSmearVertex
Generation().addTool( UniformSmearVertex )
Generation().UniformSmearVertex.BeamDirection = 1

# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/20000000.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 20000000
#
# ASCII decay Descriptor: pp => [<Xc>]cc ...
#
from Configurables import Generation
Generation().EventType = 20000000
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_c.dec"
Generation().Inclusive.CutTool = "LHCbAcceptance"
Generation().Inclusive.InclusivePIDList = [ 421, -421, 411, -411, 431, -431, 4122, -4122, 443, 4112, -4112, 4212, -4212, 4222, -4222, 4312, -4312, 4322, -4322, 4332, -4332, 4132, -4132, 4232, -4232, 100443, 441, 10441, 20443, 445, 4214, -4214, 4224, -4224, 4314, -4314, 4324, -4324, 4334, -4334, 4412, -4412, 4414,-4414, 4422, -4422, 4424, -4424, 4432, -4432, 4434, -4434, 4444, -4444, 14122, -14122,  14124, -14124, 100441 ]

# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/10000000.py generated: Fri, 27 Mar 2015 16:10:17
#
# Event Type: 10000000
#
# ASCII decay Descriptor: pp => [<Xb>]cc ...
#
from Configurables import Generation
Generation().EventType = 10000000
Generation().SampleGenerationTool = "Inclusive"
from Configurables import Inclusive
Generation().addTool( Inclusive )
Generation().Inclusive.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_b.dec"
Generation().Inclusive.CutTool = "LHCbAcceptance"
Generation().Inclusive.InclusivePIDList = [ 521, -521, 511, -511, 531, -531, 541, -541, 5122, -5122, 5222, -5222, 5212, -5212, 5112, -5112, 5312, -5312, 5322, -5322, 5332, -5332, 5132, -5132, 5232, -5232 ]

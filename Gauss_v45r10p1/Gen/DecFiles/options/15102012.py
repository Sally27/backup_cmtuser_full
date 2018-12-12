# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15102012.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 15102012
#
# ASCII decay Descriptor: [Lambda_b0 -> p+ pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/Hb2hh.py" )
from Configurables import Generation
Generation().EventType = 15102012
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_ppi=tightCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

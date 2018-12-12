# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15296002.py generated: Fri, 27 Mar 2015 16:10:08
#
# Event Type: 15296002
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda_c+ -> p+ K+ pi-) (Ds- -> K-K+Pi-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15296002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_LambdacDs=DDALITZ,DecProdCut_pCut1600MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

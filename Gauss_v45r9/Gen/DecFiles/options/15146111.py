# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15146111.py generated: Fri, 27 Mar 2015 16:10:10
#
# Event Type: 15146111
#
# ASCII decay Descriptor: [Lambda_b0 -> K+ pi- (Lambda0 -> p+ pi-) (J/psi(1S) -> mu+ mu-)]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15146111
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiLambdaKpi,mm=DecProdCut,pCut1600MeV.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

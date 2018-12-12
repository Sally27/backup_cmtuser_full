# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15266022.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 15266022
#
# ASCII decay Descriptor: [Lambda_b0 -> ( Sigma_c++ -> (Lc+ -> pi+ K- pi+) pi+) pi- pi-]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/TracksInAccWithMinP.py" )
from Configurables import Generation
Generation().EventType = 15266022
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_Sigmac++pipi,pKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "DaughtersInLHCbAndWithMinP"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

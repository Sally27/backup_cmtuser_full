# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11196400.py generated: Fri, 27 Mar 2015 16:10:17
#
# Event Type: 11196400
#
# ASCII decay Descriptor: { [B0 -> (Ds(*)+ -> tau+ nu_tau)   (D(*)- -> pi+ pi- pi- pi0)]cc}
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2XTau.py" )
from Configurables import Generation
Generation().EventType = 11196400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DsD,taunu3pipi0=DecProdCut,tightcut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

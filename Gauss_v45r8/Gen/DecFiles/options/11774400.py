# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11774400.py generated: Fri, 27 Mar 2015 15:48:09
#
# Event Type: 11774400
#
# ASCII decay Descriptor: [[B0] -> (D*(2010)- -> (D- ->  mu- anti-nu_mu) pi0) pi+ pi- pi+ pi0]cc
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/B2XTau.py" )
from Configurables import Generation
Generation().EventType = 11774400
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Dst-3pipi0,munu=DecProdCut,TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "DaughtersInLHCbAndWithDaughAndBCuts"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

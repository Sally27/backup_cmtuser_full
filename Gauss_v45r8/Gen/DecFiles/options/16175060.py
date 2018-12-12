# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/16175060.py generated: Fri, 27 Mar 2015 15:47:57
#
# Event Type: 16175060
#
# ASCII decay Descriptor: [ Xi_bc^+ -> (Lambda_c+ -> p K- pi+)  (J/psi -> mu+ mu-) ]cc
#
from Configurables import Generation
Generation().EventType = 16175060
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "GenXiccProduction"
Generation().PileUpTool = "FixedLuminosityForRareProcess"
from Configurables import GenXiccProduction
Generation().SignalRepeatedHadronization.addTool( GenXiccProduction )
Generation().SignalRepeatedHadronization.GenXiccProduction.BaryonState = "Xi_bc^+"
from Configurables import Gauss
Generation().SignalRepeatedHadronization.GenXiccProduction.BeamMomentum = Gauss().BeamMomentum
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xibc_LambdacJpsi,pKpimm.dec"
Generation().SignalRepeatedHadronization.CutTool = "XiccDaughtersInLHCb"
from Configurables import XiccDaughtersInLHCb
Generation().SignalRepeatedHadronization.addTool( XiccDaughtersInLHCb )
Generation().SignalRepeatedHadronization.XiccDaughtersInLHCb.BaryonState = Generation().SignalRepeatedHadronization.GenXiccProduction.BaryonState

# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/39104100.py generated: Wed, 25 Jan 2017 15:25:30
#
# Event Type: 39104100
#
# ASCII decay Descriptor: [phi -> (K_S0 -> pi+ pi-) (K_S0 -> pi+ pi-)]
#
from Configurables import Generation
Generation().EventType = 39104100
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/phi_KsKs=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 333 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ ^(phi(1020) -> ^(KS0 -> ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-)) ]CC'
tightCut.Cuts      =    {
    '[pi+]cc' : ' goodPi ' ,
    'KS0' : ' goodKs ' ,
    'phi(1020)' : ' goodPhi ' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005 , GTHETA , 0.400 ) ' ,
    'goodPi = ( GPT > 0.225 * GeV ) & (GP > 1.9 * GeV) & inAcc ' ,
    'goodKs = inAcc ' ,
    'goodPhi = (GPT > 0.35 * GeV) & inAcc' ]



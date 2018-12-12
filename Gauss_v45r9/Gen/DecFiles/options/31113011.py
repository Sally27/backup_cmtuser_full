# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/31113011.py generated: Fri, 27 Mar 2015 16:10:07
#
# Event Type: 31113011
#
# ASCII decay Descriptor: [tau- -> mu- mu+ e-]cc
#
from Configurables import Generation
Generation().EventType = 31113011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/tau_mumue=OS,FromB,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 15,-15 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ ^(tau- -> ^mu- ^mu+ ^e-) ]CC'
tightCut.Cuts      =    {
    '[e-]cc'  : ' goodElectron ' ,
    '[mu+]cc'  : ' goodMuon ' , 
    '[tau+]cc' : ' goodTau  ' }
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodElectron = ( GPT > 0.20 * GeV ) & ( GP > 2.0 * GeV ) & inAcc ' ,
    'goodMuon = ( GPT > 0.20 * GeV ) & ( GP > 2.0 * GeV ) & inAcc ' , 
    'goodTau  = ~GHAS (GCHARM, HepMC.ancestors) ' ]



# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/25113006.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 25113006
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ mu- mu+]cc
#
from Configurables import Generation
Generation().EventType = 25113006
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lc_pmumu=OS,DecProdCut_FromD.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]


from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ Lambda_c+ ->  ^p+ ^mu+ ^mu- ]CC'
tightCut.Cuts      =    {
    '[mu+]cc'       : ' goodMuon    ' , 
    '[p+]cc'        : ' goodProton  ' , 
    '[Lambda_c+]cc' : ' goodLambdac ' }
tightCut.Preambulo += [
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodMuon   = ( GPT > 0.2 * GeV ) & ( GP > 2. * GeV ) & inAcc ' , 
    'goodProton = ( GPT > 0.2 * GeV ) & ( GP > 2. * GeV ) & inAcc ' , 
    'goodLambdac  = ~GHAS (GBEAUTY, HepMC.ancestors) ' ]



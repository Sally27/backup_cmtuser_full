# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/15104322.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 15104322
#
# ASCII decay Descriptor: [Lambda_b0 -> (Lambda0 -> p+ pi-) (eta' -> pi+ pi- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15104322
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_etapLambda,pi+pi-g=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]


from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 

tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = 'Lambda_b0 -> ^(eta_prime -> ^pi+ ^pi- ^gamma) ^(Lambda0 -> ^p+ ^pi-)'
tightCut.Cuts      =    {
    '[Lambda_b0]cc': ' goodLb    ' , 
    '[Lambda0]cc'  : ' goodL     ' ,
    '[pi+]cc'      : ' goodPion  ' ,
    '[p+]cc'       : ' goodProton' ,
    '[eta_prime]cc': ' goodEtap  ' }
tightCut.Preambulo += [
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodLb     = ( GPT > 1000 * MeV ) ' ,
    'goodL      = ( GPT > 1000 * MeV ) ' , 
    'goodEtap   = ( GPT > 2000 * MeV ) ' ,
    'goodPion   = ( GPT > 300 * MeV ) & inAcc ' ,
    'goodProton = ( GPT > 300 * MeV ) & inAcc ' ]



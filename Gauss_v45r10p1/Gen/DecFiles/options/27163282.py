# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/27163282.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 27163282
#
# ASCII decay Descriptor: [D_s1(2460)+ -> ( D_s*+ -> (D_s+ -> ( (phi(1020) -> K+ K-) ) pi+ ) gamma) gamma ]cc
#
from Configurables import Generation
Generation().EventType = 27163282
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds2460_Dsstgamma,Dsgamma,KKpi=DecProdCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 20433,-20433 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s1(2460)+ => (D*_s+ => (D_s+ => ( (phi(1020) => ^K+ ^K-) ) ^pi+ ) ^gamma) ^gamma ]CC'
tightCut.Cuts      =    {
    '[K+]cc'         : ' goodKaon ' , 
    '[pi+]cc'        : ' goodPion ' , 
    'gamma'          : ' goodPhoton' } 

tightCut.Preambulo += [
    'inAcc      = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodPion   = ( GPT > 0.25 * GeV ) & ( GP > 1.9 * GeV ) & inAcc ' , 
    'goodPhoton = ( GPT > 0.3  * GeV ) & inAcc' ] 



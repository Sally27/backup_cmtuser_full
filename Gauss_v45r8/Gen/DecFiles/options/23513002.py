# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23513002.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 23513002
#
# ASCII decay Descriptor: [D_s+ -> ( tau+ -> p+ mu+ mu- ) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 23513002
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_taunu,pmm=OS,FromD.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s+ -> ( ^(tau+ -> ^p+ ^mu+ ^mu-) ) nu_tau ]CC'
tightCut.Cuts      =    {
    '[mu+]cc'   : ' goodMuon ' , 
    '[p+]cc'  : ' goodProton ' , 
    '[tau+]cc'  : ' goodTau  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodMuon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodProton = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodTau  = ~GHAS (GBEAUTY, HepMC.ancestors) ' ] 



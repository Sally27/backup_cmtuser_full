# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23513011.py generated: Fri, 27 Mar 2015 16:10:13
#
# Event Type: 23513011
#
# ASCII decay Descriptor: [D_s+ -> ( tau+ -> mu+ e- mu+ ) nu_tau]cc
#
from Configurables import Generation
Generation().EventType = 23513011
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_taunu,mme=SS,FromD,TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s+ -> ( ^(tau+ -> ^mu+ ^mu+ ^e-) ) nu_tau ]CC'
tightCut.Cuts      =    {
    '[e+]cc'   : ' goodElectron ' ,
    '[mu+]cc'   : ' goodMuon ' , 
    '[tau+]cc'  : ' goodTau  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodElectron = ( GPT > 0.20 * GeV ) & ( GP > 2.0 * GeV ) & inAcc ' ,
    'goodMuon = ( GPT > 0.20 * GeV ) & ( GP > 2.0 * GeV ) & inAcc ' , 
    'goodTau  = ~GHAS (GBEAUTY, HepMC.ancestors) ' ] 



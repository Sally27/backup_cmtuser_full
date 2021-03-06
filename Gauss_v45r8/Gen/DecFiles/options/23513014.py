# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23513014.py generated: Fri, 27 Mar 2015 15:48:12
#
# Event Type: 23513014
#
# ASCII decay Descriptor: [D_s+ -> mu+ (phi -> K+ K-) nu_mu]cc
#
from Configurables import Generation
Generation().EventType = 23513014
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phimunu,KK=TightCut,FromD.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[D_s+ => ^(phi(1020) => ^K+ ^K- ) ^mu+ ^nu_mu]CC'
tightCut.Cuts      =    {
    '[K+]cc'   : ' goodKaon ' , 
    '[mu+]cc'   : ' goodMuon ' , 
    '[phi(1020)]cc'  : ' goodphi  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodMuon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodphi  = ~GHAS (GBEAUTY, HepMC.ancestors) ' ] 



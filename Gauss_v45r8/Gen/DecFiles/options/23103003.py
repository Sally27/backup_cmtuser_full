# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/23103003.py generated: Fri, 27 Mar 2015 15:48:04
#
# Event Type: 23103003
#
# ASCII decay Descriptor: [D_s+ => ( phi(1020) => K+ K- ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 23103003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds_phipi,KK=FromB.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[ D_s+ => ( ^(phi(1020) => ^K+ ^K- ) ) ^pi+  ]CC'
tightCut.Cuts      =    {
    '[K+]cc'   : ' goodKaon ' , 
    '[pi+]cc'   : ' goodPion ' , 
    '[phi(1020)]cc'  : ' goodphi  ' } 
tightCut.Preambulo += [
    'inAcc    = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodKaon = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodPion = ( GPT > 0.25 * GeV ) & ( GP > 2.5 * GeV ) & inAcc ' , 
    'goodphi  = GHAS (GBEAUTY, HepMC.ancestors) ' ] 



# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/28102003.py generated: Fri, 27 Mar 2015 16:10:11
#
# Event Type: 28102003
#
# ASCII decay Descriptor: psi(S1S) -> p+ p~-
#
from Configurables import Generation
Generation().EventType = 28102003
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/incl_psi2S,pp=Pt1.8GeV.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 100443 ]
 
from Configurables import LoKi__GenCutTool as GenCutTool 
#
Generation().SignalPlain.addTool( GenCutTool , 'TightCut' ) 
Generation().SignalPlain.TightCut.Decay = "psi(2S) => ^p+ ^p~-"
Generation().SignalPlain.TightCut.Cuts = {
    'p+'  : ' ( GPT > 1.8 * GeV ) & inAcc ',
    'p~-' : ' ( GPT > 1.8 * GeV ) & inAcc '
    }
Generation().SignalPlain.TightCut.Preambulo += [
    'inAcc   = in_range ( 0.010 , GTHETA , 0.400 ) '
    ]


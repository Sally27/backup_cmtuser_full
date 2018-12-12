# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/25103009.py generated: Fri, 27 Mar 2015 16:10:15
#
# Event Type: 25103009
#
# ASCII decay Descriptor: [Lambda_c+ -> p+ (phi(1020) -> K+ K-)]cc
#
from Configurables import Generation
Generation().EventType = 25103009
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Xic_pphi,KK=TightCut,Lifetime6.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 4122,-4122 ]
from Configurables import LHCb__ParticlePropertySvc
LHCb__ParticlePropertySvc().Particles = [ "Lambda_c+  62  4122  1.0  2.468 4.400000e-013 Lambda_c+  4122  0", "Lambda_c~-  63 -4122 -1.0  2.468 4.400000e-013  anti-Lambda_c-  -4122   0." ]

from Configurables import LoKi__GenCutTool as GenCutTool

Generation().SignalPlain.addTool( GenCutTool , 'TightCut' )
Generation().SignalPlain.TightCut.Decay = "[Lambda_c+ => ^p+ ^(phi(1020) => ^K+ ^K-)]CC"
Generation().SignalPlain.TightCut.Preambulo += [
    'from GaudiKernel.SystemOfUnits import ns, GeV, mrad, millimeter',
    'inAcc   = in_range ( 0.010 , GTHETA , 0.400 )',
    'goodLc    = (GPT > 3.9 * GeV) & (GTIME > 0.0006 * ns) & in_range( 2.0 , GY , 4.5 )',
    'goodProton = (GP > 9.9 * GeV)'
    ]
Generation().SignalPlain.TightCut.Cuts = {
    '[p+]cc'        : 'goodProton & inAcc',
    '[K+]cc'        : 'inAcc',
    '[Lambda_c+]cc' : 'goodLc'
    }


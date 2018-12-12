# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/15894301.py generated: Fri, 27 Mar 2015 16:10:12
#
# Event Type: 15894301
#
# ASCII decay Descriptor: {[Lambda_b0 => (D*_s- -> (D_s- ->(phi(1020) -> K+ K-) pi-) gamma) (Lambda_c+ -> Lambda0 nu_mu mu+)]cc}
#
from Configurables import Generation
Generation().EventType = 15894301
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_DsstLc,DsgmunuX=cocktail,DecProdCut.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

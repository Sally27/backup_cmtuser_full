# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/22164112.py generated: Fri, 27 Mar 2015 16:10:14
#
# Event Type: 22164112
#
# ASCII decay Descriptor: [D0 -> (KS0 -> pi+ pi-) (KS0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 22164112
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D0_KSKS=DecProdCut,tightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 421,-421 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
#gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
#tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '[^(D0 ==> ^(KS0 -> ^pi+ ^pi-) ^(KS0 -> ^pi+ ^pi-))]CC'
tightCut.Cuts      =    {
    '[D0]cc'    : ' goodB     ' , 
    'KS0'   : ' goodKs ' , 
    '[pi+]cc'   : ' goodTrack ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.000 , GTHETA , 0.400 ) ' , 
    'goodB     = ( GP > 10 * GeV )   & inAcc            ' , 
    'goodTrack = ( GP >  1.5 * GeV )        ' , 
    'goodKs   = ( GP >  3 * GeV) & (GPT >  100 * MeV ) & inAcc              ' ] 



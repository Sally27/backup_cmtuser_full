# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/23103270.py generated: Fri, 27 Mar 2015 16:10:09
#
# Event Type: 23103270
#
# ASCII decay Descriptor: [D_s+ -> ( eta -> pi+ pi- gamma) K+]cc
#
from Configurables import Generation
Generation().EventType = 23103270
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Ds+_etaK,pipigamma=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 431,-431 ]
                       
                                        
from Configurables import LoKi__GenCutTool 
gen = Generation()                         
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )  
tightCut = gen.SignalPlain.TightCut        
tightCut.Decay     = '^[ D_s+ -> ( eta -> ^pi+ ^pi- ^gamma ) ^K+]CC'  
tightCut.Cuts      =    {                                  
    '[pi+]cc'    : ' inAcc & dauCuts',                     
    '[K+]cc'     : ' inAcc & dauCuts',                    
    '[D_s+]cc'   : 'Dcuts' }                               
tightCut.Preambulo += [                                  
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' ,       
    'dauCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',
    'Dcuts = (GPT > 1000 * MeV)' ]                  


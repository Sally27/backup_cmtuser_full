# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/21103230.py generated: Fri, 27 Mar 2015 16:10:00
#
# Event Type: 21103230
#
# ASCII decay Descriptor: [D- -> pi- (eta' -> pi+ pi- gamma)]cc
#
from Configurables import Generation
Generation().EventType = 21103230
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_pietap,pipig=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ -> ^pi+ ( eta_prime -> ^pi+ ^pi- gamma )]CC'
tightCut.Cuts      =    {
    '[pi+]cc' : ' inAcc & piCuts',
    '[D+]cc'  : 'Dcuts' }
tightCut.Preambulo += [
    'inAcc  = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'piCuts = ( (GPT > 200 * MeV) & ( GP > 600 * MeV))',
    'Dcuts  = (GPT > 1000 * MeV)' ]


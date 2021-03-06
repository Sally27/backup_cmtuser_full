# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/21103420.py generated: Fri, 27 Mar 2015 15:47:56
#
# Event Type: 21103420
#
# ASCII decay Descriptor: [D+ -> ( eta -> pi+ pi- ) pi+]cc
#
from Configurables import Generation
Generation().EventType = 21103420
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/D+_etapi,pipi=TightCut.dec"
Generation().SignalPlain.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalPlain.SignalPIDList = [ 411,-411 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalPlain.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = gen.SignalPlain.TightCut
tightCut.Decay     = '^[ D+ -> ( eta -> ^pi+ ^pi- ) ^pi+]CC'
tightCut.Cuts      =    {
    '[pi+]cc'  : ' inAcc & dauCuts',
    '[D+]cc'   : 'Dcuts' }
tightCut.Preambulo += [
    'inAcc = in_range ( 0.005, GTHETA, 0.400 ) ' , 
    'dauCuts = ( (GPT > 225 * MeV) & ( GP > 1800 * MeV))',
    'Dcuts = (GPT > 900 * MeV)' ]


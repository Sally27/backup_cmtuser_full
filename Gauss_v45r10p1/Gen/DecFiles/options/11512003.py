# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11512003.py generated: Wed, 25 Jan 2017 15:25:27
#
# Event Type: 11512003
#
# ASCII decay Descriptor: [B0 -> (pi+ -> mu+ nu_mu) (pi- -> mu- nu_mu~)]CC
#
from Configurables import Generation
Generation().EventType = 11512003
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_pi+pi-,mm=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

#
from Configurables import LoKi__GenCutTool
gen = Generation()
gen.SignalRepeatedHadronization.setProp('MaxNumberOfRepetitions', 5000 )
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
#
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = '[ Beauty -> ^(pi+ -> ^mu+ nu_mu) ^(pi- -> ^mu- nu_mu~ )]CC'
tightCut.Preambulo += [
    "GVZ = LoKi.GenVertices.PositionZ() " ,
    "from GaudiKernel.SystemOfUnits import meter, GeV" ,
    "decay = in_range ( -1 * meter,            GFAEVX ( GVZ, 100 * meter ),                    10 * meter ) ",
#   "decay = in_range ( -1 * meter , monitor ( GFAEVX ( GVZ, 100 * meter ) , '  decay-Z\n' ) , 10 * meter ) ",
    "inAcc = in_range ( 0.0075, GTHETA, 0.400 ) " , 
]
tightCut.Cuts      =    {
    '[pi+]cc'  : ' decay & inAcc ',
#   '[mu+]cc'  : " 3 * GeV < monitor ( GP , '  mu P\n' )" , 
    '[mu+]cc'  : " 3 * GeV < GP " , 
                        }


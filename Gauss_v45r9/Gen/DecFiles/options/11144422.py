# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/11144422.py generated: Fri, 27 Mar 2015 16:09:58
#
# Event Type: 11144422
#
# ASCII decay Descriptor: [B0 -> (J/psi(1S) -> mu+ mu- ) (omega(782) -> pi+ pi- (pi0 -> gamma gamma))]cc
#
from Configurables import Generation
Generation().EventType = 11144422
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_Jpsiomega,mmpipipi0=TightCutGY.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]

# 
from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 
# 
tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = ' Beauty  -> ^( J/psi(1S) => ^mu+ ^mu-)  ^( omega(782) -> ( pi0 -> ^gamma ^gamma ) ^pi+ ^pi- )'
tightCut.Cuts      =    {
    'omega(782)': ' goodX0    ' ,
    'gamma'     : ' goodGamma ' ,
    '[mu+]cc'   : ' goodMuon  ' , 
    '[pi+]cc'   : ' goodPion  ' , 
    'J/psi(1S)' : ' goodPsi   ' }
tightCut.Preambulo += [  "GY = LoKi.GenParticles.Rapidity()" ]
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'inEcalX   = abs ( GPX / GPZ ) < 4.5 / 12.5      ' , 
    'inEcalY   = abs ( GPY / GPZ ) < 3.5 / 12.5      ' , 
    'goodX0    =   GPT > 2.25 * GeV                  ' , 
    'goodMuon  = ( GPT > 500  * MeV ) & ( GP > 6 * GeV )     & inAcc   ' , 
    'goodPion  = ( GPT > 100  * MeV )                        & inAcc   ' , 
    'goodGamma = ( 0 < GPZ ) & ( 150 * MeV < GPT ) & inEcalX & inEcalY ' ,
    'goodPsi   = ( GPT > 500  * MeV ) & in_range ( 1.8 , GY , 4.5 )    ' ]



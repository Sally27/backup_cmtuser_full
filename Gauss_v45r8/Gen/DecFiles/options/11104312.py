# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/11104312.py generated: Fri, 27 Mar 2015 15:48:05
#
# Event Type: 11104312
#
# ASCII decay Descriptor: [B0 -> (eta' -> pi+ pi- gamma) (K_S0 -> pi+ pi-)]cc
#
from Configurables import Generation
Generation().EventType = 11104312
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_etapKs,pi+pi-g=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool 
gen = Generation() 
gen.SampleGenerationTool="SignalRepeatedHadronization"
gen.SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' ) 

tightCut = gen.SignalRepeatedHadronization.TightCut
tightCut.Decay     = 'B0 -> ^(eta_prime -> ^pi+ ^pi- ^gamma) ^(KS0 -> ^pi+ ^pi-)'
tightCut.Cuts      =    {
    '[B0]cc'       : ' goodB     ' , 
    '[KS0]cc'      : ' goodKS    ' ,
    '[pi+]cc'      : ' goodTrack ' ,
    '[eta_prime]cc': ' goodEtap  ' }
tightCut.Preambulo += [
    'inAcc     = in_range ( 0.005 , GTHETA , 0.400 ) ' , 
    'goodB     = ( GPT > 1500 * MeV ) ' ,
    'goodKS    = ( GPT > 1200 * MeV ) ' ,
    'goodEtap  = ( GPT > 2000 * MeV ) ' ,
    'goodTrack = ( GPT > 300 * MeV ) & inAcc ' ]



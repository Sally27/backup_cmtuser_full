# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/11198021.py generated: Wed, 25 Jan 2017 15:25:36
#
# Event Type: 11198021
#
# ASCII decay Descriptor: [B0 -> (D*+ -> (D0 -> K- pi+) pi+) (D*- -> (anti-D0 -> K+ pi-) pi-) K+ pi-]cc
#
from Configurables import Generation
Generation().EventType = 11198021
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bd_DstDstKpi,D0Pi,D0Pi=TightCut.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 511,-511 ]


from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool( LoKi__GenCutTool , 'TightCut')
acceptance = Generation().SignalRepeatedHadronization.TightCut
acceptance.Decay = "[B0 => ^(D*(2010)+ => ^(D0 => ^K- ^pi+) pi+ )  ^(D*(2010)- => ^(D~0 => ^K+ ^pi-) ^pi-) ^K+ ^pi-  ]CC"
acceptance.Preambulo += [ "from LoKiCore.functions import in_range",
                          "from GaudiKernel.SystemOfUnits import  GeV, mrad",
                          "inAcc = ( in_range( 5*mrad, GTHETA, 400*mrad) ) ",
                          "goodPi_Dau = (GNINTREE( ('pi+'==GABSID) & inAcc, 1)  >0.5 )",
                          "goodK_Dau  = (GNINTREE( ('K+'==GABSID)  & inAcc ,1) > 0.5 )"
                        ]
acceptance.Cuts = {
    '[D0]cc'       : 'goodPi_Dau & goodK_Dau',
    '[D~0]cc'      : 'goodPi_Dau & goodK_Dau',
    '[K+]cc'       : 'inAcc' }



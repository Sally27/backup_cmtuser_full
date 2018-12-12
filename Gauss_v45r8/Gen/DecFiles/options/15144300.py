# file /home/hep/ss4314/cmtuser/Gauss_v45r8/Gen/DecFiles/options/15144300.py generated: Fri, 27 Mar 2015 15:48:10
#
# Event Type: 15144300
#
# ASCII decay Descriptor: [Lambda_b0 -> (J/psi -> mu+ mu-) (Sigma0 -> (Lambda0 -> p+ pi-) gamma)]cc
#
from Configurables import Generation
Generation().EventType = 15144300
Generation().SampleGenerationTool = "SignalPlain"
from Configurables import SignalPlain
Generation().addTool( SignalPlain )
Generation().SignalPlain.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Lb_JpsiSigma0,mm,Lambdagamma,ppi=phsp,DecProd.dec"
Generation().SignalPlain.CutTool = "LHCbAcceptance"
Generation().SignalPlain.SignalPIDList = [ 5122,-5122 ]

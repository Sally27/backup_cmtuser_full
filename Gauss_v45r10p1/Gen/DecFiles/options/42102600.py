# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42102600.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 42102600
#
# ASCII decay Descriptor: pp -> [Z -> (omega(782) -> pi+ pi- (pi0 -> gamma gamma)) gamma]cc ...
#
from Configurables import Generation
Generation().EventType = 42102600
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_Omegagamma=NoCut.dec"
Generation().Special.CutTool = ""

# Stop pile-up generation.
Generation().PileUpTool = "FixedLuminosityForRareProcess"

# Pythia8 options.
from Gaudi.Configuration import importOptions
from Configurables import Pythia8Production
importOptions('$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py')
Generation().Special.addTool(Pythia8Production)
Generation().Special.Pythia8Production.Commands += [
    'WeakSingleBoson:ffbar2gmZ = on',
    'WeakZ0:gmZmode = 2',
    '23:mayDecay = false']



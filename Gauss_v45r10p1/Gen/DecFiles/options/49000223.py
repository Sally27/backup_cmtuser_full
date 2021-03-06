# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/49000223.py generated: Wed, 25 Jan 2017 15:25:29
#
# Event Type: 49000223
#
# ASCII decay Descriptor: pp -> (gamma + X) ...
#
from Configurables import Generation
Generation().EventType = 49000223
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/gamma=pt20,pt50GeV.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twoToTwoInAcc"

# Switch off all Pythia 6 and Pythia 8 options.
from Gaudi.Configuration import importOptions
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

# Pythia 6 options.
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 10",              # Hard process.
    "pysubs ckin 3 20.0",          # Minimum pT.
    "pysubs ckin 4 50.0"]          # Maximum pT.

# Pythia 8 options.
from Configurables import Pythia8Production
Generation().Special.addTool( Pythia8Production )
Generation().Special.Pythia8Production.Commands += [
    "PromptPhoton:all = on",       # Hard process.
    "PhaseSpace:pTHatMin = 20.0",  # Minimum pT.
    "PhaseSpace:pTHatMax = 50.0"]  # Maximum pT.

# Cuts.
# WARNING: this cut is based on the Pythia 8 event record structure
# and consequently is both fragile and generator specific.
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twoToTwoInAcc" )
twoToTwoInAcc = Generation().twoToTwoInAcc
twoToTwoInAcc.Code = "( count( out1 ) == 1 ) | ( count( out2 ) == 1 )"
twoToTwoInAcc.Preambulo += [
    "from GaudiKernel.SystemOfUnits import GeV, mrad",
    "out1 = ( ( GBARCODE == 5 ) & ( GABSID == 22 ) "
    "& ( GTHETA < 400.0*mrad ) & ( GPT > 5.0*GeV ) )",
    "out2 = ( ( GBARCODE == 6 ) & ( GABSID == 22 ) "
    "& ( GTHETA < 400.0*mrad ) & ( GPT > 5.0*GeV ) )"]

# Keep 2 -> 2 hard process in MCParticles.
from Configurables import GenerationToSimulation
GenerationToSimulation("GenToSim").KeepCode = (
    "( GBARCODE >= 1 ) & ( GBARCODE <= 6 )")


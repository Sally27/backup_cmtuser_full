# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/49000002.py generated: Wed, 25 Jan 2017 15:25:33
#
# Event Type: 49000002
#
# ASCII decay Descriptor: pp -> (jet + jet) ...
#
from Configurables import Generation
Generation().EventType = 49000002
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "Pythia8Production"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/dijet=udsg,pt15,pt20GeV.dec"
Generation().Special.CutTool = ""
Generation().FullGenEventCutTool = "LoKi::FullGenEventCut/twoToTwoInAcc"

# Switch off all Pythia 6 and Pythia 8 options.
from Gaudi.Configuration import importOptions
importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

# Pythia 6 options.
from Configurables import PythiaProduction
Generation().Special.addTool( PythiaProduction )
Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 1",               # Hard process.
    "pysubs ckin 3 15.0",          # Minimum pT.
    "pysubs ckin 4 20.0"]          # Maximum pT.

# Pythia 8 options.
from Configurables import Pythia8Production
Generation().Special.addTool( Pythia8Production )
Generation().Special.Pythia8Production.Commands += [
    "HardQCD:all = on",            # Hard process.
    "PhaseSpace:pTHatMin = 15.0",  # Minimum pT.
    "PhaseSpace:pTHatMax = 20.0"]  # Maximum pT.

# Cuts.
# WARNING: this cut is based on the Pythia 8 event record structure
# and consequently is both fragile and generator specific.
from Configurables import LoKi__FullGenEventCut
Generation().addTool( LoKi__FullGenEventCut, "twoToTwoInAcc" )
twoToTwoInAcc = Generation().twoToTwoInAcc
twoToTwoInAcc.Code = "( count( out1 ) == 1 ) & ( count( out2 ) == 1 )"
twoToTwoInAcc.Preambulo += [
    "from GaudiKernel.SystemOfUnits import GeV, mrad",
    "out1 = ( ( GBARCODE == 5 ) "
    "& ( GTHETA < 400.0*mrad ) & ( GPT > 15.0*GeV ) )",
    "out2 = ( ( GBARCODE == 6 ) "
    "& ( GTHETA < 400.0*mrad ) & ( GPT > 15.0*GeV ) )"]

# Keep 2 -> 2 hard process in MCParticles.
from Configurables import GenerationToSimulation
GenerationToSimulation("GenToSim").KeepCode = (
    "( GBARCODE >= 1 ) & ( GBARCODE <= 6 )")


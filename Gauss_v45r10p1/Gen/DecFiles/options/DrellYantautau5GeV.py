# Pythia options for Z/gamma->tautau 42102012
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction  )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [
    "pysubs msel 11" ,
    "pysubs ckin 1 5",  # low Z/gamma mass cut
    "pypars mstp 43 3" ,
    "pydat3 mdme 162 1 0" ,
    "pydat3 mdme 163 1 0" ,
    "pydat3 mdme 164 1 0" ,
    "pydat3 mdme 165 1 0" ,
    "pydat3 mdme 166 1 0" ,
    "pydat3 mdme 167 1 0" ,
    "pydat3 mdme 168 1 0" ,
    "pydat3 mdme 169 1 0" ,
    "pydat3 mdme 170 1 0" ,
    "pydat3 mdme 171 1 0" ,
    "pydat3 mdme 172 1 1" ,
    "pydat3 mdme 173 1 0" ,
    "pydat3 mdme 174 1 0" ,
    "pydat3 mdme 175 1 0" ,
    "pydat3 mdme 176 1 0" ,
    "pydat3 mdme 177 1 0" ,
    "pydat3 mdme 178 1 0" ,
    "pydat3 mdme 179 1 0" ,
    "pydat3 mdme 180 1 0" ,
    "pydat3 mdme 181 1 0" ,
    "pydat3 mdme 182 1 0" ,
    "pydat3 mdme 183 1 0" ,
    "pydat3 mdme 184 1 0" ,
    "pydat3 mdme 185 1 0" ,
    "pydat3 mdme 186 1 1" ,
    "pydat3 mdme 187 1 0" ,
    "pydat3 mdme 188 1 0" ,
    "pydat3 mdme 189 1 0" ,
]


Generation().Special.Pythia8Production.Commands += [
  "WeakSingleBoson:ffbar2gmZ = on", # Z0/gamma* production
  "PhaseSpace:mHatMin = 5.",        # constrain inv mass
  "23:mMin = 5.",                   # min mass of Z0 in GeV
  "23:onMode = off",                # turn it off
  "23:onIfMatch = 15 -15",          # turn it on for the decay to tau final state only
]

Generation().Special.CutTool = "PythiaHiggsType"
from Configurables import PythiaHiggsType
Generation().Special.addTool( PythiaHiggsType ) 
Generation().Special.PythiaHiggsType.TypeOfLepton = [ "tau+" ]
# Allow Pythia to handle tau decays (not EvtGen through TAUOLA).
Generation().Special.DecayTool = ""


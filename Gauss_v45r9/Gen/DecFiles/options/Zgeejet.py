# Pythia options for Z/r*->eejet 42122021 with invariant mass cut of 40GeV
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [ "pysubs msel 13" , #Z0+jet production
                                                    "pypars mstp 43 3" , #Z0/gamma* interference
                                                    "pydat3 mdme 174 1 0" ,
                                                    "pydat3 mdme 175 1 0" ,
                                                    "pydat3 mdme 176 1 0" ,
                                                    "pydat3 mdme 177 1 0" ,
                                                    "pydat3 mdme 178 1 0" ,
                                                    "pydat3 mdme 179 1 0" ,
                                                    "pydat3 mdme 180 1 0" ,
                                                    "pydat3 mdme 181 1 0" ,
                                                    "pydat3 mdme 182 1 1" , #Z0-->e+ e-
                                                    "pydat3 mdme 183 1 0" ,
                                                    "pydat3 mdme 184 1 0" ,
                                                    "pydat3 mdme 185 1 0" ,
                                                    "pydat3 mdme 186 1 0" ,
                                                    "pydat3 mdme 187 1 0" ,
                                                    "pydat3 mdme 188 1 0" ,
                                                    "pydat3 mdme 189 1 0"
                                                    ]
Generation().Special.Pythia8Production.Commands += [
    "SpaceShower:rapidityOrder = off", #pT ordering!
    "WeakBosonAndParton:qqbar2gmZg = on", #q qbar -> gamma^*/Z^0 g
    "WeakBosonAndParton:qg2gmZq = on", #q g -> gamma^*/Z^0 q
    "23:mMin = 40.", #min mass of Z0 in GeV
    "TimeShower:mMaxGamma = 40.", #max inv mass in photon conversion
    "PhaseSpace:mHatMin = 40.", #constrain dielectron inv mass to be 40 GeV
    "23:onMode = off", #turn it off
    "23:onIfMatch = 11 -11" # turn it on for the decay to e final state only
    ]

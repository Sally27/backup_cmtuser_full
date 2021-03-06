# Pythia options for Z->gmumu with PHOTOS 42112003
from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import Special, PythiaProduction, Pythia8Production

Generation().addTool( Special )
Generation().Special.addTool( PythiaProduction )
Generation().Special.addTool( Pythia8Production )

Generation().Special.PythiaProduction.Commands += [ "pysubs msel 11" ,
                                                    "pypars mstp 43 3" ,
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
                                                    "pydat3 mdme 184 1 1" ,
                                                    "pydat3 mdme 185 1 0" ,
                                                    "pydat3 mdme 186 1 0" ,
                                                    "pydat3 mdme 187 1 0" ,
                                                    "pydat3 mdme 188 1 0" ,
                                                    "pydat3 mdme 189 1 0"
                                                    ]

Generation().Special.Pythia8Production.Commands += [
                                                     "PartonLevel:FSR=off",
                                                     "WeakSingleBoson:ffbar2gmZ = on", #Z0/gamma* production
                                                     "23:mMin = 40.", #min mass of Z0 in GeV
                                                     "TimeShower:mMaxGamma = 40.", #max inv mass in photon conversion
                                                     "PhaseSpace:mHatMin = 40.", #constrain dimuon inv mass to be 40 GeV
                                                     "23:onMode = off", #turn it off
                                                     "23:onIfMatch = 13 -13" # turn it on for the decay to mu final state only
                                                     ]

def appendPhotos():
  from Configurables import ApplyPhotos
  GaudiSequencer( "GeneratorSlotMainSeq" ).Members += [ ApplyPhotos( ) ]
  ApplyPhotos().PDGId = [ 23 ] 
  
appendPostConfigAction(appendPhotos)

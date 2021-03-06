from Configurables import Generation
from Gaudi.Configuration import *

Generation().PileUpTool = "FixedLuminosityForRareProcess"

importOptions( "$DECFILESROOT/options/SwitchOffAllPythiaProcesses.py" )

from Configurables import SignalPlain, PythiaProduction

Generation().addTool( SignalPlain )
Generation().SignalPlain.addTool( PythiaProduction )

Generation().SignalPlain.PythiaProduction.Commands += [
    "pysubs msel 0" ,
    "pysubs msub 461 0" ,
    "pysubs msub 462 0" ,
    "pysubs msub 463 0" ,
    "pysubs msub 464 0" ,
    "pysubs msub 465 0" ,
    "pysubs msub 466 0" ,
    "pysubs msub 467 0" ,
    "pysubs msub 468 0" ,
    "pysubs msub 469 0" ,
    "pysubs msub 470 0" ,
    "pysubs msub 471 0" ,
    "pysubs msub 473 0" ,
    "pysubs msub 474 0" ,
    "pysubs msub 475 0" ,
    "pysubs msub 476 0" ,
    "pysubs msub 477 0" ,
    "pysubs msub 478 0" ,
    "pysubs msub 479 0" ,
    "pysubs msub 481 1" ,
    "pysubs msub 482 1" ,
    "pysubs msub 483 1" ,
    "pysubs msub 484 1"
]

Generation().SignalPlain.SignalPIDList = [ 100553 ]

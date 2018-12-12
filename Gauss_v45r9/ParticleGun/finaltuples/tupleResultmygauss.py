
from Configurables import (
    DaVinci,
    EventSelector,
    PrintMCTree,
    MCDecayTreeTuple
)
from DecayTreeTuple.Configuration import *

"""Configure the variables below with:
decay: Decay you want to inspect, using 'newer' LoKi decay descriptor syntax,
decay_heads: Particles you'd like to see the decay tree of,
datafile: Where the file created by the Gauss generation phase is, and
year: What year the MC is simulating.
"""

import os
ls = os.listdir('.')
ls = [x for x in ls if x.endswith('.xgen')]
sort = [(x, os.path.getmtime(x)) for x in ls]
sort.sort(key=lambda x: x[1])



# https://twiki.cern.ch/twiki/bin/view/LHCb/FAQ/LoKiNewDecayFinders
decay = "[B+ => ^mu+ ^mu- ^(K*(892)+ => ^mu+ ^nu_mu)]CC" #,(B- => ^mu- ^mu+ ^(K*- => ^K- ^pi0))]"
decay_heads = ["B+","B-"]
datafile = sort[-1][0]
year = 2012

# For a quick and dirty check, you don't need to edit anything below here.
##########################################################################

# Create an MC DTT containing any candidates matching the decay descriptor
import sys, os
from DaVinci.Configuration import *
from Gaudi.Configuration import *
from Configurables import MCTupleToolKinematic, MCTupleToolHierarchy, TupleToolMCTruth, TupleToolMCBackgroundInfo

mctuple = MCDecayTreeTuple("MCDecayTreeTuple")
mctuple.Decay = decay
mctuple.ToolList = [
    "MCTupleToolHierarchy",
    "LoKi::Hybrid::MCTupleTool/LoKi_Photos",
    "TupleToolMCTruth"
     ]


# Add a 'number of photons' branch
#mctuple.addTupleTool(TupleToolMCTruth)
mctuple.addTupleTool("MCTupleToolKinematic").Verbose = True
mctuple.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Photos").Variables = {
    "nPhotos": "MCNINTREE(('gamma' == MCABSID))"
}

# Print the decay tree for any particle in decay_heads
printMC = PrintMCTree()
printMC.ParticleNames = decay_heads

# Name of the .xgen file produced by Gauss
EventSelector().Input = ["DATAFILE='{0}' TYP='POOL_ROOTTREE' Opt='READ'".format(datafile)]

# Configure DaVinci
DaVinci().TupleFile = "playagain.root"
DaVinci().Simulation = True
DaVinci().Lumi = False
DaVinci().DataType = str(year)
#DaVinci().UserAlgorithms = [printMC, mctuple]
DaVinci().UserAlgorithms = [mctuple]

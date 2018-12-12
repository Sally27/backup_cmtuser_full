from Configurables import DaVinci
from Configurables import EventSelector
from Configurables import PrintMCTree
from Configurables import MCDecayTreeTuple
from DecayTreeTuple.Configuration import *

import os
ls = os.listdir('.')
ls = [x for x in ls if x.endswith('.xgen')]
sort = [(x, os.path.getmtime(x)) for x in ls]
sort.sort(key=lambda x: x[1])


# https://twiki.cern.ch/twiki/bin/view/LHCb/FAQ/LoKiNewDecayFinders
decay = "[B0 => ^(K*(892)0 => ^K+ ^pi-) ^(H_10 => ^mu+ ^mu-)]CC"
#decay = "[B+ => ^K+ ^(H_10 => ^mu+ ^mu-)]CC"
decay_heads = ["B0", "B~0"]
datafile = sort[-1][0]
year = 2012

# For a quick and dirty check, you don't need to edit anything below here.
##########################################################################

# Create an MC DTT containing any candidates matching the decay descriptor
mctuple = MCDecayTreeTuple("MCDecayTreeTuple")
mctuple.Decay = decay
mctuple.ToolList = [
        "MCTupleToolHierarchy",
        "LoKi::Hybrid::MCTupleTool/LoKi_Photos"
]
# Add a 'number of photons' branch
mctuple.addTupleTool("MCTupleToolKinematic").Verbose = True
mctuple.addTupleTool("LoKi::Hybrid::TupleTool/LoKi_Photos").Variables = {
        "nPhotos": "MCNINTREE(('gamma' == MCABSID))"
}
#mctuple.Branches = {
    #'Kstar' : "[B0 => ^(K*(892)0 ==> K+ pi-) (Higgs0 ==> mu+ mu-)]CC",
    #'K' : "[B0 => (K*(892)0 ==> ^K+ pi-) (Higgs0 ==> mu+ mu-)]CC",
    #'pi' : "[B0 => (K*(892)0 ==> K+ ^pi-) (Higgs0 ==> mu+ mu-)]CC",
    #'x' : "[B0 => (K*(892)0 ==> K+ ^pi-) ^(Higgs0 ==> mu+ mu-)]CC",
#}

# Print the decay tree for any particle in decay_heads
printMC = PrintMCTree()
printMC.ParticleNames = decay_heads

# Name of the .xgen file produced by Gauss
EventSelector().Input = ["DATAFILE='{0}' TYP='POOL_ROOTTREE' Opt='READ'".format(datafile)]

# Configure DaVinci
DaVinci().TupleFile = "DVntuple.root"
DaVinci().Simulation = True
DaVinci().Lumi = False
DaVinci().DataType = str(year)
#DaVinci().UserAlgorithms = [printMC, mctuple]
DaVinci().UserAlgorithms = [mctuple]

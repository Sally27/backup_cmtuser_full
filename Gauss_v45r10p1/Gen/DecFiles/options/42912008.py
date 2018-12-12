# file /home/hep/ss4314/cmtuser/Gauss_v45r10p1/Gen/DecFiles/options/42912008.py generated: Wed, 25 Jan 2017 15:25:17
#
# Event Type: 42912008
#
# ASCII decay Descriptor: pp -> (Z-> mu mu) (b b~)...
#
from Gaudi.Configuration import *
importOptions( "$DECFILESROOT/options/DiJetbbmasscut.py" )
from Configurables import Generation
Generation().EventType = 42912008
Generation().SampleGenerationTool = "Special"
from Configurables import Special
Generation().addTool( Special )
Generation().Special.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Z_mumubb=MassCut_AlpGen.dec"
Generation().Special.CutTool = ""

Generation.AlpGenDict = {
'alpgen_nevxiter' : 100000,
'alpgen_niter' : 2,
'alpgen_nwgtev' : 1000000,
'alpgen_FileLabel' : "zbb",
'alpgen_njets' : 0, #number of light jets
'alpgen_etabmin' : 1.596,
'alpgen_ptbmin' : 3.0,
'alpgen_drbmin' : 0.1,
'alpgen_etabmax' : 10.0,
'alpgen_eta1lmin' : 1.596,
'alpgen_ptlmin' : 10.0,
'alpgen_drlmin' : 0.,
'alpgen_etalmax' : 10.0,
'alpgen_izdecmode' : 2,
'alpgen_ndns' : 9,
}



# file /home/hep/ss4314/cmtuser/Gauss_v45r9/Gen/DecFiles/options/12165113.py generated: Fri, 27 Mar 2015 16:10:12
#
# Event Type: 12165113
#
# ASCII decay Descriptor: [B+ -> (D~0 -> (KS0 -> pi+ pi-) K+ pi-) pi+]cc
#
from Configurables import Generation
Generation().EventType = 12165113
Generation().SampleGenerationTool = "SignalRepeatedHadronization"
from Configurables import SignalRepeatedHadronization
Generation().addTool( SignalRepeatedHadronization )
Generation().SignalRepeatedHadronization.ProductionTool = "PythiaProduction"
from Configurables import ToolSvc
from Configurables import EvtGenDecay
ToolSvc().addTool( EvtGenDecay )
ToolSvc().EvtGenDecay.UserDecayFile = "$DECFILESROOT/dkfiles/Bu_D0pi,KSK-pi+=TightCut,PHSP.dec"
Generation().SignalRepeatedHadronization.CutTool = "LoKi::GenCutTool/TightCut"
Generation().SignalRepeatedHadronization.SignalPIDList = [ 521,-521 ]

#
from Configurables import LoKi__GenCutTool
from Gauss.Configuration import *
Generation().SignalRepeatedHadronization.addTool ( LoKi__GenCutTool , 'TightCut' )
tightCut = Generation().SignalRepeatedHadronization.TightCut
tightCut.Decay     = '^[B+ -> ^(D~0 => ^(KS0 => ^pi+ ^pi-) ^K+ ^pi-) ^pi+]CC'
tightCut.Preambulo += [
    'GVZ = LoKi.GenVertices.PositionZ() ' ,
    'from GaudiKernel.SystemOfUnits import millimeter',
    'inAcc        = (in_range (0.005, GTHETA, 0.400))',
    'goodB        = (GP > 55000 * MeV) & (GPT > 5000 * MeV) & (GTIME > 0.135 * millimeter)',
    'goodD        = (GP > 25000 * MeV) & (GPT > 2500 * MeV)',
    'goodKS       = (GFAEVX(abs(GVZ), 0) < 2500.0 * millimeter)',
    'goodDDaugPi  = (GNINTREE (("pi+" == GABSID) & (GP > 2000 * MeV) & inAcc, 4) > 2.5)',
    'goodDDaugK  = (GNINTREE (("K+" == GABSID) & (GP > 2000 * MeV) & inAcc, 4) > 0.5)',
    'goodKsDaugPi = (GNINTREE (("pi+" == GABSID) & (GP > 2000 * MeV) & inAcc, 4) > 1.5)',
    'goodBachPi   = (GNINTREE (("pi+" == GABSID) & (GP > 5000 * MeV) & (GPT > 500 * MeV) & inAcc, 1) > 0.5)',
]
tightCut.Cuts      =    {
    '[B+]cc'         : 'goodB  & goodBachPi',
    '[D0]cc'         : 'goodD  & goodDDaugPi & goodDDaugK',
    '[KS0]cc'        : 'goodKS & goodKsDaugPi',
    '[pi+]cc'        : 'inAcc',
    '[K+]cc'        : 'inAcc'
    }


# Ad-hoc particle gun code

from Configurables import ParticleGun
pgun = ParticleGun("ParticleGun")
pgun.SignalPdgCode = 521
pgun.DecayTool = "EvtGenDecay"
pgun.GenCutTool = "DaughtersInLHCb"

from Configurables import FlatNParticles
pgun.NumberOfParticlesTool = "FlatNParticles"
pgun.addTool( FlatNParticles , name = "FlatNParticles" )

from Configurables import MomentumSpectrum
pgun.ParticleGunTool = "MomentumSpectrum"
pgun.addTool( MomentumSpectrum , name = "MomentumSpectrum" )
pgun.MomentumSpectrum.PdgCodes = [ 521,-521 ]
pgun.MomentumSpectrum.InputFile = "$PGUNSDATAROOT/data/Ebeam4000GeV/MomentumSpectrum_521.root"
pgun.MomentumSpectrum.BinningVariables = "pteta"
pgun.MomentumSpectrum.HistogramPath = "h_pteta"

from Configurables import BeamSpotSmearVertex
pgun.addTool(BeamSpotSmearVertex, name="BeamSpotSmearVertex")
pgun.VertexSmearingTool = "BeamSpotSmearVertex"
pgun.EventType = 12165113

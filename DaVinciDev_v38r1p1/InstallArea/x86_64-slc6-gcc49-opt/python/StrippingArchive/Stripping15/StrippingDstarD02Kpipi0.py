#######################################################################
#
# Options for pre-selecting prompt D*->D(KPiPi0)Pi events, favoured and suppressed mode
#
# @author Andrea Contu, University of Oxford
# @date 2010-01-22
#
# Converted to LineBuilder by Anton Poluektov, 25/02/2010
# 
########################################################################                   
__author__ = 'Andrea Contu'
__date__ = '04/10/2010'
__version__ = '$Revision: 1.5 $'

from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles, ConjugateNeutralPID
from PhysSelPython.Wrappers import Selection, DataOnDemand, MergedSelection
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder, checkConfig
from StandardParticles import ( StdNoPIDsPions,
                                StdNoPIDsKaons,
                                StdLooseMergedPi0,
                                StdLooseResolvedPi0 )

name = "DstarD2Kpipi0"

config = {
  "RSPrescale" : 0.25, 
  "WSPrescale" : 0.0025
}

class DstarD02Kpipi0Conf(LineBuilder) : 

    __configuration_keys__ = ("RSPrescale", "WSPrescale")

    def __init__(self, name, config) : 

	LineBuilder.__init__(self, name, config)

	d0 = makeD02kpipi0(name)
	
	d0conj = ConjugateNeutralPID()
	d0ws = Selection("D0WSFor" + name, Algorithm = d0conj, RequiredSelections = [ d0 ] )
	
	dstar = makeDstar2Dpi(name, d0)
	dstarws = makeDstar2Dpi(name, d0ws)

	lineRS = StrippingLine(name + "RS"
               , prescale = config["RSPrescale"]
               , selection = dstar
               )

	lineWS = StrippingLine(name + "WS"
               , prescale = config["WSPrescale"]
               , selection = dstarws
               )
	
	self.registerLine( lineRS )
	self.registerLine( lineWS )


def makeD02kpipi0(name) : 

    pi0sel = MergedSelection("Pi0For" + name, RequiredSelections = [ StdLooseMergedPi0, StdLooseResolvedPi0 ] )

    str_D0_ChargedDau="(PT>500*MeV) & (P>5*GeV) & (MIPCHI2DV(PRIMARY)>4) & (TRCHI2DOF<5)"
    str_D0_Pi0="(PT>800*MeV) & (P>5*GeV)"
    str_D0_CombCuts="(ADAMASS('D0')<200*MeV) & (ADOCA(1,2) < 1.5) & (AHASCHILD(((ABSID == 'K+') | (ABSID == 'pi+')) & (MIPCHI2DV(PRIMARY)>40)))"
    str_D0_MotherCuts="(BPVDIRA>0.9) & (PT>2.5*GeV) & (VFASPF(VCHI2/VDOF)<10) & (BPVVDCHI2>36)"
    str_D0_DecayDescriptor_RS="[D0 -> K- pi+ pi0]cc"
    str_D0_Sidebands="200*MeV"

    d0 = CombineParticles()
    d0.DecayDescriptor = str_D0_DecayDescriptor_RS
    d0.DaughtersCuts = { "K-"  : str_D0_ChargedDau+' & ((PPINFO(LHCb.ProtoParticle.RichDLLk,-1000))>0)',
                         "pi+" : str_D0_ChargedDau+' & ((PPINFO(LHCb.ProtoParticle.RichDLLk,-1000))<0)',
                         "pi0" : str_D0_Pi0}
    d0.CombinationCut = str_D0_CombCuts
    d0.MotherCut = str_D0_MotherCuts

    return Selection("D02Kpipi0For" + name, 
                     Algorithm = d0, 
                     RequiredSelections = [ pi0sel, StdNoPIDsPions, StdNoPIDsKaons ] )

def makeDstar2Dpi(name, dsel) : 
    
    str_DStar_SlowPiCuts="(PT>170*MeV) & (BPVIP()<0.5*mm)"
    str_DStar_CombCuts="(ADAMASS('D*(2010)+')<200*MeV)"
    str_DStar_MotherCuts="(PT>3*GeV) & ((M-M2)>(145.5-10)*MeV) & ((M-M2)<(145.5+20)*MeV)  & (VFASPF(VCHI2/VDOF)<10) & (BPVIPCHI2()<100)"
    
    dstar = CombineParticles()
    dstar.DecayDescriptor = "[D*(2010)+ -> pi+ D0]cc"
    dstar.DaughtersCuts = { "D0" : "(ALL)",
                            "pi+" : str_DStar_SlowPiCuts}
    dstar.CombinationCut = str_DStar_CombCuts
    dstar.MotherCut = str_DStar_MotherCuts
    
    return Selection("Dstar2DpiWith" + dsel.name() + "For" + name, 
                     Algorithm = dstar, 
                     RequiredSelections = [StdNoPIDsPions, dsel] )

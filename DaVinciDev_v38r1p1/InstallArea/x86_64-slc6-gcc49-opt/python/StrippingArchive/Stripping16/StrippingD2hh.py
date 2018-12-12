# $Id: StrippingBs2JpsiPhiPrescaledAndDetatched.py,v 1.1 2010-06-30 12:53:17 jpalac Exp $
__author__ = ['Marco Gersabeck']
__date__ = '21/02/2011'
__version__ = '$Revision: 1.1 $'

'''
This file contains stripping lines for time-dependent two-body charm analyses of mixing, yCP, and A_Gamma
'''
from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import CombineParticles
from PhysSelPython.Wrappers import Selection
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from StandardParticles import StdAllNoPIDsKaons, StdAllNoPIDsPions

default_config = { 'DaugPtMin': 800.,
           'DaugPtMax': 1500.,
           'DaugP': 5000.,
           'DaugIPChi2': 9.,
           'DaugTrkChi2': 3.,
           'HighPIDK': 5.,
           'LowPIDK': 0.,
           'D0Pt': 2000.,
           'D0MassWindowCentre': 1865.,
           'D0MassWindowWidth': 100.,
           'D0PiPiMassWindowWidthLow':  -75.,
           'D0PiPiMassWindowWidthHigh': 100.,
           'D0KKMassWindowWidthLow': -100.,
           'D0KKMassWindowWidthHigh': 75.,
           'D0P': 5000.,
           'D0VtxChi2Ndof': 10.,
           'D0FDChi2': 40.,
           'D0BPVDira': 0.9999,
           'D0DOCA': 0.07,
           'Daug_TRCHI2DOF_MAX': 5.,
           'Dstar_AMDiff_MAX': 165.,
           'Dstar_VCHI2VDOF_MAX': 100.,
           'Dstar_MDiff_MAX': 160.,
           'UntaggedCFLinePrescale': 0.2,
           'UntaggedCFLinePostscale': 1.,
           'UntaggedSCSLinePrescale': 1.,
           'UntaggedSCSLinePostscale': 1.,
           'TaggedRSLinePrescale': 1.,
           'TaggedRSLinePostscale': 1.,
           'TaggedWSLinePrescale': 1.,
           'TaggedWSLinePostscale': 1.,
           'TaggedSCSLinePrescale': 1.,
           'TaggedSCSLinePostscale': 1.,
         }

class D2hhConf(LineBuilder) :

    '''
    Produces 7 lines, 3 untagged and 4 tagged D->hh lines:
    untagged:
    - D->Kpi
    - D->KK
    - D->pipi
    tagged, D*->D0pi with:
    - D->Kpi RS
    - D->Kpi WS
    - D->KK
    - D->pipi

    Usage:
    from StrippingSelections import StrippingD2hh
    confD2hh = StrippingD2hh.D2hhConf("D2hh",StrippingD2hh.default_config)
    stream.appendLines( confD2hh.lines() )
    '''

    __configuration_keys__ = ('DaugPtMin',
	     		      'DaugPtMax',
	     		      'DaugP',
	     		      'DaugIPChi2',
	     		      'DaugTrkChi2',
	     		      'HighPIDK',
	     		      'LowPIDK',
	     		      'D0Pt',
	     		      'D0MassWindowCentre',
	     		      'D0MassWindowWidth',
	     		      'D0PiPiMassWindowWidthLow',
	     		      'D0PiPiMassWindowWidthHigh',
	     		      'D0KKMassWindowWidthLow',
	     		      'D0KKMassWindowWidthHigh',
	     		      'D0P',
	     		      'D0VtxChi2Ndof',
	     		      'D0FDChi2',
	     		      'D0BPVDira',
	     		      'D0DOCA',
                              'Daug_TRCHI2DOF_MAX',
                              'Dstar_AMDiff_MAX',
                              'Dstar_VCHI2VDOF_MAX',
                              'Dstar_MDiff_MAX',
                              'UntaggedCFLinePrescale',
                              'UntaggedCFLinePostscale',
                              'UntaggedSCSLinePrescale',
                              'UntaggedSCSLinePostscale',
                              'TaggedRSLinePrescale',
                              'TaggedRSLinePostscale',
                              'TaggedWSLinePrescale',
                              'TaggedWSLinePostscale',
                              'TaggedSCSLinePrescale',
                              'TaggedSCSLinePostscale',
                              )

    def __init__(self, name, config) :

        LineBuilder.__init__(self, name, config)

        stdNoPIDsKaons = StdAllNoPIDsKaons
        stdNoPIDsPions = StdAllNoPIDsPions

        d2kpi_name = name+'PromptD2KPi'
        d0RS_name =  name+'PromptD0RS'
        d0WS_name = name+'PromptD0WS'
        d2kk_name = name+'PromptD2KK'
        d2pipi_name = name+'PromptD2PiPi'
        dst2DPiPi_name = name+'PromptDst2D2PiPi'
        dst2DKK_name = name+'PromptDst2D2KK'
        dst2DRS_name = name+'PromptDst2D2RS'
        dst2DWS_name = name+'PromptDst2D2WS'

        # D0 -> hh' selections
        self.selD2Kpi = makeD2hh(d2kpi_name,  
			         config,
 				 KPIDK_string = ' & (PIDK > %(HighPIDK)s)',
				 PiPIDK_string = ' & (PIDK < %(LowPIDK)s)',
				 CombPIDK_string = '',
				 DecayDescriptor = '[D0 -> K- pi+]cc',
			         inputSel = [stdNoPIDsPions, stdNoPIDsKaons]
			        )

        self.selD0KK = makeD2hhAsymm(d2kk_name,  
			        config,
 				KPIDK_string = ' & (PIDK > %(LowPIDK)s)',
				PiPIDK_string = '',
				Mass_low_string = '& (DAMASS(%(D0MassWindowCentre)s* MeV) > %(D0KKMassWindowWidthLow)s* MeV)',
				Mass_high_string = '& (DAMASS(%(D0MassWindowCentre)s* MeV) < %(D0KKMassWindowWidthHigh)s* MeV)',
				CombPIDK_string = ' & (AHASCHILD( PIDK > %(HighPIDK)s ) )',
				DecayDescriptor = 'D0 -> K+ K-',
			        inputSel = [stdNoPIDsKaons]
			       )

        self.selD0PiPi = makeD2hhAsymm(d2pipi_name,  
			          config,
 				  KPIDK_string = '',
				  PiPIDK_string = ' & (PIDK < %(HighPIDK)s)',
				  Mass_low_string = '& (DAMASS(%(D0MassWindowCentre)s* MeV) > %(D0PiPiMassWindowWidthLow)s* MeV)',
				  Mass_high_string = '& (DAMASS(%(D0MassWindowCentre)s* MeV) < %(D0PiPiMassWindowWidthHigh)s* MeV)',
				  CombPIDK_string = '',
				  DecayDescriptor = 'D0 -> pi+ pi-',
			          inputSel = [stdNoPIDsPions]
			         )

        from Configurables import ConjugateNeutralPID
        from PhysSelPython.Wrappers import Selection
        _localConj_KPi = ConjugateNeutralPID('Conjugate'+d0WS_name)
        _localConj_KK = ConjugateNeutralPID('Conjugate'+d2kk_name)
        _localConj_PiPi = ConjugateNeutralPID('Conjugate'+d2pipi_name)
        self.selD0WS = Selection(d0WS_name, Algorithm=_localConj_KPi, RequiredSelections=[self.selD2Kpi])
        self.selD0ConjKK = Selection('SelConjugate'+d2kk_name, Algorithm = _localConj_KK, RequiredSelections = [self.selD0KK])
        self.selD0ConjPiPi = Selection('SelConjugate'+d2pipi_name, Algorithm = _localConj_PiPi, RequiredSelections = [self.selD0PiPi])

        # Dstar -> D0 pi selections
	self.selDstRS = makeDstar2D0Pi( dst2DRS_name
				   , config
                                   , '[D*(2010)+ -> D0 pi+]cc'
                                   , inputSel = [self.selD2Kpi, stdNoPIDsPions]
                                 )

	self.selDstWS = makeDstar2D0Pi( dst2DWS_name
				   , config
                                   , '[D*(2010)+ -> D0 pi+]cc'
                                   , inputSel = [self.selD0WS, stdNoPIDsPions]
                                 )

	self.selDstKK = makeDstar2D0Pi( dst2DKK_name
				   , config
                                   , '[D*(2010)+ -> D0 pi+]cc'
                                   , inputSel = [self.selD0KK, self.selD0ConjKK, stdNoPIDsPions]
                                 )

	self.selDstPiPi = makeDstar2D0Pi( dst2DPiPi_name
				   , config
                                   , '[D*(2010)+ -> D0 pi+]cc'
                                   , inputSel = [self.selD0PiPi, self.selD0ConjPiPi, stdNoPIDsPions]
                                 )

        # Untagged lines
        self.d2kpi_line = StrippingLine(d2kpi_name+"Line",
                                        prescale = config['UntaggedCFLinePrescale'],
                                        postscale = config['UntaggedCFLinePostscale'],
                                        selection = self.selD2Kpi
                                       )

        self.d2kk_line = StrippingLine(d2kk_name+"Line",
                                        prescale = config['UntaggedSCSLinePrescale'],
                                        postscale = config['UntaggedSCSLinePostscale'],
                                        selection = self.selD0KK
                                       )

        self.d2pipi_line = StrippingLine(d2pipi_name+"Line",
                                        prescale = config['UntaggedSCSLinePrescale'],
                                        postscale = config['UntaggedSCSLinePostscale'],
                                        selection = self.selD0PiPi
                                       )

        # Tagged lines
        self.dstRS_line = StrippingLine(dst2DRS_name+"Line",
                                        prescale = config['TaggedRSLinePrescale'],
                                        postscale = config['TaggedRSLinePostscale'],
                                        selection = self.selDstRS
                                       )

        self.dstWS_line = StrippingLine(dst2DWS_name+"Line",
                                        prescale = config['TaggedWSLinePrescale'],
                                        postscale = config['TaggedWSLinePostscale'],
                                        selection = self.selDstWS
                                       )

        self.dstKK_line = StrippingLine(dst2DKK_name+"Line",
                                        prescale = config['TaggedSCSLinePrescale'],
                                        postscale = config['TaggedSCSLinePostscale'],
                                        selection = self.selDstKK
                                       )

        self.dstPiPi_line = StrippingLine(dst2DPiPi_name+"Line",
                                        prescale = config['TaggedSCSLinePrescale'],
                                        postscale = config['TaggedSCSLinePostscale'],
                                        selection = self.selDstPiPi
                                       )

        # register lines
        self.registerLine(self.d2kpi_line)
        self.registerLine(self.d2kk_line)
        self.registerLine(self.d2pipi_line)

        self.registerLine(self.dstRS_line)
        self.registerLine(self.dstWS_line)
        self.registerLine(self.dstKK_line)
        self.registerLine(self.dstPiPi_line)

def makeD2hh(name,
             config,
	     KPIDK_string,
	     PiPIDK_string,
	     CombPIDK_string,
	     DecayDescriptor,
             inputSel
            ) :
    """
    Create and return a D0 -> hh' Selection object.
    Arguments:
    name        : name of the Selection.
    config      : dictionary of cut values.
    ..._string  : cut implementation for PIDK cuts.
    DecayDescriptor: DecayDescriptor.
    inputSel    : input selections
    """

    _Kcuts1  = "(PT > %(DaugPtMin)s* MeV) & (MIPCHI2DV(PRIMARY) > %(DaugIPChi2)s)" % locals()['config']
    _KcutsPIDK  = KPIDK_string % locals()['config']
    _Kcuts2  = " & (ISLONG) & (P > %(DaugP)s* MeV) & (TRCHI2DOF < %(DaugTrkChi2)s)" % locals()['config']
    _Kcuts = _Kcuts1 + _KcutsPIDK + _Kcuts2
    _Picuts1 = "(PT > %(DaugPtMin)s* MeV) & (MIPCHI2DV(PRIMARY) > %(DaugIPChi2)s)" % locals()['config']
    _PicutsPIDK  = PiPIDK_string % locals()['config']
    _Picuts2 = " & (ISLONG) & (P > %(DaugP)s* MeV) & (TRCHI2DOF < %(DaugTrkChi2)s)" % locals()['config']
    _Picuts = _Picuts1 + _PicutsPIDK + _Picuts2
    _dauCuts = { 'K+': _Kcuts, 'pi+': _Picuts }

    _combCuts1 = "(APT > %(D0Pt)s* MeV)" \
		"& (AHASCHILD( PT > %(DaugPtMax)s* MeV ) )" \
    		"& (ADOCA(1,2)< %(D0DOCA)s* mm)" \
                "& (ADAMASS(%(D0MassWindowCentre)s* MeV) < %(D0MassWindowWidth)s* MeV)" \
                "& (AP > %(D0P)s* MeV)" % locals()['config']
    _combCutsPIDK = CombPIDK_string % locals()['config']
    _combCuts = _combCuts1 + _combCutsPIDK

    _motherCuts = "(VFASPF(VCHI2PDOF) < %(D0VtxChi2Ndof)s)" \
                  "& (BPVVDCHI2 > %(D0FDChi2)s)" \
                  "& (BPVDIRA > %(D0BPVDira)s)" % locals()['config']

    _D0 = CombineParticles( DecayDescriptor = DecayDescriptor,
                            MotherCut = _motherCuts,
                            CombinationCut = _combCuts,
                            DaughtersCuts = _dauCuts)

    return Selection ( name+'Sel',
                       Algorithm = _D0,
                       RequiredSelections = inputSel )

def makeD2hhAsymm(name,
             config,
	     KPIDK_string,
	     PiPIDK_string,
	     Mass_low_string,
	     Mass_high_string,
	     CombPIDK_string,
	     DecayDescriptor,
             inputSel
            ) :
    """
    Create and return a D0 -> hh' Selection object.
    Arguments:
    name        : name of the Selection.
    config      : dictionary of cut values.
    ..._string  : cut implementation for PIDK cuts.
    DecayDescriptor: DecayDescriptor.
    inputSel    : input selections
    """

    _Kcuts1  = "(PT > %(DaugPtMin)s* MeV) & (MIPCHI2DV(PRIMARY) > %(DaugIPChi2)s)" % locals()['config']
    _KcutsPIDK  = KPIDK_string % locals()['config']
    _Kcuts2  = " & (ISLONG) & (P > %(DaugP)s* MeV) & (TRCHI2DOF < %(DaugTrkChi2)s)" % locals()['config']
    _Kcuts = _Kcuts1 + _KcutsPIDK + _Kcuts2
    _Picuts1 = "(PT > %(DaugPtMin)s* MeV) & (MIPCHI2DV(PRIMARY) > %(DaugIPChi2)s)" % locals()['config']
    _PicutsPIDK  = PiPIDK_string % locals()['config']
    _Picuts2 = " & (ISLONG) & (P > %(DaugP)s* MeV) & (TRCHI2DOF < %(DaugTrkChi2)s)" % locals()['config']
    _Picuts = _Picuts1 + _PicutsPIDK + _Picuts2
    _dauCuts = { 'K+': _Kcuts, 'pi+': _Picuts }

    _massLow  = Mass_low_string % locals()['config']
    _massHigh  = Mass_high_string % locals()['config']
    _combCuts1 = "(APT > %(D0Pt)s* MeV)" \
		"& (AHASCHILD( PT > %(DaugPtMax)s* MeV ) )" \
    		"& (ADOCA(1,2)< %(D0DOCA)s* mm)" \
                "& (AP > %(D0P)s* MeV)" % locals()['config']
    _combCutsPIDK = CombPIDK_string % locals()['config']
    _combCuts = _combCuts1 + _combCutsPIDK + _massLow + _massHigh

    _motherCuts = "(VFASPF(VCHI2PDOF) < %(D0VtxChi2Ndof)s)" \
                  "& (BPVVDCHI2 > %(D0FDChi2)s)" \
                  "& (BPVDIRA > %(D0BPVDira)s)" % locals()['config']

    _D0 = CombineParticles( DecayDescriptor = DecayDescriptor,
                            MotherCut = _motherCuts,
                            CombinationCut = _combCuts,
                            DaughtersCuts = _dauCuts)

    return Selection ( name+'Sel',
                       Algorithm = _D0,
                       RequiredSelections = inputSel )

def makeDstar2D0Pi( name
                    , config
                    , DecayDescriptor
                    , inputSel
                  ) :

    """
    Create and return a D* -> D0 pi Selection object.
    Arguments:
    name        : name of the Selection.
    config      : dictionary of cut values.
    DecayDescriptor: DecayDescriptor.
    inputSel    : input selections
    """

    daugCuts = "(TRCHI2DOF < %(Daug_TRCHI2DOF_MAX)s)" % locals()['config']
    combCuts = "((AM - AM1) < %(Dstar_AMDiff_MAX)s* MeV)" % locals()['config']
    dstarCuts = "(VFASPF(VCHI2/VDOF) < %(Dstar_VCHI2VDOF_MAX)s)" \
                "& ((M - M1) < %(Dstar_MDiff_MAX)s* MeV)" % locals()['config']

    _Dstar = CombineParticles( DecayDescriptor = DecayDescriptor
                             , DaughtersCuts = { "pi+" : daugCuts }
                             , CombinationCut = combCuts
                             , MotherCut = dstarCuts
                             )

    return Selection( name+'Sel',
                      Algorithm = _Dstar,
                      RequiredSelections = inputSel
                    )


#!/usr/bin/env python
# $Id: StrippingD2hhh_conf.py,v 1.1 2011-02-14 12:53:17 polye Exp $
'''
Module for construction of D->HHH based on 
 Bs->JpsiPhi pre-scaled and detatched stripping Selections and StrippingLines
 from Greig and Juan and D->HHH selections cuts from Hamish and Mat.
Provides functions to build D2KKP, D2KPP, D2PPP, D2KPPos selections using 
 StdLooseDplus and D2KKK and D2hhh inclusive using CombineParticles.
Provides class D2hhhConf, which constructs the Selections and 
StrippingLines given a configuration dictionary.
Exported symbols (use python help!):
   - D2hhhConf
   - makeStdD2hhh
   - makeD2KKK   
   - makeD2hhhInc
'''

__author__ = ['Erica Polycarpo','Alberto Reis']
__date__ = '14/02/2011'
__version__ = '$Revision: 1.1 $'

__all__ = ('D2hhhConf',
           'makeStdD2hhh', 'makeD2KKK', 'makeD2HHHInc' )

from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles
from PhysSelPython.Wrappers import Selection, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from StandardParticles import ( StdNoPIDsPions,
                                StdTightKaons ) 

name = "D2hhh"

class D2hhhConf(LineBuilder) :
    """
    Builder of D->hhh stripping Selection and StrippingLine.
    Constructs D ->hhh Selections and StrippingLines from a configuration dictionary.
    Usage:
    >>> config = { .... }
    >>> D2HHHConf = D2hhhConf('D2HHHtest',config)
    >>> D2hhhLines = D2HHHConf.lines
    >>> for line in line :
    >>>  print line.name(), line.outputLocation()
    The lines can be used directly to build a StrippingStream object.

    Exports as instance data members:
    selKKP             :  get StdLooseDplus2KKP 
    selKPP             :  get StdLooseDplus2KPP 
    selPPP             :  get StdLooseDplus2PPP 
    selKPPos           :  get StdLooseDplus2KPPi (DCS)
    selTightKaon       :  get StdTightKaons
    selNoPIDsPion      :  get StdNoPIDsPion 
    D2KKP_line         :  StrippingLine made out of selKKP 
    D2KPP_line         :  StrippingLine made out of selKPP 
    D2PPP_line         :  StrippingLine made out of selPPP 
    D2KPPos_line       :  StrippingLine made out of selKPPos
    D2KKK_line         :  StrippingLine made out of 3K combinations
    D2HHHInc_line      :  StrippingLine made out of 3PI combinations with large mass window
    lines              :  List of lines [D2KKP_line, D2KPP_line, D2PPP_line, D2KPPos_line, D2KKK_line, D2HHHInc_line]

    Exports as class data member:
    D2HHHConf.__configuration_keys__ : List of required configuration parameters.
    """

    __configuration_keys__ = ('DaughterPT',                       
                              'DaughterP',
                              'DaughterIPChi2',
                              'Daughter2IPChi2',
                              'D2KKKDaughterIPChi2',
                              'D2KKKDaughter2IPChi2',
                              'D2KKKDaughter1IPChi2',
                              'KPIDK',
                              'piPIDK',
                              'PTSum',
                              'DOCAChi2',
                              'DPt',
                              'DIPChi2',
                              'DdcaFDChi2',
                              'DDIRA',
                              'DVXChi2NDOF',
                              'MinMassPosFit',
                              'MaxMassPosFit',
                              'D2KPPMaxMassPosFit',
                              'D2HHHIncMinMassPosFit',
                              'D2HHHIncMaxMassPosFit',
                              'MaxTracksInEvent',
                              'D2KKPLinePrescale',
                              'D2KKPLinePostscale',
                              'D2KPPLinePrescale',
                              'D2KPPLinePostscale',
                              'D2PPPLinePrescale',
                              'D2PPPLinePostscale',
                              'D2KKKLinePrescale',
                              'D2KKKLinePostscale',
                              'D2KPPosLinePrescale',
                              'D2KPPosLinePostscale',
                              'D2HHHIncLinePrescale',
                              'D2HHHIncLinePostscale'
                              )

    def __init__(self, name, config) :

        LineBuilder.__init__(self, name, config)

        D2KKP_name = name+'_KKP'
        D2KPP_name = name+'_KPP'
        D2PPP_name = name+'_PPP'
        D2KPPos_name = name+'_KPPos'
        D2KKK_name = name+'_KKK'
        D2HHHInc_name = name+'_HHHInc'

        self.selKKP = DataOnDemand(Location = "Phys/StdLooseDplus2KKPi/Particles")
        self.selKPP = DataOnDemand(Location = "Phys/StdLooseDplus2KPiPi/Particles")
        self.selPPP = DataOnDemand(Location = "Phys/StdLooseDplus2PiPiPi/Particles")
        self.selKPPos = DataOnDemand(Location = "Phys/StdLooseDplus2KPiPiOppSignPi/Particles")


        self.selD2KKP = makeStdD2hhh(D2KKP_name,  
                                     hhhSel = self.selKKP, 
                                     DaughterPT= config['DaughterPT'],
                                     DaughterP = config['DaughterP'],
                                     DaughterIPChi2 = config['DaughterIPChi2'],
                                     Daughter2IPChi2 = config['Daughter2IPChi2'],
                                     PTSum = config['PTSum'],
				     DDIRA= config['DDIRA'],
				     DIPChi2= config['DIPChi2'],
				     DdcaFDChi2= config['DdcaFDChi2'],
                                     DPt = config['DPt'],
                                     DVXChi2NDOF = config['DVXChi2NDOF'],
				     MinMassPosFit= config['MinMassPosFit'],
				     MaxMassPosFit= config['MaxMassPosFit'],
                                     KPIDK = config['KPIDK'],
                                     piPIDK = config['piPIDK']
			             )
        self.selD2KPP = makeStdD2hhh(D2KPP_name,  
                                     hhhSel = self.selKPP, 
                                     DaughterPT= config['DaughterPT'],
                                     DaughterP = config['DaughterP'],
                                     DaughterIPChi2 = config['DaughterIPChi2'],
                                     Daughter2IPChi2 = config['Daughter2IPChi2'],
                                     PTSum = config['PTSum'],
				     DDIRA= config['DDIRA'],
				     DIPChi2= config['DIPChi2'],
				     DdcaFDChi2= config['DdcaFDChi2'],
                                     DPt = config['DPt'],
                                     DVXChi2NDOF = config['DVXChi2NDOF'],
				     MinMassPosFit= config['MinMassPosFit'],
				     MaxMassPosFit= config['D2KPPMaxMassPosFit'],
                                     KPIDK = config['KPIDK'],
                                     piPIDK = config['piPIDK']
			             )
        self.selD2PPP = makeStdD2hhh(D2PPP_name,  
                                     hhhSel = self.selPPP, 
                                     DaughterPT= config['DaughterPT'],
                                     DaughterP = config['DaughterP'],
                                     DaughterIPChi2 = config['DaughterIPChi2'],
                                     Daughter2IPChi2 = config['Daughter2IPChi2'],
                                     PTSum = config['PTSum'],
				     DDIRA= config['DDIRA'],
				     DIPChi2= config['DIPChi2'],
				     DdcaFDChi2= config['DdcaFDChi2'],
                                     DPt = config['DPt'],
                                     DVXChi2NDOF = config['DVXChi2NDOF'],
				     MinMassPosFit= config['MinMassPosFit'],
				     MaxMassPosFit= config['MaxMassPosFit'],
                                     piPIDK = config['piPIDK']
                                     )
        self.selD2KPPos = makeStdD2hhh(D2KPPos_name,  
                                     hhhSel = self.selKPPos, 
                                     DaughterPT= config['DaughterPT'],
                                     DaughterP = config['DaughterP'],
                                     DaughterIPChi2 = config['DaughterIPChi2'],
                                     Daughter2IPChi2 = config['Daughter2IPChi2'],
                                     PTSum = config['PTSum'],
				     DDIRA= config['DDIRA'],
				     DIPChi2= config['DIPChi2'],
				     DdcaFDChi2= config['DdcaFDChi2'],
                                     DPt = config['DPt'],
                                     DVXChi2NDOF = config['DVXChi2NDOF'],
				     MinMassPosFit= config['MinMassPosFit'],
				     MaxMassPosFit= config['MaxMassPosFit'],
                                     KPIDK = config['KPIDK'],
                                     piPIDK = config['piPIDK']
                                     )
        self.selD2KKK = makeD2KKK(D2KKK_name,  
                                     DaughterPT= config['DaughterPT'],
                                     DaughterP = config['DaughterP'],
                                     DaughterIPChi2 = config['D2KKKDaughterIPChi2'],
                                     Daughter2IPChi2 = config['D2KKKDaughter2IPChi2'],
                                     Daughter1IPChi2 = config['D2KKKDaughter1IPChi2'],
                                     PTSum = config['PTSum'],
                                     DaughterDOCA = config['DOCAChi2'],
				     DDIRA= config['DDIRA'],
				     DIPChi2= config['DIPChi2'],
				     DdcaFDChi2= config['DdcaFDChi2'],
                                     DPt = config['DPt'],
                                     DVXChi2NDOF = config['DVXChi2NDOF'],
				     MinMassPosFit= config['MinMassPosFit'],
				     MaxMassPosFit= config['MaxMassPosFit'],
                                     KPIDK = config['KPIDK']
                                     )
        self.selD2HHHInc = makeD2HHHInc(D2HHHInc_name,  
                                     DaughterPT= config['DaughterPT'],
                                     DaughterP = config['DaughterP'],
                                     DaughterIPChi2 = config['DaughterIPChi2'],
                                     Daughter2IPChi2 = config['Daughter2IPChi2'],
                                     PTSum = config['PTSum'],
                                     DaughterDOCA = config['DOCAChi2'],
				     DDIRA= config['DDIRA'],
				     DIPChi2= config['DIPChi2'],
				     DdcaFDChi2= config['DdcaFDChi2'],
                                     DPt = config['DPt'],
                                     DVXChi2NDOF = config['DVXChi2NDOF'],
				     MinMassPosFit= config['D2HHHIncMinMassPosFit'],
				     MaxMassPosFit= config['D2HHHIncMaxMassPosFit']
                                     )
        self.filterGE = globalEventCutFilter(name + 'GECFilter', 
                                    MaxTrSIZE = config['MaxTracksInEvent'])

        self.D2KKP_line = StrippingLine(D2KKP_name+"Line",
                                        prescale = config['D2KKPLinePrescale'],
                                        postscale = config['D2KKPLinePostscale'],
                                        selection = self.selD2KKP,
                                        FILTER = self.filterGE 
                                        )
        self.D2KPP_line = StrippingLine(D2KPP_name+"Line",
                                        prescale = config['D2KPPLinePrescale'],
                                        postscale = config['D2KPPLinePostscale'],
                                        selection = self.selD2KPP,
                                        FILTER = self.filterGE 
                                        )
        self.D2PPP_line = StrippingLine(D2PPP_name+"Line",
                                        prescale = config['D2PPPLinePrescale'],
                                        postscale = config['D2PPPLinePostscale'],
                                        selection = self.selD2PPP,
                                        FILTER = self.filterGE 
                                        )
        self.D2KPPos_line = StrippingLine(D2KPPos_name+"Line",
                                        prescale = config['D2KPPosLinePrescale'],
                                        postscale = config['D2KPPosLinePostscale'],
                                        selection = self.selD2KPPos,
                                        FILTER = self.filterGE 
                                        )
        self.D2KKK_line = StrippingLine(D2KKK_name+"Line",
                                        prescale = config['D2KKKLinePrescale'],
                                        postscale = config['D2KKKLinePostscale'],
                                        selection = self.selD2KKK,
                                        FILTER = self.filterGE 
                                        )
        self.D2HHHInc_line = StrippingLine(D2HHHInc_name+"Line",
                                        prescale = config['D2HHHIncLinePrescale'],
                                        postscale = config['D2HHHIncLinePostscale'],
                                        selection = self.selD2HHHInc,
                                        FILTER = self.filterGE 
                                        )

        self.registerLine(self.D2KKP_line)
        self.registerLine(self.D2KPP_line)
        self.registerLine(self.D2PPP_line)
        self.registerLine(self.D2KPPos_line)
        self.registerLine(self.D2KKK_line)
        self.registerLine(self.D2HHHInc_line)


def makeStdD2hhh(name,
                 hhhSel,
		 DaughterPT,
		 DaughterP,
		 DaughterIPChi2,
		 Daughter2IPChi2, 
		 PTSum,
		 DDIRA,
		 DIPChi2,
		 DdcaFDChi2,
		 DPt,
		 DVXChi2NDOF,
		 MinMassPosFit,
		 MaxMassPosFit,
		 KPIDK=None,
		 piPIDK=None
                 ):
    """
    Create and return a D -> HHH Selection object.
    Arguments:
    name           : name of the Selection.
    hhhSel         : Standard Specific D2HHH selection    
    DaughterPT     : Minimum PT among daughters
    DaughterIPChi2 : Minimum IPChi2 among daughters
    Daughter2IPChi2: Minimum IPChi2 required to at least 2 daughters 
    DaughterP      : Minimum P among daughters
    PTSum          : Minimum sum of daughters momenta
    DDIRA          : Minimum opening angle between sum_p and FD-direction
    DIPChi2        : Maximum IPChi2 of the D
    DdcaFDChi2     : Minimum distance from SV to any PV
    DPt            : Minimum D Momentum
    DVXChi2NDOF    : Maximum Chi2 of the D Vertex
    MinMassPosFit  : Minimum value of HHH invariant mass (MeV)
    MaxMassPosFit  : Maximum value of HHH invariant mass (MeV).
    KPIDK=None     : Minimum Kaon - pion DLL for kaons
    piPIDK=None    : Maximum Kaon - pion DLL for pions
    """
    _Daughtercuts_pi = """
                       (MINTREE('pi+'==ABSID, PT) > %(DaughterPT)s ) &
                       (MINTREE('pi+'==ABSID, P ) > %(DaughterP)s) &
                       (MINTREE('pi+'==ABSID, MIPCHI2DV(PRIMARY)) > %(DaughterIPChi2)s ) 
                       """ %locals()
    _Daughtercuts_K = """
                      (MINTREE('K-'==ABSID, PT) > %(DaughterPT)s ) &
                      (MINTREE('K-'==ABSID, P ) > %(DaughterP)s) & 
                      (MINTREE('K-'==ABSID, MIPCHI2DV(PRIMARY)) > %(DaughterIPChi2)s ) 
                      """ %locals() 
    _Combcuts_HHH =""" 
                   (SUMTREE( ISBASIC , PT ) > %(PTSum)s*MeV) &
                   (2 <= NINGENERATION((MIPCHI2DV(PRIMARY) > %(Daughter2IPChi2)s ) , 1)) 
                   """ % locals()
                    
    _Mothercuts_HHH = """ 
                      (PT > %(DPt)s) & (VFASPF(VCHI2/VDOF) < %(DVXChi2NDOF)s) & 
                      (BPVDIRA > %(DDIRA)s) & (BPVIPCHI2() < %(DIPChi2)s) & 
                      (VFASPF(VMINVDCHI2DV(PRIMARY)) > %(DdcaFDChi2)s)
                      """ % locals()
    _cutsMassPosFit = " (in_range ( %(MinMassPosFit)s ,  M  , %(MaxMassPosFit)s )) " % locals()
    _DaughterCuts = _Daughtercuts_pi
    
    if piPIDK != None :
       _DaughterCuts += " & (MAXTREE('pi+'==ABSID, PIDK-PIDpi) < %(piPIDK)s) " % locals() 
   
    if KPIDK != None :
       _DaughterCuts += " & (MINTREE('K-'==ABSID, PIDK-PIDpi) > %(KPIDK)s )" %locals()
       _DaughterCuts += " & "+_Daughtercuts_K   
  
    _code = '('+_DaughterCuts+'&'+_Combcuts_HHH+'&'+_Mothercuts_HHH+'&'+_cutsMassPosFit+')'
 
    _filterHHH = FilterDesktop( Code = _code ) 
   
    return Selection ( name,
                       Algorithm = _filterHHH,
                       RequiredSelections = [hhhSel])


def makeD2KKK(name,
#              kaonSel,
              DaughterPT,
              DaughterP,
              DaughterIPChi2,
              Daughter2IPChi2,
              Daughter1IPChi2,
              DaughterDOCA,
              PTSum,
              DDIRA,
              DIPChi2,
              DdcaFDChi2,
              DPt,
              DVXChi2NDOF,
              MinMassPosFit,
              MaxMassPosFit,
              KPIDK=None
              ):
    """
    Create and return a D -> KKK Selection object.
    Arguments:
    name           : name of the Selection.
    kaonSel        : Input Selection of Kaons 
    DaughterPT     : Minimum PT among daughters
    DaughterP      : Minimum P among daughters
    DaughterIPChi2 : Minimum IPChi2 among daughters
    Daughter2IPChi2: Minimum IPChi2 required to at least 2 daughters 
    Daughter1IPChi2: Minimum IPChi2 required to at least 1 daughters 
    DaughterDOCA   : Maximum distance of closest approach between 2 daughters 
    PTSum          : Minimum sum of daughters momenta
    DDIRA          : Minimum opening angle between sum_p and FD-direction
    DIPChi2        : Maximum IPChi2 of the D
    DdcaFDChi2     : Minimum distance from SV to any PV
    DPt            : Minimum D Momentum
    DVXChi2NDOF    : Maximum Chi2 of the D Vertex
    MinMassPosFit  : Minimum value of HHH invariant mass (MeV)
    MaxMassPosFit  : Maximum value of HHH invariant mass (MeV).
    KPIDK=None     : Minimum Kaon - pion DLL for kaons
    """

    _Daughtercuts_K = "(PT > %(DaughterPT)s *MeV) & (P > %(DaughterP)s *MeV) &((MIPCHI2DV(PRIMARY)) > %(DaughterIPChi2)s ) " % locals() 
                      
    _Combcuts_HHH = "(ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) > %(PTSum)s*MeV) &(ADOCACHI2CUT( %(DaughterDOCA)s , '' )) &(ANUM(MIPCHI2DV(PRIMARY) > %(Daughter2IPChi2)s ) >= 2) & (AHASCHILD((MIPCHI2DV(PRIMARY)) > %(Daughter1IPChi2)s))" % locals() 
                    
    _Mothercuts_HHH = """ 
                      (PT > %(DPt)s) & (VFASPF(VCHI2/VDOF) < %(DVXChi2NDOF)s) & 
                      (BPVDIRA > %(DDIRA)s) & (BPVIPCHI2() < %(DIPChi2)s) & 
                      (VFASPF(VMINVDCHI2DV(PRIMARY)) > %(DdcaFDChi2)s)
                      """ % locals()

    _cutsMassPosFit = " (in_range ( %(MinMassPosFit)s ,  M  , %(MaxMassPosFit)s )) " % locals()

    _DaughterCuts = _Daughtercuts_K

    if KPIDK != None :
       _DaughterCuts += " & ((PIDK-PIDpi) > %(KPIDK)s )" %locals()
                   
    _combKKK = CombineParticles()
    _combKKK.DecayDescriptor = '[D+ -> K- K+ K+]cc' 
    _combKKK.DaughtersCuts = { "K+" : '(' + _DaughterCuts + ')' } 
    _combKKK.CombinationCut = '(' + _Combcuts_HHH + ')' 
    _combKKK.MotherCut = '(' + _Mothercuts_HHH + ' & ' + _cutsMassPosFit  + ')' 


    return Selection ( name,
                       Algorithm = _combKKK,
                       RequiredSelections = [StdTightKaons])

def makeD2HHHInc(name,
              DaughterPT,
              DaughterP,
              DaughterIPChi2,
              Daughter2IPChi2,
              DaughterDOCA,
              PTSum,
              DDIRA,
              DIPChi2,
              DdcaFDChi2,
              DPt,
              DVXChi2NDOF,
              MinMassPosFit,
              MaxMassPosFit
              ):
    """
    Create and return a D -> HHHInclusive selection 
    Arguments:
    name           : name of the Selection.
    pionSel        : Pion Selection (from CommonParticles) 
    DaughterPT     : Minimum PT among daughters
    DaughterP      : Minimum P among daughters
    DaughterIPChi2 : Minimum IPChi2 among daughters
    Daughter2IPChi2: Minimum IPChi2 required to at least 2 daughters 
    DaughterDOCA   : Maximum distance of closest approach between 2 daughters 
    PTSum          : Minimum sum of daughters momenta
    DDIRA          : Minimum opening angle between sum_p and FD-direction
    DIPChi2        : Maximum IPChi2 of the D
    DdcaFDChi2     : Minimum distance from SV to any PV
    DPt            : Minimum D Momentum
    DVXChi2NDOF    : Maximum Chi2 of the D Vertex
    MinMassPosFit  : Minimum value of HHH invariant mass (MeV)
    MaxMassPosFit  : Maximum value of HHH invariant mass (MeV).
    """

    _DaughterCuts = "((MIPCHI2DV(PRIMARY)) > %(DaughterIPChi2)s ) & (P > %(DaughterP)s *MeV) & (PT > %(DaughterPT)s *MeV) " % locals() 
                      
    _Combcuts_HHH = "(ADOCACHI2CUT( %(DaughterDOCA)s , '' )) & (ACHILD(PT,1)+ACHILD(PT,2)+ACHILD(PT,3) > %(PTSum)s*MeV) & (ANUM(MIPCHI2DV(PRIMARY) > %(Daughter2IPChi2)s ) >= 2) " % locals()
                   
    _Mothercuts_HHH = """ 
                      (PT > %(DPt)s) & (VFASPF(VCHI2/VDOF) < %(DVXChi2NDOF)s) & 
                      (BPVDIRA > %(DDIRA)s) & (BPVIPCHI2() < %(DIPChi2)s) & 
                      (VFASPF(VMINVDCHI2DV(PRIMARY)) > %(DdcaFDChi2)s)
                      """ % locals()
    _cutsMassPosFit = " (in_range ( %(MinMassPosFit)s ,  M  , %(MaxMassPosFit)s )) " % locals()
                   
    _combHHH = CombineParticles()
    _combHHH.DecayDescriptor = '[D+ -> pi- pi+ pi+]cc' 
    _combHHH.DaughtersCuts = { "pi+" : '(' + _DaughterCuts + ')' } 
    _combHHH.CombinationCut = '(' + _Combcuts_HHH + ')' 
    _combHHH.MotherCut = '(' + _Mothercuts_HHH + ' & ' + _cutsMassPosFit  + ')' 


    return Selection ( name,
                       Algorithm = _combHHH,
                       RequiredSelections = [StdNoPIDsPions])


def globalEventCutFilter(name, 
                         MaxTrSIZE = None 
                         ) :
#  
  if MaxTrSIZE == None : return None
  
  from Configurables import LoKi__VoidFilter as VoidFilter
  from Configurables import LoKi__Hybrid__CoreFactory as CoreFactory
  modules = CoreFactory('CoreFactory').Modules
  for i in ['LoKiTracks.decorators']:
     if i not in modules : modules.append(i)
  
  _code = "TrSOURCE('Rec/Track/Best') >> (TrSIZE < %(MaxTrSIZE)s )" % locals()
  
  
  return _code          


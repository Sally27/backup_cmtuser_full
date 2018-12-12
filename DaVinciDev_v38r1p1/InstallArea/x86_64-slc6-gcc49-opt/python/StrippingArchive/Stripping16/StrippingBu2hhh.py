 # $Id: StrippingBu2hhh.py,v 1.0 2011-05-26 samba team $
'''
Module for construction of Bu->hhh from:   
   Inclusive KKK line for light decay modes (pipipi, Kpipi, KKpi and KKK) 
   Inclusive pph line for heavy modes (pppi, ppK)

Exported symbols (use python help!):
   - Bu2hhhBuilder
   - makeKKK_incl  
   - makepph_incl
'''

__author__ = ['Irina Nasteva', 'Jussara Miranda']
__date__ = '22/07/2011'
__version__ = '$Revision: 1.0 $'

__all__ = ('Bu2hhhBuilder',
           'makeKKK_incl', 
           'makepph_incl', 
	   )


config_params = {
    'MaxTrSIZE'             : 450 ,      ## GEC maximim Rec/Track/Best TrSIZE
    '_h_PT'                 : 100. ,     ## tracks min PT
    '_h_P'                  : 1500. ,    ## tracks min P  
    '_h_IPCHI2'             : 1. ,       ## min tracks IP wrt OWNPV
    '_h_TRCHI2DOF'          : 3.0 ,      ## max tracks CHI2DOF
    '_3h_DOCA'              : .2 ,       ## max DOCA between h and 2h 
    '_3h_PTmax'             : 1500 ,     ## min PT of the 3h highest PT track
    '_3h_DIRA'              : .99998 ,   ## min cos angle between 3h momentum and PV decay direction   
    '_3h_FDCHI2'            : 500. ,     ## min 3h FDCHI2 wrt best 3h PV  
    '_3h_PVDOCAmin'         : 3.0 ,      ## min value of the 3h doca wrt any PV
    '_3h_CHI2'              : 12.0 ,     ## max 3h vertex CHI2 
    '_3h_IPCHI2'            : 10. ,      ## max 3h IP CHI2 wrt best 3h PV
    '_3h_PT'                : 1000. ,    ## min 3h PT   
    '_3h_PTsum'             : 4250. ,    ## min of 3h tracks PT sum 
    '_3h_Psum'              : 20000. ,   ## min of 3h tracks P sum 
    '_3h_PVIPCHI2sum'       : 500. ,     ## min of the 3h tracks IP wrt best 3h PV
    '_3h_TRKCHIDOFmin'      : 3.0,       ## max track CHI2DOF for the track with smalest CHI2DOF
    '_3h_Charge'            : 1 ,        ## 3h tracks charge sum ==+-1
    '_3h_CORRMmax'          : 7000. ,    ## max corrected mass for 3h candidate  
    '_3h_CORRMmin'          : 4000. ,    ## min corrected mass for 3h candidate   
    '_3hKKK_Mmax'           : 6300. ,    ## max 3h mass for inclusive KKK line       
    '_3hKKK_Mmin'           : 5050. ,    ## min 3h mass for inclusive KKK line
    '_3hpph_deltaMmax'      : 400,       ## max 3h mass difference for inclusive ppK line
    '_3hpph_deltaMmin'      : 200,       ## min 3h mass difference for inclusive ppK line 
    'KKK_inclLinePrescale'  : 1.0,
    'KKK_inclLinePostscale' : 1.0,
    'pph_inclLinePrescale'  : 1.0,
    'pph_inclLinePostscale' : 1.0
    }


"""
B+ -> h+h-h+ channels
"""

from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles

import StandardParticles

if hasattr(StandardParticles, "StdAllNoPIDsKaons"):
  from StandardParticles import StdAllNoPIDsKaons as StdNoPIDsKaons
else:
  from StandardParticles import StdNoPIDsKaons as StdNoPIDsKaons

if hasattr(StandardParticles, "StdAllTightProtons"):
  from StandardParticles import StdAllTightProtons as StdTightProtons
else:
  from StandardParticles import StdTightProtons as StdTightProtons



from PhysSelPython.Wrappers import Selection
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from Configurables import LoKi__VoidFilter as VoidFilter

default_name = "Bu2hhh"

class Bu2hhhBuilder(LineBuilder) :
    __configuration_keys__ = ('MaxTrSIZE',
                              '_h_PT',             
                              '_h_P',               
                              '_h_IPCHI2',         
                              '_h_TRCHI2DOF',       
                              '_3h_DOCA',            
                              '_3h_PTmax',          
                              '_3h_DIRA',            
                              '_3h_FDCHI2',         
                              '_3h_PVDOCAmin',      
                              '_3h_CHI2',           
                              '_3h_IPCHI2',             
                              '_3h_PT',              
                              '_3h_PTsum',              
                              '_3h_Psum',              
                              '_3h_PVIPCHI2sum',              
			      '_3h_TRKCHIDOFmin',
                              '_3h_Charge',         
                              '_3h_CORRMmax',       
                              '_3h_CORRMmin',       
                              '_3hKKK_Mmax',                 
                              '_3hKKK_Mmin',             
                              '_3hpph_deltaMmax',
                              '_3hpph_deltaMmin',
                              'KKK_inclLinePrescale',
                              'KKK_inclLinePostscale',
                              'pph_inclLinePrescale',
                              'pph_inclLinePostscale'
)

    def __init__(self, name, config) :

        LineBuilder.__init__(self, name, config)

        _KKK_inclName = name + '_KKK_incl'
        _pph_inclName = name + '_pph_incl'
	
				      

	self.selKKK = makeKKK_incl( 'KKKinclFor' + _KKK_inclName + 'Sel', 
                             _h_PT           = config['_h_PT'],
                             _h_P            = config['_h_P'],
                             _h_IPCHI2       = config['_h_IPCHI2'],
                             _h_TRCHI2DOF    = config['_h_TRCHI2DOF'], 
                             _3h_DOCA        = config['_3h_DOCA'],
                             _3h_PTmax       = config['_3h_PTmax'],
                             _3h_DIRA        = config['_3h_DIRA'],
                             _3h_FDCHI2      = config['_3h_FDCHI2'],
                             _3h_PVDOCAmin   = config['_3h_PVDOCAmin'],
                             _3h_CHI2        = config['_3h_CHI2'],
                             _3h_IPCHI2      = config['_3h_IPCHI2'],
                             _3h_PT          = config['_3h_PT'],
                             _3h_PTsum       = config['_3h_PTsum'],
                             _3h_Psum        = config['_3h_Psum'],
                             _3h_PVIPCHI2sum = config['_3h_PVIPCHI2sum'],
                             _3h_TRKCHIDOFmin= config['_3h_TRKCHIDOFmin'],
                             _3h_Charge      = config['_3h_Charge'],
                             _3h_CORRMmax    = config['_3h_CORRMmax'],
                             _3h_CORRMmin    = config['_3h_CORRMmin'],
                             _3hKKK_Mmin     = config['_3hKKK_Mmin'],
                             _3hKKK_Mmax     = config['_3hKKK_Mmax'])

	self.selpph = makepph_incl( 'pphinclFor' + _pph_inclName + 'Sel', 
                             _h_PT           = config['_h_PT'],
                             _h_P            = config['_h_P'],
                             _h_IPCHI2       = config['_h_IPCHI2'],
                             _h_TRCHI2DOF    = config['_h_TRCHI2DOF'], 
                             _3h_DOCA        = config['_3h_DOCA'],
                             _3h_PTmax       = config['_3h_PTmax'],
                             _3h_DIRA        = config['_3h_DIRA'],
                             _3h_FDCHI2      = config['_3h_FDCHI2'],
                             _3h_PVDOCAmin   = config['_3h_PVDOCAmin'],
                             _3h_CHI2        = config['_3h_CHI2'],
                             _3h_IPCHI2      = config['_3h_IPCHI2'],
                             _3h_PT          = config['_3h_PT'],
                             _3h_PTsum       = config['_3h_PTsum'],
                             _3h_Psum        = config['_3h_Psum'],
                             _3h_PVIPCHI2sum = config['_3h_PVIPCHI2sum'],
                             _3h_TRKCHIDOFmin= config['_3h_TRKCHIDOFmin'],
                             _3h_Charge      = config['_3h_Charge'],
                             _3h_CORRMmax    = config['_3h_CORRMmax'],
                             _3h_CORRMmin    = config['_3h_CORRMmin'],
                             _3hpph_deltaMmax= config['_3hpph_deltaMmax'],
                             _3hpph_deltaMmin= config['_3hpph_deltaMmin'])

	self.gECFilter = globalEventCutFilter(name + 'GlobalEventCutFilter', MaxTrSIZE = config['MaxTrSIZE'])
	
        self.algosKKK = []
        if self.gECFilter != None  : self.algosKKK.append(self.gECFilter)

	self.algosKKK.append(self.selKKK)
	
        self.algospph = []
        if self.gECFilter != None : self.algospph.append(self.gECFilter)

        self.algospph.append(self.selpph)	
	

        self.lineKKK_incl = StrippingLine( _KKK_inclName + 'Line',
                                     prescale   = config['KKK_inclLinePrescale'],
                                     postscale  = config['KKK_inclLinePostscale'],
                                     algos      = self.algosKKK)
        
	self.linepph_incl = StrippingLine( _pph_inclName + 'Line',
                                     prescale   = config['pph_inclLinePrescale'],
                                     postscale  = config['pph_inclLinePostscale'],
                                     algos      = self.algospph)

        self.registerLine(self.lineKKK_incl)
        self.registerLine(self.linepph_incl)


def makeKKK_incl(name,
           _h_PT,
           _h_P,
           _h_IPCHI2,
           _h_TRCHI2DOF,
           _3h_DOCA,
           _3h_PTmax,
           _3h_DIRA,
           _3h_FDCHI2,
           _3h_PVDOCAmin,
           _3h_CHI2,
           _3h_IPCHI2,
           _3h_PT,
           _3h_PTsum,
           _3h_Psum,
           _3h_PVIPCHI2sum,
	   _3h_TRKCHIDOFmin,
           _3h_Charge,
           _3h_CORRMmax,
           _3h_CORRMmin,
           _3hKKK_Mmin,
           _3hKKK_Mmax) :

    _daughtersCuts = {"K+" : "(PT > %(_h_PT)s*MeV) \
                             & (P > %(_h_P)s*MeV) \
                             & (MIPCHI2DV(PRIMARY) > %(_h_IPCHI2)s) \
                             & (TRCHI2DOF < %(_h_TRCHI2DOF)s)" % locals()}
    _combinationCut = "(AM < %(_3hKKK_Mmax)s*MeV) \
                     & (AM > %(_3hKKK_Mmin)s*MeV) \
		     & (AMAXDOCA('LoKi::TrgDistanceCalculator') < %(_3h_DOCA)s)" % locals()
    _motherCut = "(MAXTREE(((ABSID=='K+') | (ABSID=='K-')),PT) > %(_3h_PTmax)s*MeV) \
                & (BPVDIRA > %(_3h_DIRA)s) \
		& (BPVVDCHI2 > %(_3h_FDCHI2)s) \
		& (VFASPF(VMINVDDV(PRIMARY)) > %(_3h_PVDOCAmin)s) \
		& (VFASPF(VCHI2) < %(_3h_CHI2)s) \
		& (MIPCHI2DV(PRIMARY) < %(_3h_IPCHI2)s) \
		& (PT > %(_3h_PT)s*MeV) \
		& (SUMTREE(PT,((ABSID=='K+') | (ABSID=='K-')),0.0) > %(_3h_PTsum)s*MeV) \
		& (SUMTREE(P,((ABSID=='K+') | (ABSID=='K-')),0.0) > %(_3h_Psum)s*MeV) \
		& (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='K+') | (ABSID=='K-')),0.0) > %(_3h_PVIPCHI2sum)s) \
		& (MINTREE((('K+'==ABSID) | ('K-'==ABSID)),TRCHI2DOF) < %(_3h_TRKCHIDOFmin)s) \
		& (abs(CHILD(Q,1) + CHILD(Q,2) + CHILD(Q,1))== %(_3h_Charge)s ) \
		& (BPVCORRM < %(_3h_CORRMmax)s * MeV)& (BPVCORRM > %(_3h_CORRMmin)s*MeV)" % locals()
   
    _KKK=CombineParticles()
    _KKK.DecayDescriptors  = ["[B+ -> K+ K+ K-]cc"]
    _KKK.MotherCut         = _motherCut
    _KKK.CombinationCut    = _combinationCut
    _KKK.DaughtersCuts     = _daughtersCuts

    return Selection ( name,
                       Algorithm = _KKK,
                       RequiredSelections = [StdNoPIDsKaons])


def makepph_incl(name,
           _h_PT,
           _h_P,
           _h_IPCHI2,
           _h_TRCHI2DOF,
           _3h_DOCA,
           _3h_PTmax,
           _3h_DIRA,
           _3h_FDCHI2,
           _3h_PVDOCAmin,
           _3h_CHI2,
           _3h_IPCHI2,
           _3h_PT,
           _3h_PTsum,
           _3h_Psum,
           _3h_PVIPCHI2sum,
	   _3h_TRKCHIDOFmin,
           _3h_Charge,
           _3h_CORRMmax,
           _3h_CORRMmin,
           _3hpph_deltaMmax,
           _3hpph_deltaMmin) :

    _daughtersCuts = {"p+" : "(PT > %(_h_PT)s*MeV) \
                             & (P > %(_h_P)s*MeV) \
                             & (MIPCHI2DV(PRIMARY) > %(_h_IPCHI2)s) \
                             & (TRCHI2DOF < %(_h_TRCHI2DOF)s)" % locals(),
		      "K+" :  "(PT > %(_h_PT)s*MeV) \
                             & (P > %(_h_P)s*MeV) \
                             & (MIPCHI2DV(PRIMARY) > %(_h_IPCHI2)s) \
                             & (TRCHI2DOF < %(_h_TRCHI2DOF)s)" % locals()}
    _combinationCut = "(AM < (5279.15 + %(_3hpph_deltaMmax)s)*MeV) \
                     & (AM > (5279.15 - %(_3hpph_deltaMmin)s)*MeV) \
		     & (AMAXDOCA('LoKi::TrgDistanceCalculator') < %(_3h_DOCA)s)" % locals()
    _motherCut = "(MAXTREE(((ABSID=='p+') |(ABSID=='p~-') |(ABSID=='K+') | (ABSID=='K-')),PT) > %(_3h_PTmax)s*MeV) \
                & (BPVDIRA > %(_3h_DIRA)s) \
		& (BPVVDCHI2 > %(_3h_FDCHI2)s) \
		& (VFASPF(VMINVDDV(PRIMARY)) > %(_3h_PVDOCAmin)s) \
		& (VFASPF(VCHI2) < %(_3h_CHI2)s) \
		& (MIPCHI2DV(PRIMARY) < %(_3h_IPCHI2)s) \
		& (PT > %(_3h_PT)s*MeV) \
		& (SUMTREE(PT,((ABSID=='p+') |(ABSID=='p~-') |(ABSID=='K+') | (ABSID=='K-')),0.0) > %(_3h_PTsum)s*MeV) \
		& (SUMTREE(P,((ABSID=='p+') |(ABSID=='p~-') |(ABSID=='K+') | (ABSID=='K-')),0.0) > %(_3h_Psum)s*MeV) \
		& (SUMTREE(MIPCHI2DV(PRIMARY),((ABSID=='p+') |(ABSID=='p~-') |(ABSID=='K+') | (ABSID=='K-')),0.0) > %(_3h_PVIPCHI2sum)s) \
		& (MINTREE(((ABSID=='p+') |(ABSID=='p~-') |('K+'==ABSID) | ('K-'==ABSID)),TRCHI2DOF) < %(_3h_TRKCHIDOFmin)s) \
		& (abs(CHILD(Q,1) + CHILD(Q,2) + CHILD(Q,3))== %(_3h_Charge)s ) \
		& (BPVCORRM < %(_3h_CORRMmax)s * MeV)& (BPVCORRM > %(_3h_CORRMmin)s*MeV)" % locals()
   
    _pph=CombineParticles()
    _pph.DecayDescriptors  = ["[B+ -> p+ p~- K+]cc"]
    _pph.MotherCut         = _motherCut
    _pph.CombinationCut    = _combinationCut
    _pph.DaughtersCuts     = _daughtersCuts

    return Selection ( name,
                       Algorithm = _pph,
                       RequiredSelections = [StdNoPIDsKaons,StdTightProtons])


def globalEventCutFilter(name, 
	                 MaxTrSIZE = None 
	                 ) :
  
  if MaxTrSIZE == None : return None
  
  _code = ""
  from Configurables import LoKi__VoidFilter as VoidFilter
  from Configurables import LoKi__Hybrid__CoreFactory as CoreFactory
  modules = CoreFactory('CoreFactory').Modules
  for i in ['LoKiTracks.decorators']:
     if i not in modules : modules.append(i)
  if MaxTrSIZE != None : _code += "TrSOURCE('Rec/Track/Best') >> (TrSIZE < %(MaxTrSIZE)s )" % locals()
  globalFilter= VoidFilter(name)
  globalFilter.Code = _code
  
  return globalFilter

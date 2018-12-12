'''
Module for construction of Bs-->PhiK*0 stripping selections and lines

Exported symbols (use python help!):
   - StrippingBs2PhiKstConf
   - makeBs2PhiKst
   - makeKst2Kpi
   - makePhi2KK
'''

__author__ = ['Cibran Santamarina','Brais Sanmartin Sedes']
__date__ = '27/08/2014'
__version__= '4.0'

__all__=('StrippingBs2PhiKstConf',
         'makeBs2PhiKst',
         'makeKst2Kpi',
         'makePhi2KK',
	 'default_config')


default_config = {
	"NAME"	      	: "Bs2PhiKst",
	"WGs"	      	: ['Charmless'],
	"BUILDERTYPE" 	: 'StrippingBs2PhiKstConf',
	"CONFIG"	: {"KaonPT"                : 500.0 
          ,     "KaonIPCHI2"            : 9.    
          ,     "KaonPIDK"              : 0.    
          ,     "PionPT"                : 500.0 
          ,     "PionIPCHI2"            : 9.    
          ,     "PionPIDK"              : 10.    
          ,     "PhiVCHI2"              : 9.    
          ,     "PhiPT"                 : 900.0 
          ,     "PhiMassWin"            : 25.0  
          ,     "KstarVCHI2"            : 9.0   
          ,     "KstarPT"               : 900.0 
          ,     "KstarMassWin"          : 150.0 
          ,     "BMassWin"              : 500.0 
          ,     "BVCHI2"                : 15.0  
          ,     "BDOCA"                 : 0.3   
          ,  "BDIRA"                    : 0.99     
          					},
	"STREAMS"	: ['Bhadron']
	}




from Gaudi.Configuration import *
from LHCbKernel.Configuration import *
from CommonParticles.Utils import *
from Configurables import FilterDesktop, CombineParticles, OfflineVertexFitter	
from PhysSelPython.Wrappers import Selection, SelectionSequence, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder

default_name = "Bs2PhiKst"

#confdict = {
#          "KaonPT"                : 500.0 # MeV
#          ,     "KaonIPCHI2"            : 9.    # adimensional
#          ,     "KaonPIDK"              : 0.    # adimensional
#          ,     "PionPT"                : 500.0 # MeV
#          ,     "PionIPCHI2"            : 9.    # adimensional
#          ,     "PionPIDK"              : 10.    # adimensional
#          ,     "PhiVCHI2"              : 9.    # adimensional
#          ,     "PhiPT"                 : 900.0 # MeV
#          ,     "PhiMassWin"            : 25.0  # MeV
#          ,     "KstarVCHI2"            : 9.0   # adimensional
#          ,     "KstarPT"               : 900.0 # MeV
#          ,     "KstarMassWin"          : 150.0 # MeV
#          ,     "BMassWin"              : 500.0 # MeV
#          ,     "BVCHI2"                : 15.0  # adimensional
#          ,     "BDOCA"                 : 0.3   # mm
#          ,  "BDIRA"                    : 0.99      # adimensional
#          }


class StrippingBs2PhiKstConf(LineBuilder):
     """
     Builder of:
     - Bs-> Phi Kst0 stripping line (Bs2PhiKst)

     Usage:
     >>> config = { .... }
     >>> bsConf = StrippingBs2PhiKstConf('Bs2PhiKstTest',config)
     >>> bsLines = bsConf.lines
     >>> for line in line :
     >>>  print line.name(), line.outputLocation()
     The lines can be used directly to build a StrippingStream object.


     Exports as instance data members:
     selKst2Kpi               : nominal Kst->Kpi Selection object
     selBs2KstKst             : nominal Bs -> Kst(K+pi-) anti-Kst(K-pi+) Selection object
     Bs2KstKst_line           : StrippingLine made out of selBs2KstKst
     lines                    : List of lines, [Bs2KstKst_line]
    
     Exports as class data member:
     StrippingBs2PhiKstConf.__configuration_keys__ : List of required configuration parameters.
     """
     __configuration_keys__ = (
          "KaonPT",
          "KaonIPCHI2",
          "KaonPIDK",
          "PionPT",
          "PionIPCHI2",
          "PionPIDK",
          "PhiVCHI2",
          "PhiPT",
          "PhiMassWin",
          "KstarVCHI2",
          "KstarPT",
          "KstarMassWin",
          "BMassWin",
          "BVCHI2",
          "BDOCA",
          "BDIRA")


     def __init__(self, name, config) :

          LineBuilder.__init__(self, name, config)

          PhiKst_name = name+"Nominal"

          self.selKst2Kpi = makeKst2Kpi('Kst2KpiFor'+name,
                                        KaonPT = config['KaonPT'],
                                        KaonIPCHI2 = config['KaonIPCHI2'],
                                        PionPT = config['PionPT'],
                                        PionIPCHI2 = config['PionIPCHI2'],
                                        PionPIDK = config['PionPIDK'],
                                        KstarPT = config["KstarPT"],
                                        KaonPIDK = config['KaonPIDK'],
                                        KstarVCHI2 = config['KstarVCHI2'],
                                        KstarMassWin = config['KstarMassWin'])

          self.selPhi2KK = makePhi2KK('Phi2KKFor'+name,
                                    KaonPT = config['KaonPT'],
                                    KaonIPCHI2 = config['KaonIPCHI2'],
                                    KaonPIDK = config['KaonPIDK'],
                                    PhiMassWin = config['PhiMassWin'],
                                    PhiPT = config['PhiPT'],
                                    PhiVCHI2 = config['PhiVCHI2'])

          self.selBs2PhiKst = makeBs2PhiKst(PhiKst_name,
                                            Phisel = self.selPhi2KK,
                                            Kstsel = self.selKst2Kpi,
                                            BMassWin = config['BMassWin'],
                                            BVCHI2 = config['BVCHI2'],
                                            BDOCA = config['BDOCA'],
                                            BDIRA = config['BDIRA'])
          
          self.Bs2PhiKst_line = StrippingLine(PhiKst_name+"Line",
                                              prescale = 1,
                                              postscale = 1,
                                              algos = [ self.selBs2PhiKst ]
                                              )

          self.registerLine(self.Bs2PhiKst_line)

def makePhi2KK( name,
                KaonPT,
                KaonIPCHI2,
                KaonPIDK,
                PhiMassWin,
                PhiPT,
                PhiVCHI2):

    """
    Create and return a Phi -> KK Selection object.
    Starts from DataOnDemand 'Phys/StdLoosePhi2KK'.
    Arguments:
    name             : name of the Selection.
    KaonPT           : Minimum transverse momentum of K (MeV).
    KaonIPCHI2       : Minimum impact parameter chi2 of K.
    KaonPIDK         : Minimum PID_{K-pi} of K.
    PhiPT            : Minimum transverse momentum of Phi (MeV).
    PhiMassWin       : Phi invariant mass window around PDG mass value (MeV).
    PhiVCHI2         : Maximum Phi vertex chi2 (per degree of freedom?)
    """

    _params = locals()
    _code = " (MINTREE('K+'==ABSID,PIDK)> %(KaonPIDK)s)"    \
            "& (MINTREE(ABSID=='K+',PT)> %(KaonPT)s *MeV)"  \
            "& (MINTREE(ABSID=='K+',MIPCHI2DV(PRIMARY))> %(KaonIPCHI2)s)"        \
            "& (ADMASS('phi(1020)') < %(PhiMassWin)s *MeV)" \
            "& (PT > %(PhiPT)s *MeV)" \
            "& (VFASPF(VCHI2/VDOF) < %(PhiVCHI2)s)" % _params
    StdLoosePhi2KK = DataOnDemand(Location = "Phys/StdLoosePhi2KK/Particles")
    _phiFilter = FilterDesktop("PhiFilterForBs2JpsiPhi",
                               Code = _code)

    return Selection (name,
                      Algorithm = _phiFilter,
                      RequiredSelections = [StdLoosePhi2KK])


def makeKst2Kpi(name,
                KaonPT,
                KaonIPCHI2,
                PionPT,
                PionIPCHI2,
                PionPIDK,
                KstarPT,
                KaonPIDK,
                KstarVCHI2,
                KstarMassWin):

    """
    Create and return a Kstar -> K+pi- Selection object.
    Starts from DataOnDemand 'Phys/StdVeryLooseDetachedKst2Kpi'.
    Arguments:
    name             : name of the Selection.
    KaonPT           : Minimum transverse momentum of K (MeV).
    KaonIPCHI2       : Minimum impact parameter chi2 of K.
    PionPT           : Minimum transverse momentum of pi (MeV).
    PionIPCHI2       : Minimum impact parameter chi2 of pi.
    PionPIDK         : Maximum PID_{K-pi} of pi.
    KstarPT          : Minimum transverse momentum of Kstar (MeV).
    KaonPIDK         : Minimum PID_{K-pi} of K.
    KstarVCHI2       : Maximum Kstar vertex chi2 per degree of freedom.
    KstarMassWin     : Kstar invariant mass window around PDG mass value (MeV).
    """


    KstarCuts = "(INTREE((ABSID=='K+') & (PT > %(KaonPT)s *MeV) & (MIPCHI2DV(PRIMARY)> %(KaonIPCHI2)s) & (PIDK > %(KaonPIDK)s)  ))"\
        "& (INTREE((ABSID=='pi-') & (PT > %(PionPT)s *MeV) & (MIPCHI2DV(PRIMARY)> %(PionIPCHI2)s) & (PIDK < %(PionPIDK)s)  ))"\
        "& (ADMASS('K*(892)0') < %(KstarMassWin)s *MeV)"\
        "& (BPVDIRA > 0) & (VFASPF(VCHI2/VDOF)< %(KstarVCHI2)s) & (PT > %(KstarPT)s *MeV)"% locals()


    _KstarFilter = FilterDesktop("_filterFor"+name)
    _KstarFilter.Code = KstarCuts
    _stdKst2Kpi = DataOnDemand(Location="Phys/StdVeryLooseDetachedKst2Kpi/Particles")


    return Selection (name,
                      Algorithm = _KstarFilter,
                      RequiredSelections = [_stdKst2Kpi])


def makeBs2PhiKst(name,
                  Phisel,
                  Kstsel,
                  BMassWin,
                  BVCHI2,
                  BDOCA,
                  BDIRA):
       """
       Create and return a Bs -> Phi (KK) Kstar (Kpi) Selection object.
       Arguments:
       name        : name of the Selection.
       Phisel      : Phi -> K+K- Selection object.
       Kstsel      : Kst -> K+pi- Selection object.
       BMassWin    : Bs invariant mass window around PDG mass value (MeV).
       BVCHI2      : Maximum Bs vertex chi2 per degree of freedom.
       BDOCA       : Maximum Bs DOCA.
       """ 
       
       _motherCuts = "(VFASPF(VCHI2/VDOF) < %(BVCHI2)s) & (BPVDIRA > %(BDIRA)s)"% locals()
       _combinationCut = "(ADAMASS('B_s0') < %(BMassWin)s *MeV) & (AMAXDOCA('')< %(BDOCA)s *mm)" % locals() 

       _Bs = CombineParticles('_'+name)
       _Bs.DecayDescriptor = "[B_s0 -> phi(1020) K*(892)~0]cc"
       _Bs.CombinationCut = _combinationCut
       _Bs.MotherCut = _motherCuts

       _Bs.ReFitPVs = True

       _Bs.addTool( OfflineVertexFitter )
#       _Bs.VertexFitters.update( { "" : "OfflineVertexFitter"} )
       _Bs.ParticleCombiners.update( { "" : "OfflineVertexFitter"} ) # Fix for DaVinci v32r0 by A.Poluektov
       _Bs.OfflineVertexFitter.useResonanceVertex = False


       return Selection ( name,
                          Algorithm = _Bs,
                          RequiredSelections = [Phisel,Kstsel])

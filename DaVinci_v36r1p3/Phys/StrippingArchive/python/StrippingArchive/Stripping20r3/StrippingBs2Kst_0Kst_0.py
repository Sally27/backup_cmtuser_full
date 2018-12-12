'''
Module for construction of Bs-->K*_0(1430)0 K*_0(1430)~0 stripping selections and lines

Exported symbols (use python help!):
   - StrippingBs2Kst_0Kst_0Conf
   - makeBs2Kst_0Kst_0
   - makeKst_02Kpi
'''

__author__ = ['Paula Alvarez Cartelle']
__date__ = '26/08/2011'
__version__= '2.0'

__all__=('StrippingBs2Kst_0Kst_0Conf',
         'makeBs2Kst_0Kst_0',
         'makeKst_02Kpi')


__config_default__ = { 
     "KaonPT"		: 500.0 # MeV
     ,  "KaonIPCHI2"	: 9. 	# adimensional
     ,  "PionPT"           : 500.0 # MeV
     ,  "PionIPCHI2"       : 9.	# adimensional
     ,  "PionPIDK"         : 0. #adimensional
     ,  "KstarVCHI2"	: 9.0   # adimensional
     ,  "KstarPT"		: 900.0 # MeV
     ,  "KaonPIDK"         : 2.0  # adimensional
     ,  "KstarMassWin"     : 680.0 # MeV 
     ,  "KstarAPT"         : 800.0 # MeV
     ,  "BMassWin"		: 500.0 # MeV
     ,  "BVCHI2"		: 15.0	# adimensional
     ,  "BDOCA"            : 0.3   # mm
     ,  "BIPCHI2"          : 25.   # adimensional
     ,  "BFDistanceCHI2"   : 81.   # adimensional
     ,  "SumPT"            : 5000  # MeV
     ,  "MaxGHOSTPROB"             : 0.8   # adimensional
     ,  "BDIRA"                    : 0.99      # adimensional
     }

from Gaudi.Configuration import *
from LHCbKernel.Configuration import *
from CommonParticles.Utils import *
from Configurables import FilterDesktop, CombineParticles, OfflineVertexFitter	
from PhysSelPython.Wrappers import Selection, SelectionSequence, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder


default_name = "Bs2Kst_0Kst_0"


class StrippingBs2Kst_0Kst_0Conf(LineBuilder):
     """
     Builder of:
     - Bs-> Kst_0(1430)0 anti-Kst_0(1430)0 stripping line (Bs2Kst_0Kst_0)
     

     Usage:
     >>> config = { .... }
     >>> bsConf = StrippingBs2KstKst_0Conf('Bs2KstKst_0Test',config)
     >>> bsLines = bsConf.lines
     >>> for line in line :
     >>>  print line.name(), line.outputLocation()
     The lines can be used directly to build a StrippingStream object.


     Exports as instance data members:
     selKst_02Kpi             : nominal Kst_0->Kpi Selection object
     selBs2Kst_0Kst_0         : nominal Bs -> Kst_0(1430)(K+pi-) anti-Kst_0(1430)(K-pi+) Selection object
     Bs2Kst_0Kst_0_line         : StrippingLine made out of selBs2Kst_0Kst_0
     
     lines                    : List of lines, [Bs2Kst_0Kst_0_line]
    
     Exports as class data member:
     StrippingBs2Kst_0Kst_0Conf.__configuration_keys__ : List of required configuration parameters.
     """
     __configuration_keys__ = (
          "KaonPT",
          "KaonIPCHI2",
          "PionPT",
          "PionIPCHI2",
          "PionPIDK",
          "KstarVCHI2",
          "KstarPT",
          "KaonPIDK",
          "KstarMassWin",
          "KstarAPT",
          "BMassWin",
          "BVCHI2",
          "BDOCA",
          "BIPCHI2",
          "BFDistanceCHI2",
          "SumPT",
          "MaxGHOSTPROB",
          "BDIRA")


     


     def __init__(self, name, config) :

          LineBuilder.__init__(self, name, config)

          Kst_0Kst_0_name = name+"Nominal"


          self.selKst_02Kpi = makeKst_02Kpi('Kst_02KpiFor'+name,
                                        KaonPT = config['KaonPT'],
                                        KaonIPCHI2 = config['KaonIPCHI2'],
                                        PionPT = config['PionPT'],
                                        PionIPCHI2 = config['PionIPCHI2'],
                                        KstarPT = config["KstarPT"],
                                        KstarAPT = config["KstarAPT"],
                                        KaonPIDK = config['KaonPIDK'],
                                        KstarVCHI2 = config['KstarVCHI2'],
                                        KstarMassWin = config['KstarMassWin'],
                                        PionPIDK = config['PionPIDK'],
                                        MaxGHOSTPROB = config['MaxGHOSTPROB'])



          self.selBs2Kst_0Kst_0 = makeBs2Kst_0Kst_0(Kst_0Kst_0_name,
                                            Kst_0sel = self.selKst_02Kpi,
                                            BMassWin = config['BMassWin'],
                                            BVCHI2 = config['BVCHI2'],
                                            BDOCA = config['BDOCA'],
                                            BIPCHI2 = config['BIPCHI2'],
                                            BFDistanceCHI2 = config['BFDistanceCHI2'],
                                            SumPT = config['SumPT'],
                                            BDIRA = config['BDIRA'])
          
        
          self.Bs2Kst_0Kst_0_line = StrippingLine(Kst_0Kst_0_name+"Line",
                                              prescale = 1,
                                              postscale = 1,
                                              algos = [ self.selBs2Kst_0Kst_0 ]
                                              )
          

          self.registerLine(self.Bs2Kst_0Kst_0_line)




        
def makeKst_02Kpi(name,
                KaonPT,
                KaonIPCHI2,
                PionPT,
                PionIPCHI2,
                KstarPT,
                KstarAPT,
                KaonPIDK,
                KstarVCHI2,
                KstarMassWin,
                PionPIDK,
                MaxGHOSTPROB):

    """
    Create and return a Kstar_0(1430) -> K+pi- Selection object.
    Starts from DataOnDemand 'Phys/StdLoosePions' and 'Phys/StdLooseKaons'.
    Arguments:
    name             : name of the Selection.
    KaonPT           : Minimum transverse momentum of K (MeV).
    KaonIPCHI2       : Minimum impact parameter chi2 of K.
    PionPT           : Minimum transverse momentum of pi (MeV).
    PionIPCHI2       : Minimum impact parameter chi2 of pi.
    PionPIDK         : Maximum PID_{K-pi} of pi.
    KstarPT          : Minimum transverse momentum of Kstar (MeV).
    KstarAPT         : Minimum transverse momentum of Kpi (MeV).
    KaonPIDK         : Minimum PID_{K-pi} of K.
    KstarVCHI2       : Maximum Kstar vertex chi2 per degree of freedom.
    KstarMassWin     : Kstar invariant mass window around PDG mass value (MeV).
    MaxGHOSTPROB     : Maximum Ghost Probability
    """


    _stdKaons = DataOnDemand(Location="Phys/StdLooseKaons/Particles")
    _stdPions = DataOnDemand(Location="Phys/StdLoosePions/Particles")


    _Kstar_02Kpi = CombineParticles ("Combine"+name)

    _Kstar_02Kpi.DecayDescriptor = "[K*_0(1430)0 -> K+ pi-]cc"
    _Kstar_02Kpi.DaughtersCuts = {"K+" : "(PT > %(KaonPT)s *MeV) & (PIDK > %(KaonPIDK)s) & (MIPCHI2DV(PRIMARY)> %(KaonIPCHI2)s) & (TRGHOSTPROB < %(MaxGHOSTPROB)s)"% locals()
                                ,"pi-" : "(PT > %(PionPT)s *MeV) & (PIDK < %(PionPIDK)s) & (MIPCHI2DV(PRIMARY)> %(PionIPCHI2)s) & (TRGHOSTPROB < %(MaxGHOSTPROB)s)"% locals()}
                                
    _Kstar_02Kpi.CombinationCut = "(ADAMASS('K*_0(1430)0') < %(KstarMassWin)s *MeV) & (APT > %(KstarAPT)s *MeV)"% locals()
    _Kstar_02Kpi.MotherCut = "(VFASPF(VCHI2/VDOF)< %(KstarVCHI2)s) & (PT > %(KstarPT)s *MeV)"% locals()



    return Selection (name,
                      Algorithm = _Kstar_02Kpi,
                      RequiredSelections = [_stdKaons,_stdPions])




def makeBs2Kst_0Kst_0(name,
                  Kst_0sel,
                  BMassWin,
                  BVCHI2,
                  BDOCA,
                  BIPCHI2,
                  BFDistanceCHI2,
                  SumPT,
                      BDIRA):

       """
       Create and return a Bs -> Kstar_0(1430)(Kpi) anti-Kstar_0(1430)(Kpi) Selection object.
       Arguments:
       name           : name of the Selection.
       Kst_0sel       : Kst_0(1430) -> K+pi- Selection object.
       BMassWin       : Bs invariant mass window around PDG mass value (MeV).
       BVCHI2         : Maximum Bs vertex chi2 per degree of freedom.
       BDOCA          : Maximum Bs DOCA.
       BFDistanceCHI2 : Minimum Bs Flight Distance chi2.
       SumPT          : Sum|pT| of the daughters.
       """ 
       
       _motherCuts = " (VFASPF(VCHI2/VDOF) < %(BVCHI2)s) & (MIPCHI2DV(PRIMARY)< %(BIPCHI2)s) & (BPVVDCHI2 > %(BFDistanceCHI2)s) & (BPVDIRA > %(BDIRA)s)"% locals()
       _combinationCut = "(ADAMASS('B_s0') < %(BMassWin)s *MeV) & (AMAXDOCA('')< %(BDOCA)s *mm) "\
                         "& ( (AMINCHILD(PT,ID=='K+') + AMINCHILD(PT,ID=='K-') + AMINCHILD(PT,ID=='pi-') + AMINCHILD(PT,ID=='pi+'))> %(SumPT)s *MeV)" % locals() 

       _Bs = CombineParticles('_'+name)
       _Bs.DecayDescriptor = "B_s0 -> K*_0(1430)0 K*_0(1430)~0"
       _Bs.CombinationCut = _combinationCut
       _Bs.MotherCut = _motherCuts

       _Bs.ReFitPVs = True

       _Bs.addTool( OfflineVertexFitter )
#       _Bs.VertexFitters.update( { "" : "OfflineVertexFitter"} )
       _Bs.ParticleCombiners.update( { "" : "OfflineVertexFitter"} ) # Fix for DaVinci v32r0 by A.Poluektov 
       _Bs.OfflineVertexFitter.useResonanceVertex = False


       return Selection ( name,
                          Algorithm = _Bs,
                          RequiredSelections = [Kst_0sel])




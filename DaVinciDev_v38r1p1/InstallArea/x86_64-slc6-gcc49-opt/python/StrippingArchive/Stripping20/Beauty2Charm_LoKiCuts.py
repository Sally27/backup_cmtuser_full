#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop
from GaudiConfUtils.ConfigurableGenerators import CombineParticles
from PhysSelPython.Wrappers import Selection, MergedSelection
from StandardParticles import StdNoPIDsPions, StdNoPIDsKaons

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

class LoKiCuts(object):
    ''' Class to automatically build LoKi cut strings.

    Each functor has a "key" which is just the functor name if the functor does
    not have any special characters or ()s.  See the "functors" dictionary
    below for the full list of keys (the values are the functor strings).

    The cut string is built by supplying a dictionary of cuts and a list of
    functor keys to use.  The entries in the cuts dict must be of the form
    <functor key>_<MIN or MAX> : <value>.

    Ex.) cuts = {"PT_MIN":"500*MeV", "VCHI2DOF_MAX":30, "ASUMPT_MIN":"1*GeV"}
         code = LoKiCuts(["PT","VCHI2DOF"],cuts).code()

    The result is: "(PT > 500*MeV) & (VFASPF(VCHI2/VDOF) < 30)".  Notice that
    the MIN and MAX suffixes determine the > or < usage (both are allowed if
    the user supplies separate entries to the cuts dict).  Also notice how the
    full functor is used (not the key) and that cuts are ignored if the key
    is not supplied to LoKiCuts.
    '''
    
    functors = {'TRCHI2DOF' : 'TRCHI2DOF',
                'P'         : 'P',
                'PT'        : 'PT',
                'MIPCHI2DV' : 'MIPCHI2DV(PRIMARY)',
                'ASUMPT'    : 'ASUM(PT)',
                'AMAXDOCA'  : "ACUTDOCA(%s,'LoKi::DistanceCalculator')",
                #'AMAXDOCA' : "AMAXDOCA('LoKi::DistanceCalculator')" 
                'VCHI2DOF'  : "VFASPF(VCHI2/VDOF)",
                'BPVVDCHI2' : 'BPVVDCHI2',
                'BPVDIRA'   : 'BPVDIRA',
                'SUMPT'     : "ASUM(SUMTREE(PT,(ISBASIC | (ID=='gamma')),0.0))",
                'BPVIPCHI2' : 'BPVIPCHI2()',
                'BPVLTIME'  : 'BPVLTIME()',
                'MM'        : 'MM',
                'CHILDCL1'  : 'CHILD(CL,1)',
                'CHILDCL2'  : 'CHILD(CL,2)',
                'PIDK'      : 'PIDK',
                'PIDp'      : 'PIDp',
                'BPVVDRHO'  : 'BPVVDRHO',
                'BPVVDZ'    : 'BPVVDZ',
                'DOCAMAX'   : 'DOCAMAX',
                'AM'        : 'AM',
                'CL'        : 'CL', 
                'TRGHP'     : 'TRGHP'
                }
                
    def __init__(self,cuts,config):
        self.cuts = cuts
        self.config = config

    def code(self):
        cuts = []
        for cut in self.cuts: cuts += self._getCut(cut)
        return LoKiCuts.combine(cuts)
        
    def _getCut(self,cut):
        cuts = []
        fun = self.functors[cut]
        if cut is 'AMAXDOCA': # Use ACUTDOCA instead (slightly faster)
            if self.config.has_key(cut+'_MAX'):
                return [fun%self.config[cut+'_MAX']]
            else: # Look for ADOCA(N,M) entries
                for key,val in self.config.iteritems():
                    if key.startswith('ADOCA') and key.endswith('MAX'):
                        cuts.append(key.replace('_MAX','')+'<'+str(val))
                return cuts
        for key,val in self.config.iteritems():
            if key.startswith(cut+'_'):                
                if key.endswith('MIN'): cuts.append(fun+'>'+str(val))
                else: cuts.append(fun+'<'+str(val))
        return cuts

    @staticmethod
    def cutValue(cut):
        '''Takes X*Units and returns X as an int and Units'''
        info = cut.split('*')
        return (int(info[0]),info[1])

    @staticmethod
    def combine(cuts):
        '''Simple combine of list of LoKi cut strings.'''
        cutList = []
        for c in cuts:
            if c:
                if not c.startswith('('): c = '('+c+')'
                cutList.append(c)
        return ' & '.join(cutList)

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

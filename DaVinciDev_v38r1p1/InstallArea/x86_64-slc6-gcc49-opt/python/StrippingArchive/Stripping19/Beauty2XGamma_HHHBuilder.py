#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

from copy import deepcopy
from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import CombineParticles
from PhysSelPython.Wrappers import Selection
from Beauty2Charm_LoKiCuts import LoKiCuts
from Beauty2XGamma_Utils import *

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

class HHHBuilder(object):
    '''Produces all HHH quasi-particles for the Beauty2XGamma module.'''

    def __init__(self,pions,kaons,protons,pi0,config):
        self.pions = filterInputs("HHHPions",[pions],config['DAUGHTERS'])
        self.kaons = filterInputs("HHHKaons",[kaons],config['DAUGHTERS'])
        self.protons = filterInputs("HHHProtons",[protons],config['DAUGHTERS'])
        self.pi0 = pi0
        self.config = config
        #self.pipipi = [self._makePiPiPi()]
        #self.kpipi = [self._makeKPiPi()]
        #self.ppbarpi = [self._makeppbarPi()]
        #self.ppbark = [self._makeppbarK()]
        #self.pipipi0 = [self._makePiPiPi0()]
        self.omega = self._makeOmegaHHH()

    def _massWindow(self,which,name):
        return "ADAMASS('%s') < %s" % (name,self.config['MASS_WINDOW'][which])

    def _makeX2HHH(self,name,decays,amass,config,inputs,pi0=False):
        ''' Makes all X -> HHH selections involving neutrals.'''
        comboCuts = [LoKiCuts(['ASUMPT'],config).code(),amass,hasTopoChild()]
        comboCuts = LoKiCuts.combine(comboCuts)
        momCuts = LoKiCuts(['VCHI2DOF','BPVVDCHI2'],config).code()
        cp = CombineParticles(CombinationCut=comboCuts,MotherCut=momCuts,DecayDescriptors=decays)
        if pi0:
            cp = cp.configurable(name+'Beauty2XGammaCombiner')
            cp.ParticleCombiners = { '' : 'LoKi::VertexFitter' }
        return Selection(name+'Beauty2XGamma',Algorithm=cp,RequiredSelections=inputs)

#    def _makePiPiPi(self):
#       '''Makes X -> pi+pi-pi+'''
#        massWindow = "(AM < %s)" % (self.config['MASS_WINDOW']['A1'])
#        return self._makeX2HHH('X2PiPiPi',['[a_1(1260)+ -> pi+ pi- pi+]cc'],
#                              massWindow,self.config,[self.pions])

#    def _makeKPiPi(self):
#        '''Makes X -> K+pi-pi+ + c.c.'''
#        massWindow = "(AM < %s)" % (self.config['MASS_WINDOW']['K1'])
#        return self._makeX2HHH('X2KPiPi',['[K_1(1270)+ -> K+ pi- pi+]cc'],
#                              massWindow,self.config,
#                              [self.pions,self.kaons])

#    def _makeppbarPi(self):
#        '''Makes X -> p pbar-pi+ + c.c.'''
#        massWindow = "(AM < %s)" % (self.config['MASS_WINDOW']['PPH'])
#        return self._makeX2HHH('X2ppbarPi',['[a_1(1260)+ -> p+ p~- pi+]cc'],
#                              massWindow,self.config,
#                              [self.pions,self.protons])

#    def _makeppbarK(self):
#        '''Makes X -> p pbar-K+ + c.c.'''
#        massWindow = "(AM < %s)" % (self.config['MASS_WINDOW']['PPH'])
#        return self._makeX2HHH('X2ppbarK',['[a_1(1260)+ -> p+ p~- K+]cc'],
#                              massWindow,self.config,
#                              [self.kaons,self.protons])
    
    def _makeOmegaHHH(self):    
        '''Makes omega -> pi pi pi0 + cc '''
        #massWindow = '(750*MeV < AM < 815*MeV)'
        #massWindow = "(AM < %s)" % (self.config['MASS_WINDOW']['OMEGA'])

        r = self._makeX2HHH('Omega2PiPiPi0Resolved',['omega(782) -> pi+ pi- pi0'],'(AM<1200*MeV)',self.config,[self.pions]+self.pi0['Resolved'],True)
        m = self._makeX2HHH('Omega2PiPiPi0Merged',['omega(782) -> pi+ pi- pi0'],'(AM<1200*MeV)',self.config,[self.pions]+self.pi0['Merged'],True)
        mass = self._massWindow('OMEGA','omega(782)').replace('ADAMASS','ADMASS')
        presel = MergedSelection('Omega2PiPiPi0Beauty2XGamma',RequiredSelections=[r,m])
        return [filterSelection('Omega2PiPiPi0',mass,[presel])]

#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\#

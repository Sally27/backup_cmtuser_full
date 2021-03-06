from copy import deepcopy
from Gaudi.Configuration import *
from Beauty2Charm_LoKiCuts import LoKiCuts
from Beauty2XGamma_Utils import *

class Lb2XGammaBuilder(object):
    '''Makes all Lambda_b -> X Gamma lines.'''

    def __init__(self, gamma, hh, config):
        self.gamma = gamma if isinstance(gamma, list) else [gamma]
        self.hh = hh
        self.config = deepcopy(config)
        self.config['AM_MIN'] = '4500*MeV'
        self.config['AM_MAX'] = '6700*MeV'
        self.lines = []
        # Lambda_b -> Lambda(pH) Gamma
        self._makeLb2PHGamma()

    def _makeLb2PHGamma(self):
        '''Makes RS Lb -> D0(HH) p+- H-+ + c.c.'''
        decs = ["[Lambda_b0 -> Lambda0 gamma]cc"]
        decays = {'Lb2PHGamma': decs}
        inputs = {'Lb2PHGamma': self.gamma+self.hh.ph_pid}
        rs = makeB2XSels(decays, 'Lb2PHGamma', inputs, self.config)
        self.lines.append(ProtoLine(rs,1.0))
    
# EOF

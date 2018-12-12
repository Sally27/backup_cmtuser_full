#!/usr/bin/env python
# =============================================================================
# @file Beauty2XGamma_B2XGammaBuilder.py
# @author Albert Puig Navarro (albert.puig@cern.ch)
# @date 2011-11-17
# =============================================================================

from Gaudi.Configuration import *
from Beauty2XGamma_Utils import *

class B2XGammaBuilder(object):
    '''Makes all B->XGamma decays for the Beauty2XGamma module.'''

    def __init__(self, gamma, topoPions, topoKaons, ks, pi0, hh, hhh, config):
        self.config = config
        self.topoPions = [topoPions]
        self.topoKaons = [topoKaons]
        self.hh = hh
        self.hhh = hhh
        self.ks = ks
        self.pi0 = pi0
        self.gamma = gamma if isinstance(gamma, list) else [gamma]
        self.lines = []        
        # B -> V gamma
        self._makeB2VGamma('_B2VG_')
        # B -> V P gamma
        self._makeB2VPGamma('_B2VPG_')
        # B -> VV gamma
        self._makeB2VVGamma('_B2VVG_')

    def _makeB2VGamma(self, name):
        """Makes B -> V gamma"""
        decays = { 'B2KstarGamma'    : ['[B0 -> K*(892)0 gamma]cc'],
                   'B2PhiGamma'      : ['[B_s0 -> phi(1020) gamma]cc'],
                   'B2RhoGamma'      : ['[B_s0 -> rho(770)0 gamma]cc'],
                   'B2OmegaGammaHH'  : ['[B0 -> omega(782) gamma]cc'],
                   'B2OmegaGammaHHH' : ['[B0 -> omega(782) gamma]cc'],
                   'B2KstarIsoGamma' : ['[B+ -> K*(892)+ gamma]cc'],
                   }
        inputs = { 'B2KstarGamma'    : self.gamma + self.hh.kstar0,
                   'B2PhiGamma'      : self.gamma + self.hh.phi,
                   'B2RhoGamma'      : self.gamma + self.hh.rho0,
                   'B2OmegaGammaHH'  : self.gamma + self.hh.omega,
                   'B2OmegaGammaHHH' : self.gamma + self.hhh.omega,
                   'B2KstarIsoGamma' : self.gamma + self.hh.kspi,
                   }
        b2vgamma = makeB2XSels(decays, name, inputs, self.config)
        self.lines.append(ProtoLine(b2vgamma, 1.0))

    def _makeB2VPGamma(self, name):
        """Makes B -> V P gamma"""
        # Charged
        decays = { 'B2KstarPiGamma'    : ['[B+ -> K*(892)0 pi+ gamma]cc'],
                   'B2PhiKGamma'       : ['[B+ -> phi(1020) K+ gamma]cc'],
                  }
        inputs = { 'B2KstarPiGamma'    : self.gamma + self.hh.kstar0 + self.topoPions,
                   'B2PhiKGamma'       : self.gamma + self.hh.phi + self.topoKaons,
                  }
        b2vchargedgamma = makeB2XSels(decays, name, inputs, self.config)
        # Neutral
        decays = { 'B2KstarKSLLGamma'          : ['[B0 -> K*(892)0 KS0 gamma]cc'],
                   'B2KstarKSDDGamma'          : ['[B0 -> K*(892)0 KS0 gamma]cc'],
                   'B2KstarPi0GammaResolved'   : ['[B0 -> K*(892)0 pi0 gamma]cc'],
                   'B2KstarPi0GammaMerged'     : ['[B0 -> K*(892)0 pi0 gamma]cc'],
                   'B2PhiKSGammaLL'            : ['[B_s0 -> phi(1020) KS0 gamma]cc'],
                   'B2PhiKSGammaDD'            : ['[B_s0 -> phi(1020) KS0 gamma]cc'],
                   'B2PhiPi0GammaResolved'     : ['[B_s0 -> phi(1020) pi0 gamma]cc'],
                   'B2PhiPi0GammaMerged'       : ['[B_s0 -> phi(1020) pi0 gamma]cc'],
                 }
        inputs = { 'B2KstarKSLLGamma'        : self.gamma + self.hh.kstar0 + self.ks['LL'],
                   'B2KstarKSDDGamma'        : self.gamma + self.hh.kstar0 + self.ks['DD'],
                   'B2KstarPi0GammaResolved' : self.gamma + self.hh.kstar0 + self.pi0['Resolved'],
                   'B2KstarPi0GammaMerged'   : self.gamma + self.hh.kstar0 + self.pi0['Merged'],
                   'B2PhiKSGammaLL'          : self.gamma + self.hh.phi + self.ks['LL'],
                   'B2PhiKSGammaDD'          : self.gamma + self.hh.phi + self.ks['DD'],
                   'B2PhiPi0GammaResolved'   : self.gamma + self.hh.phi + self.pi0['Resolved'],
                   'B2PhiPi0GammaMerged'     : self.gamma + self.hh.phi + self.pi0['Merged'],
                 }
        b2vneutralgamma = makeB2XSels(decays, name, inputs, self.config)      
        self.lines.append(ProtoLine(b2vchargedgamma, 1.0))
        self.lines.append(ProtoLine(b2vneutralgamma, 1.0))

    def _makeB2VVGamma(self, name):
        """Makes B -> V V gamma"""
        decays = { 'B2KstarPhiGamma'    : ['[B0 -> K*(892)0 phi(1020) gamma]cc'],
                   'Bs2KstarPhiGamma'   : ['[B_s0 -> K*(892)0 phi(1020) gamma]cc'],
                   'Bs2KstarKstarGamma' : ['[B_s0 -> K*(892)0 K*(892)0 gamma]cc'],
                   'Bs2PhiPhiGamma'     : ['[B_s0 -> phi(1020) phi(1020) gamma]cc'],
                 }
        inputs = { 'B2KstarPhiGamma'    : self.gamma + self.hh.kstar0 + self.hh.phi,
                   'Bs2KstarPhiGamma'   : self.gamma + self.hh.kstar0 + self.hh.phi,
                   'Bs2KstarKstarGamma' : self.gamma + self.hh.kstar0,
                   'Bs2PhiPhiGamma'     : self.gamma + self.hh.phi,
                 }
        b2vvgamma = makeB2XSels(decays, name, inputs, self.config)
        self.lines.append(ProtoLine(b2vvgamma, 1.0))
    
# EOF

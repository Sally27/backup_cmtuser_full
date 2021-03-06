
import os, sys
__path__ = [d for d in [os.path.join(d, 'StrippingArchive/Stripping20r0p3') for d in sys.path if d]
            if (d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1/build.x86_64-slc6-gcc49-opt') or
                d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1')) and
               (os.path.exists(d) or 'python.zip' in d)]
"""
Module with stripping selection line builder modules.
All line builders available via function lineBuilders().
"""

__author__ = 'Juan Palacios palacios@physik.uzh.ch'

# Gamma from trees
import StrippingB2DX
import StrippingUnbiasedB2DPi
import StrippingB2DXHltTisTos
import StrippingBeauty2Charm
import StrippingDstarD02Kpipi0
import StrippingB2D3H
import StrippingB2KShh

import StrippingDstarVeryLooseWithD02Kpi
import StrippingBs2PhiMuMu
import StrippingBs2JpsiPhiPrescaledAndDetatched
import StrippingB2hhLTUnbiased
import StrippingNeuroBayesMuMu
import StrippingChiCJPsiGammaConv
import StrippingB2nbody
import StrippingTwoBody_prompt
import StrippingHb2Charged2Body
import StrippingB2Kphiphi
import StrippingBd2DstarMuNu
import StrippingB0q2DplusMuX
import StrippingBd2DstarTauNu
import StrippingB2XuMuNu
import StrippingB2DMuNuX
import StrippingCharmFromBSemi
import StrippingDstarD0ToKsHHPi0
import StrippingCharmFromBSemiForProtonPID
import StrippingCharmFromBSemiForHadronAsy
import StrippingCrossSectionB2DMuNuX
import StrippingPhiToKSKS


import StrippingInclPhi
import StrippingV0ForPID

# B2CC
import StrippingB2JpsiXforBeta_s
import StrippingB2Psi2SX
import StrippingB2Psi2SXMuMu

import StrippingBs2JpsieePhi
import StrippingB2CharmlessQuasi2Body
import StrippingBs2PhiPhi
import StrippingBs2Kst0Kst0
import StrippingBs2Kst_0Kst_0
import StrippingBs2PhiKst0
import StrippingB2CharmoniumX_6H
import StrippingBs2Q2B
import StrippingB2JpsiKShh

import StrippingBs2MuMuPhi
import StrippingB2XMuMu
import StrippingBd2KstarMuMu
import StrippingB2XMuMuSS
import StrippingTriMuons
import StrippingB2XGamma
import StrippingBs2MuMuLines
import StrippingB2MuMuMuMuLines
import StrippingB2MuMuX
import StrippingBu2LLK
import StrippingBd2eeKstar
import StrippingBd2eeKstarBDT
import StrippingBd2MuMuKstarBDT
import StrippingBeauty2XGamma
import StrippingBLVLines
import StrippingLc23MuLines
import StrippingB23MuLines

import StrippingDiMuonNew
import StrippingDiMuonForXsection
import StrippingDiMuonNew
import StrippingBc2JpsiHNew
import StrippingBc2JpsiMuXNew
import StrippingJpsiMuMuforD0MuMu
import StrippingBuToKX3872
import StrippingSingleTrackTIS
import StrippingDiElectronNew
import StrippingElectronID
import StrippingCcbar2PpbarNew
import StrippingCcbar2PhiPhi
import StrippingDForBSemi
import StrippingD0ForBXX
import StrippingJpsippForD0MuMu
import StrippingCharmAssociative
import StrippingHeavyBaryons
import StrippingPsiX0
import StrippingPsiXForBandQ
import StrippingX2psiPiPi
import StrippingX2psiGamma
import StrippingBetac2PhiP
import StrippingBB2DMuNuX

import StrippingZ02MuMu
import StrippingZ02ee
import StrippingZ02TauTauProng
import StrippingWMu
import StrippingWe
import StrippingDY2MuMu
import StrippingDY2ee
import StrippingMuMuSS
import StrippingLowMult
import StrippingDiPhotonDiMuon
import StrippingA1MuMu
import StrippingHighPtTopo
import StrippingStrangeBaryons
import StrippingStrangeBaryonsNoPID
import StrippingDisplVertices
import StrippingHighPtJets
import StrippingInclbJets
import StrippingLLP2MuX
import StrippingHighPtGamma
import StrippingWMuJets
import StrippingWmuAKTJets
import StrippingWeJets
import StrippingWeAKTJets
import StrippingBjets
import StrippingDijets
import StrippingH24MuLines
import StrippingH24MuSameMassLine

import StrippingMiniBias
import StrippingProtonIonMinBias
import StrippingSbarSCorrelations

import StrippingNoPIDDstarWithD02RSKPi

import StrippingB2DMuForTauMu
import StrippingB2XTauNu
import StrippingJPsiForSL
import StrippingCharmForVub
import StrippingDstarD02KMuNu
import StrippingD02MuMu
import StrippingPromptCharm
import StrippingSigmacForPID
import StrippingD2hh
import StrippingD2KS0H_conf
import StrippingD2KS0HHH_conf
import StrippingCharmedAndCharmedStrangeSpectroscopy
import StrippingD2hhh_conf
import StrippingD2XMuMuSS
import StrippingDstarD02xx
import StrippingDstarPromptWithD02HH
import StrippingXicc
import StrippingXic2HHH
import StrippingXibc
import StrippingDstarD02KKmumuRegular
import StrippingDstarD02KKpipiRegular
import StrippingDstarPromptWithD02HHHH
import StrippingDstarPromptWithD02HHMuMu
import StrippingDstarD2KShh
import StrippingB2ppipiSigmacmm_Lcpi
import StrippingD2KShh_samesign


import StrippingD02K3PiForXSec
import StrippingD02KPiGeoForXSec
import StrippingDstar2D0Pi_D02KPiForXSec
import StrippingLambdac2PKPiForXSec
import StrippingD2PhiPiForXSec
import StrippingD2HHHForXSec
import StrippingD02HHForXSec
import StrippingD02KSKS
import StrippingB2Xic2815Sc2455

## the following two module names added December 13, 2013  M. Sokoloff
import StrippingChargedHyperons
#import StrippingKshort2MuMuPiPi

import StrippingKshort2MuMuMuMu
import StrippingKshort2PiPiMuMu
import StrippingKshort2eePiPi
import StrippingK0S24X

#import StrippingBu3hFrom2h
import StrippingB2HHPi0
import StrippingLb2V0hh
#import StrippingB2PPbar
import StrippingB2TwoBaryons
import StrippingB2FourKHigh
import StrippingBs2KKhh
import StrippingBs2KSKS
import StrippingB2XEta
import StrippingBu2KSh
import StrippingB2HHBkg

import StrippingB2SameChargeMuon
import StrippingHyperCPX
import StrippingExclusiveDiMuon

import StrippingCcbar2Baryons

# Calibration
import StrippingTrackEffDownMuon
import StrippingTrackEffVeloMuon
import StrippingTrackEffMuonTT
import StrippingMuIDCalib
import StrippingD02KPiPi0
import StrippingBeamGas
import StrippingForTriggerValidation
import StrippingDstarD02KShhForTrackingEff
import StrippingB2LcpXLc2Kpi # new to Stripping20rXp2

import StrippingD2HHLTUnbiased
import StrippingBu2hhh
import StrippingZ02TauTau
import StrippingX2D0D0
import StrippingCC2DD
import StrippingB2XTau

import StrippingK0S24X
import StrippingK0s2MuMuLines
import StrippingTau2PMuMu
import StrippingVeryDetachedJPsiLines
import StrippingInflaton2MuMuLine
import StrippingTau23MuLines
import StrippingLb2pMuNu
import StrippingLb2pMuNuVub

import StrippingLFVLines
import StrippingBu2K1MuMu
import StrippingBs2Phif0

import StrippingBu2MuNu

import StrippingDstarD2hhpi0
import StrippingDstarD0ToHHPi0
import StrippingD2XGamma

import StrippingBu2Kpi0
import StrippingB2HHBDT
import StrippingD2HHBDT
import StrippingB2DHHHForBXX
import StrippingB2KSKpi
import StrippingButo5h
import StrippingBu2rho0rhoPlus
import StrippingB2pphh
import StrippingBc2XK
import StrippingLb2PhipK

import StrippingBs2D0KS0
import StrippingB2LambdaMuLines
import StrippingTau2LambdaMuLines
import StrippingD2PiPi0
import StrippingRareStrange
import StrippingBc3h
import StrippingXibStarToXibZero

import StrippingDarkBoson
import StrippingZVTOP
import StrippingK0s2Pi0MuMuLines

import StrippingB2DHForTauMu


from sys import modules as _modules
_this = _modules[__name__]

_strippingKeys = filter ( lambda x : x[:9]=='Stripping',
                          locals().keys())

_strippingModules = [getattr(_this, _k) for _k in _strippingKeys]

from StrippingUtils.Utils import getLineBuildersFromModule as _getter

_lineBuilders = {}

for _sm in _strippingModules :
    _lineBuilders.update(_getter(_sm))

def lineBuilders() :
    """
    Return all the line builders in the module.
    """
    return dict(_lineBuilders)

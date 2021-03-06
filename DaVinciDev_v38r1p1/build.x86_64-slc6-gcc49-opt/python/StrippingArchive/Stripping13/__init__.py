
import os, sys
__path__ = [d for d in [os.path.join(d, 'StrippingArchive/Stripping13') for d in sys.path if d]
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
import StrippingDstarD02Kpipi0
import StrippingB2D3H
import StrippingBu2D0h_D02KShh_NoPID
import StrippingBu2D0h_D02KShh_NoPID_WS
import StrippingB2KShh

import StrippingDstarVeryLooseWithD02Kpi
import StrippingBs2PhiMuMu
import StrippingBs2JpsiPhiPrescaledAndDetatched
import StrippingB2hhLTUnbiased
import StrippingNeuroBayesMuMu
import StrippingB2nbody
import StrippingHb2Charged2Body
import StrippingBd2DstarMuNu
import StrippingB0q2DplusMuX
import StrippingBd2DstarTauNu
import StrippingB2XuMuNu
import StrippingB2DMuNuX
import StrippingInclPhi
import StrippingV0ForPID
import StrippingB2JpsiXforBeta_s
import StrippingB2Psi2SX
import StrippingB2Psi2SXMuMu
import StrippingBs2JpsieePhi
import StrippingB2CharmlessQuasi2Body
import StrippingBs2PhiPhi
import StrippingBs2Kst0Kst0
import StrippingBs2PhiKst0
import StrippingBs2EtacPhi
import StrippingBs2ChicPhi_Chic2KKPiPi
import StrippingBs2ChicPhi_Chic2PiPiPiPi

import StrippingBs2MuMuPhi
import StrippingB2XMuMu
import StrippingBd2KstarMuMu
import StrippingB2XMuMuSS
import StrippingTriMuons
import StrippingB2XGamma
import StrippingBs2MuMuLines
import StrippingB2MuMuMuMuLines
import StrippingBu2LLK
import StrippingBd2eeKstar
import StrippingBd2JpsieeKstar

import StrippingDiMuonNew
import StrippingBc2JpsiHNew
import StrippingBc2JpsiMuXNew
import StrippingJpsiMuMuforD0MuMu
import StrippingBuToKX3872
import StrippingSingleTrackTIS
import StrippingDiElectronNew
import StrippingElectronID
import StrippingCcbar2PpbarNew
import StrippingDForBSemi
import StrippingD0ForBXX
import StrippingJpsippForD0MuMu

import StrippingZ02MuMu
import StrippingZ02ee
import StrippingWMu
import StrippingWe
import StrippingDY2MuMu
import StrippingDY2ee
import StrippingMuMuSS
import StrippingLowMult
import StrippingDiPhotonDiMuon

import StrippingDisplVertices

import StrippingHighPtJets

import StrippingMiniBias

import StrippingNoPIDDstarWithD02RSKPi

import StrippingDstarD02KMuNu
import StrippingD02MuMu
import StrippingPromptCharm
import StrippingD2hh
import StrippingD2KS0H_conf
import StrippingCharmedAndCharmedStrangeSpectroscopy
import StrippingD2hhh_conf
import StrippingD2XMuMuSS
import StrippingDstarD02xx
import StrippingDstarPromptWithD02HH
import StrippingXicc
import StrippingDstarD02KKmumuRegular
import StrippingDstarD02KKpipiRegular
import StrippingDstarPromptWithD02HHHH
import StrippingDstarD2KShh

import StrippingD02K3PiForXSec
import StrippingD02KPiGeoForXSec
import StrippingDstar2D0Pi_D02KPiForXSec
import StrippingLambdac2PKPiForXSec
import StrippingD2PhiPiForXSec
import StrippingD2HHHForXSec
import StrippingD02HHForXSec

import StrippingBu3hFrom2h
import StrippingB2HHPi0

# Calibration
import StrippingTrackEffDownMuon
import StrippingTrackEffVeloMuon
import StrippingTrackEffMuonTT
import StrippingMuIDCalib
import StrippingD02KPiPi0
import StrippingBeamGas

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


import os, sys
__path__ = [d for d in [os.path.join(d, 'StrippingArchive/Stripping23/StrippingCharm') for d in sys.path if d]
            if (d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1/build.x86_64-slc6-gcc49-opt') or
                d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1')) and
               (os.path.exists(d) or 'python.zip' in d)]
"""
Module importing stripping selection line builder modules
for Charm WG.
"""

_selections = (
    'StrippingD02HHForXSec',
    'StrippingD02K3PiForXSec',
    'StrippingD2HHHForXSec',
    'StrippingD2PhiPiForXSec',
    'StrippingLambdac2PHHForXSec',
    'StrippingXic2PKKPiForXSec',
    'StrippingXic2PKPiForXSec',
    "StrippingB2ppipiSigmacmm_Lcpi" ,
    'StrippingPromptCharm',
    'StrippingD2hh',
    'StrippingDstarD0ToHHPi0',
    'StrippingDstarD2KShh',
    'StrippingD02KSKS',
    'StrippingCharmFromBSemi',
    'StrippingXicc',
    'StrippingChargedHyperons',
    'StrippingD2KS0H_conf',
    'StrippingDstarD2HHHH',
    'StrippingDstarD02xx',
    'StrippingD2PiPi0',
    'StrippingLambdac2V0H',
    'StrippingDstarD2XGamma',
    'StrippingD2HHHKs',
    'StrippingDstarD2KSHHPi0',
    'StrippingD2HHHPi0',
    'StrippingDstarPromptWithD02HHMuMu',
    'StrippingD2XMuMuSS',
    'StrippingCharmForVub',
    'StrippingD2hhh_conf',

    )

for _sel in _selections :
    try :
        __import__( '%s.%s'  % ( __name__, _sel ) )
    except Exception, x:
        print '[WARNING] Submodule %s.%s raises the exception "%s" and will be skipped !' % ( __name__,_sel,x )

from sys import modules as _modules
_this = _modules[__name__]

_strippingKeys = filter ( lambda x : x[:9]=='Stripping',
                          locals().keys())

_strippingModules = [getattr(_this, _k) for _k in _strippingKeys]


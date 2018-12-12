
import os, sys
__path__ = [d for d in [os.path.join(d, 'StrippingArchive/Stripping24/StrippingBandQ') for d in sys.path if d]
            if (d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1/build.x86_64-slc6-gcc49-opt') or
                d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1')) and
               (os.path.exists(d) or 'python.zip' in d)]
"""
Module importing stripping selection line builder modules
for BandQ WG.
"""

_selections = (
    'StrippingDiMuonForXsection',
    'StrippingB2JpsiXforEM_s'   ,
    'StrippingXibc'             ,
    'StrippingCC2DD'            ,
    'StrippingBc3h'             , 
    'StrippingCharmAssociative' , 
#    'StrippingPsiX0'            , ## no need to run in production 
#    'StrippingPsiXForBandQ'     , ## no need to run in production
#    'StrippingUpsilonExotic'    , ## no need to run in production
    'StrippingDiMuonNew'        ,
    'StrippingChiCJPsiGammaConv',
    'StrippingXic2HHH',
    'StrippingDiMuonInherit',
    'StrippingHeavyBaryons',
    'StrippingBc2Ds1Gamma',
    #
    'StrippingBc2JpsiHBDT',
    'StrippingBc2JpsiMuXNew',
    'StrippingCcbar2PpbarNew',
    'StrippingCcbar2PhiPhi',
    'StrippingCcbar2PPPiPi',
    'StrippingLb2EtacKp'
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


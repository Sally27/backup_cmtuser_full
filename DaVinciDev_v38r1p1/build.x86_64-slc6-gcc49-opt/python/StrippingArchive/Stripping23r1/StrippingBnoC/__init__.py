
import os, sys
__path__ = [d for d in [os.path.join(d, 'StrippingArchive/Stripping23r1/StrippingBnoC') for d in sys.path if d]
            if (d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1/build.x86_64-slc6-gcc49-opt') or
                d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1')) and
               (os.path.exists(d) or 'python.zip' in d)]
"""
Module importing stripping selection line builder modules
for BnoC WG.
"""

_selections = [ 'StrippingHb2Charged2Body', 
                'StrippingB2CharmlessQuasi2Body', 
                'StrippingB2HHBDT',
                'StrippingD2HHBDT', 
                'StrippingBc2hhh_BnoC',
                'StrippingBu2hhh',
                'StrippingB2pphh',
                'StrippingBs2Kst_0Kst_0',
                'StrippingB2HHPi0',
                'StrippingB2KShh',
                'StrippingLb2V0hh',
                'StrippingBs2PhiPhi']

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


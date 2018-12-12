
import os, sys
__path__ = [d for d in [os.path.join(d, 'StrippingArchive/Stripping23r1/StrippingB2CC') for d in sys.path if d]
            if (d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1/build.x86_64-slc6-gcc49-opt') or
                d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1')) and
               (os.path.exists(d) or 'python.zip' in d)]
"""
Module importing stripping selection line builder modules
for B2CC WG.
"""

# last update: 12th May 2015
_selections = ['StrippingB2JpsiXforBeta_s',
               'StrippingBs2EtacPhiBDT',
               'StrippingBd2JpsieeKS',
               'StrippingBs2JpsieePhi',
               'StrippingB2JpsiPi0']

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


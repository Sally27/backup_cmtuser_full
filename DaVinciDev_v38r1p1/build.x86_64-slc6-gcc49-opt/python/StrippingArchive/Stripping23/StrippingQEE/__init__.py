
import os, sys
__path__ = [d for d in [os.path.join(d, 'StrippingArchive/Stripping23/StrippingQEE') for d in sys.path if d]
            if (d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1/build.x86_64-slc6-gcc49-opt') or
                d.startswith('/home/hep/ss4314/cmtuser/DaVinciDev_v38r1p1')) and
               (os.path.exists(d) or 'python.zip' in d)]
"""
Module importing stripping selection line builder modules
for QEE WG.
"""


_selections = (
  ## These line has explicit request from users for Run-II measurement.
  'StrippingDitau', 
  'StrippingDisplVertices',    
  'StrippingH24Mu',
  'StrippingInclbJets',
  'StrippingLowMultINC',       
  'StrippingMuMuSS',           
  'StrippingSingleTrackTIS',
  'StrippingWMu',
  'StrippingWmuAKTJets',
  'StrippingWeAKTJets',
  'StrippingZ02MuMu',

  ## These lines are recovered from S21 `just-in-case`, 
  ## but there's no explicit request in S23 yet.
  'StrippingDijets',
  'StrippingDY2ee',
  'StrippingDY2MuMu',
  'StrippingHighPtTopoJets',
  'StrippingJets',
  'StrippingLLP2MuX',
  'StrippingSbarSCorrelations',
  'StrippingStrangeBaryons',
  'StrippingStrangeBaryonsNoPID',
  'StrippingWe',
  'StrippingZ02ee',
)

for _sel in _selections :  
  try :
    __import__( '%s.%s'  % ( __name__, _sel ) )
  except Exception, x:
    print '[WARNING] Submodule %s.%s raises the exception "%s" and will be skipped !' % ( __name__,_sel,x )

_strippingModules = [ val for key,val in dict(locals()).iteritems() if key.startswith('Stripping') ]

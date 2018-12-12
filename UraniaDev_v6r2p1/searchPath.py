from LbConfiguration.SP2.options import (SearchPath, SearchPathEntry,
                                         EnvSearchPathEntry, NightlyPathEntry,
                                         LHCbDevPathEntry)

path = SearchPath([EnvSearchPathEntry('User_release_area', '/home/hep/ss4314/cmtuser'), EnvSearchPathEntry('CMTPROJECTPATH', '/home/hep/ss4314/cmtuser:/cvmfs/lhcb.cern.ch/lib/lhcb:/cvmfs/lhcb.cern.ch/lib/lcg/releases:/cvmfs/lhcb.cern.ch/lib/lcg/app/releases:/cvmfs/lhcb.cern.ch/lib/lcg/external'), EnvSearchPathEntry('LHCBPROJECTPATH', '/cvmfs/lhcb.cern.ch/lib/lhcb:/cvmfs/lhcb.cern.ch/lib/lcg/releases:/cvmfs/lhcb.cern.ch/lib/lcg/app/releases:/cvmfs/lhcb.cern.ch/lib/lcg/external'), EnvSearchPathEntry('CMAKE_PREFIX_PATH', '/cvmfs/lhcb.cern.ch/lib/lhcb/LBSCRIPTS/LBSCRIPTS_v9r1p5/LbRelease/data/DataPkgEnvs:/cvmfs/lhcb.cern.ch/lib/lhcb/LBSCRIPTS/LBSCRIPTS_v9r1p5/LbUtils/cmake')])

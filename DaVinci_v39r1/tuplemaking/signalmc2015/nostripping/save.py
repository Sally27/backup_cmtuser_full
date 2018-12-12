
from Configurables import EventNodeKiller
eventNodeKiller = EventNodeKiller('Stripkiller')
eventNodeKiller.Nodes = ['/Event/AllStreams','/Event/Strip']

from Gaudi.Configuration import *
MessageSvc().Format = "% F%30W%S%7W%R%T %0W%M"

# Tighten Trk Chi2 to <3
from CommonParticles.Utils import DefaultTrackingCuts
DefaultTrackingCuts().Cuts  = { "Chi2Cut" : [ 0, 4 ],
                                "CloneDistCut" : [5000, 9e+99 ] }

#
# Build the streams and stripping object
#
from StrippingArchive.Stripping21.StrippingB23MuNu import B23MuNuConf as builder
#from StrippingArchive.Stripping21.StrippingB23MuNu import default_config as config
from StrippingConf.Configuration import StrippingConf, StrippingStream
#from StrippingSettings.Utils import strippingConfiguration
#from StrippingArchive.Utils import buildStreams, cloneLinesFromStream
#from StrippingArchive import strippingArchive
config['MuonPID'] = -999999

stripping='stripping21'
#get the configuration dictionary from the database
config  = strippingConfiguration(stripping)
#config['HLT_FILTER_HMuNu']=""
lb = builder('B23MuNu',config)
print config
#get the line builders from the archive


#
# Merge into one stream and run in flag mode
#
AllStreams = StrippingStream("Semileptonic")

for line in lb.lines():
    if line.name() == 'StrippingB23MuNu_TriMuLine':
        AllStreams.appendLines([line])


sc = StrippingConf( Streams = [ AllStreams ],
                    MaxCandidates = 2000
                    )

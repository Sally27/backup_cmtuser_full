from Gaudi.Configuration import *
from Configurables import DaVinci

##### STRIPPING 
from StrippingConf.Configuration import StrippingConf
from StrippingConf.StrippingStream import StrippingStream
SL_stream = StrippingStream("SL_DST")
from StrippingSelections import StrippingTrackEffD0ToK3Pi 

from GaudiKernel.SystemOfUnits import mm, GeV
config = StrippingTrackEffD0ToK3Pi.default_config.copy()
#config["Kaon_MIN_PIDK"] = 2
#config["Pion_MAX_PIDK"] = 20
#config["D0_MIN_FD"] = 2*mm
#config["Dst_MAX_M"] = 2.1*GeV
#config["Dst_MAX_DTFCHI2"] = 10.
#config["VeloMINIP"] = 0.00*mm
#config["VeloLineForTiming"] = True
SL_stream.appendLines( StrippingTrackEffD0ToK3Pi.TrackEffD0ToK3PiAllLinesConf("TrackEffD0ToK3Pi", config).lines() )
SL_stream.appendLines( StrippingTrackEffD0ToK3Pi.TrackEffD0ToK3PiAllLinesConf("MYTEST", config).lines() )

##### CONFIGURE THE STRIPPING
from Configurables import  ProcStatusCheck
ActiveStreams = [SL_stream]
sc = StrippingConf( Streams = ActiveStreams,
                    MaxCandidates = 2000,
                    AcceptBadEvents = False,
                    BadEventSelection = ProcStatusCheck() )

from Configurables import AuditorSvc, ChronoAuditor
AuditorSvc().Auditors.append( ChronoAuditor("Chrono") )

from Configurables import StrippingReport
sr = StrippingReport(Selections = sc.selections())
sr.OnlyPositive = False
sr.ReportFrequency = 100
    
########### main sequence
#from Configurables import FilterDesktop
#StdParticles = ["StdAllLoosePions","StdNoPIDsPions","StdLoosePions","StdLooseKaons"]
#MakePionsEtc = FilterDesktop('MakePionsEtc')
#MakePionsEtc.Inputs=StdParticles
#MakePionsEtc.Code="ALL"

#from Configurables import MicroDSTWriter
#writer = MicroDSTWriter("MicroDST0")
#writer.OutputFileSuffix = "Test"
#writer.SelectionSequences = sc.activeStreams()

from Configurables import SelDSTWriter
writer = SelDSTWriter("SelDST0")
writer.OutputFileSuffix = "Test"
writer.SelectionSequences = sc.activeStreams()

from Configurables import  EventNodeKiller, StoreExplorerAlg, DataObjectVersionFilter, GaudiSequencer

# you need first to load the raw banks
loadCalo = DataObjectVersionFilter( "LoadCaloRawEvent",
                                    DataObjectLocation = "/Event/Calo/RawEvent",
                                    MaxVersion = 999 )
loadMuon = DataObjectVersionFilter( "LoadMuonRawEvent",
                                    DataObjectLocation = "/Event/Muon/RawEvent",
                                    MaxVersion = 999 )
loadRich = DataObjectVersionFilter( "LoadRichRawEvent",
                                    DataObjectLocation = "/Event/Rich/RawEvent",
                                    MaxVersion = 999 )
loadOther = DataObjectVersionFilter( "LoadOtherRawEvent",
                                     DataObjectLocation = "/Event/Other/RawEvent",
                                     MaxVersion = 999 )
killer = EventNodeKiller( name = "KillDAQBanks",
                          Nodes = [ "/Event/DAQ/RawEvent",
                                    "/Event/Calo/RawEvent",
                                    "/Event/Muon/RawEvent",
                                    "/Event/Rich/RawEvent",
                                    "/Event/Other/RawEvent" ]
                          )
KillSeq = GaudiSequencer("MySeq")
KillSeq.Members += [ loadCalo,loadMuon,loadRich,loadOther,killer,sc.sequence() ]

DaVinci().PrintFreq = 1000
DaVinci().HistogramFile = 'DV_stripping_histos.root'
DaVinci().EvtMax = -1
#DaVinci().TupleFile = 'DVTuples.root'
#DaVinci().appendToMainSequence( [MakePionsEtc] )

DaVinci().appendToMainSequence( [ sc.sequence() ] )
DaVinci().appendToMainSequence( [ sr ] )
#DaVinci().appendToMainSequence( [ KillSeq ] )
DaVinci().appendToMainSequence( [ KillSeq , writer.sequence() ] )
MODE="DATA"
if MODE == "MC":
    DaVinci().DataType = "2011"
    DaVinci().Simulation = True
    DaVinci().InputType = 'DST'
    from GaudiConf import IOHelper
    IOHelper().inputFiles(['PFN:root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/MC11a/ALLSTREAMS.DST/00014704/0000/00014704_00000001_1.allstreams.dst'])
else:
    DaVinci().DataType = "2012"
    DaVinci().Simulation = False
    DaVinci().InputType = 'SDST'
    importOptions("$STRIPPINGSELECTIONSROOT/tests/data/Reco14_Run125113.py")
    DaVinci().DDDBtag  = "dddb-20120831"
    DaVinci().CondDBtag = "cond-20121008"

#Wed Apr 26 11:34:47 2017"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class TupleToolAllTracks( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'InputParticles' : [ 'Phys/StdAllNoPIDsPions/Particles' ], # list
    'Target' : 'Charm', # str
    'ANNPID' : -1.00000, # float
    'Theta' : -1.00000, # float
    'DeltaPhi' : -1.00000, # float
    'GhostProb' : 1.00000, # float
    'DLLPID' : -9999.00, # float
    'NewVertexChi2' : -1.00000, # float
    'ImprovedVertex' : -1.00000, # float
    'IPchi2' : -1.00000, # float
    'PVIPchi2' : -1.00000, # float
    'MHi' : -1.00000, # float
    'AddMax' : 200, # int
    'WritePXPYPZ' : False, # bool
    'CorrectedMass' : False, # bool
  }
  _propertyDocDct = { 
    'WritePXPYPZ' : """ Write PX, PY, PZ of added particle alone and target+particle combination """,
    'AddMax' : """ Maximal number of added particles """,
    'MHi' : """ Cut on invariant mass of Target+input particles """,
    'ImprovedVertex' : """ Cut on Vertex chi2 w added particle - Vertex chi2 w/o added particle """,
    'NewVertexChi2' : """ Cut on Vertex chi2 with added particle """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoDir' : """ Histogram Directory """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'Verbose' : """ add extra variables for this tool """,
    'Theta' : """ Cut on theta angle of the added input particle """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'GhostProb' : """ Cut on the added input particle ghost probability """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'CorrectedMass' : """ Write corrected mass and it's error of mother+added particle """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'StatPrint' : """ Print the table of counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'PVIPchi2' : """ Cut on IPchi2 of added particle w.r.t. closest primary vertex """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'ANNPID' : """ Cut on ProbNN of added input particle type """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'DeltaPhi' : """ Cut on the difference between phi angles of target and added particle """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'Target' : """ Particle to add Particles to """,
    'IPchi2' : """ Cut on IPchi2 of added particle w.r.t. new vertex """,
    'DLLPID' : """ Cut on DLL of added input particle type """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'InputParticles' : """ List of input Particles """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolAllTracks, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolAllTracks'
  pass # class TupleToolAllTracks

class TupleToolAngles( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'WRTMother' : True, # bool
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'WRTMother' : """ Turn false to fill angles with respect to top of tree """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolAngles, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolAngles'
  pass # class TupleToolAngles

class TupleToolBeamSpot( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'Bound' : 10.000000, # float
  }
  _propertyDocDct = { 
    'Bound' : """ Bound to pass to beamspot constructor """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolBeamSpot, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolBeamSpot'
  pass # class TupleToolBeamSpot

class TupleToolBremInfo( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'Particle' : [ 'e+' , 'gamma' ], # list
    'fullDST' : True, # bool
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolBremInfo, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolBremInfo'
  pass # class TupleToolBremInfo

class TupleToolCaloDigits( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'DigitLocation' : 'Raw/Spd/Digits', # str
    'CaloName' : 'Spd', # str
    'CaloLocation' : '/dd/Structure/LHCb/DownstreamRegion/Spd', # str
    'MaxDigits' : 4096, # int
    'AutoConfigure' : False, # bool
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolCaloDigits, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolCaloDigits'
  pass # class TupleToolCaloDigits

class TupleToolCaloHypo( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'DataList' : [ 'All' ], # list
    'AllowBremHypo' : False, # bool
    'AllowChargedHypo' : False, # bool
    'AllowDaughtersHypo' : False, # bool
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolCaloHypo, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolCaloHypo'
  pass # class TupleToolCaloHypo

class TupleToolDecayTreeFitter( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'daughtersToConstrain' : [  ], # list
    'constrainToOriginVertex' : False, # bool
    'Substitutions' : {  }, # list
    'StoreRefittedPVsTwice' : False, # bool
    'UpdateDaughters' : False, # bool
    'StateProvider' : PublicToolHandle('TrackStateProvider'), # GaudiHandle
  }
  _propertyDocDct = { 
    'UpdateDaughters' : """ Store updated momenta of tracks in the decay tree """,
    'Substitutions' : """ PID-substitutions :  { ' decay-component' : 'new-pid' } """,
    'constrainToOriginVertex' : """ Do a refit constraining to Origin Vertex (could be PV) """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'daughtersToConstrain' : """ List of particles to contrain to mass """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'StoreRefittedPVsTwice' : """ Store PV even if a refitted version is already the best PV (i.e store twice) """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolDecayTreeFitter, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolDecayTreeFitter'
  pass # class TupleToolDecayTreeFitter

class TupleToolDira( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolDira, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolDira'
  pass # class TupleToolDira

class TupleToolGeometry( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'RefitPVs' : False, # bool
    'PVReFitter' : 'LoKi::PVReFitter:PUBLIC', # str
    'FillMultiPV' : False, # bool
  }
  _propertyDocDct = { 
    'RefitPVs' : """ Refit PVs when doing next best PV checks """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'FillMultiPV' : """ Fill Multi PV arrays """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'PVReFitter' : """ PV refitter algorithm name (':PUBLIC' at end of algo name makes sure a public instance is used) """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolGeometry, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolGeometry'
  pass # class TupleToolGeometry

class TupleToolIsolationTwoBody( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'ParticlePath' : '/Event/Phys/StdAllNoPIDsPions/Particles', # str
    'angle' : 0.27000000, # float
    'fc' : 0.60000000, # float
    'doca' : 0.13000000, # float
    'ips' : 3.0000000, # float
    'svdis' : -0.15000000, # float
    'svdis_h' : 30.000000, # float
    'pvdis' : 0.50000000, # float
    'pvdis_h' : 40.000000, # float
    'ghost' : 1000000.0, # float
    'clone' : -1000000.0, # float
    'trchi2' : 1000000.0, # float
    'tracktype' : 3, # int
    'hltgood' : -10.000000, # float
    'PVInputLocation' : 'Rec/Vertex/Primary', # str
    'MuChi2' : True, # bool
    'isMC' : False, # bool
    'IP2MCPAssociatorType' : 'DaVinciSmartAssociator', # str
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolIsolationTwoBody, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolIsolationTwoBody'
  pass # class TupleToolIsolationTwoBody

class TupleToolKinematic( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'Transporter' : 'ParticleTransporter:PUBLIC', # str
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolKinematic, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolKinematic'
  pass # class TupleToolKinematic

class TupleToolMassHypo( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'PIDReplacements' : {  }, # list
    'CC' : True, # bool
  }
  _propertyDocDct = { 
    'PIDReplacements' : """ List of PID replacements as dictionary of strings """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'CC' : """ Do cc by default """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolMassHypo, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolMassHypo'
  pass # class TupleToolMassHypo

class TupleToolNeutrinoReco( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'MotherMass' : 0.0000000, # float
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolNeutrinoReco, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolNeutrinoReco'
  pass # class TupleToolNeutrinoReco

class TupleToolP2VV( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'Calculator' : 'Bd2KstarMuMuAngleCalculator', # str
    'FillTransversity' : True, # bool
    'FillHelicity' : True, # bool
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolP2VV, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolP2VV'
  pass # class TupleToolP2VV

class TupleToolParticleReFit( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolParticleReFit, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolParticleReFit'
  pass # class TupleToolParticleReFit

class TupleToolParticleStats( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'InputLocations' : [ 'StdLooseAllPhotons' ], # list
  }
  _propertyDocDct = { 
    'InputLocations' : """ Locations to look at """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolParticleStats, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolParticleStats'
  pass # class TupleToolParticleStats

class TupleToolPhotonInfo( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolPhotonInfo, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolPhotonInfo'
  pass # class TupleToolPhotonInfo

class TupleToolPi0Info( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'RequireMCTruth' : False, # bool
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolPi0Info, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolPi0Info'
  pass # class TupleToolPi0Info

class TupleToolPid( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolPid, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolPid'
  pass # class TupleToolPid

class TupleToolPropertime( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'FitToPV' : False, # bool
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolPropertime, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolPropertime'
  pass # class TupleToolPropertime

class TupleToolSelResults( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'Selections' : [  ], # list
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'Selections' : """ List of algorithm names """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSelResults, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSelResults'
  pass # class TupleToolSelResults

class TupleToolSubMass( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'SetMax' : 0, # int
    'Substitution' : [  ], # list
    'DoubleSubstitution' : [  ], # list
    'SubVertexFit' : True, # bool
    'EndTreePIDs' : [ 22 , 310 , 3122 ], # list
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSubMass, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSubMass'
  pass # class TupleToolSubMass

class TupleToolSwimmingInfo( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'RelationsLocation' : '', # str
    'ReportStage' : 'Trigger', # str
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSwimmingInfo, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSwimmingInfo'
  pass # class TupleToolSwimmingInfo

class TupleToolTagging( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'TaggingToolName' : '', # str
    'StoreTaggersInfo' : False, # bool
    'ActiveTaggers' : [ 'OS_Muon' , 'OS_Electron' , 'OS_Kaon' , 'SS_Kaon' , 'SS_Pion' , 'SS_PionBDT' , 'VtxCharge' , 'OS_nnetKaon' , 'SS_nnetKaon' , 'SS_Proton' , 'OS_Charm' ], # list
    'useFTonDST' : False, # bool
  }
  _propertyDocDct = { 
    'TaggingToolName' : """ The Tagging Tool, if empty string, the tool will be retrieved from the parent DVAlg """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolTagging, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolTagging'
  pass # class TupleToolTagging

class TupleToolTwoParticleMatching( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'MatchLocations' : {  }, # list
    'ToolList' : [ 'TupleToolKinematic' , 'TupleToolPid' , 'TupleToolMCTruth' , 'TupleToolMCBackgroundInfo' ], # list
    'Prefix' : 'Matched_', # str
    'Suffix' : '', # str
    'MatcherTool' : 'TeslaMatcher:PUBLIC', # str
    'MatchWith' : 'OBSOLETE', # str
    'TupleTools' : [ 'TupleToolKinematic' , 'TupleToolPid' , 'TupleToolMCTruth' , 'TupleToolMCBackgroundInfo' ], # list
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolTwoParticleMatching, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolTwoParticleMatching'
  pass # class TupleToolTwoParticleMatching

class TupleToolVeto( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
    'Particle' : '', # str
    'Veto' : {  }, # list
    'VetoOther' : {  }, # list
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVeto, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVeto'
  pass # class TupleToolVeto

class TupleToolVtxIsoln( ConfigurableAlgTool ) :
  __slots__ = { 
    'MonitorService' : 'MonitorSvc', # str
    'OutputLevel' : 7, # int
    'AuditTools' : False, # bool
    'AuditInitialize' : False, # bool
    'AuditStart' : False, # bool
    'AuditStop' : False, # bool
    'AuditFinalize' : False, # bool
    'ErrorsPrint' : True, # bool
    'PropertiesPrint' : False, # bool
    'StatPrint' : True, # bool
    'TypePrint' : True, # bool
    'Context' : '', # str
    'RootInTES' : '', # str
    'RootOnTES' : '', # str
    'GlobalTimeOffset' : 0.0000000, # float
    'StatTableHeader' : ' |    Counter                                      |     #     |    sum     | mean/eff^* | rms/err^*  |     min     |     max     |', # str
    'RegularRowFormat' : ' | %|-48.48s|%|50t||%|10d| |%|11.7g| |%|#11.5g| |%|#11.5g| |%|#12.5g| |%|#12.5g| |', # str
    'EfficiencyRowFormat' : ' |*%|-48.48s|%|50t||%|10d| |%|11.5g| |(%|#9.6g| +- %|-#9.6g|)%%|   -------   |   -------   |', # str
    'UseEfficiencyRowFormat' : True, # bool
    'CounterList' : [ '.*' ], # list
    'StatEntityList' : [  ], # list
    'ContextService' : 'AlgContextSvc', # str
    'HistoProduce' : True, # bool
    'HistoPrint' : False, # bool
    'HistoCountersPrint' : True, # bool
    'HistoCheckForNaN' : True, # bool
    'HistoSplitDir' : False, # bool
    'HistoOffSet' : 0, # int
    'HistoTopDir' : '', # str
    'HistoDir' : 'AlgTool', # str
    'FullDetail' : False, # bool
    'MonitorHistograms' : True, # bool
    'FormatFor1DHistoTable' : '| %2$-45.45s | %3$=7d |%8$11.5g | %10$-11.5g|%12$11.5g |%14$11.5g |', # str
    'ShortFormatFor1DHistoTable' : ' | %1$-25.25s %2%', # str
    'HeaderFor1DHistoTable' : '|   Title                                       |    #    |     Mean   |    RMS     |  Skewness  |  Kurtosis  |', # str
    'UseSequencialNumericAutoIDs' : False, # bool
    'AutoStringIDPurgeMap' : { '/' : '=SLASH=' }, # list
    'NTupleProduce' : True, # bool
    'NTuplePrint' : True, # bool
    'NTupleSplitDir' : False, # bool
    'NTupleOffSet' : 0, # int
    'NTupleLUN' : 'FILE1', # str
    'NTupleTopDir' : '', # str
    'NTupleDir' : 'AlgTool', # str
    'EvtColsProduce' : False, # bool
    'EvtColsPrint' : False, # bool
    'EvtColSplitDir' : False, # bool
    'EvtColOffSet' : 0, # int
    'EvtColLUN' : 'EVTCOL', # str
    'EvtColTopDir' : '', # str
    'EvtColDir' : 'AlgTool', # str
    'ExtraName' : '', # str
    'Verbose' : False, # bool
    'MaxPV' : 100, # int
  }
  _propertyDocDct = { 
    'MaxPV' : """ Maximal number of PVs considered """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'StatPrint' : """ Print the table of counters """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'HistoDir' : """ Histogram Directory """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVtxIsoln, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVtxIsoln'
  pass # class TupleToolVtxIsoln

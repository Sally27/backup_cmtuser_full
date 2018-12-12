#Thu Mar 23 14:20:10 2017"""Automatically generated. DO NOT EDIT please"""
from GaudiKernel.GaudiHandles import *
from GaudiKernel.Proxy.Configurable import *

class TupleTTInfo( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleTTInfo, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleTTInfo'
  pass # class TupleTTInfo

class TupleTTInfo2( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleTTInfo2, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleTTInfo2'
  pass # class TupleTTInfo2

class TupleTTInfo3( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleTTInfo3, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleTTInfo3'
  pass # class TupleTTInfo3

class TupleTTInfo3sta( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleTTInfo3sta, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleTTInfo3sta'
  pass # class TupleTTInfo3sta

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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'WRTMother' : """ Turn false to fill angles with respect to top of tree """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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

class TupleToolApplyKMuIsolation( ConfigurableAlgTool ) :
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
    'MaxDeltaChi2' : 9.0000000, # float
    'MaxChi2' : 9.0000000, # float
    'VertexFit' : 'default', # str
    'InputParticles' : [ '/Event/Phys/StdAllNoPIDsPions' , '/Event/Phys/StdNoPIDsUpPions' , 'Phys/StdNoPIDsVeloPions' ], # list
    'OutputSuffix' : '', # str
    'WeightsFile' : 'weights.xml', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolApplyKMuIsolation, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolApplyKMuIsolation'
  pass # class TupleToolApplyKMuIsolation

class TupleToolApplyPiMuIsolation( ConfigurableAlgTool ) :
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
    'MaxDeltaChi2' : 9.0000000, # float
    'MaxChi2' : 9.0000000, # float
    'VertexFit' : 'default', # str
    'InputParticles' : [ '/Event/Phys/StdAllNoPIDsPions' , '/Event/Phys/StdNoPIDsUpPions' , 'Phys/StdNoPIDsVeloPions' ], # list
    'OutputSuffix' : '', # str
    'WeightsFile' : 'weights.xml', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolApplyPiMuIsolation, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolApplyPiMuIsolation'
  pass # class TupleToolApplyPiMuIsolation

class TupleToolApplypMuIsolation( ConfigurableAlgTool ) :
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
    'MaxDeltaChi2' : 9.0000000, # float
    'MaxChi2' : 9.0000000, # float
    'VertexFit' : 'default', # str
    'InputParticles' : [ '/Event/Phys/StdAllNoPIDsPions' , '/Event/Phys/StdNoPIDsUpPions' , 'Phys/StdNoPIDsVeloPions' ], # list
    'OutputSuffix' : '', # str
    'WeightsFile' : 'weights.xml', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolApplypMuIsolation, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolApplypMuIsolation'
  pass # class TupleToolApplypMuIsolation

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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'Substitutions' : """ PID-substitutions :  { ' decay-component' : 'new-pid' } """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'UpdateDaughters' : """ Store updated momenta of tracks in the decay tree """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'daughtersToConstrain' : """ List of particles to contrain to mass """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'StoreRefittedPVsTwice' : """ Store PV even if a refitted version is already the best PV (i.e store twice) """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'constrainToOriginVertex' : """ Do a refit constraining to Origin Vertex (could be PV) """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'FillMultiPV' : False, # bool
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'RefitPVs' : """ Refit PVs when doing next best PV checks """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'FillMultiPV' : """ Fill Multi PV arrays """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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

class TupleToolL0PtLUT( ConfigurableAlgTool ) :
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
    'LUT' : {  }, # list
    'LUT_loc' : '', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'LUT_loc' : """ location of LUT txt file """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'LUT' : """ map of LUT positions """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolL0PtLUT, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolL0PtLUT'
  pass # class TupleToolL0PtLUT

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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'PIDReplacements' : """ List of PID replacements as dictionary of strings """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'CC' : """ Do cc by default """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
    'InputLocations' : """ Locations to look at """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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

class TupleToolSallyCCvs5( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSallyCCvs5, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSallyCCvs5'
  pass # class TupleToolSallyCCvs5

class TupleToolSallyCCvs6( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSallyCCvs6, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSallyCCvs6'
  pass # class TupleToolSallyCCvs6

class TupleToolSallyOSmis( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSallyOSmis, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSallyOSmis'
  pass # class TupleToolSallyOSmis

class TupleToolSallyvs3( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSallyvs3, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSallyvs3'
  pass # class TupleToolSallyvs3

class TupleToolSallyvs4( ConfigurableAlgTool ) :
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolSallyvs4, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolSallyvs4'
  pass # class TupleToolSallyvs4

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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'Selections' : """ List of algorithm names """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'ReportsLocation' : '/Event/SwimmingMicroDST/SingleCandidate/P2TPRelations', # str
    'UseExtraLocation' : False, # bool
    'ExtraLocation' : '', # str
    'ReportStage' : 'Trigger', # str
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'TaggingToolName' : """ The Tagging Tool, if empty string, the tool will be retrieved from the parent DVAlg """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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

class TupleToolVertexCCMisMuMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCMisMuMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCMisMuMuMu'
  pass # class TupleToolVertexCCMisMuMuMu

class TupleToolVertexCCMismpMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCMismpMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCMismpMuMu'
  pass # class TupleToolVertexCCMismpMuMu

class TupleToolVertexCCMispmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCMispmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCMispmMuMu'
  pass # class TupleToolVertexCCMispmMuMu

class TupleToolVertexCCMisppMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCMisppMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCMisppMuMu'
  pass # class TupleToolVertexCCMisppMuMu

class TupleToolVertexCCPiMuMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCPiMuMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCPiMuMuMu'
  pass # class TupleToolVertexCCPiMuMuMu

class TupleToolVertexCCPimpMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCPimpMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCPimpMuMu'
  pass # class TupleToolVertexCCPimpMuMu

class TupleToolVertexCCPipmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCPipmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCPipmMuMu'
  pass # class TupleToolVertexCCPipmMuMu

class TupleToolVertexCCPippMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexCCPippMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexCCPippMuMu'
  pass # class TupleToolVertexCCPippMuMu

class TupleToolVertexDataMuMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexDataMuMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexDataMuMuMu'
  pass # class TupleToolVertexDataMuMuMu

class TupleToolVertexDatampMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexDatampMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexDatampMuMu'
  pass # class TupleToolVertexDatampMuMu

class TupleToolVertexDatapmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexDatapmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexDatapmMuMu'
  pass # class TupleToolVertexDatapmMuMu

class TupleToolVertexDatappMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexDatappMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexDatappMuMu'
  pass # class TupleToolVertexDatappMuMu

class TupleToolVertexMisIDmu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMisIDmu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMisIDmu'
  pass # class TupleToolVertexMisIDmu

class TupleToolVertexMisMuMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMisMuMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMisMuMuMu'
  pass # class TupleToolVertexMisMuMuMu

class TupleToolVertexMisOSMuMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMisOSMuMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMisOSMuMuMu'
  pass # class TupleToolVertexMisOSMuMuMu

class TupleToolVertexMisOSmpMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMisOSmpMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMisOSmpMuMu'
  pass # class TupleToolVertexMisOSmpMuMu

class TupleToolVertexMisOSpmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMisOSpmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMisOSpmMuMu'
  pass # class TupleToolVertexMisOSpmMuMu

class TupleToolVertexMisOSppMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMisOSppMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMisOSppMuMu'
  pass # class TupleToolVertexMisOSppMuMu

class TupleToolVertexMismpMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMismpMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMismpMuMu'
  pass # class TupleToolVertexMismpMuMu

class TupleToolVertexMispmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMispmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMispmMuMu'
  pass # class TupleToolVertexMispmMuMu

class TupleToolVertexMisppMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMisppMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMisppMuMu'
  pass # class TupleToolVertexMisppMuMu

class TupleToolVertexMuMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexMuMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexMuMuMu'
  pass # class TupleToolVertexMuMuMu

class TupleToolVertexPRMuMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 211, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexPRMuMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexPRMuMuMu'
  pass # class TupleToolVertexPRMuMuMu

class TupleToolVertexPRmpMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 211, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexPRmpMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexPRmpMuMu'
  pass # class TupleToolVertexPRmpMuMu

class TupleToolVertexPRpmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 211, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexPRpmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexPRpmMuMu'
  pass # class TupleToolVertexPRpmMuMu

class TupleToolVertexPRppMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 211, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexPRppMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexPRppMuMu'
  pass # class TupleToolVertexPRppMuMu

class TupleToolVertexPions( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 211, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexPions, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexPions'
  pass # class TupleToolVertexPions

class TupleToolVertexXmu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexXmu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexXmu'
  pass # class TupleToolVertexXmu

class TupleToolVertexXmutrial( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexXmutrial, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexXmutrial'
  pass # class TupleToolVertexXmutrial

class TupleToolVertexmpMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexmpMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexmpMuMu'
  pass # class TupleToolVertexmpMuMu

class TupleToolVertexpmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexpmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexpmMuMu'
  pass # class TupleToolVertexpmMuMu

class TupleToolVertexppMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexppMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexppMuMu'
  pass # class TupleToolVertexppMuMu

class TupleToolVertexthreeSSmuonDatampMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexthreeSSmuonDatampMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexthreeSSmuonDatampMuMu'
  pass # class TupleToolVertexthreeSSmuonDatampMuMu

class TupleToolVertexthreeSSmuonDatapmMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexthreeSSmuonDatapmMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexthreeSSmuonDatapmMuMu'
  pass # class TupleToolVertexthreeSSmuonDatapmMuMu

class TupleToolVertexthreeSSmuonDatappMuMu( ConfigurableAlgTool ) :
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
    'VertexFitter' : 'LoKi::VertexFitter', # str
    'VertexCov' : False, # bool
    'MomCov' : False, # bool
    'MotherID' : 521, # int
    'XID' : 13, # int
  }
  _propertyDocDct = { 
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
  }
  def __init__(self, name = Configurable.DefaultName, **kwargs):
      super(TupleToolVertexthreeSSmuonDatappMuMu, self).__init__(name)
      for n,v in kwargs.items():
         setattr(self, n, v)
  def getDlls( self ):
      return 'DecayTreeTuple'
  def getType( self ):
      return 'TupleToolVertexthreeSSmuonDatappMuMu'
  pass # class TupleToolVertexthreeSSmuonDatappMuMu

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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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
    'EvtColSplitDir' : """ Split long directory names into short pieces """,
    'NTupleDir' : """ Subdirectory for N-Tuples """,
    'StatTableHeader' : """ The header row for the output Stat-table """,
    'ExtraName' : """ prepend the name of any variable with this string """,
    'ErrorsPrint' : """ Print the statistics of errors/warnings/exceptions """,
    'NTupleLUN' : """ Logical File Unit for N-tuples """,
    'EvtColTopDir' : """ Top-level directory for Event Tag Collections """,
    'EvtColLUN' : """ Logical File Unit for Event Tag Collections """,
    'NTupleSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'HeaderFor1DHistoTable' : """ The table header for printout of 1D histograms  """,
    'StatPrint' : """ Print the table of counters """,
    'HistoDir' : """ Histogram Directory """,
    'NTupleTopDir' : """ Top-level directory for N-Tuples """,
    'TypePrint' : """ Add the actal C++ component type into the messages """,
    'EvtColsPrint' : """ Print statistics for Event Tag Collections  """,
    'Verbose' : """ add extra variables for this tool """,
    'HistoTopDir' : """ Top level histogram directory (take care that it ends with '/') """,
    'AutoStringIDPurgeMap' : """ Map of strings to search and replace when using the title as the basis of automatically generated literal IDs """,
    'NTuplePrint' : """ Print N-tuple statistics """,
    'CounterList' : """ RegEx list, of simple integer counters for CounterSummary. """,
    'ShortFormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'EfficiencyRowFormat' : """ The format for the regular row in the output Stat-table """,
    'EvtColsProduce' : """ General switch to enable/disable Event Tag Collections """,
    'EvtColOffSet' : """ Offset for numerical N-tuple ID """,
    'PropertiesPrint' : """ Print the properties of the component  """,
    'EvtColDir' : """ Subdirectory for Event Tag Collections """,
    'HistoSplitDir' : """ Split long directory names into short pieces (suitable for HBOOK) """,
    'ContextService' : """ The name of Algorithm Context Service """,
    'HistoProduce' : """ Switch on/off the production of histograms """,
    'UseEfficiencyRowFormat' : """ Use the special format for printout of efficiency counters """,
    'HistoPrint' : """ Switch on/off the printout of histograms at finalization """,
    'RegularRowFormat' : """ The format for the regular row in the output Stat-table """,
    'FormatFor1DHistoTable' : """ Format string for printout of 1D histograms """,
    'NTupleOffSet' : """ Offset for numerical N-tuple ID """,
    'HistoOffSet' : """ OffSet for automatically assigned histogram numerical identifiers  """,
    'UseSequencialNumericAutoIDs' : """ Flag to allow users to switch back to the old style of creating numerical automatic IDs """,
    'StatEntityList' : """ RegEx list, of StatEntity counters for CounterSummary. """,
    'HistoCountersPrint' : """ Switch on/off the printout of histogram counters at finalization """,
    'HistoCheckForNaN' : """ Switch on/off the checks for NaN and Infinity for histogram fill """,
    'MaxPV' : """ Maximal number of PVs considered """,
    'NTupleProduce' : """ General switch to enable/disable N-tuples """,
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

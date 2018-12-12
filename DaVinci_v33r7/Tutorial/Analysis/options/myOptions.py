from Gaudi.Configuration import *
from Configurables import DaVinci
DaVinci() 

DaVinci().HistogramFile = "DVHistos.root" # Histogram file
DaVinci().EvtMax = 1000 # Number of events
DaVinci().DataType = "2012" # Default anyway
DaVinci().TupleFile = "DVnTuples.root" # A file to store nTuples, such as the Lumi ntuple
DaVinci().Lumi = True # integrate the luminosity FSRs and print/store the result 

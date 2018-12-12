'''
Module for construction of lepton flavor violation stripping selections and lines

Exported symbols (use python help!):
    
'''

__author__ = ['Johannes Albrecht']
__date__ = '20/08/2012'
__version__ = '$Revision: 1.1 $'

__all__ = ('LFVLinesConf',
           'default_config',
           )

from Gaudi.Configuration import *
#from Configurables import FilterDesktop, CombineParticles
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles, DaVinci__N3BodyDecays
from PhysSelPython.Wrappers import Selection, DataOnDemand, MergedSelection
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from GaudiKernel.PhysicalConstants import c_light
from GaudiKernel.SystemOfUnits import GeV, MeV, mm
from copy import deepcopy
#
# Configure related info tools
# some of these tools are used several times:
# eg the related_info_Jpsi2eMu tool can be used for both 
# the prompt and the detached Jpsi line.
#

related_info_tools_B2eMu = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                            'Variables' : ['BSMUMUCDFISO',
                                           'BSMUMUOTHERBMAG',
                                           'BSMUMUOTHERBANGLE',
                                           'BSMUMUOTHERBBOOSTMAG',
                                           'BSMUMUOTHERBBOOSTANGLE',
                                           'BSMUMUOTHERBTRACKS'],
                            'Location'  : 'BSMUMUVARIABLES',  ## For the B
                            'tracktype' : 3,
                            'makeTrackCuts' : False
                            },
                            {'Type' : 'RelInfoBs2MuMuTrackIsolations',
                            'Variables' : ['BSMUMUTRACKPLUSISO',
                                           'BSMUMUTRACKPLUSISOTWO',
                                           'ISOTWOBODYQPLUS',
                                           'ISOTWOBODYMASSISOPLUS',
                                           'ISOTWOBODYCHI2ISOPLUS',
                                           'ISOTWOBODYISO5PLUS'],
                            'DaughterLocations' : {
                            '[B_s0 -> e+ ^[mu-]cc]CC' :  'Muon_ISO',
                            '[B_s0 -> ^e+ [mu-]cc]CC' :  'Electron_ISO',
                            },
    
                            'tracktype'  : 3,
                            'angle'      : 0.27,
                            'fc'         : 0.60,
                            'doca_iso'   : 0.13,
                            'ips'        : 3.0,
                            'svdis'      : -0.15,
                            'svdis_h'    : 30.,
                            'pvdis'      : 0.5,
                            'pvdis_h'    : 40.,
                            'makeTrackCuts' : False,
                            'IsoTwoBody' : True
                            },
                            
                            {'Type': 'RelInfoVertexIsolation',
                            'Location':'VtxIsoInfo',
                            },
                            
                            {'Type': 'RelInfoConeVariables',
                             'Location':'ConeIsoInfo',
                            },
                            
                            {'Type': 'RelInfoVertexIsolationBDT',
                             'Location':'VtxIsoInfoBDT',
                            },
                            
                            {'Type': 'RelInfoTrackIsolationBDT',
                             'Variables' : 0,
                             'DaughterLocations': {
                             '[B_s0 -> e+ ^[mu-]cc]CC' :  'Muon_TrackIsoBDT',
                             '[B_s0 -> ^e+ [mu-]cc]CC' :  'Electron_TrackIsoBDT',
                            }},
                            ] ## matches 'RelatedInfoTools'

related_info_tools_JPsi2eMu = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                            'Variables' : [
                                            'BSMUMUCDFISO', 
                                            'BSMUMUOTHERBMAG',
                                            'BSMUMUOTHERBANGLE', 
                                            'BSMUMUOTHERBBOOSTMAG',
                                            'BSMUMUOTHERBBOOSTANGLE',
                                            'BSMUMUOTHERBTRACKS'
                                          ],
                            'Location'  : 'BSMUMUVARIABLES',  ## For the B
                            'tracktype' : 3,
                            'makeTrackCuts' : False
                            },
                            {
                              'Type' : 'RelInfoBs2MuMuTrackIsolations',
                              'Variables' : [
                                              'BSMUMUTRACKPLUSISO', 
                                              'BSMUMUTRACKPLUSISOTWO',
                                              'ISOTWOBODYQPLUS', 
                                              'ISOTWOBODYMASSISOPLUS',
                                              'ISOTWOBODYCHI2ISOPLUS', 
                                              'ISOTWOBODYISO5PLUS'
                                            ],
                              'DaughterLocations' : {
                                '[J/psi(1S) -> e+ ^[mu-]cc]CC' :  'Muon_ISO',
                                '[J/psi(1S) -> ^e+ [mu-]cc]CC' :  'Electron_ISO',
                              },
    
                              'tracktype'  : 3,
                              'angle'      : 0.27,
                              'fc'         : 0.60,
                              'doca_iso'   : 0.13,
                              'ips'        : 3.0,
                              'svdis'      : -0.15,
                              'svdis_h'    : 30.,
                              'pvdis'      : 0.5,
                              'pvdis_h'    : 40.,
                              'makeTrackCuts' : False,
                              'IsoTwoBody' : True
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 1,
                              "DaughterLocations" : {
                                "[J/psi(1S) -> e+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT6vars',
                                "[J/psi(1S) -> ^e+ [mu-]cc]CC" :  'Electron_TrackIso_BDT6vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 2,
                              "DaughterLocations" : {
                                "[J/psi(1S) -> e+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT9vars',
                                "[J/psi(1S) -> ^e+ [mu-]cc]CC" :  'Electron_TrackIso_BDT9vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
                            },
                            { 
                              'Type' : 'RelInfoConeVariables',
                              'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                              'Location'  : 'coneInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolation',
                              'Location':'VtxIsoInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolationBDT',
                              'Location':'VtxIsoInfoBDT'
                            }
                            ] ## matches 'RelatedInfoTools'

related_info_tools_JPsi2MuMuControl = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                            'Variables' : [
                                            'BSMUMUCDFISO', 
                                            'BSMUMUOTHERBMAG',
                                            'BSMUMUOTHERBANGLE', 
                                            'BSMUMUOTHERBBOOSTMAG',
                                            'BSMUMUOTHERBBOOSTANGLE',
                                            'BSMUMUOTHERBTRACKS'
                                          ],
                            'Location'  : 'BSMUMUVARIABLES',  ## For the B
                            'tracktype' : 3,
                            'makeTrackCuts' : False
                            },
                            {
                              'Type' : 'RelInfoBs2MuMuTrackIsolations',
                              'Variables' : [
                                              'BSMUMUTRACKPLUSISO', 
                                              'BSMUMUTRACKPLUSISOTWO',
                                              'ISOTWOBODYQPLUS', 
                                              'ISOTWOBODYMASSISOPLUS',
                                              'ISOTWOBODYCHI2ISOPLUS', 
                                              'ISOTWOBODYISO5PLUS'
                                            ],
                              'DaughterLocations' : {
                                '[J/psi(1S) -> mu+ ^[mu-]cc]CC' :  'Muon_ISO',
                                '[J/psi(1S) -> ^mu+ [mu-]cc]CC' :  'Electron_ISO',
                              },
    
                              'tracktype'  : 3,
                              'angle'      : 0.27,
                              'fc'         : 0.60,
                              'doca_iso'   : 0.13,
                              'ips'        : 3.0,
                              'svdis'      : -0.15,
                              'svdis_h'    : 30.,
                              'pvdis'      : 0.5,
                              'pvdis_h'    : 40.,
                              'makeTrackCuts' : False,
                              'IsoTwoBody' : True
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 1,
                              "DaughterLocations" : {
                                "[J/psi(1S) -> mu+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT6vars',
                                "[J/psi(1S) -> ^mu+ [mu-]cc]CC" :  'Electron_TrackIso_BDT6vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 2,
                              "DaughterLocations" : {
                                "[J/psi(1S) -> mu+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT9vars',
                                "[J/psi(1S) -> ^mu+ [mu-]cc]CC" :  'Electron_TrackIso_BDT9vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
                            },
                            { 
                              'Type' : 'RelInfoConeVariables',
                              'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                              'Location'  : 'coneInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolation',
                              'Location':'VtxIsoInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolationBDT',
                              'Location':'VtxIsoInfoBDT'
                            }
                            ] ## matches 'RelatedInfoTools'

related_info_tools_JPsi2eeControl = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                            'Variables' : [
                                            'BSMUMUCDFISO', 
                                            'BSMUMUOTHERBMAG',
                                            'BSMUMUOTHERBANGLE', 
                                            'BSMUMUOTHERBBOOSTMAG',
                                            'BSMUMUOTHERBBOOSTANGLE',
                                            'BSMUMUOTHERBTRACKS'
                                          ],
                            'Location'  : 'BSMUMUVARIABLES',  ## For the B
                            'tracktype' : 3,
                            'makeTrackCuts' : False
                            },
                            {
                              'Type' : 'RelInfoBs2MuMuTrackIsolations',
                              'Variables' : [
                                              'BSMUMUTRACKPLUSISO', 
                                              'BSMUMUTRACKPLUSISOTWO',
                                              'ISOTWOBODYQPLUS', 
                                              'ISOTWOBODYMASSISOPLUS',
                                              'ISOTWOBODYCHI2ISOPLUS', 
                                              'ISOTWOBODYISO5PLUS'
                                            ],
                              'DaughterLocations' : {
                                '[J/psi(1S) -> e+ ^[e-]cc]CC' :  'Muon_ISO',
                                '[J/psi(1S) -> ^e+ [e-]cc]CC' :  'Electron_ISO',
                              },
    
                              'tracktype'  : 3,
                              'angle'      : 0.27,
                              'fc'         : 0.60,
                              'doca_iso'   : 0.13,
                              'ips'        : 3.0,
                              'svdis'      : -0.15,
                              'svdis_h'    : 30.,
                              'pvdis'      : 0.5,
                              'pvdis_h'    : 40.,
                              'makeTrackCuts' : False,
                              'IsoTwoBody' : True
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 1,
                              "DaughterLocations" : {
                                "[J/psi(1S) -> e+ ^[e-]cc]CC" :  'Muon_TrackIso_BDT6vars',
                                "[J/psi(1S) -> ^e+ [e-]cc]CC" :  'Electron_TrackIso_BDT6vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 2,
                              "DaughterLocations" : {
                                "[J/psi(1S) -> e+ ^[e-]cc]CC" :  'Muon_TrackIso_BDT9vars',
                                "[J/psi(1S) -> ^e+ [e-]cc]CC" :  'Electron_TrackIso_BDT9vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
                            },
                            { 
                              'Type' : 'RelInfoConeVariables',
                              'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                              'Location'  : 'coneInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolation',
                              'Location':'VtxIsoInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolationBDT',
                              'Location':'VtxIsoInfoBDT'
                            }
                            ] ## matches 'RelatedInfoTools' 

related_info_tools_B2hemu = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                            'Variables' : [
                                            'BSMUMUCDFISO', 
                                            'BSMUMUOTHERBMAG',
                                            'BSMUMUOTHERBANGLE', 
                                            'BSMUMUOTHERBBOOSTMAG',
                                            'BSMUMUOTHERBBOOSTANGLE',
                                            'BSMUMUOTHERBTRACKS'
                                          ],
                            'Location'  : 'BSMUMUVARIABLES',  ## For the B
                            'tracktype' : 3,
                            'makeTrackCuts' : False
                            },
                            {
                              'Type' : 'RelInfoBs2MuMuTrackIsolations',
                              'Variables' : [
                                              'BSMUMUTRACKPLUSISO', 
                                              'BSMUMUTRACKPLUSISOTWO',
                                              'ISOTWOBODYQPLUS', 
                                              'ISOTWOBODYMASSISOPLUS',
                                              'ISOTWOBODYCHI2ISOPLUS', 
                                              'ISOTWOBODYISO5PLUS'
                                            ],
                              'DaughterLocations' : {
                                '[[B+]cc -> ^X [e+]cc [mu-]cc]CC' :  'Hadron_ISO',
                                '[[B+]cc -> X [e+]cc ^[mu-]cc]CC' :  'Muon_ISO',
                                '[[B+]cc -> X ^[e+]cc [mu-]cc]CC' :  'Electron_ISO'
                              },
    
                              'tracktype'  : 3,
                              'angle'      : 0.27,
                              'fc'         : 0.60,
                              'doca_iso'   : 0.13,
                              'ips'        : 3.0,
                              'svdis'      : -0.15,
                              'svdis_h'    : 30.,
                              'pvdis'      : 0.5,
                              'pvdis_h'    : 40.,
                              'makeTrackCuts' : False,
                              'IsoTwoBody' : True
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 1,
                              "DaughterLocations" : {
                                '[[B+]cc -> ^X [e+]cc [mu-]cc]CC' :  'Hadron_TrackIso_BDT6vars',
                                '[[B+]cc -> X [e+]cc ^[mu-]cc]CC' :  'Muon_TrackIso_BDT6vars',
                                '[[B+]cc -> X ^[e+]cc [mu-]cc]CC' :  'Electron_TrackIso_BDT6vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 2,
                              "DaughterLocations" : {
                                '[[B+]cc -> ^X [e+]cc [mu-]cc]CC' :  'Hadron_TrackIso_BDT9vars',
                                '[[B+]cc -> X [e+]cc ^[mu-]cc]CC' :  'Muon_TrackIso_BDT9vars',
                                '[[B+]cc -> X ^[e+]cc [mu-]cc]CC' :  'Electron_TrackIso_BDT9vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
                            },
                            { 
                              'Type' : 'RelInfoConeVariables',
                              'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                              'Location'  : 'coneInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolation',
                              'Location':'VtxIsoInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolationBDT',
                              'Location':'VtxIsoInfoBDT'
                            }
                            ] ## matches 'RelatedInfoTools'                           

related_info_tools_Phi2eMu = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                            'Variables' : [
                                           'BSMUMUCDFISO',
                                           'BSMUMUOTHERBMAG',
                                           'BSMUMUOTHERBANGLE', 
                                           'BSMUMUOTHERBBOOSTMAG',
                                           'BSMUMUOTHERBBOOSTANGLE', 
                                           'BSMUMUOTHERBTRACKS'
                                          ],
                            'Location'  : 'BSMUMUVARIABLES',  ## For the B
                            'tracktype' : 3,
                            'makeTrackCuts' : False
                            },
                            {
                            'Type' : 'RelInfoBs2MuMuTrackIsolations',
                            'Variables' : [
                                           'BSMUMUTRACKPLUSISO', 
                                           'BSMUMUTRACKPLUSISOTWO',
                                           'ISOTWOBODYQPLUS', 
                                           'ISOTWOBODYMASSISOPLUS',
                                           'ISOTWOBODYCHI2ISOPLUS', 
                                           'ISOTWOBODYISO5PLUS'
                                          ],
                            'DaughterLocations' : {
                            '[phi(1020) -> e+ ^[mu-]cc]CC' :  'Muon_ISO',
                            '[phi(1020) -> ^e+ [mu-]cc]CC' :  'Electron_ISO',
                            },
    
                            'tracktype'  : 3,
                            'angle'      : 0.27,
                            'fc'         : 0.60,
                            'doca_iso'   : 0.13,
                            'ips'        : 3.0,
                            'svdis'      : -0.15,
                            'svdis_h'    : 30.,
                            'pvdis'      : 0.5,
                            'pvdis_h'    : 40.,
                            'makeTrackCuts' : False,
                            'IsoTwoBody' : True
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 1,
                              "DaughterLocations" : {
                                "[phi(1020) -> e+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT6vars',
                                "[phi(1020) -> ^e+ [mu-]cc]CC" :  'Electron_TrackIso_BDT6vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 2,
                              "DaughterLocations" : {
                                "[phi(1020) -> e+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT9vars',
                                "[phi(1020) -> ^e+ [mu-]cc]CC" :  'Electron_TrackIso_BDT9vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
                            },
                            { 
                              'Type' : 'RelInfoConeVariables',
                              'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                              'Location'  : 'coneInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolation',
                              'Location':'VtxIsoInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolationBDT',
                              'Location':'VtxIsoInfoBDT',
                            }
                            ] ## matches 'RelatedInfoTools'

related_info_tools_Phi2MuMuControl = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                            'Variables' : [
                                           'BSMUMUCDFISO',
                                           'BSMUMUOTHERBMAG',
                                           'BSMUMUOTHERBANGLE', 
                                           'BSMUMUOTHERBBOOSTMAG',
                                           'BSMUMUOTHERBBOOSTANGLE', 
                                           'BSMUMUOTHERBTRACKS'
                                          ],
                            'Location'  : 'BSMUMUVARIABLES',  ## For the B
                            'tracktype' : 3,
                            'makeTrackCuts' : False
                            },
                            {
                            'Type' : 'RelInfoBs2MuMuTrackIsolations',
                            'Variables' : [
                                           'BSMUMUTRACKPLUSISO', 
                                           'BSMUMUTRACKPLUSISOTWO',
                                           'ISOTWOBODYQPLUS', 
                                           'ISOTWOBODYMASSISOPLUS',
                                           'ISOTWOBODYCHI2ISOPLUS', 
                                           'ISOTWOBODYISO5PLUS'
                                          ],
                            'DaughterLocations' : {
                            '[phi(1020) -> mu+ ^[mu-]cc]CC' :  'Muon_ISO',
                            '[phi(1020) -> ^mu+ [mu-]cc]CC' :  'Electron_ISO',
                            },
    
                            'tracktype'  : 3,
                            'angle'      : 0.27,
                            'fc'         : 0.60,
                            'doca_iso'   : 0.13,
                            'ips'        : 3.0,
                            'svdis'      : -0.15,
                            'svdis_h'    : 30.,
                            'pvdis'      : 0.5,
                            'pvdis_h'    : 40.,
                            'makeTrackCuts' : False,
                            'IsoTwoBody' : True
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 1,
                              "DaughterLocations" : {
                                "[phi(1020) -> mu+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT6vars',
                                "[phi(1020) -> ^mu+ [mu-]cc]CC" :  'Electron_TrackIso_BDT6vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
                            },
                            { 
                              "Type" : "RelInfoTrackIsolationBDT",
                              "Variables" : 2,
                              "DaughterLocations" : {
                                "[phi(1020) -> mu+ ^[mu-]cc]CC" :  'Muon_TrackIso_BDT9vars',
                                "[phi(1020) -> ^mu+ [mu-]cc]CC" :  'Electron_TrackIso_BDT9vars'
                              },
                              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
                            },
                            { 
                              'Type' : 'RelInfoConeVariables',
                              'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                              'Location'  : 'coneInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolation',
                              'Location':'VtxIsoInfo'
                            },
                            {
                              'Type': 'RelInfoVertexIsolationBDT',
                              'Location':'VtxIsoInfoBDT',
                            }
                            ] ## matches 'RelatedInfoTools'

related_info_tools_Phi2eeControl = deepcopy(related_info_tools_Phi2MuMuControl) # copy phi2mm configuration
related_info_tools_Phi2eeControl[1]['DaughterLocations'] = {
                            '[phi(1020) -> e+ ^[e-]cc]CC' :  'Muon_ISO',
                            '[phi(1020) -> ^e+ [e-]cc]CC' :  'Electron_ISO',
                            }
related_info_tools_Phi2eeControl[2]['DaughterLocations'] = {
                                "[phi(1020) -> e+ ^[e-]cc]CC" :  'Muon_TrackIso_BDT6vars',
                                "[phi(1020) -> ^e+ [e-]cc]CC" :  'Electron_TrackIso_BDT6vars'
                              }
related_info_tools_Phi2eeControl[3]['DaughterLocations'] = {
                                "[phi(1020) -> e+ ^[e-]cc]CC" :  'Muon_TrackIso_BDT9vars',
                                "[phi(1020) -> ^e+ [e-]cc]CC" :  'Electron_TrackIso_BDT9vars'
                              }


related_info_tools_B2ee = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                           'Variables' : ['BSMUMUCDFISO',
                                          'BSMUMUOTHERBMAG',
                                          'BSMUMUOTHERBANGLE',
                                          'BSMUMUOTHERBBOOSTMAG',
                                          'BSMUMUOTHERBBOOSTANGLE',
                                          'BSMUMUOTHERBTRACKS'],
                           'Location'  : 'BSMUMUVARIABLES',  ## For the B
                           'tracktype' : 3,
                           'makeTrackCuts' : False
                           },
                           {'Type' : 'RelInfoBs2MuMuTrackIsolations',
                           'Variables' : ['BSMUMUTRACKPLUSISO',
                                          'BSMUMUTRACKPLUSISOTWO',
                                          'ISOTWOBODYQPLUS',
                                          'ISOTWOBODYMASSISOPLUS',
                                          'ISOTWOBODYCHI2ISOPLUS',
                                          'ISOTWOBODYISO5PLUS'],
                           'DaughterLocations' : {
                           '[B_s0 -> ^e+ [e-]cc]CC' :  'Electron1_ISO',
                           '[B_s0 -> e+ ^[e-]cc]CC' :  'Electron2_ISO',
                           },
                           
                           'tracktype' : 3,
                           'angle'      : 0.27,
                           'fc'         : 0.60,
                           'doca_iso'   : 0.13,
                           'ips'        : 3.0,
                           'svdis'      : -0.15,
                           'svdis_h'    : 30.,
                           'pvdis'      : 0.5,
                           'pvdis_h'    : 40.,
                           'makeTrackCuts' : False,
                           'IsoTwoBody' : True
                           },
                           
                           {'Type': 'RelInfoVertexIsolation',
                           'Location':'VtxIsoInfo',
                           },
                           
                           {'Type': 'RelInfoConeVariables',
                           'Location':'ConeIsoInfo',
                           },
                           
                           {'Type': 'RelInfoVertexIsolationBDT',
                           'Location':'VtxIsoInfoBDT',
                           },
                           {'Type': 'RelInfoTrackIsolationBDT',
                            'Variables' : 0,
                            'DaughterLocations': {
                            '[B_s0 -> e+ ^[e-]cc]CC' :  'Electron1_TrackIsoBDT',
                            '[B_s0 -> ^e+ [e-]cc]CC' :  'Electron2_TrackIsoBDT',
                                }},
                           ] ## matches 'RelatedInfoTools'

related_info_tools_Tau2MuEtaPrime = [{'Type': 'RelInfoVertexIsolation',
                           'Location':'VtxIsoInfo',
                           },
                           
                           {'Type': 'RelInfoVertexIsolationBDT',
                           'Location':'VtxIsoInfoBDT',
                           },
                           ] ## matches 'RelatedInfoTools'

related_info_tools_Tau2PhiMu = [{ 'Type' : 'RelInfoConeVariables', 'ConeAngle' : 0.5,
                                'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                                'Location'  : 'coneInfoTau05',  ## For the tau
                                'DaughterLocations' : {
                                '[tau+ -> ^(phi(1020)->K+ K-) mu+]CC': 'coneInfoPhi05',
                                '[tau+ -> (phi(1020)->K+ K-) ^mu+]CC' : 'coneInfoMu05',
                                '[tau+ -> (phi(1020)->^K+ K-) mu+]CC' : 'coneInfoKplus05',
                                '[tau+ -> (phi(1020)->K+ ^K-) mu+]CC': 'coneInfoKminus05'
                                }},
                                
                                { 'Type' : 'RelInfoConeVariables', 'ConeAngle' : 0.8,
                                'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                                'Location'  : 'coneInfoTau08',  ## For the tau
                                'DaughterLocations' : {
                                '[tau+ -> ^(phi(1020)->K+ K-) mu+]CC' : 'coneInfoPhi08',
                                '[tau+ -> (phi(1020)->K+ K-) ^mu+]CC' : 'coneInfoMu08',
                                '[tau+ -> (phi(1020)->^K+ K-) mu+]CC' : 'coneInfoKplus08',
                                '[tau+ -> (phi(1020)->K+ ^K-) mu+]CC' : 'coneInfoKminus08'
                                }},
                                { 'Type' : 'RelInfoConeVariables', 'ConeAngle' : 1.0,
                                'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                                'Location'  : 'coneInfoTau10',  ## For the tau
                                'DaughterLocations' : {
                                '[tau+ -> ^(phi(1020)->K+ K-) mu+]CC' : 'coneInfoPhi10',
                                '[tau+ -> (phi(1020)->K+ K-) ^mu+]CC' : 'coneInfoMu10',
                                '[tau+ -> (phi(1020)->^K+ K-) mu+]CC' : 'coneInfoKplus10',
                                '[tau+ -> (phi(1020)->K+ ^K-) mu+]CC' : 'coneInfoKminus10'
                                }},
                                
                                { 'Type' : 'RelInfoConeVariables', 'ConeAngle' : 1.2,
                                'Variables' : ['CONEANGLE', 'CONEMULT', 'CONEPT', 'CONEPTASYM'],
                                'Location'  : 'coneInfoTau12',  ## For the tau
                                'DaughterLocations' : {
                                '[tau+ -> ^(phi(1020)->K+ K-) mu+]CC' : 'coneInfoPhi12',
                                '[tau+ -> (phi(1020)->K+ K-) ^mu+]CC' : 'coneInfoMu12',
                                '[tau+ -> (phi(1020)->^K+ K-) mu+]CC' : 'coneInfoKplus12',
                                '[tau+ -> (phi(1020)->K+ ^K-) mu+]CC' : 'coneInfoKminus12'
                                }},
                                
                                {'Type': 'RelInfoVertexIsolation',
                                'Location':'VtxIsoInfo',
                                'Variables'  : [ 'VTXISONUMVTX',
                                                'VTXISODCHI2ONETRACK', 'VTXISODCHI2MASSONETRACK',
                                                'VTXISODCHI2TWOTRACK', 'VTXISODCHI2MASSTWOTRACK' ],},
                                { 'Type': 'RelInfoTrackIsolationBDT',
                                'DaughterLocations' : {
                                '[tau+ -> (phi(1020)->K+ K-) ^mu+]CC' : 'MuonTrackIsoBDTInfo',
                                '[tau+ -> (phi(1020)->^K+ K-) mu+]CC' : 'KplusTrackIsoBDTInfo',
                                '[tau+ -> (phi(1020)->K+ ^K-) mu+]CC' : 'KminusTrackIsoBDTInfo'
                                }}
                                ]

related_info_tools_Bu2KJPsiee = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                           'Variables' : ['BSMUMUCDFISO',
                                          'BSMUMUOTHERBMAG',
                                          'BSMUMUOTHERBANGLE',
                                          'BSMUMUOTHERBBOOSTMAG',
                                          'BSMUMUOTHERBBOOSTANGLE',
                                          'BSMUMUOTHERBTRACKS'],
                           'Location'  : 'BSMUMUVARIABLES',  ## For the B
                             'DaughterLocations' : {
                           '[B+ -> ^(J/psi(1S) -> e+ e-) K+]CC' :  'Jpsi_ISO',
                           },
                           'tracktype' : 3,
                           'makeTrackCuts' : False
                           },
                           {'Type' : 'RelInfoBs2MuMuTrackIsolations',
                           'Variables' : ['BSMUMUTRACKPLUSISO',
                                          'BSMUMUTRACKPLUSISOTWO',
                                          'ISOTWOBODYQPLUS',
                                          'ISOTWOBODYMASSISOPLUS',
                                          'ISOTWOBODYCHI2ISOPLUS',
                                          'ISOTWOBODYISO5PLUS'],
                           'DaughterLocations' : {
                           '[B+ -> (J/psi(1S) -> ^e+ e-) K+]CC' :  'Electron1_ISO',
                           '[B+ -> (J/psi(1S) -> e+ ^e-) K+]CC' :  'Electron2_ISO',
                           '[B+ -> (J/psi(1S) -> e+ e-) ^K+]CC' :  'Kplus_ISO',
                           },
                           
                           'tracktype' : 3,
                           'angle'      : 0.27,
                           'fc'         : 0.60,
                           'doca_iso'   : 0.13,
                           'ips'        : 3.0,
                           'svdis'      : -0.15,
                           'svdis_h'    : 30.,
                           'pvdis'      : 0.5,
                           'pvdis_h'    : 40.,
                           'makeTrackCuts' : False,
                           'IsoTwoBody' : True
                           },
                           
                           {'Type': 'RelInfoVertexIsolation',
                           'Location':'VtxIsoInfo',
                           },
                           
                           {'Type': 'RelInfoConeVariables',
                           'Location':'ConeIsoInfo',
                           },
                                 
                            {'Type': 'RelInfoVertexIsolationBDT',
                            'Location':'VtxIsoInfoBDT',
                            },
                            {'Type': 'RelInfoTrackIsolationBDT',
                             'Variables' : 0,
                             'DaughterLocations': {
                             '[B+ -> (J/psi(1S) -> ^e+ e-) K+]CC' :  'Electron1_TrackIsoBDT',
                             '[B+ -> (J/psi(1S) -> e+ ^e-) K+]CC' :  'Electron2_TrackIsoBDT',
                                }},
                            ] ## matches 'RelatedInfoTools'


related_info_tools_Upsilon2eMu = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                                  'Variables' : ['BSMUMUCDFISO',
                                                 'BSMUMUOTHERBMAG',
                                                 'BSMUMUOTHERBANGLE',
                                                 'BSMUMUOTHERBBOOSTMAG',
                                                 'BSMUMUOTHERBBOOSTANGLE',
                                                 'BSMUMUOTHERBTRACKS'],
                                  'Location'  : 'BSMUMUVARIABLES',  ## For the Upsilon
                                  'tracktype' : 3,
                                  'makeTrackCuts' : False
                                  },
                                  {'Type' : 'RelInfoBs2MuMuTrackIsolations',
                                  'Variables' : ['BSMUMUTRACKPLUSISO',
                                                 'BSMUMUTRACKPLUSISOTWO',
                                                 'ISOTWOBODYQPLUS',
                                                 'ISOTWOBODYMASSISOPLUS',
                                                 'ISOTWOBODYCHI2ISOPLUS',
                                                 'ISOTWOBODYISO5PLUS'],
                                  'DaughterLocations' : {
                                  '[Upsilon(1S) -> e+ ^[mu-]cc]CC' :  'Muon_ISO',
                                  '[Upsilon(1S) -> ^e+ [mu-]cc]CC' :  'Electron_ISO',
                                  },
                                  
                                  'tracktype'  : 3,
                                  'angle'      : 0.27,
                                  'fc'         : 0.60,
                                  'doca_iso'   : 0.13,
                                  'ips'        : 3.0,
                                  'svdis'      : -0.15,
                                  'svdis_h'    : 30.,
                                  'pvdis'      : 0.5,
                                  'pvdis_h'    : 40.,
                                  'makeTrackCuts' : False,
                                  'IsoTwoBody' : True
                                  },
                                  
                                  {'Type': 'RelInfoVertexIsolation',
                                  'Location':'VtxIsoInfo',
                                  },
                                  
                                  {'Type': 'RelInfoConeVariables',
                                  'Location':'ConeIsoInfo',
                                  },
                                  
                                  {'Type': 'RelInfoVertexIsolationBDT',
                                  'Location':'VtxIsoInfoBDT',
                                  },
                                  
                                  {'Type': 'RelInfoTrackIsolationBDT',
                                  'Variables' : 0,
                                  'DaughterLocations': {
                                  '[Upsilon(1S) -> e+ ^[mu-]cc]CC' :  'Muon_TrackIsoBDT',
                                  '[Upsilon(1S) -> ^e+ [mu-]cc]CC' :  'Electron_TrackIsoBDT',
                                  }},
                                  ] ## matches 'RelatedInfoTools'


related_info_tools_Upsilon2ee = [{'Type' : 'RelInfoBs2MuMuBIsolations',
                                 'Variables' : ['BSMUMUCDFISO',
                                                'BSMUMUOTHERBMAG',
                                                'BSMUMUOTHERBANGLE',
                                                'BSMUMUOTHERBBOOSTMAG',
                                                'BSMUMUOTHERBBOOSTANGLE',
                                                'BSMUMUOTHERBTRACKS'],
                                 'Location'  : 'BSMUMUVARIABLES',  ## For the Upsilon
                                 'tracktype' : 3,
                                 'makeTrackCuts' : False
                                 },
                                 {'Type' : 'RelInfoBs2MuMuTrackIsolations',
                                 'Variables' : ['BSMUMUTRACKPLUSISO',
                                                'BSMUMUTRACKPLUSISOTWO',
                                                'ISOTWOBODYQPLUS',
                                                'ISOTWOBODYMASSISOPLUS',
                                                'ISOTWOBODYCHI2ISOPLUS',
                                                'ISOTWOBODYISO5PLUS'],
                                 'DaughterLocations' : {
                                 '[Upsilon(1S) -> e+ ^[e-]cc]CC' :  'Electron2_ISO',
                                 '[Upsilon(1S) -> ^e+ [e-]cc]CC' :  'Electron1_ISO',
                                 },
                                 
                                 'tracktype'  : 3,
                                 'angle'      : 0.27,
                                 'fc'         : 0.60,
                                 'doca_iso'   : 0.13,
                                 'ips'        : 3.0,
                                 'svdis'      : -0.15,
                                 'svdis_h'    : 30.,
                                 'pvdis'      : 0.5,
                                 'pvdis_h'    : 40.,
                                 'makeTrackCuts' : False,
                                 'IsoTwoBody' : True
                                 },
                                 
                                 {'Type': 'RelInfoVertexIsolation',
                                 'Location':'VtxIsoInfo',
                                 },
                                 
                                 {'Type': 'RelInfoConeVariables',
                                 'Location':'ConeIsoInfo',
                                 },
                                 
                                 {'Type': 'RelInfoVertexIsolationBDT',
                                 'Location':'VtxIsoInfoBDT',
                                 },
                                 
                                 {'Type': 'RelInfoTrackIsolationBDT',
                                 'Variables' : 0,
                                 'DaughterLocations': {
                                 '[Upsilon(1S) -> e+ ^[e-]cc]CC' :  'Electron2_TrackIsoBDT',
                                 '[Upsilon(1S) -> ^e+ [e-]cc]CC' :  'Electron1_TrackIsoBDT',
                                 }},
                                 ] ## matches 'RelatedInfoTools'



default_config = {
    'NAME' : 'LFV',
    'BUILDERTYPE' : 'LFVLinesConf' ,
    'STREAMS' : {    
        'Dimuon' : [
          'StrippingLFVJPsi2MuMuControlLine',
          'StrippingLFVJPsi2eeControlLine',
          'StrippingLFVPromptJPsi2MuMuControlLine',
          'StrippingLFVPromptJPsi2eeControlLine'
        ],
        'Leptonic' : [
          'StrippingLFVTau2PhiMuLine',
          'StrippingLFVTau2eMuMuLine',
          'StrippingLFVB2eMuLine',
          'StrippingLFVJPsi2eMuLine',
          'StrippingLFVPromptJPsi2eMuLine',
          'StrippingLFVJPsi2MuMuControlLine',
          'StrippingLFVJPsi2eeControlLine',
          'StrippingLFVPromptJPsi2MuMuControlLine',
          'StrippingLFVPromptJPsi2eeControlLine',
          'StrippingLFVPhi2eMuLine',
          'StrippingLFVPromptPhi2eMuLine',
          'StrippingLFVPhi2MuMuControlLine',
          'StrippingLFVPhi2eeControlLine',
          'StrippingLFVPromptPhi2MuMuControlLine',
          'StrippingLFVPromptPhi2eeControlLine',
          'StrippingLFVB2eeLine',
          'StrippingLFVB2heMuLine',
          'StrippingLFVB2hMuLine',
          'StrippingLFVBu2KJPsieeLine',
          'StrippingLFVB2hTauMuLine',
          'StrippingLFVTau2MuEtaP2pipigLine',
          'StrippingLFVTau2MuEtaP2pipipiLine',
          'StrippingLFVupsilon2eMuLine',
          'StrippingLFVupsilon2eeLine'
        ]
    },
    'WGs'     : [ 'RD' ],
    'CONFIG'  : {
    'Postscale'                         :1,
    'TauPrescale'                       :1,
    'Tau2MuMuePrescale'                 :1,
    'B2eMuPrescale'                     :1,
    'JPsi2eMuPrescale'                  :1,
    'JPsi2MuMuControlPrescale'          :0.05,
    'JPsi2eeControlPrescale'            :0.05,
    'PromptJPsi2eMuPrescale'            :1,
    'PromptJPsi2MuMuControlPrescale'    :0.05,
    'PromptJPsi2eeControlPrescale'      :0.05,
    'Phi2eMuPrescale'                   :1,
    'Phi2MuMuControlPrescale'           :0.05,
    'Phi2eeControlPrescale'             :0.05,
    'PromptPhi2eMuPrescale'             :1,
    'PromptPhi2MuMuControlPrescale'     :0.01,
    'PromptPhi2eeControlPrescale'       :0.01,
    'B2eePrescale'                      :1,
    'B2heMuPrescale'                    :1,
    'B2pMuPrescale'                     :1,
    'Bu2KJPsieePrescale'                :1,
    'B2TauMuPrescale'                   :1,
    'B2hTauMuPrescale'                  :1,
    'Tau2MuEtaPrimePrescale'            :1,
    'Upsilon2eMuPrescale'   :1,
    'Upsilon2eePrescale'    :0.6,
    'RelatedInfoTools_B2eMu'            : related_info_tools_B2eMu,
    'RelatedInfoTools_JPsi2eMu'         : related_info_tools_JPsi2eMu,
    'RelatedInfoTools_JPsi2MuMuControl' : related_info_tools_JPsi2MuMuControl,
    'RelatedInfoTools_JPsi2eeControl'   : related_info_tools_JPsi2eeControl,
    'RelatedInfoTools_Phi2eMu'          : related_info_tools_Phi2eMu,
    'RelatedInfoTools_Phi2MuMuControl'  : related_info_tools_Phi2MuMuControl,
    'RelatedInfoTools_Phi2eeControl'    : related_info_tools_Phi2eeControl,
    'RelatedInfoTools_B2ee'             : related_info_tools_B2ee,
    'RelatedInfoTools_B2hemu'           : related_info_tools_B2hemu,
    'RelatedInfoTools_Tau2PhiMu'        : related_info_tools_Tau2PhiMu,
    'RelatedInfoTools_Bu2KJPsiee'       : related_info_tools_Bu2KJPsiee,
    'RelatedInfoTools_Tau2MuEtaPrime'   : related_info_tools_Tau2MuEtaPrime,
    'RelatedInfoTools_Upsilon2eMu'      : related_info_tools_Upsilon2eMu,
    'RelatedInfoTools_Upsilon2ee'      : related_info_tools_Upsilon2ee,
    'config_B2eMu'          : {
      'min_MIPCHI2DV': 25.,
      'max_ADAMASS'  : 1200*MeV,
      'max_TRCHI2DV' : 3.,
      'max_TRGHOSTPROB'  : 0.3,
      'max_AMAXDOCA' : 0.3*mm,
      'min_BPVDIRA'  : 0.,
      'min_BPVVDCHI2': 225.,
      'max_BPVIPCHI2': 25.
    },
    'config_JPsi2eMu'          : {
      'min_MIPCHI2DV'     : 36.,
      'max_ADAMASS'       : 1000*MeV,
      'max_TRCHI2DV'      : 3,
      'max_TRGHOSTPROB'   : 0.3,
      'max_AMAXDOCA'      : 0.3*mm,
      'min_BPVDIRA'       : 0,
      'min_BPVVDCHI2'     : 324.,
      'max_VtxChi2DoF'    : 2.5,
      'min_ProbNN'        : 0.3,
      'min_ProbNN_phi'    : 0.4,
      'max_JpsiMass'      : 4096*MeV,
      'min_JpsiMass'      : 2200*MeV,
      'max_PhiMass'       : 2020*MeV,
      'min_PhiMass'       : 300*MeV,
      'min_Pt'            : 300*MeV
    },
    'config_PromptJPsi2eMu'     : {
      'max_MIPCHI2DV'           : 9.,
      'max_BPVVDCHI2'           : 9.,
      'max_BPVIPCHI2'           : 9.,
      'max_TRCHI2DV'            : 3,
      'max_TRGHOSTPROB'         : 0.2,
      'max_AMAXDOCA'            : 0.3*mm,
      'max_SPD'                 : 350,
      'max_JpsiMass'            : 4096*MeV,
      'min_JpsiMass'            : 2200*MeV,
      'min_ProbNN'              : 0.8,
      'min_ProbNN_phi'          : 0.8,
      'max_VtxChi2DoF'          : 2.5,
      'min_Pt'                  : 300*MeV,
      'max_PhiMass'             : 2020*MeV,
      'min_PhiMass'             : 300*MeV,
      'min_ProbNN_Control'      : 0.65
    },

    'config_Tau2MuEtaPrime' : {
        'muplus_cuts'       : '(ISLONG) & (TRCHI2DOF < 3 )  & (MIPCHI2DV(PRIMARY) >  9.) & (PT > 300*MeV) & (TRGHOSTPROB < 0.3)',
        'tau_mass_window'   : "(ADAMASS('tau+')<150*MeV)",
        'tau_cuts'          : "(BPVIPCHI2()< 100) & (VFASPF(VCHI2/VDOF)<6.) & (BPVLTIME()*c_light > 50.*micrometer) & (BPVLTIME()*c_light < 400.*micrometer) & (PT>500*MeV)"\
        " & (D2DVVD(2) < 80*micrometer)", #maybe PT 1000
        
        'config_EtaPrime2pipigamma'   : {
            'gamma_cuts'        :   '(PT > 300*MeV) & (CL > 0.1)',  #CL might exclude pi0?
            'piplus_cuts'       :   "(PROBNNpi > 0.1) & (PT > 250*MeV) & (TRGHOSTPROB < 0.3) & (TRCHI2DOF < 3.0) & (MIPCHI2DV(PRIMARY) > 9.)",
            'piminus_cuts'      :   "(PROBNNpi > 0.1) & (PT > 250*MeV) & (TRGHOSTPROB < 0.3) & (TRCHI2DOF < 3.0) & (MIPCHI2DV(PRIMARY) > 9.)",
            'etap_mass_window'   :  "(ADAMASS('eta') < 80*MeV) | (ADAMASS('eta_prime') < 80*MeV)",
            'etap_cuts'          :  '(PT > 500*MeV) & (VFASPF(VCHI2/VDOF) < 6.0)',# & (MIPCHI2DV(PRIMARY)> 9)',
            'pipi_cuts'          :  '(ACHI2DOCA(1,2)<16)',
        }, #matches config_EtaPrime2pipigamma
    
        'config_EtaPrime2pipipi'   : {
            'pi0_cuts'        :     "(PT > 250*MeV)",
            'piplus_cuts'       :   "(PROBNNpi > 0.1) & (PT > 250*MeV) & (TRGHOSTPROB < 0.3) & (TRCHI2DOF < 3.0) & (MIPCHI2DV(PRIMARY) > 9.)",
            'piminus_cuts'      :   "(PROBNNpi > 0.1) & (PT > 250*MeV) & (TRGHOSTPROB < 0.3) & (TRCHI2DOF < 3.0) & (MIPCHI2DV(PRIMARY) > 9.)",
            'etap_mass_window'   :  "(ADAMASS('eta') < 80*MeV) | (ADAMASS('eta_prime') < 80*MeV)", #"(in_range(450, AM, 1050))",
            'etap_cuts'          :  '(PT > 500*MeV) & (VFASPF(VCHI2/VDOF) < 6.0)',# & (MIPCHI2DV(PRIMARY)> 9)',
            'pipi_cuts'          :  'ACHI2DOCA(1,2)<16',
        }, #matches config_EtaPrime2pipipi
    }, #matches config_Tau2MuEtaPrime


        'config_Upsilon2eMu' : {
            'mu_cuts'           :   "(PT > 1000.*MeV) & (P > 8000.*MeV) & (TRCHI2DOF < 3.)",
            'e_cuts'            :   "(PT > 1000.*MeV) & (P > 8000.*MeV) & (TRCHI2DOF < 3.) & (PIDe > 1)",
            'comb_cuts'         :   "in_range(7250, AM, 11000) & ACUTDOCA(0.3*mm,'')",
            'upsilon_cuts'      :   "(VFASPF(VCHI2) < 25) & (BPVIPCHI2() < 9) & (BPVVDCHI2 < 25)"
    }, #matches config_Upsilon2eMu

        'config_Upsilon2ee' : {
            'e_cuts'            :   "(PT > 1000.*MeV) & (P > 8000.*MeV) & (TRCHI2DOF < 3.) & (PIDe > 1)",
            'comb_cuts'         :   "in_range(6000, AM, 11000) & ACUTDOCA(0.3*mm,'')",
            'upsilon_cuts'      :   "(VFASPF(VCHI2) < 25) & (BPVIPCHI2() < 9) & (BPVVDCHI2 < 25)"
    }#matches config_Upsilon2ee
} #matches 'CONFIG'
}

class LFVLinesConf(LineBuilder) :
    
    
    __configuration_keys__ = ('Postscale',
                              'TauPrescale',
                              'Tau2MuMuePrescale',
                              'B2eMuPrescale',
                              'JPsi2eMuPrescale',
                              'JPsi2MuMuControlPrescale',
                              'JPsi2eeControlPrescale',
                              'PromptJPsi2eMuPrescale',
                              'PromptJPsi2MuMuControlPrescale',
                              'PromptJPsi2eeControlPrescale',
                              'Phi2eMuPrescale',
                              'Phi2MuMuControlPrescale',
                              'Phi2eeControlPrescale',
                              'PromptPhi2eMuPrescale',
                              'PromptPhi2MuMuControlPrescale',
                              'PromptPhi2eeControlPrescale',
                              'B2eePrescale',
                              'B2heMuPrescale',
                              'B2pMuPrescale',
                              'Bu2KJPsieePrescale',
                              'B2TauMuPrescale',
                              'B2hTauMuPrescale',
                              'Tau2MuEtaPrimePrescale',
                              'Upsilon2eMuPrescale',
                              'Upsilon2eePrescale',
                              'RelatedInfoTools_B2eMu',
                              'RelatedInfoTools_JPsi2eMu',
                              'RelatedInfoTools_JPsi2MuMuControl',
                              'RelatedInfoTools_JPsi2eeControl',
                              'RelatedInfoTools_Phi2eMu',
                              'RelatedInfoTools_Phi2MuMuControl',
                              'RelatedInfoTools_Phi2eeControl',
                              'RelatedInfoTools_B2ee',
                              'RelatedInfoTools_B2hemu',
                              'RelatedInfoTools_Tau2PhiMu',
                              'RelatedInfoTools_Bu2KJPsiee',
                              'RelatedInfoTools_Tau2MuEtaPrime',
                              'RelatedInfoTools_Upsilon2eMu',
                              'RelatedInfoTools_Upsilon2ee',
                              'config_B2eMu',
                              'config_JPsi2eMu',
                              'config_PromptJPsi2eMu',
                              'config_Tau2MuEtaPrime',
                              'config_Upsilon2eMu',
                              'config_Upsilon2ee'
                              )
        
    def __init__(self,
                 name = 'LFV',
                 config = None) :
            
            LineBuilder.__init__(self, name, config)

            tau_name = name+'Tau2PhiMu'
            mme_name = name+'Tau2eMuMu'
            emu_name=name+'B2eMu'
            JPsiemu_name=name+'JPsi2eMu'
            JPsimumuControl_name=name+'JPsi2MuMuControl'
            JPsieeControl_name=name+'JPsi2eeControl'
            PromptJPsiemu_name=name+'PromptJPsi2eMu'
            PromptJPsimumuControl_name=name+'PromptJPsi2MuMuControl'
            PromptJPsieeControl_name=name+'PromptJPsi2eeControl'
            Phiemu_name=name+'Phi2eMu'
            PhimumuControl_name=name+'Phi2MuMuControl'
            PhieeControl_name=name+'Phi2eeControl'
            PromptPhiemu_name=name+'PromptPhi2eMu'
            PromptPhimumuControl_name=name+'PromptPhi2MuMuControl'
            PromptPhieeControl_name=name+'PromptPhi2eeControl'
            ee_name=name+'B2ee'
            hemu_name=name+'B2heMu'
            pmu_name=name+'B2hMu'
            bu_name=name+'Bu2KJPsiee'
            taumu_name=name+'B2TauMu'
            htaumu_name=name+'B2hTauMu'
            muetap_gamma_name = name+'Tau2MuEtaP2pipig'
            muetap_pi_name = name+'Tau2MuEtaP2pipipi'
            upsilon2eMu_name = name+'upsilon2eMu'
            upsilon2ee_name = name+'upsilon2ee'


            self.selTau2PhiMu       = makeTau2PhiMu(tau_name)
            self.selTau2eMuMu       = makeTau2eMuMu(mme_name)
            self.selB2eMu           = makeB2eMu(emu_name, config['config_B2eMu'])
            #JPsi LFV lines with Jpsi2ee/mumu control modes
            self.selJPsi2eMu         = makeJPsi2eMu(JPsiemu_name, config['config_JPsi2eMu'])
            self.selJPsi2MuMuControl = makeJPsi2MuMuControl(JPsimumuControl_name, config['config_JPsi2eMu'])
            self.selJPsi2eeControl   = makeJPsi2eeControl(JPsieeControl_name, config['config_JPsi2eMu'])
            # prompt Jpsi LFV with control channels
            self.selPromptJPsi2eMu          = makePromptJPsi2eMu(PromptJPsiemu_name, config['config_PromptJPsi2eMu'])
            self.selPromptJPsi2MuMuControl  = makePromptJPsi2MuMuControl(PromptJPsimumuControl_name, config['config_PromptJPsi2eMu'])
            self.selPromptJPsi2eeControl    = makePromptJPsi2eeControl(PromptJPsieeControl_name, config['config_PromptJPsi2eMu'])
            # detached Phi line can use jpsi config only mass cut in prompt line differs
            self.selPhi2eMu                 = makePhi2eMu(Phiemu_name, config['config_JPsi2eMu'])
            self.selPhi2MuMuControl         = makePhi2MuMuControl(PhimumuControl_name, config['config_JPsi2eMu'])
            self.selPhi2eeControl           = makePhi2eeControl(PhieeControl_name, config['config_JPsi2eMu'])
            # promtp phi LFV lines
            self.selPromptPhi2eMu           = makePromptPhi2eMu(PromptPhiemu_name, config['config_PromptJPsi2eMu'])
            self.selPromptPhi2MuMuControl   = makePromptPhi2MuMuControl(PromptPhimumuControl_name, config['config_PromptJPsi2eMu'])
            self.selPromptPhi2eeControl   = makePromptPhi2eeControl(PromptPhieeControl_name, config['config_PromptJPsi2eMu'])
            # ===============================================
            self.selB2ee            = makeB2ee(ee_name)
            self.selB2heMu          = makeB2heMu(hemu_name)
            self.selB2pMu           = makeB2pMu(pmu_name)
            self.selBu              = makeBu(bu_name)
            #self.selB2TauMu        = makeB2TauMu(taumu_name)
            self.selB2hTauMu        = makeB2hTauMu(htaumu_name)
            self.selTau2MuEtaPrime_gamma  = makeTau2MuEtaPrime(self, muetap_gamma_name, config['config_Tau2MuEtaPrime'], 'gamma')
            self.selTau2MuEtaPrime_pi     = makeTau2MuEtaPrime(self, muetap_pi_name, config['config_Tau2MuEtaPrime'], 'pi0')
            self.selUpsilon2eMu = makeUpsilon2eMu(self, upsilon2eMu_name, config['config_Upsilon2eMu'])
            self.selUpsilon2ee = makeUpsilon2ee(self, upsilon2ee_name, config['config_Upsilon2ee'])




            self.tau2PhiMuLine = StrippingLine(tau_name+'Line',
                                               prescale = config['TauPrescale'],
                                               postscale = config['Postscale'],
                                               MDSTFlag = False,
                                               selection=self.selTau2PhiMu,
                                               RelatedInfoTools = config['RelatedInfoTools_Tau2PhiMu'],
                                               )
                                               
            self.tau2eMuMuLine = StrippingLine(mme_name+'Line',
                                               prescale = config['Tau2MuMuePrescale'],
                                               postscale = config['Postscale'],
                                               algos = [ self.selTau2eMuMu ]
                                               )
                                               
            self.b2eMuLine = StrippingLine(emu_name+'Line',
                                           prescale = config['B2eMuPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_B2eMu'],
                                           #MDSTFlag = False,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selB2eMu ]
                                           )
            #================ JPsi LFV lines
            self.jpsi2eMuLine = StrippingLine(JPsiemu_name+'Line',
                                           prescale = config['JPsi2eMuPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_JPsi2eMu'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           RequiredRawEvents = ['Calo'],
                                           algos = [ self.selJPsi2eMu ]
                                           )
            self.promptjpsi2eMuLine = StrippingLine(PromptJPsiemu_name+'Line',
                                           prescale = config['PromptJPsi2eMuPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_JPsi2eMu'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           RequiredRawEvents = ['Calo'],
                                           algos = [ self.selPromptJPsi2eMu ],
                                           L0DU="(L0_DATA('Spd(Mult)') < {})".format(config['config_PromptJPsi2eMu']['max_SPD'])
                                           )
            #================ JPsi LFV control lines
            self.jpsi2MuMuControlLine   = StrippingLine(JPsimumuControl_name+'Line',
                                           prescale = config['JPsi2MuMuControlPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_JPsi2MuMuControl'],
                                           #MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selJPsi2MuMuControl ]
                                           )
            self.jpsi2eeControlLine   = StrippingLine(JPsieeControl_name+'Line',
                                           prescale = config['JPsi2eeControlPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_JPsi2eeControl'],
                                           #MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           RequiredRawEvents = ['Calo'],
                                           algos = [ self.selJPsi2eeControl ]
                                           )
            self.promptjpsi2MuMuControlLine = StrippingLine(PromptJPsimumuControl_name+'Line',
                                                  prescale = config['PromptJPsi2MuMuControlPrescale'],
                                                  postscale = config['Postscale'],
                                                  RelatedInfoTools = config['RelatedInfoTools_JPsi2MuMuControl'],
                                                  #MDSTFlag = True,
                                                  #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                                  algos = [ self.selPromptJPsi2MuMuControl ],
                                                  L0DU="(L0_DATA('Spd(Mult)') < {})".format(config['config_PromptJPsi2eMu']['max_SPD'])
                                                  )
            self.promptjpsi2eeControlLine = StrippingLine(PromptJPsieeControl_name+'Line',
                                                  prescale = config['PromptJPsi2eeControlPrescale'],
                                                  postscale = config['Postscale'],
                                                  RelatedInfoTools = config['RelatedInfoTools_JPsi2eeControl'],
                                                  #MDSTFlag = True,
                                                  #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                                  RequiredRawEvents = ['Calo'],
                                                  algos = [ self.selPromptJPsi2eeControl ],
                                                  L0DU="(L0_DATA('Spd(Mult)') < {})".format(config['config_PromptJPsi2eMu']['max_SPD'])
                                                  )            
            #================ Phi LFV lines
            self.phi2eMuLine = StrippingLine(Phiemu_name+'Line',
                                           prescale = config['Phi2eMuPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_Phi2eMu'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selPhi2eMu ]
                                           )

            self.promptphi2eMuLine = StrippingLine(PromptPhiemu_name+'Line',
                                           prescale = config['PromptPhi2eMuPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_Phi2eMu'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selPromptPhi2eMu ],
                                           L0DU = "(L0_DATA('Spd(Mult)') < {})".format(config['config_PromptJPsi2eMu']['max_SPD'])
                                           )                      
            #================ Phi LFV control lines
            self.phi2MuMuControlLine = StrippingLine(PhimumuControl_name+'Line',
                                           prescale = config['Phi2MuMuControlPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_Phi2MuMuControl'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selPhi2MuMuControl ]
                                           )

            self.phi2eeControlLine  = StrippingLine(PhieeControl_name+'Line',
                                           prescale = config['Phi2eeControlPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_Phi2eeControl'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selPhi2eeControl ]
                                           )

            self.promptphi2MuMuControlLine = StrippingLine(PromptPhimumuControl_name+'Line',
                                           prescale = config['PromptPhi2MuMuControlPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_Phi2MuMuControl'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selPromptPhi2MuMuControl ],
                                           L0DU = "(L0_DATA('Spd(Mult)') < {})".format(config['config_PromptJPsi2eMu']['max_SPD'])
                                           )  

            self.promptphi2eeControlLine = StrippingLine(PromptPhieeControl_name+'Line',
                                           prescale = config['PromptPhi2eeControlPrescale'],
                                           postscale = config['Postscale'],
                                           RelatedInfoTools = config['RelatedInfoTools_Phi2eeControl'],
                                           MDSTFlag = True,
                                           #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                           algos = [ self.selPromptPhi2eeControl ],
                                           L0DU = "(L0_DATA('Spd(Mult)') < {})".format(config['config_PromptJPsi2eMu']['max_SPD'])
                                           )    
            '''
            self.b2TauMuLine = StrippingLine(taumu_name+'Line',
                                            prescale = config['B2TauMuPrescale'],
                                            postscale = config['Postscale'],
                                            algos = [ self.selB2TauMu ]
                                            )
            '''

                                           
            self.b2eeLine = StrippingLine(ee_name+'Line',
                                          prescale = config['B2eePrescale'],
                                          postscale = config['Postscale'],
                                          RelatedInfoTools = config['RelatedInfoTools_B2ee'],
                                          algos = [ self.selB2ee ]
                                          )
                                       
            self.b2hTauMuLine = StrippingLine(htaumu_name+'Line',
                                              prescale = config['B2hTauMuPrescale'],
                                              postscale = config['Postscale'],
                                              algos = [ self.selB2hTauMu ]
                                              )
                                       
            self.b2heMuLine = StrippingLine(hemu_name+'Line',
                                            prescale = config['B2heMuPrescale'],
                                            postscale = config['Postscale'],
                                            RelatedInfoTools = config['RelatedInfoTools_B2hemu'],
                                            algos = [ self.selB2heMu ]
                                            )
                
                                       
            self.b2pMuLine = StrippingLine(pmu_name+'Line',
                                           prescale = config['B2pMuPrescale'],
                                           postscale = config['Postscale'],
                                           algos = [ self.selB2pMu ]
                                           )
                
            self.buLine = StrippingLine(bu_name+'Line',
                                        prescale = config['Bu2KJPsieePrescale'],
                                        postscale = config['Postscale'],
                                        algos = [ self.selBu ],
                                        #RequiredRawEvents = ['Calo'],
                                        RelatedInfoTools = config['RelatedInfoTools_Bu2KJPsiee']
                                        )
                                        
            self.Tau2MuEtaPrime_gamma = StrippingLine(muetap_gamma_name+'Line',
                                        prescale = config['Tau2MuEtaPrimePrescale'],
                                        postscale = config['Postscale'],
                                        algos = [ self.selTau2MuEtaPrime_gamma ],
                                        #MDSTFlag = False,
                                        RelatedInfoTools = config['RelatedInfoTools_Tau2MuEtaPrime'],
                                        #RequiredRawEvents = ['Calo'],
                                        )
                                        
            self.Tau2MuEtaPrime_pi = StrippingLine(muetap_pi_name+'Line',
                                                prescale = config['Tau2MuEtaPrimePrescale'],
                                                postscale = config['Postscale'],
                                                algos = [ self.selTau2MuEtaPrime_pi ],
                                                #MDSTFlag = False,
                                                RelatedInfoTools = config['RelatedInfoTools_Tau2MuEtaPrime'],
                                                #RequiredRawEvents = ['Calo'],
                                                )
                                                
                                                
            self.Upsilon2eMuLine = StrippingLine(upsilon2eMu_name+'Line',
                                                 prescale = config['Upsilon2eMuPrescale'],
                                                 postscale = config['Postscale'],
                                                 algos = [ self.selUpsilon2eMu ],
                                                 RelatedInfoTools = config['RelatedInfoTools_Upsilon2eMu'],
                                                 #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                                 )
                                                
            self.Upsilon2eeLine = StrippingLine(upsilon2ee_name+'Line',
                                                prescale = config['Upsilon2eePrescale'],
                                                postscale = config['Postscale'],
                                                algos = [ self.selUpsilon2ee ],
                                                RelatedInfoTools = config['RelatedInfoTools_Upsilon2ee'],
                                                #RequiredRawEvents = ['Velo', 'Muon', 'Calo'],
                                                )
                                        
            
            self.registerLine(self.tau2PhiMuLine)
            self.registerLine(self.tau2eMuMuLine)
            self.registerLine(self.b2eMuLine)
            # JPsi LFV
            self.registerLine(self.jpsi2eMuLine)
            self.registerLine(self.promptjpsi2eMuLine)
            # JPsi LFV control
            self.registerLine(self.jpsi2MuMuControlLine)
            self.registerLine(self.jpsi2eeControlLine)
            self.registerLine(self.promptjpsi2MuMuControlLine)
            self.registerLine(self.promptjpsi2eeControlLine)
            # Phi LFV
            self.registerLine(self.phi2eMuLine)
            self.registerLine(self.promptphi2eMuLine)
            # Phi LFV control
            self.registerLine(self.phi2MuMuControlLine)
            self.registerLine(self.phi2eeControlLine)
            self.registerLine(self.promptphi2MuMuControlLine)
            self.registerLine(self.promptphi2eeControlLine)
            ####
            self.registerLine(self.b2eeLine)
            self.registerLine(self.b2heMuLine)
            self.registerLine(self.b2pMuLine)
            self.registerLine(self.buLine)
            ##self.registerLine(self.b2TauMuLine)
            self.registerLine(self.b2hTauMuLine)
            self.registerLine(self.Tau2MuEtaPrime_gamma)
            self.registerLine(self.Tau2MuEtaPrime_pi)
            self.registerLine(self.Upsilon2eMuLine)
            self.registerLine(self.Upsilon2eeLine)






def makeTau2PhiMu(name):
    """
    Please contact Giulio Dujany if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    #from Configurables import OfflineVertexFitter
    Tau2PhiMu = CombineParticles()
    Tau2PhiMu.DecayDescriptor = " [ tau+ -> phi(1020) mu+ ]cc"

    makePhi = CombineParticles()
    makePhi.DecayDescriptor =  "phi(1020) -> K+ K-"
    makePhi.DaughtersCuts = {"K+": "(ISLONG) & (TRCHI2DOF < 3 ) & (TRGHOSTPROB<0.3) & (PT>300*MeV) & (PIDK > 0) & ( BPVIPCHI2 () >  9 )",
                             "K-": "(ISLONG) & (TRCHI2DOF < 3 ) & (TRGHOSTPROB<0.3) & (PT>300*MeV) & (PIDK > 0) & ( BPVIPCHI2 () >  9 )"}
    
    _kaons = DataOnDemand(Location='Phys/StdLooseKaons/Particles')
    
    makePhi.CombinationCut =  "(ADAMASS('phi(1020)')<30*MeV)"
    makePhi.MotherCut = " ( VFASPF(VCHI2) < 25 ) & (MIPCHI2DV(PRIMARY)> 9)"

    SelPhi = Selection( name+"SelPhi",
                        Algorithm= makePhi,
                        RequiredSelections=[_kaons] )


    Tau2PhiMu.DaughtersCuts = { "mu-" : " ( PT > 300 * MeV ) & ( TRCHI2DOF < 3 ) & (TRGHOSTPROB<0.3) & ( BPVIPCHI2 () >  9 )" }
    Tau2PhiMu.CombinationCut = "(ADAMASS('tau-')<150*MeV)"

    Tau2PhiMu.MotherCut = "( VFASPF(VCHI2) < 25 ) &  ( (BPVLTIME () * c_light)   > 50 * micrometer ) &  ( BPVIPCHI2() < 100 ) "
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

    SelTau = Selection (name+"makeTau",
                        Algorithm = Tau2PhiMu,
                        RequiredSelections = [ SelPhi, _stdLooseMuons ])
    
    
    # Trigger selection
    from Configurables import TisTosParticleTagger
    _tisTosFilter = TisTosParticleTagger( name + "Triggered" )
    _tisTosFilter.TisTosSpecs = { 'L0Global%TIS' : 0,
                                  'L0MuonDecision%TOS' : 0,
                                  'Hlt1TrackAllL0Decision%TOS' : 0,
                                  'Hlt1TrackMuonDecision%TOS' : 0
                                  }

    SelTau_triggered =  Selection( name,
                                   Algorithm = _tisTosFilter,
                                   RequiredSelections = [ SelTau ],
                                   )

    return SelTau_triggered

    
def makeTau2eMuMu(name):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    #from Configurables import OfflineVertexFitter
    #Tau2eMuMu = CombineParticles()
    Tau2eMuMu = DaVinci__N3BodyDecays()
    Tau2eMuMu.DecayDescriptors = [" [ tau+ -> e+ mu+ mu- ]cc"," [ tau+ -> mu+ mu+ e- ]cc"]
    Tau2eMuMu.DaughtersCuts = { "mu+" : " ( PT > 300 * MeV ) & ( TRCHI2DOF < 3  ) & ( BPVIPCHI2 () >  9 ) & (TRGHOSTPROB<0.3) " ,
                                "e+" : " ( PT > 300 * MeV ) & ( TRCHI2DOF < 3  ) & ( BPVIPCHI2 () >  9 ) "\
                                "& (PIDe > 2) " }
    Tau2eMuMu.CombinationCut = "(ADAMASS('tau+')<200*MeV)"

    # cut added along with the switch to DaVinci__N3BodyDecays instead of CombineParticles
    Tau2eMuMu.Combination12Cut = "(AM < 200*MeV)"

    Tau2eMuMu.MotherCut = """
            ( VFASPF(VCHI2) < 15 ) &
            ( (BPVLTIME () * c_light)   > 100 * micrometer ) &
            ( BPVIPCHI2() < 100 )
            """ 
                             
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdLooseElectrons= DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = Tau2eMuMu,
                      RequiredSelections = [ _stdLooseMuons,_stdLooseElectrons]) 


def makeB2TauMu(name):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    Bs2TauMu = CombineParticles()
    Bs2TauMu.DecayDescriptors = ["[B_s0 -> tau+ mu-]cc","[B_s0 -> tau+ mu+]cc"]
    # Set the OfflineVertexFitter to keep the 4 tracks and not the J/Psi Kstar:
    #Bs2TauMu.addTool( OfflineVertexFitter )
    #Bs2TauMu.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    #Bs2TauMu.OfflineVertexFitter.useResonanceVertex = False
    #Bs2TauMu.ReFitPVs = True
    Bs2TauMu.DaughtersCuts = { "mu+" : "(MIPCHI2DV(PRIMARY)> 25.)&(TRCHI2DOF < 3 ) & (TRGHOSTPROB<0.3)"}

    Bs2TauMu.CombinationCut = "(ADAMASS('B_s0')<1200*MeV)"\
                            "& (AMAXDOCA('')<0.3*mm)"

    Bs2TauMu.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                              "& (ADMASS('B_s0') < 1200*MeV )"\
                              "& (BPVDIRA > 0) "\
                              "& (BPVVDCHI2> 225)"\
                              "& (BPVIPCHI2()< 25) "
    
    from CommonParticles import StdLooseDetachedTau, StdLooseDipion
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdLooseDetachedTaus= DataOnDemand(Location = "Phys/StdLooseDetachedTau3pi/Particles")

    return Selection (name,
                      Algorithm = Bs2TauMu,
                      RequiredSelections = [ _stdLooseMuons,_stdLooseDetachedTaus])


def makeB2eMu(name, myconfig):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    Bs2eMu = CombineParticles(
    
        DecayDescriptors = ["[B_s0 -> e+ mu-]cc","[B_s0 -> e+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & (TRCHI2DOF < {max_TRCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB})".format(**myconfig) ,
          "e+"  : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV})&(TRCHI2DOF < {max_TRCHI2DV})".format(**myconfig),
        },

        CombinationCut = "(ADAMASS('B_s0') < {max_ADAMASS})"\
                            "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                              "& (ADMASS('B_s0') < {max_ADAMASS} )"\
                              "& (BPVDIRA > {min_BPVDIRA}) "\
                              "& (BPVVDCHI2 > {min_BPVVDCHI2})"\
                              "& (BPVIPCHI2() < {max_BPVIPCHI2}) ".format(**myconfig),
    )
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdLooseElectrons= DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = Bs2eMu,
                      RequiredSelections = [ _stdLooseMuons,_stdLooseElectrons])


def makeJPsi2eMu(name, myconfig):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    JPsi2eMu = CombineParticles(
    
        DecayDescriptors = ["[J/psi(1S) -> e+ mu-]cc","[J/psi(1S) -> e+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV})"\
                  " & (TRCHI2DOF < {max_TRCHI2DV}) & (PROBNNmu > {min_ProbNN}) &"\
                  "(TRGHOSTPROB< {max_TRGHOSTPROB}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e+"  : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (PROBNNe > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_JpsiMass}, AM, {max_JpsiMass} )"\
                          "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) &"\
                     "in_range( {min_JpsiMass}, MM, {max_JpsiMass} )"\
                     "& (BPVDIRA > {min_BPVDIRA}) "\
                     "& (BPVVDCHI2 > {min_BPVVDCHI2})".format(**myconfig)
    )
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdLooseElectrons= DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = JPsi2eMu,
                      RequiredSelections = [ _stdLooseMuons,_stdLooseElectrons])


def makeJPsi2MuMuControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if any issues 
    occur with this line. 
    Cloned from JPsi2eMu Line except for the PID criteria

    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    JPsi2MuMuControl = CombineParticles(
    
        DecayDescriptors = ["J/psi(1S) -> mu+ mu-","[J/psi(1S) -> mu+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB< {max_TRGHOSTPROB}) & (PROBNNmu > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "mu-"  : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (PROBNNmu > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig) # remove PIDe>-2 for muon!
        },

        CombinationCut = "(ADAMASS('J/psi(1S)') < {max_ADAMASS})"\
                            "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF)<{max_VtxChi2DoF}) "\
                    " & in_range( {min_JpsiMass}, MM, {max_JpsiMass} )"\
                    " & (BPVDIRA > {min_BPVDIRA}) "\
                    " & (BPVVDCHI2 > {min_BPVVDCHI2})".format(**myconfig)
    )
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    
    return Selection (name,
                      Algorithm = JPsi2MuMuControl,
                      RequiredSelections = [ _stdLooseMuons])


def makeJPsi2eeControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if any issues 
    occur with this line. 
    Cloned from JPsi2eMu Line except for the PID criteria

    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    JPsi2eeControl = CombineParticles(
    
        DecayDescriptors = ["J/psi(1S) -> e+ e-","[J/psi(1S) -> e+ e+]cc"],
        DaughtersCuts = {
          "e+" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & (TRCHI2DOF < {max_TRCHI2DV}) & "\
                 "(TRGHOSTPROB< {max_TRGHOSTPROB}) & (PROBNNe > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e-" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & (TRCHI2DOF < {max_TRCHI2DV}) &"\
                 "(TRGHOSTPROB< {max_TRGHOSTPROB}) & (PROBNNe > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig) # remove PIDe>-2 for muon! IS implicitly made in stdLooseElectrons
        },

        CombinationCut = "in_range( {min_JpsiMass}, AM, {max_JpsiMass} )"\
                         "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                    "& in_range( {min_JpsiMass}, MM, {max_JpsiMass} )"\
                    "& (BPVDIRA > {min_BPVDIRA}) "\
                    "& (BPVVDCHI2 > {min_BPVVDCHI2})".format(**myconfig)
    )
    
    _stdLooseElectrons = DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")
    
    return Selection (name,
                      Algorithm = JPsi2eeControl,
                      RequiredSelections = [ _stdLooseElectrons])


def makePromptJPsi2eMu(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """

    #from Configurables import OfflineVertexFitter
    PromptJPsi2eMu = CombineParticles(
    
        DecayDescriptors = ["[J/psi(1S) -> e+ mu-]cc","[J/psi(1S) -> e+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB})"\
                  " & (PROBNNmu > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e+"  : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) & "\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB})"\
                  " & ( PROBNNe > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_JpsiMass}, AM, {max_JpsiMass} )"\
                         "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                    "& in_range( {min_JpsiMass}, MM, {max_JpsiMass} )"\
                    "& (BPVVDCHI2 < {max_BPVVDCHI2})"\
                    "& (BPVIPCHI2() < {max_BPVIPCHI2})".format(**myconfig),
    )
    
    _stdAllLooseMuons = DataOnDemand(Location = "Phys/StdAllLooseMuons/Particles")
    _stdAllLooseElectrons= DataOnDemand(Location = "Phys/StdAllLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = PromptJPsi2eMu,
                      RequiredSelections = [ _stdAllLooseMuons,_stdAllLooseElectrons])


def makePromptJPsi2MuMuControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if 
    this line has issues. 
    
    Arguments:
    name        : name of the Selection.
    """

    #from Configurables import OfflineVertexFitter
    PromptJPsi2MuMuControl = CombineParticles(
    
        DecayDescriptors = ["J/psi(1S) -> mu+ mu-","[J/psi(1S) -> mu+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB})"\
                  " & (PROBNNmu > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "mu-" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB})"\
                  " & ( PROBNNmu > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_JpsiMass}, AM, {max_JpsiMass} )"\
                         "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                    "& in_range( {min_JpsiMass}, MM, {max_JpsiMass} )"\
                    "& (BPVVDCHI2 < {max_BPVVDCHI2})"\
                    "& (BPVIPCHI2() < {max_BPVIPCHI2})".format(**myconfig),
    )
    
    _stdAllLooseMuons = DataOnDemand(Location = "Phys/StdAllLooseMuons/Particles")

    return Selection (name,
                      Algorithm = PromptJPsi2MuMuControl,
                      RequiredSelections = [ _stdAllLooseMuons])


def makePromptJPsi2eeControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if 
    this line has issues. 
    
    Arguments:
    name        : name of the Selection.
    """

    #from Configurables import OfflineVertexFitter
    PromptJPsi2eeControl = CombineParticles(
    
        DecayDescriptors = ["J/psi(1S) -> e+ e-","[J/psi(1S) -> e+ e+]cc"],
        DaughtersCuts = {
          "e+" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB})"\
                  " & (PROBNNe > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e-" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & (TRGHOSTPROB< {max_TRGHOSTPROB})"\
                  " & ( PROBNNe > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_JpsiMass}, AM, {max_JpsiMass} )"\
                         "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                    "& in_range( {min_JpsiMass}, MM, {max_JpsiMass} )"\
                    "& (BPVVDCHI2 < {max_BPVVDCHI2})"\
                    "& (BPVIPCHI2() < {max_BPVIPCHI2})".format(**myconfig),
    )
    
    _stdAllLooseElectrons = DataOnDemand(Location = "Phys/StdAllLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = PromptJPsi2eeControl,
                      RequiredSelections = [ _stdAllLooseElectrons])


def makePhi2eMu(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    Phi2eMu = CombineParticles(
    
        DecayDescriptors = ["[phi(1020) -> e+ mu-]cc","[phi(1020) -> e+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & "\
                  "(TRCHI2DOF < {max_TRCHI2DV}) &"\
                  "(TRGHOSTPROB< {max_TRGHOSTPROB}) & "\
                  "(PROBNNmu > {min_ProbNN_phi}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e+"  : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & "\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB< {max_TRGHOSTPROB}) & "\
                  "(PROBNNe > {min_ProbNN_phi}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "(ADAMASS('phi(1020)') < {max_ADAMASS})"\
                            "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                              "& (MM > {min_PhiMass}) & (MM < {max_PhiMass})"\
                              "& (BPVDIRA > {min_BPVDIRA}) "\
                              "& (BPVVDCHI2 > {min_BPVVDCHI2})".format(**myconfig)
    )
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdLooseElectrons= DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = Phi2eMu,
                      RequiredSelections = [ _stdLooseMuons,_stdLooseElectrons])


def makePhi2MuMuControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if experience 
    issues with this line
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    Phi2MuMuControl = CombineParticles(
    
        DecayDescriptors = ["phi(1020) -> mu+ mu-","[phi(1020) -> mu+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY) > {min_MIPCHI2DV}) & "\
                  "(TRCHI2DOF < {max_TRCHI2DV}) &"\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) &"\
                  "(PROBNNmu > {min_ProbNN_phi}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "mu-" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & "\
                  "(TRCHI2DOF < {max_TRCHI2DV}) &"\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) &"\
                  "(PROBNNmu > {min_ProbNN_phi}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_PhiMass}, AM, {max_PhiMass} )"\
                            "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF} ) "\
                              "& (MM > {min_PhiMass}) & (MM < {max_PhiMass})"\
                              "& (BPVDIRA > {min_BPVDIRA}) "\
                              "& (BPVVDCHI2 > {min_BPVVDCHI2})".format(**myconfig)
    )
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

    return Selection (name,
                      Algorithm = Phi2MuMuControl,
                      RequiredSelections = [ _stdLooseMuons])


def makePhi2eeControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if experience 
    issues with this line
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    Phi2eeControl = CombineParticles(
    
        DecayDescriptors = ["phi(1020) -> e+ e-","[phi(1020) -> e+ e+]cc"],
        DaughtersCuts = {
          "e+" : "(MIPCHI2DV(PRIMARY) > {min_MIPCHI2DV}) & "\
                  "(TRCHI2DOF < {max_TRCHI2DV}) &"\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) &"\
                  "(PROBNNe > {min_ProbNN_phi}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e-" : "(MIPCHI2DV(PRIMARY)> {min_MIPCHI2DV}) & "\
                  "(TRCHI2DOF < {max_TRCHI2DV}) &"\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) &"\
                  "(PROBNNe > {min_ProbNN_phi}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_PhiMass}, AM, {max_PhiMass} )"\
                            "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF} ) "\
                              "& (MM > {min_PhiMass}) & (MM < {max_PhiMass})"\
                              "& (BPVDIRA > {min_BPVDIRA}) "\
                              "& (BPVVDCHI2 > {min_BPVVDCHI2})".format(**myconfig)
    )
    
    _stdLooseElectrons = DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = Phi2eeControl,
                      RequiredSelections = [ _stdLooseElectrons])


def makePromptPhi2eMu(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """

    #from Configurables import OfflineVertexFitter
    PromptPhi2eMu = CombineParticles(
    
        DecayDescriptors = ["[phi(1020) -> e+ mu-]cc","[phi(1020) -> e+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) &"\
                  "(PROBNNmu > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e+"  : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) & "\
                  "( PROBNNe > {min_ProbNN}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_PhiMass}, AM, {max_PhiMass} )"\
                         "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                    "& (MM < {max_PhiMass})"\
                    "& (MM > {min_PhiMass} )"\
                    "& (BPVVDCHI2 < {max_BPVVDCHI2})"\
                    "& (BPVIPCHI2() < {max_BPVIPCHI2})".format(**myconfig),
    )
    
    _stdAllLooseMuons = DataOnDemand(Location = "Phys/StdAllLooseMuons/Particles")
    _stdAllLooseElectrons= DataOnDemand(Location = "Phys/StdAllLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = PromptPhi2eMu,
                      RequiredSelections = [ _stdAllLooseMuons,_stdAllLooseElectrons])


def makePromptPhi2MuMuControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if you see 
    issues with this line.
    
    Arguments:
    name        : name of the Selection.
    """

    #from Configurables import OfflineVertexFitter
    PromptPhi2MuMuControl = CombineParticles(
    
        DecayDescriptors = ["phi(1020) -> mu+ mu-","[phi(1020) -> mu+ mu+]cc"],
        DaughtersCuts = {
          "mu+" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) & "\
                  "(PROBNNmu > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "mu-" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) & "\
                  "(PROBNNmu > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_PhiMass}, AM, {max_PhiMass} )"\
                         "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                    "& (MM < {max_PhiMass})"\
                    "& (MM > {min_PhiMass} )"\
                    "& (BPVVDCHI2 < {max_BPVVDCHI2})"\
                    "& (BPVIPCHI2() < {max_BPVIPCHI2})".format(**myconfig),
    )
    
    _stdAllLooseMuons = DataOnDemand(Location = "Phys/StdAllLooseMuons/Particles")

    return Selection (name,
                      Algorithm = PromptPhi2MuMuControl,
                      RequiredSelections = [ _stdAllLooseMuons])

def makePromptPhi2eeControl(name, myconfig):
    """
    Please contact Maximilian Schlupp or Johannes Albrecht if you see 
    issues with this line.
    
    Arguments:
    name        : name of the Selection.
    """

    #from Configurables import OfflineVertexFitter
    PromptPhi2eeControl = CombineParticles(
    
        DecayDescriptors = ["phi(1020) -> e+ e-","[phi(1020) -> e+ e+]cc"],
        DaughtersCuts = {
          "e+" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) & "\
                  "(PROBNNe > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig) ,
          "e-" : "(MIPCHI2DV(PRIMARY) < {max_MIPCHI2DV}) &"\
                  "(TRCHI2DOF < {max_TRCHI2DV}) & "\
                  "(TRGHOSTPROB < {max_TRGHOSTPROB}) & "\
                  "(PROBNNe > {min_ProbNN_Control}) & "\
                  "(PT > {min_Pt})".format(**myconfig),
        },

        CombinationCut = "in_range( {min_PhiMass}, AM, {max_PhiMass} )"\
                         "& (AMAXDOCA('') < {max_AMAXDOCA})".format(**myconfig),

        MotherCut = "(VFASPF(VCHI2/VDOF) < {max_VtxChi2DoF}) "\
                    "& (MM < {max_PhiMass})"\
                    "& (MM > {min_PhiMass} )"\
                    "& (BPVVDCHI2 < {max_BPVVDCHI2})"\
                    "& (BPVIPCHI2() < {max_BPVIPCHI2})".format(**myconfig),
    )
    
    _stdAllLooseElectrons = DataOnDemand(Location = "Phys/StdAllLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = PromptPhi2eeControl,
                      RequiredSelections = [ _stdAllLooseElectrons])


def makeB2ee(name):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    Bs2ee = CombineParticles()
    Bs2ee.DecayDescriptors = ["B_s0 -> e+ e-","[B_s0 -> e+ e+]cc"]

    #Bs2ee.addTool( OfflineVertexFitter )
    #Bs2ee.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    #Bs2ee.OfflineVertexFitter.useResonanceVertex = False
    Bs2ee.ReFitPVs = False
    Bs2ee.DaughtersCuts = { "e+" : "(MIPCHI2DV(PRIMARY)> 25.)&(TRCHI2DOF < 3 )"}

    Bs2ee.CombinationCut = "(ADAMASS('B_s0')<1200*MeV)"\
                            "& (AMAXDOCA('')<0.3*mm)"

    Bs2ee.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                              "& (ADMASS('B_s0') < 1200*MeV )"\
                              "& (BPVDIRA > 0) "\
                              "& (BPVVDCHI2> 225)"\
                              "& (BPVIPCHI2()< 25) "
                             
    _stdLooseElectrons= DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = Bs2ee,
                      RequiredSelections = [ _stdLooseElectrons])


def makeB2hTauMu(name):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    #Bs2hTauMu = CombineParticles()
    Bs2hTauMu = DaVinci__N3BodyDecays()
    Bs2hTauMu.DecayDescriptors = ["[B+ -> K+ tau+ mu-]cc","[B+ -> K- tau+ mu+]cc", "[B+ -> K+ tau- mu+]cc",
                                  "[B+ -> pi+ tau+ mu-]cc","[B+ -> pi- tau+ mu+]cc", "[B+ -> pi+ tau- mu+]cc",
                                  "[B+ -> p+ tau+ mu-]cc","[B- -> p+ tau- mu-]cc", "[B+ -> p+ tau- mu+]cc"]
    #Bs2hTauMu.addTool( OfflineVertexFitter )
    #Bs2hTauMu.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    #Bs2hTauMu.OfflineVertexFitter.useResonanceVertex = False
    #Bs2hTauMu.ReFitPVs = True
    Bs2hTauMu.DaughtersCuts = { "mu+" : "(MIPCHI2DV(PRIMARY)>36.)&(TRCHI2DOF<3)& (TRGHOSTPROB<0.3)",
                              "pi+" : "(MIPCHI2DV(PRIMARY)>36.)&(TRCHI2DOF<3) & (TRGHOSTPROB<0.3)",
                              "K+" : "(MIPCHI2DV(PRIMARY)>36.)&(TRCHI2DOF<3)&(PIDK>5)& (TRGHOSTPROB<0.3)",
                              "p+" : "(MIPCHI2DV(PRIMARY)>36.)&(TRCHI2DOF<3)&(PIDp>5)& (TRGHOSTPROB<0.3)"}

    Bs2hTauMu.CombinationCut = "(ADAMASS('B+')<400*MeV)"\
                            "& (AMAXDOCA('')<0.15*mm)"

    # cut added along with the switch to DaVinci__N3BodyDecays instead of CombineParticles
    Bs2hTauMu.Combination12Cut = "(AM < 6100*MeV)"\
                                 "& (AMAXDOCA('')<0.15*mm)"

    Bs2hTauMu.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                          "& (BPVDIRA>0.999)"\
                          "& (ADMASS('B_s0') < 400*MeV )"\
                          "& (BPVDIRA > 0) "\
                          "& (BPVVDCHI2> 225)"\
                          "& (BPVIPCHI2()< 16) "#maybe 16
    
    from CommonParticles import StdLooseDetachedTau, StdLooseDipion
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdLooseDetachedTaus= DataOnDemand(Location = "Phys/StdLooseDetachedTau3pi/Particles")
    _stdNoPIDsPions= DataOnDemand(Location = "Phys/StdNoPIDsPions/Particles")
    _stdNoPIDsKaons= DataOnDemand(Location = "Phys/StdNoPIDsKaons/Particles")
    _stdNoPIDsProtons= DataOnDemand(Location = "Phys/StdNoPIDsProtons/Particles")
    

    return Selection (name,
                      Algorithm = Bs2hTauMu,
                      RequiredSelections = [ _stdLooseMuons,_stdLooseDetachedTaus,
                                             _stdNoPIDsPions, _stdNoPIDsKaons,
                                             _stdNoPIDsProtons ])
                      

def makeB2heMu(name):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    #Bs2heMu = CombineParticles()
    Bs2heMu = DaVinci__N3BodyDecays()
    Bs2heMu.DecayDescriptors = ["[B+ -> K+ e+ mu-]cc","[B+ -> K- e+ mu+]cc", "[B+ -> K+ e- mu+]cc",
                                "[B+ -> pi+ e+ mu-]cc","[B+ -> pi- e+ mu+]cc" , "[B+ -> pi+ e- mu+]cc",
                                "[B+ -> p+ e+ mu-]cc","[B- -> p+ e- mu-]cc", "[B+ -> p+ e- mu+]cc"]
    #Bs2heMu.addTool( OfflineVertexFitter )
    #Bs2heMu.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    #Bs2heMu.OfflineVertexFitter.useResonanceVertex = False
    #Bs2heMu.ReFitPVs = True
    Bs2heMu.DaughtersCuts = { "mu+" : "(MIPCHI2DV(PRIMARY)>25.)&(TRCHI2DOF<3) & (TRGHOSTPROB<0.3)",
                              "e+" : "(MIPCHI2DV(PRIMARY)>25.)&(TRCHI2DOF<3) & (PIDe > 2)",
                              "pi+" : "(MIPCHI2DV(PRIMARY)>25.)&( TRCHI2DOF < 3 )& (TRGHOSTPROB<0.3)",
                              "p+" : "(MIPCHI2DV(PRIMARY)>25.)&(TRCHI2DOF<3)&(PIDp>5) & (TRGHOSTPROB<0.3)",
                              "K+" : "(MIPCHI2DV(PRIMARY)>25.)&(TRCHI2DOF<3)&(PIDK>5) & (TRGHOSTPROB<0.3)"}

    Bs2heMu.CombinationCut = "(ADAMASS('B+')<600*MeV)"\
                            "& (AMAXDOCA('')<0.3*mm)"
    # cut added along with the switch to DaVinci__N3BodyDecays instead of CombineParticles
    Bs2heMu.Combination12Cut = "(AM < 6300*MeV)"\
                               "& (AMAXDOCA('')<0.3*mm)"


    Bs2heMu.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                              "& (ADMASS('B_s0') < 600*MeV )"\
                              "& (BPVDIRA > 0) "\
                              "& (BPVVDCHI2> 225)"\
                              "& (BPVIPCHI2()< 25) "

    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdLooseElectrons= DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")
    _stdNoPIDsPions= DataOnDemand(Location = "Phys/StdNoPIDsPions/Particles")
    _stdNoPIDsKaons= DataOnDemand(Location = "Phys/StdNoPIDsKaons/Particles")
    _stdNoPIDsProtons= DataOnDemand(Location = "Phys/StdNoPIDsProtons/Particles")
    
    return Selection (name,
                      Algorithm = Bs2heMu,
                      RequiredSelections = [ _stdLooseMuons,_stdLooseElectrons,
                                             _stdNoPIDsPions, _stdNoPIDsKaons,
                                             _stdNoPIDsProtons ])


def makeB2pMu(name):
    """
    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    
    #from Configurables import OfflineVertexFitter
    Bs2pMu = CombineParticles()
    Bs2pMu.DecayDescriptors = [ "[B_s0 -> p+ mu-]cc","[B_s0 -> p+ mu+]cc",
                                "[B_s0 -> pi+ mu-]cc","[B_s0 -> pi+ mu+]cc",
                                "[B_s0 -> K+ mu-]cc","[B_s0 -> K+ mu+]cc"]
    #Bs2pMu.addTool( OfflineVertexFitter )
    #Bs2pMu.VertexFitters.update( { "" : "OfflineVertexFitter"} )
    #Bs2pMu.OfflineVertexFitter.useResonanceVertex = False
    #Bs2pMu.ReFitPVs = True
    Bs2pMu.DaughtersCuts = { "mu+" : "(MIPCHI2DV(PRIMARY)> 25.)&(TRCHI2DOF < 3 ) & (TRGHOSTPROB<0.3)",
                             "pi+" : "(MIPCHI2DV(PRIMARY)>36.)&(TRCHI2DOF<3)&(TRGHOSTPROB<0.3)",
                             "K+" : "(MIPCHI2DV(PRIMARY)>25.)&(TRCHI2DOF<3) & (PIDK>5) & (TRGHOSTPROB<0.3)",
                             "p+" : "(MIPCHI2DV(PRIMARY)> 25.)&(TRCHI2DOF < 3 )& (PIDp>5) & (TRGHOSTPROB<0.3)"}

    Bs2pMu.CombinationCut = "(ADAMASS('B_s0')<300*MeV)"\
                            "& (AMAXDOCA('')<0.1*mm)"
    
    Bs2pMu.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                       "& (ADMASS('B_s0') < 600*MeV )"\
                       "& (BPVDIRA > 0) "\
                       "& (BPVVDCHI2> 225)"\
                       "& (BPVIPCHI2()< 25) "

    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")
    _stdNoPIDsPions= DataOnDemand(Location = "Phys/StdNoPIDsPions/Particles")
    _stdNoPIDsKaons= DataOnDemand(Location = "Phys/StdNoPIDsKaons/Particles")
    _stdNoPIDsProtons= DataOnDemand(Location = "Phys/StdNoPIDsProtons/Particles")
    


    return Selection (name,
                      Algorithm = Bs2pMu,
                      RequiredSelections = [ _stdLooseMuons,_stdNoPIDsPions,
                                             _stdNoPIDsKaons,_stdNoPIDsProtons ])


def makeBu(name) :
    """
    detached Bu-->JPsiK selection.

    Please contact Flavio Archilli if you think of prescaling this line!

    Arguments:
    name        : name of the Selection.
    """

    
    #from Configurables import OfflineVertexFitter
   
    SelDJPsi = makeDetachedJPsi(name)

    PreselBu2JPsiKCommon = CombineParticles()
    PreselBu2JPsiKCommon.DecayDescriptor =  " [B+ -> J/psi(1S) K+]cc ";
    #PreselBu2JPsiKCommon.addTool( OfflineVertexFitter )
    #PreselBu2JPsiKCommon.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    #PreselBu2JPsiKCommon.OfflineVertexFitter.useResonanceVertex = False
    PreselBu2JPsiKCommon.ReFitPVs = True
    PreselBu2JPsiKCommon.DaughtersCuts = { "K+" : "(ISLONG) & (TRCHI2DOF < 3 ) &(MIPCHI2DV(PRIMARY)>25)& (PT>250*MeV) & (TRGHOSTPROB<0.3) "}
    PreselBu2JPsiKCommon.CombinationCut = "(ADAMASS('B+') < 600*MeV)"
    PreselBu2JPsiKCommon.MotherCut = "(BPVIPCHI2()< 25)& (VFASPF(VCHI2)<45) "

    _kaons = DataOnDemand(Location='Phys/StdNoPIDsKaons/Particles')

    return Selection( "SelBu2KJPsiee",
                         Algorithm = PreselBu2JPsiKCommon,
                         RequiredSelections=[SelDJPsi,_kaons] )


def makeDetachedJPsi(name) :
    """
    detached JPsi selection for B--> JPsi X calibration and
    normalization channels. 

    Please contact Flavio Archilli if you think of prescaling this line!

    Arguments:
    name        : name of the Selection.
    """
    #from Configurables import OfflineVertexFitter
    DetachedJPsi = CombineParticles()
    DetachedJPsi.DecayDescriptor = "J/psi(1S) -> e+ e-"
    #DetachedJPsi.addTool( OfflineVertexFitter )
    #DetachedJPsi.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    #DetachedJPsi.OfflineVertexFitter.useResonanceVertex = False
    DetachedJPsi.ReFitPVs = True
    DetachedJPsi.DaughtersCuts = { "e+" : "(TRCHI2DOF < 3 ) "\
                                   "& (MIPCHI2DV(PRIMARY)> 25.) "\
                                   "& (PIDe > 2) "}
                                 
    DetachedJPsi.CombinationCut = "(ADAMASS('J/psi(1S)')<1000*MeV) "\
                                   "& (AMAXDOCA('')<0.3*mm)"

    DetachedJPsi.MotherCut = "(VFASPF(VCHI2)<9) "\
                             "& (ADMASS('J/psi(1S)') < 1000*MeV )"\
                             "& (BPVDIRA > 0) "\
                             "& (BPVVDCHI2>169)"

    _stdLooseElectrons = DataOnDemand(Location = "Phys/StdLooseElectrons/Particles")

    return Selection (name,
                      Algorithm = DetachedJPsi,
                      RequiredSelections = [ _stdLooseElectrons ])


def makeTau2MuEtaPrime(self, name, config, setEtaPrime) :
    
    """
    tau -> mu eta' selection
        
    Please contact Guido Andreassi if you think of prescaling this line!
        
    Arguments:
    name        : name of the Selection, configuration dictionary.
    """
            
    if setEtaPrime == 'gamma':
        self.SelEtaPrime = makeEtaPrime2pipigamma("selEtap_gamma", config['config_EtaPrime2pipigamma'])
    
    if setEtaPrime == 'pi0':
        self.SelEtaPrime = makeEtaPrime2pipipi("selEtap_pi0", config['config_EtaPrime2pipipi'])


    Tau2MuEtaPrime = CombineParticles()
    Tau2MuEtaPrime.DecayDescriptor =  "[tau+ -> mu+ eta_prime]cc ";
    Tau2MuEtaPrime.ReFitPVs = True
    Tau2MuEtaPrime.DaughtersCuts = { "mu+" : "{muplus_cuts}".format(**config)}
    Tau2MuEtaPrime.CombinationCut = "{tau_mass_window}".format(**config)
    Tau2MuEtaPrime.MotherCut = "{tau_cuts}".format(**config)
                
    _muons = DataOnDemand(Location="Phys/StdLooseMuons/Particles")
                    
    return Selection( name,
                        Algorithm = Tau2MuEtaPrime,
                        RequiredSelections=[self.SelEtaPrime,_muons] )


def makeEtaPrime2pipigamma(name, config) :
    """
        eta' selection for tau -> mu eta'
        Please contact Guido Andreassi if you think of prescaling this line!
        
        Arguments:
        name        : name of the Selection , config:  configuration dictionary.
        """
    EtaPrime2pipigamma = DaVinci__N3BodyDecays()
    EtaPrime2pipigamma.DecayDescriptor = "eta_prime -> pi+ pi- gamma"
    EtaPrime2pipigamma.ReFitPVs = True
    EtaPrime2pipigamma.Combination12Cut  = "{pipi_cuts}".format(**config)
    EtaPrime2pipigamma.DaughtersCuts = {"pi+"     : "{piplus_cuts}".format(**config),
                              "pi-"     : "{piminus_cuts}".format(**config),
                              "gamma"   : "{gamma_cuts}".format(**config)}
                                    
    EtaPrime2pipigamma.CombinationCut = "{etap_mass_window}".format(**config)
    EtaPrime2pipigamma.MotherCut = "{etap_cuts}".format(**config)
                                            
    _stdLoosePions = DataOnDemand (Location = "Phys/StdLoosePions/Particles")
    _stdLooseAllPhotons = DataOnDemand (Location = "Phys/StdLooseAllPhotons/Particles")
    
    return Selection (name,
                        Algorithm = EtaPrime2pipigamma,
                        RequiredSelections = [ _stdLoosePions, _stdLooseAllPhotons ])


def makeEtaPrime2pipipi(name, config) :
    """
        eta' selection for tau -> mu eta'
        Please contact Guido Andreassi if you think of prescaling this line!
        
        Arguments:
        name        : name of the Selection , config:  configuration dictionary.
        """
    EtaPrime2pipipi = DaVinci__N3BodyDecays()
    EtaPrime2pipipi.DecayDescriptor = "eta_prime -> pi+ pi- pi0"
    EtaPrime2pipipi.ReFitPVs = True
    EtaPrime2pipipi.Combination12Cut  = "{pipi_cuts}".format(**config)
    EtaPrime2pipipi.DaughtersCuts = {"pi+"     : "{piplus_cuts}".format(**config),
                                     "pi-"     : "{piminus_cuts}".format(**config),
                                     "pi0"     : "{pi0_cuts}".format(**config)}

    EtaPrime2pipipi.CombinationCut = "{etap_mass_window}".format(**config)
    EtaPrime2pipipi.MotherCut = "{etap_cuts}".format(**config)
    
    _stdLoosePions = DataOnDemand (Location = "Phys/StdLoosePions/Particles")
    _stdLooseResolvedPi0 = DataOnDemand (Location = "Phys/StdLooseResolvedPi0/Particles")
    _stdLooseMergedPi0 = DataOnDemand (Location = "Phys/StdLooseMergedPi0/Particles")
    _stdPi0 = MergedSelection("Pi0For" + name, RequiredSelections = [ _stdLooseResolvedPi0, _stdLooseMergedPi0 ])

    return Selection (name,
                      Algorithm = EtaPrime2pipipi,
                      RequiredSelections = [ _stdLoosePions, _stdPi0])





def makeUpsilon2eMu(self, name, config):
    """
        eta' selection for upsilon -> e mu
        Please contact Guido Andreassi if you think of modifying this line!
        
        Arguments:
        name        : name of the Selection , config:  configuration dictionary.
        """
    
    Upsilon2eMu = CombineParticles(
                                   DecayDescriptors = ["[Upsilon(1S) -> e+ mu-]cc","[Upsilon(1S) -> e+ mu+]cc"],
                                   DaughtersCuts = {
                                   "mu+" : "{mu_cuts}".format(**config) ,
                                   "e+"  : "{e_cuts}".format(**config),
                                   },
                                   CombinationCut = "{comb_cuts}".format(**config),
                                   MotherCut = "{upsilon_cuts}".format(**config)
                                   )
        
    _stdTightMuons = DataOnDemand(Location = "Phys/StdTightMuons/Particles")
    _stdTightElectrons = DataOnDemand(Location = "Phys/StdTightElectrons/Particles")
                                   
    return Selection(name,
                     Algorithm = Upsilon2eMu,
                     RequiredSelections = [ _stdTightMuons, _stdTightElectrons])


def makeUpsilon2ee(self, name, config):
    """
        eta' selection for upsilon -> e e
        Please contact Guido Andreassi if you think of modifying this line!
        
        Arguments:
        name        : name of the Selection , config:  configuration dictionary.
        """
    
    Upsilon2ee = CombineParticles(
                                  DecayDescriptors = ["Upsilon(1S) -> e+ e-","[Upsilon(1S) -> e+ e+]cc"],
                                  DaughtersCuts = {"e+"  : "{e_cuts}".format(**config)},
                                  CombinationCut = "{comb_cuts}".format(**config),
                                  MotherCut = "{upsilon_cuts}".format(**config)
                                  )
        
    _stdTightElectrons = DataOnDemand(Location = "Phys/StdTightElectrons/Particles")
                                  
    return Selection(name,
                     Algorithm = Upsilon2ee,
                     RequiredSelections = [_stdTightElectrons])


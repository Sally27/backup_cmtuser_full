
'''
Module for construction of Bs-->MuMu stripping selections and lines

Exported symbols (use python help!):
   - Bs2MuMuLinesConf
   - makeDefault
   - makeBs2mmWide
   - makeLoose
   - makeDetachedJPsi
   - makeDetachedJPsiLoose
   - makePromptJPsi
'''

__author__ = ['Marc-Olivier Bettler']
__date__ = '07/08/2014'
__version__ = '$Revision: 1.3 $'

__all__ = ('Bs2MuMuLinesConf',
           'default_config',
           'makeDefault',
           'makeBs2mmWide',
           'makeLoose',
           'makeBu',
           'makeBs',
           'makeBd',
           'makeSS',
           'makeBs2mmLTUB',
           'makeBs2KKLTUB'
#           'makeDetachedJPsi',
#           'makeDetachedJPsiLoose',
#           'makePromptJPsi'
           )

default_config = {
    'Name' : 'Bs2MuMuLines',
    'WGs'  : ['RD'],
    'BUILDERTYPE' : 'Bs2MuMuLinesConf',
    'CONFIG'   : {
        'DefaultLinePrescale'    : 1,
        'DefaultPostscale'   : 1,
        'Bs2mmWideLinePrescale'  : 1,
        'LooseLinePrescale'      : 0.,
        'BuPrescale'    : 1,
        'BsPrescale'    : 1,
        'BdPrescale'    : 1,
        'JPsiLinePrescale'       : 1,
        'JPsiLooseLinePrescale'  : 0.1,
        'JPsiPromptLinePrescale' : 0.005,
        'SSPrescale'             : 1 ,
        'Bs2mmLTUBLinePrescale'  : 1 ,
        'Bs2KKLTUBLinePrescale' : 1 ,
        'MuIPChi2_loose'        :  9,
        'MuTrChi2_loose'        : 10,
        'BIPChi2_loose'         : 64,
        'BFDChi2_loose'         : 100,
        'BPVVDChi2'            : 121, 
        'daugt_IPChi2'            : 9
        },
    'STREAMS' : ['Dimuon']
        }                
    
tighter_config = {
    'Name' : 'Bs2MuMuLines',
    'WGs'  : ['RD'],
    'BUILDERTYPE' : 'Bs2MuMuLinesConf',
    'CONFIG'   : {
        'DefaultLinePrescale'    : 1,
        'DefaultPostscale'   : 1,
        'Bs2mmWideLinePrescale'  : 1,
        'LooseLinePrescale'      : 0.,
        'BuPrescale'    : 1,
        'BsPrescale'    : 1,
        'BdPrescale'    : 1,
        'JPsiLinePrescale'       : 1,
        'JPsiLooseLinePrescale'  : 0.1,
        'JPsiPromptLinePrescale' : 0.005,
        'SSPrescale'             : 1 ,
        'Bs2mmLTUBLinePrescale'  : 1 ,
        'Bs2KKLTUBLinePrescale' : 1 ,
        'MuIPChi2_loose'        :  9,
        'MuTrChi2_loose'        : 10,
        'BIPChi2_loose'         : 64,
        'BFDChi2_loose'         : 100,
        'BPVVDChi2'            : 144, 
        'daugt_IPChi2'            : 12.25
        },
    'STREAMS' : ['Dimuon']
        }  

##########################################
## define local stdjets
from Gaudi.Configuration   import *
from CommonParticles.Utils import *

##########################################
## standard jetID
from JetAccessories.JetMaker_Config import JetMakerConf
stdjets_name_noban = "StdJetsNoJetIDNoBan"
StdJetsNoJetIDNoBan = JetMakerConf(stdjets_name_noban,
                                   R = 0.7 ,
                                   PtMin = 500.,
                                   JetIDCut = False).algorithms[0]

## configure Data-On-Demand service                                                        
locations = updateDoD ( StdJetsNoJetIDNoBan )


# the muons banning and B adding is line dependent (need to provide the location of the muons/B!)
def create_stdjets(strob,line_location,stdjets_name_ban, stdjets_name_addb):
    
    myconf1 = JetMakerConf(stdjets_name_ban,
                           R = 0.7 ,
                           PtMin = 500.,
                           listOfParticlesToBan = [line_location],
                           JetIDCut = False).algorithms[0]
    
    if "StdJetsNoJetIDBan" in dir(strob): strob.StdJetsNoJetIDBan.append(myconf1)
    else: strob.StdJetsNoJetIDBan= [myconf1]
                                      
    ## configure Data-On-Demand service                                            
    locations = updateDoD ( myconf1 )

    myconf2 = JetMakerConf(stdjets_name_addb,
                           Inputs = ['Phys/PFParticles/Particles',line_location],
                           R = 0.7,
                           PtMin = 500.,
                           JetIDCut = False).algorithms[0]

    if "StdJetsNoJetIDAddB" in dir(strob):  strob.StdJetsNoJetIDAddB.append(myconf2)
    else:  strob.StdJetsNoJetIDAddB=[myconf2]
        
    ## configure Data-On-Demand service                                            
    locations = updateDoD ( myconf2 )



##########################################

from Gaudi.Configuration import *
from Configurables import FilterDesktop, CombineParticles
from PhysSelPython.Wrappers import Selection, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
#from StrippingSelections.Utils import checkConfig



class Bs2MuMuLinesConf(LineBuilder) :
    """
    Builder of:
     - Bs-> mumu stripping lines: default, loose and lifetime unbiased
     - detached JPsi lines: default, loose and prescaled prompt
    

    Usage:
    >>> config = { .... }
    >>> bsConf = Bs2MuMuLinesConf('PrescaledBs2MuMuTest',config)
    >>> bsLines = bsConf.lines
    >>> for line in line :
    >>>  print line.name(), line.outputLocation()
    The lines can be used directly to build a StrippingStream object.


    Exports as instance data members:
    selDefault     : nominal Bs2mumu stripping line
    selLoose       : loose Bs2MuMu stripping line to understand systematics
    defaultLine    : Stripping line made from selDefault
    looseLine      : Stripping line made from selLoose
    lines          : lsit of lines:  [ defaultLine, looseLine ]
    
    Exports as class data member:
    Bs2MuMuLinesConf.__configuration_keys__ : List of required configuration parameters.
    """

    __configuration_keys__ = ('MuIPChi2_loose',
                              'MuTrChi2_loose',
                              'BIPChi2_loose',
                              'BFDChi2_loose',
                              'DefaultLinePrescale',
                              'DefaultPostscale',
                              'Bs2mmWideLinePrescale',
                              'LooseLinePrescale',
                              'BuPrescale',
                              'BsPrescale',
                              'BdPrescale',
                              'JPsiLinePrescale',
                              'JPsiLooseLinePrescale',
                              'JPsiPromptLinePrescale',
                              'SSPrescale',
                              'Bs2mmLTUBLinePrescale',
                              'Bs2KKLTUBLinePrescale',
                              'BPVVDChi2',
                              'daugt_IPChi2'                             
                              )



    def __init__(self, 
                 name = 'Bs2MuMu',
                 config=default_config):#None ) :

        LineBuilder.__init__(self, name, config)
        #checkConfig(Bs2MuMuLinesConf.__configuration_keys__,config)

        default_name=name+'NoMuID'
        wide_name = name+'WideMass'
        loose_name=name+'NoMuIDLoose'
        bu_name=name+'Bu2JPsiK'
        bs_name=name+'Bs2JPsiPhi'
        bd_name=name+'Bd2JPsiKst'
        ss_name = name+'SS'
        ltub_name = name+'LTUB'
        Bs2KKltub_name = name+'Bs2KKLTUB'

        self.selDefault = makeDefault(default_name,
                                      BPVVDChi2 = config['BPVVDChi2'],
                                      Muon_MIPChi2DV = config['daugt_IPChi2']
                                      )
 

        self.selWide = makeBs2mmWide(wide_name,
                                     BPVVDChi2 = config['BPVVDChi2'],
                                     Muon_MIPChi2DV = config['daugt_IPChi2']
                                     )

        self.selLoose = makeLoose(loose_name,
                                  MuIPChi2=config['MuIPChi2_loose'],
                                  MuTrChi2=config['MuTrChi2_loose'],
                                  BIPChi2=config['BIPChi2_loose'],
                                  BFDChi2=config['BFDChi2_loose']
                                  )
        
        self.selBu = makeBu(bu_name,
                            K_MIPChi2DV = config['daugt_IPChi2'],
                            Jpsi_BPVVDChi2 = config['BPVVDChi2']
                            )

        self.selBs = makeBs(bs_name,
                            Phi_MIPChi2DV = config['daugt_IPChi2'],
                            Jpsi_BPVVDChi2 = config['BPVVDChi2']
                            )

        self.selBd = makeBd(bd_name,
                            Kst_MIPChi2DV = config['daugt_IPChi2'],
                            Jpsi_BPVVDChi2 = config['BPVVDChi2']
                            )

        self.selSS = makeSS(ss_name,                            
                            BPVVDChi2 = config['BPVVDChi2'],
                            Muon_MIPChi2DV = config['daugt_IPChi2']
                            )

        self.selLTUB = makeBs2mmLTUB(ltub_name)

        self.selBs2KKLTUB = makeBs2KKLTUB(Bs2KKltub_name)

        #Jet Information
        stdjets_name_ban_default = "StdJetsNoJetIDBanMuonsDef"
        stdjets_name_addb_default = "StdJetsNoJetIDAddBDef"
 
        stdjets_name_ban_wide = "StdJetsNoJetIDBanMuonsWide"
        stdjets_name_addb_wide = "StdJetsNoJetIDAddBWide"

        stdjets_name_ban_SS = "StdJetsNoJetIDBanMuonsSS"
        stdjets_name_addb_SS = "StdJetsNoJetIDAddBSS"

        stdjets_name_ban_LTUB = "StdJetsNoJetIDBanMuonsLTUB"
        stdjets_name_addb_LTUB = "StdJetsNoJetIDAddBLTUB"

        stdjets_name_ban_KKLTUB = "StdJetsNoJetIDBanMuonsKKLTUB"
        stdjets_name_addb_KKLTUB = "StdJetsNoJetIDAddBKKLTUB"

        
        self.defaultLine = StrippingLine(default_name+"Line",
                                         prescale = config['DefaultLinePrescale'],
                                         postscale = config['DefaultPostscale'],
                                         MDSTFlag = True,
                                         RequiredRawEvents = ["Muon", "Calo"],
                                         algos = [ self.selDefault ],
                                         RelatedInfoTools = [
            { 'Type' : 'RelInfoJetsVariables',
              'Location': 'RelatedInfoJets',
              'Variables': ["JETNOMU1PX","JETNOMU1PY", "JETNOMU1PZ", "JETNOMU1PT", "JETNOMU1JETWIDTH", "JETNOMU1NNTAG", "JETNOMU1MNF", "JETNOMU2PX", "JETNOMU2PY", "JETNOMU2PZ", "JETNOMU2PT", "JETNOMU2JETWIDTH", "JETNOMU2NNTAG", "JETNOMU2MNF", "JETNOMU3PX", "JETNOMU3PY", "JETNOMU3PZ", "JETNOMU3PT", "JETNOMU3JETWIDTH", "JETNOMU3NNTAG", "JETNOMU3MNF", "JETMU1PX", "JETMU1PY", "JETMU1PZ", "JETMU1PT", "JETMU1JETWIDTH", "JETMU1NNTAG", "JETMU1MNF", "JETMU2PX", "JETMU2PY", "JETMU2PZ", "JETMU2PT", "JETMU2JETWIDTH", "JETMU2NNTAG", "JETMU2MNF", "JETBPX", "JETBPY", "JETBPZ", "JETBPT", "JETBJETWIDTH", "JETBNNTAG", "JETBMNF"],
              'LocationJetsNoMu' : "Phys/"+stdjets_name_ban_default+"/Particles",
              'LocationJetsNoRemove' : "Phys/"+stdjets_name_noban+"/Particles",
              'LocationJetsForceB' : "Phys/"+stdjets_name_addb_default+"/Particles"},


            { "Type" : "RelInfoBs2MuMuBIsolations"
              ,"RecursionLevel" : 0
              , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
              , "Location"  : "BSMUMUVARIABLES"},

 
            { "Type" : "RelInfoBs2MuMuTrackIsolations"
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' ,'BSMUMUTRACKID','BSMUMUTRACKTOPID','ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS' ]
                                                                                                                                                               
              ,"Locations" : {
                    'Phys/StdAllNoPIDsMuons' :  ['Muon1iso', 'Muon2iso']
                   }

              },

            { "Type" : "RelInfoBs2MuMuZVisoBDT",
              "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"  
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : { "Phys/StdAllNoPIDsMuons" : ["Muon1TrackIsoBDTInfo_0","Muon2TrackIsoBDTInfo_0"] },
              "WeightsFile" : "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : { "Phys/StdAllNoPIDsMuons" : ["Muon1TrackIsoBDTInfo_1","Muon2TrackIsoBDTInfo_1"] },
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : { "Phys/StdAllNoPIDsMuons" : ["Muon1TrackIsoBDTInfo_2","Muon2TrackIsoBDTInfo_2"] },
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : { "Phys/StdAllNoPIDsMuons" : ["Muon1TrackIsoBDTInfo_3","Muon2TrackIsoBDTInfo_3"] },
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 4,    
              "Locations" : { "Phys/StdAllNoPIDsMuons" : ["Muon1TrackIsoBDTInfo_4","Muon2TrackIsoBDTInfo_4"] },
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              } 
            ]
                                         )

         
         
        self.wideLine = StrippingLine(wide_name+"Line",
                                      prescale = config['Bs2mmWideLinePrescale'],
                                      postscale = config['DefaultPostscale'],
                                      MDSTFlag = True,
                                      RequiredRawEvents = ["Muon", "Calo"],
                                      algos = [ self.selWide ],
                                      RelatedInfoTools = [
            { 'Type' : 'RelInfoJetsVariables',
              'Location': 'RelatedInfoJets',
              'Variables': ["JETNOMU1PX","JETNOMU1PY", "JETNOMU1PZ", "JETNOMU1PT", "JETNOMU1JETWIDTH", "JETNOMU1NNTAG", "JETNOMU1MNF", "JETNOMU2PX", "JETNOMU2PY", "JETNOMU2PZ", "JETNOMU2PT", "JETNOMU2JETWIDTH", "JETNOMU2NNTAG", "JETNOMU2MNF", "JETNOMU3PX", "JETNOMU3PY", "JETNOMU3PZ", "JETNOMU3PT", "JETNOMU3JETWIDTH", "JETNOMU3NNTAG", "JETNOMU3MNF", "JETMU1PX", "JETMU1PY", "JETMU1PZ", "JETMU1PT", "JETMU1JETWIDTH", "JETMU1NNTAG", "JETMU1MNF", "JETMU2PX", "JETMU2PY", "JETMU2PZ", "JETMU2PT", "JETMU2JETWIDTH", "JETMU2NNTAG", "JETMU2MNF", "JETBPX", "JETBPY", "JETBPZ", "JETBPT", "JETBJETWIDTH", "JETBNNTAG", "JETBMNF"],
              'LocationJetsNoMu' : "Phys/"+stdjets_name_ban_wide+"/Particles",
              'LocationJetsNoRemove' : "Phys/"+stdjets_name_noban+"/Particles",
              'LocationJetsForceB' : "Phys/"+stdjets_name_addb_wide+"/Particles"},

            
       { "Type" : "RelInfoBs2MuMuBIsolations"
              ,"RecursionLevel" : 0
              , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
              , "Location"  : "BSMUMUVARIABLES"},

 
            { "Type" : "RelInfoBs2MuMuTrackIsolations"
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' , 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS','BSMUMUTRACKID','BSMUMUTRACKTOPID' ]
                                                                                                                                                               
              ,"Locations" : {
                    'Phys/StdAllLooseMuons' :  ['Muon1iso', 'Muon2iso']
                   }
                           },

            { "Type" : "RelInfoBs2MuMuZVisoBDT",
             "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"  
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : { "Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_0","Muon2TrackIsoBDTInfo_0"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_1","Muon2TrackIsoBDTInfo_1"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_2","Muon2TrackIsoBDTInfo_2"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_3","Muon2TrackIsoBDTInfo_3"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 4,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_4","Muon2TrackIsoBDTInfo_4"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              }
            
            ]
                                      )
        

        self.looseLine = StrippingLine(loose_name+"Line",
                                       prescale = config['LooseLinePrescale'],
                                       postscale = config['DefaultPostscale'],
                                       MDSTFlag = True,
                                       RequiredRawEvents = ["Muon", "Calo"],
                                       algos = [ self.selLoose ],
                                       )



        self.buLine = StrippingLine(bu_name+"Line",
                                    prescale = config['BuPrescale'],
                                    postscale = config['DefaultPostscale'],
                                    MDSTFlag = True,
                                    RequiredRawEvents = ["Muon", "Calo"],
                                    algos = [ self.selBu ],
                                    RelatedInfoTools = [
          
                { "Type" : "RelInfoBs2MuMuBIsolations"
                  ,"TopSelection": self.selBu.requiredSelections()[0]
                  ,"RecursionLevel" : 0
                  , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
                  , "Location"  : "BSMUMUVARIABLES"},
                
                { "Type" : "RelInfoBs2MuMuTrackIsolations"
                  ,"TopSelection": self.selBu.requiredSelections()[0]
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' , 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS','BSMUMUTRACKID','BSMUMUTRACKTOPID' ]
                                                                                                                                                               
              ,"Locations" : {
                    'Phys/StdAllLooseMuons' :  ['Muon1iso', 'Muon2iso']
                   }
        
              },
            
            { "Type" : "RelInfoBs2MuMuZVisoBDT",
              "TopSelection": self.selBu.requiredSelections()[0],
              "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "TopSelection": self.selBu.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : { "Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_0","Muon2TrackIsoBDTInfo_0"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "TopSelection": self.selBu.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_1","Muon2TrackIsoBDTInfo_1"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "TopSelection": self.selBu.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_2","Muon2TrackIsoBDTInfo_2"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "TopSelection": self.selBu.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_3","Muon2TrackIsoBDTInfo_3"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "TopSelection": self.selBu.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 4,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_4","Muon2TrackIsoBDTInfo_4"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              }
                ]


                                    )


     
        self.bsLine = StrippingLine(bs_name+"Line",
                                    prescale = config['BsPrescale'],
                                    postscale = config['DefaultPostscale'],
                                    MDSTFlag = True,
                                    RequiredRawEvents = ["Muon", "Calo"],
                                    algos = [ self.selBs ],
                                 RelatedInfoTools = [
            
                { "Type" : "RelInfoBs2MuMuBIsolations"
                  ,"TopSelection": self.selBs.requiredSelections()[0]
                  ,"RecursionLevel" : 0
                  , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
                  , "Location"  : "BSMUMUVARIABLES"},
                
                { "Type" : "RelInfoBs2MuMuTrackIsolations"
                  ,"TopSelection": self.selBs.requiredSelections()[0]
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' , 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS','BSMUMUTRACKID','BSMUMUTRACKTOPID' ]
                                                                                                                                                               
              ,"Locations" : {
                    'Phys/StdAllLooseMuons' :  ['Muon1iso', 'Muon2iso']
                   }
 
              },
            
            { "Type" : "RelInfoBs2MuMuZVisoBDT",
              "TopSelection": self.selBs.requiredSelections()[0],
              "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"
              },

            { "Type" : "RelInfoTrackIsolationBDT",
              "TopSelection": self.selBs.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : { "Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_0","Muon2TrackIsoBDTInfo_0"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBs.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_1","Muon2TrackIsoBDTInfo_1"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBs.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_2","Muon2TrackIsoBDTInfo_2"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBs.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_3","Muon2TrackIsoBDTInfo_3"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBs.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 4,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_4","Muon2TrackIsoBDTInfo_4"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              }
                
                ]

         

                                    )



        self.bdLine = StrippingLine(bd_name+"Line",
                                    prescale = config['BdPrescale'],
                                    postscale = config['DefaultPostscale'],
                                    MDSTFlag = True,
                                    RequiredRawEvents = ["Muon", "Calo"],
                                    algos = [ self.selBd ], 
                                    RelatedInfoTools = [
  
  
                { "Type" : "RelInfoBs2MuMuBIsolations"
                  ,"TopSelection": self.selBd.requiredSelections()[0]
                  ,"RecursionLevel" : 0
                  , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
                  , "Location"  : "BSMUMUVARIABLES"},
                
                { "Type" : "RelInfoBs2MuMuTrackIsolations"
                  ,"TopSelection": self.selBd.requiredSelections()[0]
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' , 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS','BSMUMUTRACKID','BSMUMUTRACKTOPID' ]
                                                                                                                                                               
              ,"Locations" : {
                    'Phys/StdAllLooseMuons' :  ['Muon1iso', 'Muon2iso']
                   }

              },
            
            { "Type" : "RelInfoBs2MuMuZVisoBDT",
              "TopSelection": self.selBd.requiredSelections()[0],
              "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"
              },

              { "Type" : "RelInfoTrackIsolationBDT",
              "TopSelection": self.selBd.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : { "Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_0","Muon2TrackIsoBDTInfo_0"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBd.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_1","Muon2TrackIsoBDTInfo_1"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBd.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_2","Muon2TrackIsoBDTInfo_2"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBd.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_3","Muon2TrackIsoBDTInfo_3"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
               "TopSelection": self.selBd.requiredSelections()[0],
              "RecursionLevel" : 2,
              "Variables" : 4,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_4","Muon2TrackIsoBDTInfo_4"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              }


                ]
                



                                    )



        self.ssLine = StrippingLine(ss_name+"Line",
                                    prescale = config['SSPrescale'],
                                    postscale = config['DefaultPostscale'],
                                    MDSTFlag = True,
                                    RequiredRawEvents = ["Muon", "Calo"],
                                    algos = [ self.selSS ],
                                    RelatedInfoTools = [
            { 'Type' : 'RelInfoJetsVariables',
              'Location': 'RelatedInfoJets',
              'Variables': ["JETNOMU1PX","JETNOMU1PY", "JETNOMU1PZ", "JETNOMU1PT", "JETNOMU1JETWIDTH", "JETNOMU1NNTAG", "JETNOMU1MNF", "JETNOMU2PX", "JETNOMU2PY", "JETNOMU2PZ", "JETNOMU2PT", "JETNOMU2JETWIDTH", "JETNOMU2NNTAG", "JETNOMU2MNF", "JETNOMU3PX", "JETNOMU3PY", "JETNOMU3PZ", "JETNOMU3PT", "JETNOMU3JETWIDTH", "JETNOMU3NNTAG", "JETNOMU3MNF", "JETMU1PX", "JETMU1PY", "JETMU1PZ", "JETMU1PT", "JETMU1JETWIDTH", "JETMU1NNTAG", "JETMU1MNF", "JETMU2PX", "JETMU2PY", "JETMU2PZ", "JETMU2PT", "JETMU2JETWIDTH", "JETMU2NNTAG", "JETMU2MNF", "JETBPX", "JETBPY", "JETBPZ", "JETBPT", "JETBJETWIDTH", "JETBNNTAG", "JETBMNF"],
              'LocationJetsNoMu' : "Phys/"+stdjets_name_ban_SS+"/Particles",
              'LocationJetsNoRemove' : "Phys/"+stdjets_name_noban+"/Particles",
              'LocationJetsForceB' : "Phys/"+stdjets_name_addb_SS+"/Particles"},

            { "Type" : "RelInfoBs2MuMuBIsolations"
              ,"RecursionLevel" : 0
              , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
              , "Location"  : "BSMUMUVARIABLES"},

 
            { "Type" : "RelInfoBs2MuMuTrackIsolations"
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' , 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS','BSMUMUTRACKID','BSMUMUTRACKTOPID' ]
                      ,"Locations" : {'Phys/StdAllLooseMuons' :['Muon1iso', 'Muon2iso'] }
              },
            { "Type" : "RelInfoBs2MuMuZVisoBDT",
             "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"  
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_0","Muon2TrackIsoBDTInfo_0"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_1","Muon2TrackIsoBDTInfo_1"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_2","Muon2TrackIsoBDTInfo_2"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_3","Muon2TrackIsoBDTInfo_3"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 4,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_4","Muon2TrackIsoBDTInfo_4"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              }
            ]
                                    )



       
        self.ltubLine = StrippingLine(ltub_name+"Line",
                                    prescale = config['Bs2mmLTUBLinePrescale'],
                                    postscale = config['DefaultPostscale'],
                                    MDSTFlag = True,
                                    RequiredRawEvents = ["Muon", "Calo"],
                                    algos = [ self.selLTUB ],
                                    RelatedInfoTools = [
            { 'Type' : 'RelInfoJetsVariables',
              'Location': 'RelatedInfoJets',
              'Variables': ["JETNOMU1PX","JETNOMU1PY", "JETNOMU1PZ", "JETNOMU1PT", "JETNOMU1JETWIDTH", "JETNOMU1NNTAG", "JETNOMU1MNF", "JETNOMU2PX", "JETNOMU2PY", "JETNOMU2PZ", "JETNOMU2PT", "JETNOMU2JETWIDTH", "JETNOMU2NNTAG", "JETNOMU2MNF", "JETNOMU3PX", "JETNOMU3PY", "JETNOMU3PZ", "JETNOMU3PT", "JETNOMU3JETWIDTH", "JETNOMU3NNTAG", "JETNOMU3MNF", "JETMU1PX", "JETMU1PY", "JETMU1PZ", "JETMU1PT", "JETMU1JETWIDTH", "JETMU1NNTAG", "JETMU1MNF", "JETMU2PX", "JETMU2PY", "JETMU2PZ", "JETMU2PT", "JETMU2JETWIDTH", "JETMU2NNTAG", "JETMU2MNF", "JETBPX", "JETBPY", "JETBPZ", "JETBPT", "JETBJETWIDTH", "JETBNNTAG", "JETBMNF"],
              'LocationJetsNoMu' : "Phys/"+stdjets_name_ban_LTUB+"/Particles",
              'LocationJetsNoRemove' : "Phys/"+stdjets_name_noban+"/Particles",
              'LocationJetsForceB' : "Phys/"+stdjets_name_addb_LTUB+"/Particles"},
            { "Type" : "RelInfoBs2MuMuBIsolations"
              ,"RecursionLevel" : 0
              , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
              , "Location"  : "BSMUMUVARIABLES"},

 
            { "Type" : "RelInfoBs2MuMuTrackIsolations"
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' , 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS','BSMUMUTRACKID','BSMUMUTRACKTOPID' ]
                                                                                                                                                               
              ,"Locations" : {
                    'Phys/StdAllLooseMuons' : ['Muon1iso', 'Muon2iso']
                   }
   
              },
            { "Type" : "RelInfoBs2MuMuZVisoBDT",
             "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"  
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_0","Muon2TrackIsoBDTInfo_0"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_1","Muon2TrackIsoBDTInfo_1"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_2","Muon2TrackIsoBDTInfo_2"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_3","Muon2TrackIsoBDTInfo_3"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 4,
              "Locations" : {"Phys/StdAllLooseMuons" : ["Muon1TrackIsoBDTInfo_4","Muon2TrackIsoBDTInfo_4"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              }
            ]
                                    )

        self.Bs2KKltubLine = StrippingLine(Bs2KKltub_name+"Line",
                                    prescale = config['Bs2KKLTUBLinePrescale'],
                                    postscale = config['DefaultPostscale'],
                                    MDSTFlag = True,
                                    RequiredRawEvents = ["Muon", "Calo"],
                                    algos = [ self.selBs2KKLTUB ],
                                    RelatedInfoTools = [
            { 'Type' : 'RelInfoJetsVariables',
              'Location': 'RelatedInfoJets',
              'Variables': ["JETNOMU1PX","JETNOMU1PY", "JETNOMU1PZ", "JETNOMU1PT", "JETNOMU1JETWIDTH", "JETNOMU1NNTAG", "JETNOMU1MNF", "JETNOMU2PX", "JETNOMU2PY", "JETNOMU2PZ", "JETNOMU2PT", "JETNOMU2JETWIDTH", "JETNOMU2NNTAG", "JETNOMU2MNF", "JETNOMU3PX", "JETNOMU3PY", "JETNOMU3PZ", "JETNOMU3PT", "JETNOMU3JETWIDTH", "JETNOMU3NNTAG", "JETNOMU3MNF", "JETMU1PX", "JETMU1PY", "JETMU1PZ", "JETMU1PT", "JETMU1JETWIDTH", "JETMU1NNTAG", "JETMU1MNF", "JETMU2PX", "JETMU2PY", "JETMU2PZ", "JETMU2PT", "JETMU2JETWIDTH", "JETMU2NNTAG", "JETMU2MNF", "JETBPX", "JETBPY", "JETBPZ", "JETBPT", "JETBJETWIDTH", "JETBNNTAG", "JETBMNF"],
              'LocationJetsNoMu' : "Phys/"+stdjets_name_ban_KKLTUB+"/Particles",
              'LocationJetsNoRemove' : "Phys/"+stdjets_name_noban+"/Particles",
              'LocationJetsForceB' : "Phys/"+stdjets_name_addb_KKLTUB+"/Particles"},
            { "Type" : "RelInfoBs2MuMuBIsolations"
              ,"RecursionLevel" : 0
              , "Variables" : ['BSMUMUCDFISO', 'BSMUMUOTHERBMAG', 'BSMUMUOTHERBANGLE', 'BSMUMUOTHERBBOOSTMAG', 'BSMUMUOTHERBBOOSTANGLE', 'BSMUMUOTHERBTRACKS', 'BSMUMUPARTID','BSMUMUTOPID']
              , "Location"  : "BSMUMUVARIABLES"},
            { "Type" : "RelInfoBs2MuMuTrackIsolations"
                      ,"RecursionLevel" : 1
                      , "Variables" : [  'BSMUMUTRACKPLUSISO', 'BSMUMUTRACKPLUSISOTWO' , 'ISOTWOBODYQPLUS', 'ISOTWOBODYMASSISOPLUS', 'ISOTWOBODYCHI2ISOPLUS', 'ISOTWOBODYISO5PLUS','BSMUMUTRACKID','BSMUMUTRACKTOPID' ]
                      ,"Locations" : { 'Phys/StdAllLooseKaons' :  ['Kaon1iso', 'Kaon2iso'] }
          
              },
            { "Type" : "RelInfoBs2MuMuZVisoBDT",
               "RecursionLevel" : 0,
              "Variables" : ['ZVISO'],
              "Location"  : "RelInfoZVisoBDT"  
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 0,
              "Locations" : {"Phys/StdAllLooseKaons" : ["Kaon1TrackIsoBDTInfo_0","Kaon2TrackIsoBDTInfo_0"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsA_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 1,
              "Locations" : {"Phys/StdAllLooseKaons" : ["Kaon1TrackIsoBDTInfo_1","Kaon2TrackIsoBDTInfo_1"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT6varsB_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 2,
              "Locations" : {"Phys/StdAllLooseKaons" : ["Kaon1TrackIsoBDTInfo_2","Kaon2TrackIsoBDTInfo_2"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT9vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 3,
              "Locations" : {"Phys/StdAllLooseKaons" : ["Kaon1TrackIsoBDTInfo_3","Kaon2TrackIsoBDTInfo_3"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT13vars_v1r4.xml"
              },
            { "Type" : "RelInfoTrackIsolationBDT",
              "RecursionLevel" : 2,
              "Variables" : 4,
              "Locations" : {"Phys/StdAllLooseKaons" : ["Kaon1TrackIsoBDTInfo_4","Kaon2TrackIsoBDTInfo_4"]},
              "WeightsFile"  :  "BsMuMu_TrackIsolationBDT15vars_v1r4.xml"
              }
           ]
                                 )


        create_stdjets(self,self.defaultLine.outputLocation(),stdjets_name_ban_default, stdjets_name_addb_default)
        create_stdjets(self,self.wideLine.outputLocation(),stdjets_name_ban_wide, stdjets_name_addb_wide)
        create_stdjets(self,self.ssLine.outputLocation(),stdjets_name_ban_SS, stdjets_name_addb_SS)

        create_stdjets(self,self.ltubLine.outputLocation(),stdjets_name_ban_LTUB, stdjets_name_addb_LTUB)
        create_stdjets(self,self.Bs2KKltubLine.outputLocation(),stdjets_name_ban_KKLTUB, stdjets_name_addb_KKLTUB)

        
        self.registerLine(self.defaultLine)
        self.registerLine(self.wideLine)
        self.registerLine(self.looseLine)
        self.registerLine(self.buLine)
        self.registerLine(self.bsLine)
        self.registerLine(self.bdLine)
        self.registerLine(self.ssLine)
        self.registerLine(self.ltubLine)
        self.registerLine(self.Bs2KKltubLine)

def makeDefault(name, BPVVDChi2, Muon_MIPChi2DV) :
    """
    default Bs2mumu selection object (tighter selection a la roadmap)
    starts from Phys/StdNoPIDsMuons

    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    Bs2MuMuNoMuID = CombineParticles("Comine"+name)
    Bs2MuMuNoMuID.DecayDescriptor = "B_s0 -> mu+ mu-"
    # Set the OfflineVertexFitter to keep the 4 tracks and not the J/Psi Kstar:
    Bs2MuMuNoMuID.addTool( OfflineVertexFitter )
    Bs2MuMuNoMuID.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    Bs2MuMuNoMuID.OfflineVertexFitter.useResonanceVertex = False
    Bs2MuMuNoMuID.ReFitPVs = True
    Bs2MuMuNoMuID.DaughtersCuts = { "mu+" : "(MIPCHI2DV(PRIMARY)> %(Muon_MIPChi2DV)s )&(TRCHI2DOF < 3 )"\
                                    " & (0.5<PPINFO(LHCb.ProtoParticle.InAccMuon,-1))"\
                                    " & (PT < 40*GeV)"\
                                    " & (P < 500*GeV)"\
                                    " & ( TRGHOSTPROB < 0.3 )"% locals() }
    
    Bs2MuMuNoMuID.CombinationCut = "(ADAMASS('B_s0')<500*MeV)"\
                                   "& (AMAXDOCA('')<0.3*mm)"

    Bs2MuMuNoMuID.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                              "& (ADMASS('B_s0') < 500*MeV )"\
                              "& (BPVDIRA > 0) "\
                              "& (BPVVDCHI2> %(BPVVDChi2)s)"\
                              "& (BPVIPCHI2()< 25) "\
                              "& (BPVLTIME()<13.248*ps)"\
                              "& (PT > 350*MeV)"% locals()
                             
    _stdNoPIDsMuons = DataOnDemand(Location = "Phys/StdNoPIDsMuons/Particles")

    return Selection (name,
                      Algorithm = Bs2MuMuNoMuID,
                      RequiredSelections = [ _stdNoPIDsMuons])


def makeBs2mmWide(name, BPVVDChi2, Muon_MIPChi2DV) :
    """
    Bs2mumu selection object (tighter selection a la roadmap)
    with muon Id and wide mass window (1.2GeV)
    starts from Phys/StdLooseMuons

    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    Bs2MuMuWideMass = CombineParticles("Combine"+name)
    Bs2MuMuWideMass.DecayDescriptor = "B_s0 -> mu+ mu-"
    Bs2MuMuWideMass.addTool( OfflineVertexFitter )
    Bs2MuMuWideMass.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    Bs2MuMuWideMass.OfflineVertexFitter.useResonanceVertex = False
    Bs2MuMuWideMass.ReFitPVs = True
    Bs2MuMuWideMass.DaughtersCuts = { "mu+" : "(MIPCHI2DV(PRIMARY)> %(Muon_MIPChi2DV)s)&(TRCHI2DOF < 3 )" % locals()}
    Bs2MuMuWideMass.CombinationCut = "(ADAMASS('B_s0')<1200*MeV)"\
                                     "& (AMAXDOCA('')<0.3*mm)"

    Bs2MuMuWideMass.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                                "& (ADMASS('B_s0') < 1200*MeV )"\
                                "& (BPVDIRA > 0) "\
                                "& (BPVVDCHI2> %(BPVVDChi2)s)"\
                                "& (BPVIPCHI2()< 25) "% locals()
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

    return Selection (name,
                      Algorithm = Bs2MuMuWideMass,
                      RequiredSelections = [ _stdLooseMuons])


def makeSS(name, BPVVDChi2, Muon_MIPChi2DV) :
    """
    Bs2mumu selection object (tighter selection a la roadmap)
    with muon Id and same sign muons 
    starts from Phys/StdLooseMuons

    Please contact Johannes Albrecht if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    Bs2MuMuSS = CombineParticles("Combine"+name)
    Bs2MuMuSS.DecayDescriptor = "[B_s0 -> mu+ mu+]cc"
    Bs2MuMuSS.addTool( OfflineVertexFitter )
    Bs2MuMuSS.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    Bs2MuMuSS.OfflineVertexFitter.useResonanceVertex = False
    Bs2MuMuSS.ReFitPVs = True
    Bs2MuMuSS.DaughtersCuts = { "mu+" : "(MIPCHI2DV(PRIMARY)> %(Muon_MIPChi2DV)s )&(TRCHI2DOF < 3 )" % locals()}
    Bs2MuMuSS.CombinationCut = "(ADAMASS('B_s0')<200*MeV)"\
                                     "& (AMAXDOCA('')<0.3*mm)"

    Bs2MuMuSS.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                                "& (ADMASS('B_s0') < 200*MeV )"\
                                "& (BPVDIRA > 0) "\
                                "& (BPVVDCHI2>  %(BPVVDChi2)s)"\
                                "& (BPVIPCHI2()< 25) "% locals()
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

    return Selection (name,
                      Algorithm = Bs2MuMuSS,
                      RequiredSelections = [ _stdLooseMuons])


def makeLoose(name, MuIPChi2, MuTrChi2, BIPChi2, BFDChi2 ) :
    """      
    loose Bs2mumu selection object to monitor selection,
    systematics from cuts, etc.
    starts from Phys/StdNoPIDsMuons

    prescaled

    Arguments:
    name        : name of the Selection.
    MuIPChi2    : muon MIPCHI2DV(PRIMARY)
    MuTrChi2    : muon TRCHI2
    BIPChi2     : Bs MIPCHI2DV(PRIMARY)
    BFDChi2     : Bs BPVVDCHI2> %(BFDChi2)
    """
    from Configurables import OfflineVertexFitter
    Bs2MuMuNoMuIDLoose = CombineParticles("Combine"+name)
    Bs2MuMuNoMuIDLoose.DecayDescriptor = "B_s0 -> mu+ mu-"

    Bs2MuMuNoMuIDLoose.addTool( OfflineVertexFitter )
    Bs2MuMuNoMuIDLoose.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    Bs2MuMuNoMuIDLoose.OfflineVertexFitter.useResonanceVertex = False
    Bs2MuMuNoMuIDLoose.ReFitPVs = True
    Bs2MuMuNoMuIDLoose.DaughtersCuts = { "mu+" : "(TRCHI2DOF < %(MuTrChi2)s ) "\
                                         "& (MIPCHI2DV(PRIMARY)> %(MuIPChi2)s ) "% locals() }
  
    Bs2MuMuNoMuIDLoose.CombinationCut = "(ADAMASS('B_s0')<600*MeV)"\
                                        "& (AMAXDOCA('')<0.5*mm)"

    Bs2MuMuNoMuIDLoose.MotherCut = "(VFASPF(VCHI2/VDOF)<25) "\
                                   "& (ADMASS('B_s0') < 600*MeV )"\
                                   "& (BPVDIRA > 0) "\
                                   "& (BPVVDCHI2> %(BFDChi2)s)"\
                                   "& (BPVIPCHI2()< %(BIPChi2)s) "% locals()

    _stdNoPIDsMuons = DataOnDemand(Location = "Phys/StdNoPIDsMuons/Particles")

    return Selection (name,
                      Algorithm = Bs2MuMuNoMuIDLoose,
                      RequiredSelections = [ _stdNoPIDsMuons])
    
    


def makeBu(name, K_MIPChi2DV,  Jpsi_BPVVDChi2) :
    """
    detached Bu-->JPsiK selection. Selection is aligned to the Bs2MuMu
    selection.

    Please contact Johannes Albrecht if you think of prescaling this line!

    Arguments:
    name        : name of the Selection.
    """

    
    from Configurables import OfflineVertexFitter
   
    SelDJPsi = makeDetachedJPsi(name+"SelJpsi",  Jpsi_BPVVDChi2)

    PreselBu2JPsiKCommon = CombineParticles("PreselBu2JPsiKCommon")
    PreselBu2JPsiKCommon.DecayDescriptor =  " [B+ -> J/psi(1S) K+]cc ";
    PreselBu2JPsiKCommon.addTool( OfflineVertexFitter )
    PreselBu2JPsiKCommon.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    PreselBu2JPsiKCommon.OfflineVertexFitter.useResonanceVertex = False
    PreselBu2JPsiKCommon.ReFitPVs = True
    PreselBu2JPsiKCommon.DaughtersCuts = { "K+" : "(ISLONG) & (TRCHI2DOF < 3 ) &(MIPCHI2DV(PRIMARY)>%(K_MIPChi2DV)s)& (PT>250*MeV) "% locals()}
    PreselBu2JPsiKCommon.CombinationCut = "(ADAMASS('B+') < 500*MeV)"
    PreselBu2JPsiKCommon.MotherCut = "(BPVIPCHI2()< 25)& (VFASPF(VCHI2)<45) "

    _kaons = DataOnDemand(Location='Phys/StdNoPIDsKaons/Particles')

    return Selection( name,
                         Algorithm = PreselBu2JPsiKCommon,
                         RequiredSelections=[SelDJPsi,_kaons] )


def makeBs(name, Phi_MIPChi2DV,  Jpsi_BPVVDChi2) :
    """
    detached Bs-->JPsiPhi selection. Selection is aligned to the Bs2MuMu
    selection.

    Please contact Johannes Albrecht if you think of prescaling this line!

    Arguments:
    name        : name of the Selection.
    """

    
    from Configurables import OfflineVertexFitter
   
    SelDJPsi = makeDetachedJPsi(name+"SelJpsi",  Jpsi_BPVVDChi2)

    makePhi = CombineParticles("makePhi")
    makePhi.DecayDescriptor =  "phi(1020) -> K+ K-"
    makePhi.DaughtersCuts = {"K+": "(ISLONG) & (TRCHI2DOF < 3 ) & (MIPCHI2DV(PRIMARY)> 4.) & (PT>250*MeV)"}
    
    _kaons = DataOnDemand(Location='Phys/StdNoPIDsKaons/Particles')

    makePhi.CombinationCut =  "(ADAMASS('phi(1020)')<20*MeV)"
    makePhi.MotherCut = " (MIPCHI2DV(PRIMARY)> %(Phi_MIPChi2DV)s)"% locals()
    SelPhi = Selection( name+"SelPhi",                       Algorithm= makePhi,
                        RequiredSelections=[_kaons] )

    PreselBs2JPsiPhiCommon = CombineParticles("PreselBs2JPsiPhiCommon")
    PreselBs2JPsiPhiCommon.DecayDescriptor = "B_s0 -> J/psi(1S) phi(1020)"
    PreselBs2JPsiPhiCommon.addTool( OfflineVertexFitter )
    PreselBs2JPsiPhiCommon.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    PreselBs2JPsiPhiCommon.OfflineVertexFitter.useResonanceVertex = False
    PreselBs2JPsiPhiCommon.ReFitPVs = True
    PreselBs2JPsiPhiCommon.DaughtersCuts = {}
    PreselBs2JPsiPhiCommon.CombinationCut = "(ADAMASS('B_s0') < 500*MeV)"
    PreselBs2JPsiPhiCommon.MotherCut = "(BPVIPCHI2()< 25)& (VFASPF(VCHI2)<75)"
    
    return  Selection( name,
                       Algorithm = PreselBs2JPsiPhiCommon,
                       RequiredSelections=[SelDJPsi,SelPhi] )



def makeBd(name, Kst_MIPChi2DV,  Jpsi_BPVVDChi2) :
    """
    detached Bd-->JPsiK* selection. Selection is aligned to the Bs2MuMu
    selection.

    Please contact Johannes Albrecht if you think of prescaling this line!

    Arguments:
    name        : name of the Selection.
    """

    
    from Configurables import OfflineVertexFitter
   
    SelDJPsi = makeDetachedJPsi(name+"SelJpsi",  Jpsi_BPVVDChi2)


    ## make Kstar

    makeKstar = CombineParticles("makeKstar")

    makeKstar.DecayDescriptor =  "[K*(892)0 -> K+ pi-]cc"
    makeKstar.DaughtersCuts = {"K+": "(ISLONG) & (TRCHI2DOF < 3 ) "\
                               " & ( TRGHOSTPROB < 0.3 )"\
                               " & (MIPCHI2DV(PRIMARY)> 4.)& (PT>250*MeV)",
                               "pi-":"(ISLONG) & (TRCHI2DOF < 3 ) "\
                               " & ( TRGHOSTPROB < 0.3 )"\
                               "& (MIPCHI2DV(PRIMARY)> 4.)& (PT>250*MeV)"}
    makeKstar.CombinationCut =  "(ADAMASS('K*(892)0')<2000*MeV)"#huge, to allow to study JPsi K1 etc
    makeKstar.MotherCut = " (MIPCHI2DV(PRIMARY)> %(Kst_MIPChi2DV)s)"% locals()

    _pions = DataOnDemand(Location='Phys/StdNoPIDsPions/Particles')
    _kaons = DataOnDemand(Location='Phys/StdNoPIDsKaons/Particles')

    SelKst = Selection( name+"SelKst",
                        Algorithm= makeKstar,
                        RequiredSelections=[_pions,_kaons] )
    

    ## make BtoJPsiKstar
    PreselBd2JPsiKstCommon = CombineParticles("PreselBd2JPsiKstCommon")
    PreselBd2JPsiKstCommon.DecayDescriptor = "[B0 -> J/psi(1S) K*(892)0]cc"
    PreselBd2JPsiKstCommon.addTool( OfflineVertexFitter )
    PreselBd2JPsiKstCommon.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    PreselBd2JPsiKstCommon.OfflineVertexFitter.useResonanceVertex = False
    PreselBd2JPsiKstCommon.ReFitPVs = True
    PreselBd2JPsiKstCommon.DaughtersCuts = {}
    PreselBd2JPsiKstCommon.CombinationCut = "(ADAMASS('B0') < 500*MeV)"
    PreselBd2JPsiKstCommon.MotherCut = "(BPVIPCHI2()< 25) & (VFASPF(VCHI2)<75)"

    return Selection( name,
                      Algorithm = PreselBd2JPsiKstCommon,
                      RequiredSelections=[SelDJPsi,SelKst] )




def makeDetachedJPsi(name, Jpsi_BPVVDChi2) :
    """
    detached JPsi selection for B--> JPsi X calibration and
    normalization channels. Selection is aligned to the Bs2MuMu
    selection.

    Please contact Johannes Albrecht if you think of prescaling this line!

    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    DetachedJPsi = CombineParticles("Combine"+name)
    DetachedJPsi.DecayDescriptor = "J/psi(1S) -> mu+ mu-"
    # Set the OfflineVertexFitter to keep the 4 tracks and not the J/Psi Kstar:
    DetachedJPsi.addTool( OfflineVertexFitter )
    DetachedJPsi.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    DetachedJPsi.OfflineVertexFitter.useResonanceVertex = False
    DetachedJPsi.ReFitPVs = True
    DetachedJPsi.DaughtersCuts = { "mu+" : "(TRCHI2DOF < 3 ) "\
                                    "& (MIPCHI2DV(PRIMARY)> 25.)"}
                                 
    DetachedJPsi.CombinationCut = "(ADAMASS('J/psi(1S)')<100*MeV) "\
                                   "& (AMAXDOCA('')<0.3*mm)"

    DetachedJPsi.MotherCut = "(VFASPF(VCHI2)<9) "\
                             "& (ADMASS('J/psi(1S)') < 100*MeV )"\
                             "& (BPVDIRA > 0) "\
                             "& (BPVVDCHI2> %(Jpsi_BPVVDChi2)s)"% locals()

    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

    return Selection (name,
                      Algorithm = DetachedJPsi,
                      RequiredSelections = [ _stdLooseMuons ])

def makeBs2mmLTUB(name) :
    """
    Lifetime unbiased Bs2mumu selection object
    starts from Phys/StdAllLooseMuons

    Please contact Harry Cliff if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    Bs2MuMuLTUB = CombineParticles("Comine"+name)
    Bs2MuMuLTUB.DecayDescriptor = "B_s0 -> mu+ mu-"
    Bs2MuMuLTUB.addTool( OfflineVertexFitter )
    Bs2MuMuLTUB.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    Bs2MuMuLTUB.OfflineVertexFitter.useResonanceVertex = False
    Bs2MuMuLTUB.ReFitPVs = True
    Bs2MuMuLTUB.DaughtersCuts = { "mu+" : "(PT > 500*MeV) & (TRCHI2DOF < 3 )"\
                                    " & (0.5<PPINFO(LHCb.ProtoParticle.InAccMuon,-1))"\
                                    " & (PT < 40*GeV)"\
                                    " & (P < 500*GeV)"\
                                    " & ( TRGHOSTPROB < 0.3 )" }
    
    Bs2MuMuLTUB.CombinationCut = "(ADAMASS('B_s0')<500*MeV)"\
                                   "& (AMAXDOCA('')<0.3*mm)"

    Bs2MuMuLTUB.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                              "& (ADMASS('B_s0') < 500*MeV )"\
                              "& (BPVIPCHI2()< 25) "\
                              "& (BPVLTIME()>0.6*ps)"\
                              "& (BPVLTIME()<13.248*ps)"\
                              "& (PT > 500*MeV)"
                             
    _stdAllLooseMuons = DataOnDemand(Location = "Phys/StdAllLooseMuons/Particles")

    return Selection (name,
                      Algorithm = Bs2MuMuLTUB,
                      RequiredSelections = [ _stdAllLooseMuons])

def makeBs2KKLTUB(name) :
    """
    Lifetime unbiased Bs2KK selection object
    starts from Phys/StdAllLooseKaons

    Please contact Harry Cliff if you think of prescaling this line!
    
    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    Bs2KKLTUB = CombineParticles("Comine"+name)
    Bs2KKLTUB.DecayDescriptor = "B_s0 -> K+ K-"
    Bs2KKLTUB.addTool( OfflineVertexFitter )
    Bs2KKLTUB.ParticleCombiners.update( { "" : "OfflineVertexFitter"} )
    Bs2KKLTUB.OfflineVertexFitter.useResonanceVertex = False
    Bs2KKLTUB.ReFitPVs = True
    Bs2KKLTUB.DaughtersCuts = { "K+" : "(PT > 500*MeV) & (TRCHI2DOF < 3 )"\
                                    " & (0.5<PPINFO(LHCb.ProtoParticle.InAccMuon,-1))"\
                                    " & (PT < 40*GeV)"\
                                    " & (P < 500*GeV)"\
                                    " & (TRGHOSTPROB < 0.3 )"\
                                    " & (PIDK > 5) "}
    
    Bs2KKLTUB.CombinationCut = "(ADAMASS('B_s0')<500*MeV)"\
                                   "& (AMAXDOCA('')<0.3*mm)"

    Bs2KKLTUB.MotherCut = "(VFASPF(VCHI2/VDOF)<9) "\
                              "& (ADMASS('B_s0') < 500*MeV )"\
                              "& (BPVIPCHI2()< 25) "\
                              "& (BPVLTIME()>0.6*ps)"\
                              "& (BPVLTIME()<13.248*ps)"\
                              "& (PT > 500*MeV)"
                             
    _stdAllLooseKaons = DataOnDemand(Location = "Phys/StdAllLooseKaons/Particles")

    return Selection (name,
                      Algorithm = Bs2KKLTUB,
                      RequiredSelections = [ _stdAllLooseKaons])

'''
def makeDetachedJPsiLoose(name) :
    """
    loose detached JPsi selection to monitor selection,
    systematics from cuts, etc.
    
    prescaled
    
    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    DetachedJPsiLoose = CombineParticles("Combine"+name)
    DetachedJPsiLoose.DecayDescriptor = "J/psi(1S) -> mu+ mu-"
    # Set the OfflineVertexFitter to keep the 4 tracks and not the J/Psi Kstar:
    DetachedJPsiLoose.addTool( OfflineVertexFitter )
    DetachedJPsiLoose.VertexFitters.update( { "" : "OfflineVertexFitter"} )
    DetachedJPsiLoose.OfflineVertexFitter.useResonanceVertex = False
    DetachedJPsiLoose.ReFitPVs = True
    DetachedJPsiLoose.DaughtersCuts = { "mu+" : "(TRCHI2DOF < 10 ) "\
                                    "& (MIPCHI2DV(PRIMARY)> 9.)"}
                                 
    DetachedJPsiLoose.CombinationCut = "(ADAMASS('J/psi(1S)')<120*MeV) "\
                                   "& (AMAXDOCA('')<0.5*mm)"

    DetachedJPsiLoose.MotherCut = "(VFASPF(VCHI2)<25) "\
                                  "& (ADMASS('J/psi(1S)') < 120*MeV )"\
                                  "& (BPVDIRA > 0) "\
                                  "& (BPVVDCHI2>100)"

    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

    return Selection (name,
                      Algorithm = DetachedJPsiLoose,
                      RequiredSelections = [ _stdLooseMuons ])


def makePromptJPsi(name) :
    """
    Prompt variant of the detached JPsi selection for
    B--> JPsi X calibration and normalization channels.
    Selection is aligned to the Bs2MuMu selection.
    heavily prescaled
    
    Arguments:
    name        : name of the Selection.
    """
    from Configurables import OfflineVertexFitter
    PromptJPsi = CombineParticles("Combine"+name)
    PromptJPsi.DecayDescriptor = "J/psi(1S) -> mu+ mu-"
    # Set the OfflineVertexFitter to keep the 4 tracks and not the J/Psi Kstar:
    PromptJPsi.addTool( OfflineVertexFitter )
    PromptJPsi.VertexFitters.update( { "" : "OfflineVertexFitter"} )
    PromptJPsi.OfflineVertexFitter.useResonanceVertex = False
    PromptJPsi.ReFitPVs = True
    PromptJPsi.DaughtersCuts = { "mu+" : "(TRCHI2DOF < 4 ) "}
    
    PromptJPsi.CombinationCut = "(ADAMASS('J/psi(1S)')<100*MeV) "\
                                "& (AMAXDOCA('')<0.3*mm)"
    
    PromptJPsi.MotherCut = "(VFASPF(VCHI2)<15) "\
                           "& (ADMASS('J/psi(1S)') < 100*MeV )"
    
    _stdLooseMuons = DataOnDemand(Location = "Phys/StdLooseMuons/Particles")

    return Selection (name,
                      Algorithm = PromptJPsi,
                      RequiredSelections = [ _stdLooseMuons ])
'''

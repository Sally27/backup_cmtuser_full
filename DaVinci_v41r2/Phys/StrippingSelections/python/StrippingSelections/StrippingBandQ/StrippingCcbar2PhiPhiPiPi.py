'''
Module for selecting charmonium -> phi phi pi pi 
'''

__author__=['Andrii Usachov']
__date__ = '16/04/2015'
__version__= '$Revision: 1.0 $'



__all__ = (
    'Ccbar2PhiPhiPiPiConf',
    'default_config'
    )

default_config = {
    'NAME'              :  'Ccbar2PhiPhiPiPi',
    'BUILDERTYPE'       :  'Ccbar2PhiPhiPiPiConf',
    'CONFIG'    : {
        'HLTCuts'       : "(HLT_PASS_RE('Hlt2Topo.*Decision'))",
        'PionCuts'      : "(PROBNNpi > 0.2) & (PT > 500*MeV) & (TRGHOSTPROB<0.4)",
        'Phi_TisTosSpecs'  : { "Hlt1Global%TIS" : 0 },
        'EtacComN4Cuts' : """
                          (AM > 2.7 *GeV)
                          """,
#        'EtacMomN4Cuts' : "(VFASPF(VCHI2/VDOF) < 9.) & (in_range(2.8*GeV, MM, 4.2*GeV))",  
        'EtacMomN4Cuts' : "(VFASPF(VCHI2/VDOF) < 9.) & (MM>2.8*GeV)",
        'Prescale'      : 1.,     
        'TRCHI2DOF'        :     5.,
        'KaonPIDK'         :     5.,
        'PhiMassW'         :    12.,
        'PhiVtxChi2'       :    16.,
        'KaonPT'           :   650
        },
    'STREAMS'           : ['Charm' ],
    'WGs'               : ['BandQ'],
    }



from Gaudi.Configuration import *
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles 
from PhysSelPython.Wrappers import Selection, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder
from GaudiConfUtils.ConfigurableGenerators import DaVinci__N4BodyDecays

class Ccbar2PhiPhiPiPiConf(LineBuilder):
    
    __configuration_keys__ = (
        'HLTCuts',
        'PionCuts',
        'Phi_TisTosSpecs',
        #'EtacComAMCuts',
        'EtacComN4Cuts',
        'EtacMomN4Cuts',        
        'Prescale',
        'TRCHI2DOF',
        'KaonPIDK',
        'PhiMassW',
        'PhiVtxChi2',
        'KaonPT'
        )

    
    def __init__(self, name, config ): 
        
        LineBuilder.__init__(self, name, config)
        self.name = name 
        self.config = config



        PhiVtxChi2=config['PhiVtxChi2']
        PhiMassW  =config['PhiMassW']
        KaonPT    =config['KaonPT']
        TRCHI2DOF =config['TRCHI2DOF']
        KaonPIDK  =config['KaonPIDK']





        self.SelPions = self.createSubSel( OutputList = self.name + "SelPions",
                                           InputList =  DataOnDemand(Location = 'Phys/StdLoosePions/Particles' ), 
                                           Cuts = config['PionCuts']
                                           )


        self.PhiForJpsiList = self.createSubSel( OutputList = "PhiFor" + self.name,
                                                 InputList =  DataOnDemand( Location = 'Phys/StdTightPhi2KK/Particles' ), 
                                                 Cuts = "(VFASPF(VCHI2/VDOF)<%(PhiVtxChi2)s)"\
                                                         " & (ADMASS('phi(1020)')<%(PhiMassW)s*MeV )"\
                                                         " & (MAXTREE('K+'==ABSID, TRCHI2DOF) < %(TRCHI2DOF)s )" \
                                                         " & (MINTREE('K+'==ABSID, PIDK)>0)" % self.config)


        self.TisPhiForJpsiList = self.filterTisTos( "TisPhiFor" + self.name ,
                                                    PhiInput = self.PhiForJpsiList,
                                                    myTisTosSpecs = config['Phi_TisTosSpecs']
                                                    )    


        """
        J/psi -> Phi Phi Pi Pi
        """
        self.SelCcbar2PhiPhiPiPi = self.createN4BodySel( OutputList = self.name + "SelCcbar2PhiPhiPiPi",
                                                     DaughterLists = [ self.TisPhiForJpsiList, self.SelPions ],
                                                     DecayDescriptor = "J/psi(1S) -> phi(1020) phi(1020) pi+ pi-",
                                                     #ComAMCuts      = config['EtacComAMCuts'],
                                                     PreVertexCuts  = config['EtacComN4Cuts'], 
                                                     PostVertexCuts = config['EtacMomN4Cuts']
                                                     )
        
        self.Ccbar2PhiPhiPiPiLine = StrippingLine( self.name + 'Line',                                                
                                               prescale  = config['Prescale'],
                                               HLT2      = config['HLTCuts'],
                                               algos     = [ self.SelCcbar2PhiPhiPiPi ],
                                               MDSTFlag  = False
                                               )
        self.registerLine( self.Ccbar2PhiPhiPiPiLine )
        
    def createSubSel( self, OutputList, InputList, Cuts ) :
        '''create a selection using a FilterDesktop'''
        filter = FilterDesktop(Code = Cuts)
        return Selection( OutputList,
                          Algorithm = filter,
                          RequiredSelections = [ InputList ] )
    
    def createN4BodySel( self, OutputList,
                         DecayDescriptor,
                         DaughterLists,
                         DaughterCuts = {} ,
                         ComAMCuts      = "AALL",
                         PreVertexCuts  = "AALL",
                         PostVertexCuts = "ALL" ) :
        '''create a selection using a ParticleCombiner with a single decay descriptor'''
        combiner = DaVinci__N4BodyDecays ( DecayDescriptor = DecayDescriptor,      
                                           DaughtersCuts = DaughterCuts,
                                           Combination12Cut  = ComAMCuts + "&" + "( ACHI2DOCA(1,2)<20 )",
                                           Combination123Cut = ComAMCuts + "&" + "( ACHI2DOCA(1,3)<20 ) & ( ACHI2DOCA(2,3)<20 )",
                                           CombinationCut = "( ACHI2DOCA(1,4)<20 ) & ( ACHI2DOCA(2,4)<20 ) & ( ACHI2DOCA(3,4)<20 )" + " & " + PreVertexCuts,
                                           MotherCut = PostVertexCuts,
                                           ReFitPVs = False )
        return Selection ( OutputList,
                           Algorithm = combiner,
                           RequiredSelections = DaughterLists)


    def filterTisTos(self, name,          ##OK
                     PhiInput,
                     myTisTosSpecs ) :
        from Configurables import TisTosParticleTagger
        
        myTagger = TisTosParticleTagger(name + "_TisTosTagger")
        myTagger.TisTosSpecs = myTisTosSpecs
        
        # To speed it up, TisTos only with tracking system)
        myTagger.ProjectTracksToCalo = False
        myTagger.CaloClustForCharged = False
        myTagger.CaloClustForNeutral = False
        myTagger.TOSFrac = { 4:0.0, 5:0.0 }
        
        return Selection(name + "_SelTisTos",
                         Algorithm = myTagger,
                         RequiredSelections = [ PhiInput ] )


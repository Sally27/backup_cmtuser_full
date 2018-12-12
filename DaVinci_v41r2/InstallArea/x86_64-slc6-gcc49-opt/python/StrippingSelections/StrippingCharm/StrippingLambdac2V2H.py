"""
Stripping lines for selection of general decay topologies
    [Lambda_c+ -> (V- -> (V0 -> h+ h-) h-) h+ h+]CC
In this file the stripping line for this decay is build
    [Lambda_c+ -> (Xi- -> (Lambda0 -> p+ pi-) pi-) K+ pi+]CC
Throughout this file, 'Bachelor' refers to the children of the Lambda_c+ which is
not part of the V- decay.
"""
__author__ = ['Andrea Merli']
__date__ = '07/04/2016'

__all__ = (
    'default_config',
    'StrippingLambdac2V2HConf'
)

from GaudiKernel.SystemOfUnits import MeV, GeV, mm, mrad
from GaudiConfUtils.ConfigurableGenerators import CombineParticles, FilterDesktop, DaVinci__N3BodyDecays
from StandardParticles import StdNoPIDsDownPions as InputDownPions
from StandardParticles import StdNoPIDsPions as InputPions
from StandardParticles import StdNoPIDsKaons as InputKaons
from StandardParticles import StdLooseLambdaLL as InputLambdasLL
from StandardParticles import StdLooseLambdaDD as InputLambdasDD

from PhysSelPython.Wrappers import Selection
from StrippingUtils.Utils import LineBuilder
from StrippingConf.StrippingLine import StrippingLine

default_config = {
    'NAME': 'Lambdac2V2H',
    'WGs': ['Charm'],
    'BUILDERTYPE': 'StrippingLambdac2V2HConf',
    'STREAMS': ['Charm'],
    'CONFIG': {
        # Minimum Lc+ bachelor momentum
        'Bach_P_MIN': 2.0*GeV,
        # Minimum L0 momentum
        'Lambda0_P_MIN': 2000*MeV,
        # Minimum L0 transverse momentum
        'Lambda0_PT_MIN': 250*MeV,
        # Minimum flight distance chi^2 of L0 from the primary vertex
        'Lambda0_FDCHI2_MIN': 49,
        # Maximum L0 vertex chi^2 per vertex fit DoF
        'Lambda0_VCHI2VDOF_MAX': 12.0,
        # Minimum Xi- momentum
        'Xim_P_MIN': 2000*MeV,
        # Minimum Xi- transverse momentum
        'Xim_PT_MIN': 250*MeV,
        # Minimum flight distance chi^2 of Xi- from the primary vertex
        'Xim_FDCHI2_MIN': 49,
        # Maximum Xi- vertex chi^2 per vertex fit DoF
        'Xim_VCHI2VDOF_MAX': 12.0,
        # Lc+ mass window around the nominal Lc+ mass before the vertex fit
        'Comb_ADAMASS_WIN': 120.0*MeV,
        # Lc+ mass window around the nominal Lc+ mass after the vertex fit
        'Lambdac_ADMASS_WIN': 90.0*MeV,
        # Maximum distance of closest approach of Lc+ children
        'Comb_ADOCAMAX_MAX': 0.5*mm,
        # Maximum Lc+ vertex chi^2 per vertex fit DoF
        'Lambdac_VCHI2VDOF_MAX': 12.0,
        # Maximum angle between Lc+ momentum and Lc+ direction of flight
        'Lambdac_acosBPVDIRA_MAX': 140.0*mrad,
        # Primary vertex displacement requirement, either that the Lc+ is some
        # sigma away from the PV, or it has a minimum flight time
        'Lambdac_PVDispCut': '(BPVVDCHI2 > 16.0)',
        # HLT filters, only process events firing triggers matching the RegEx
        'Hlt1Filter': None,
        'Hlt2Filter': None,
        # Fraction of candidates to randomly throw away before stripping
        'PrescaleLambdac2XiKPiLLL': 1.0,
        'PrescaleLambdac2XiKPiDDD': 1.0,
        'PrescaleLambdac2XiKPiDDL': 1.0,
        # Fraction of candidates to randomly throw away after stripping
        'PostscaleLambdac2XiKPiLLL': 1.0,
        'PostscaleLambdac2XiKPiDDD': 1.0,
        'PostscaleLambdac2XiKPiDDL': 1.0
    }
}


class StrippingLambdac2V2HConf(LineBuilder):
    """Creates LineBuilder object containing the stripping lines."""
    # Allowed configuration keys
    __configuration_keys__ = default_config['CONFIG'].keys()

    def __init__(self, name, config):
        """Initialise this LineBuilder instance."""
        self.name = name
        self.config = config
        LineBuilder.__init__(self, name, config)
        
        # Decay descriptors
        self.Lambdac2XiKpi = ['[Lambda_c+ -> Xi- K+ pi+]cc']
        self.Xi2Lambdapi = ['[Xi- -> Lambda0 pi-]cc']
        # Line names
        # 'LLL', 'DDD' and 'DDL' will be appended to these names for the LLL, DDD, DDL
        # Selection and StrippingLine instances
        self.Lambdac2XiKpi_name = '{0}_Lambdac2XiKpi'.format(name)
        # Build bachelor pion and kaon cut strings
        # Cuts MIPCHI2DV(PRIMARY)>4 & PT>250*MeV already present in the InputsParticles
        childCuts = (
            '(P > {0[Bach_P_MIN]})'
        ).format(self.config)
        
        kineticCuts = '{0}'.format(childCuts)

        # Build Lambda0 cut strings
        lambda0Cuts = (
            '(P > {0[Lambda0_P_MIN]})'
            '& (PT > {0[Lambda0_PT_MIN]})'
            '& (BPVVDCHI2 > {0[Lambda0_FDCHI2_MIN]})'
            '& (VFASPF(VCHI2/VDOF) < {0[Lambda0_VCHI2VDOF_MAX]})'
        ).format(self.config)
        ximCuts = (
            '(P > {0[Xim_P_MIN]})'
            '& (PT > {0[Xim_PT_MIN]})'
            '& (BPVVDCHI2 > {0[Xim_FDCHI2_MIN]})'
            '& (VFASPF(VCHI2/VDOF) < {0[Xim_VCHI2VDOF_MAX]})'
        ).format(self.config)
        # Define any additional cuts on LL/DD difference
        lambda0LLCuts = lambda0Cuts
        lambda0DDCuts = lambda0Cuts
        ximLLLCuts = ximCuts
        ximDDDCuts = ximCuts
        ximDDLCuts = ximCuts
        
        # Filter Input particles
        self.Pions = Selection(
            'PionsFor{0}'.format(name),
            Algorithm=FilterDesktop(
                 Code = kineticCuts
            ),
            RequiredSelections=[InputPions]
        )

        self.Kaons = Selection(
            'KaonsFor{0}'.format(name),
            Algorithm=FilterDesktop(
                 Code = kineticCuts
            ),
            RequiredSelections=[InputKaons]
        )

        self.DownPions = Selection(
            'DownPionsFor{0}'.format(name),
            Algorithm=FilterDesktop(
                 Code = kineticCuts
            ),
            RequiredSelections=[InputDownPions]
        )
        # Filter Input Lambdas
        self.Lambda0LL = Selection(
            'Lambda0LLFor{0}'.format(name),
            Algorithm=FilterDesktop(
                Code=lambda0LLCuts
            ),
            RequiredSelections=[InputLambdasLL]
        )
        self.Lambda0DD = Selection(
            'Lambda0DDFor{0}'.format(name),
            Algorithm=FilterDesktop(
                Code=lambda0DDCuts
            ),
            RequiredSelections=[InputLambdasDD]
        )

        # Make Xim
        self.Xim = self.makeXi2LambdaPi(
            name = name,
            inputSelLLL = [self.Lambda0LL,self.Pions],
            inputSelDDD = [self.Lambda0DD,self.DownPions],
            inputSelDDL = [self.Lambda0DD,self.Pions],
            LLLFilter = ximLLLCuts,
            DDDFilter = ximDDDCuts,
            DDLFilter = ximDDLCuts,
            decDescriptors=self.Xi2Lambdapi
        )

        # Build selection for Lc -> Xi K pi
        self.selLambdac2XiKPi = self.makeLambdac2VHH(
            name=self.Lambdac2XiKpi_name,
            inputSelLLL=[self.Xim['LLL'],self.Kaons,self.Pions],
            inputSelDDD=[self.Xim['DDD'],self.Kaons,self.Pions],
            inputSelDDL=[self.Xim['DDL'],self.Kaons,self.Pions],
            decDescriptors=self.Lambdac2XiKpi
        )

        # Make line for Lc -> Xi K pi
        self.line_Lambdac2XiKPiLLL = self.make_line(
            name='{0}LLLLine'.format(self.Lambdac2XiKpi_name),
            selection=self.selLambdac2XiKPi['LLL'],
            prescale=config['PrescaleLambdac2XiKPiLLL'],
            postscale=config['PostscaleLambdac2XiKPiLLL'],
            HLT1=config['Hlt1Filter'],
            HLT2=config['Hlt2Filter']
        )

        self.line_Lambdac2XiKPiDDD = self.make_line(
            name='{0}DDDLine'.format(self.Lambdac2XiKpi_name),
            selection=self.selLambdac2XiKPi['DDD'],
            prescale=config['PrescaleLambdac2XiKPiDDD'],
            postscale=config['PostscaleLambdac2XiKPiDDD'],
            HLT1=config['Hlt1Filter'],
            HLT2=config['Hlt2Filter'],
            #RequiredRawEvents = ["Rich"]
        )

        self.line_Lambdac2XiKPiDDL = self.make_line(
            name='{0}DDLLine'.format(self.Lambdac2XiKpi_name),
            selection=self.selLambdac2XiKPi['DDL'],
            prescale=config['PrescaleLambdac2XiKPiDDL'],
            postscale=config['PostscaleLambdac2XiKPiDDL'],
            HLT1=config['Hlt1Filter'],
            HLT2=config['Hlt2Filter']
        )

    def make_line(self, name, selection, prescale, postscale, **kwargs):
        """Create the stripping line defined by the selection.

        Keyword arguments:
        name -- Base name for the Line
        selection -- Selection instance
        prescale -- Fraction of candidates to randomly drop before stripping
        postscale -- Fraction of candidates to randomly drop after stripping
        **kwargs -- Keyword arguments passed to StrippingLine constructor
        """
        # Only create the line with positive pre- and postscales
        # You can disable each line by setting either to a negative value
        if prescale > 0 and postscale > 0:
            line = StrippingLine(
                name,
                selection=selection,
                prescale=prescale,
                postscale=postscale,
                **kwargs
            )
            self.registerLine(line)
            return line
        else:
            return False

    def makeXi2LambdaPi(self, name, inputSelLLL, inputSelDDD, inputSelDDL, LLLFilter, DDDFilter, DDLFilter, decDescriptors):
        """Return the dictionary for three Selection instances for a Xi- -> V0 h- decay.
        The return value is a two-tuple of Selection instances as
               {'LLL':LLL Selection, 'DDD':DDD Selection, 'DDL': DDL Selection}.
        Keyword arguments:
        name -- Name to give the Selection instance
        inputSelLLL -- List of inputs passed to Selection.RequiredSelections for the LLL Selection (LambdaLL and Pions Long)
        inputSelDDD -- List of inputs passed to Selection.RequiredSelections for the DDD Selection (LambdaDD and Pions Downstream)
        inputSelDDL -- List of inputs passed to Selection.RequiredSelections for the DDL Selection (LambdaDD and Pions Long)
        decDescriptors -- List of decay descriptors for CombineParticles

        The cuts are equal to LambdaDD and LambdaLL
        """

        # Xim StandardCuts as Lambda0 + Filters
        _XimLLL = CombineParticles(
            DecayDescriptors=decDescriptors,
            DaughtersCuts = {'pi+': '(P>2*GeV) & (MIPCHI2DV(PRIMARY)>9)'},
            CombinationCut = "(ADAMASS('Xi-')<50*MeV) & (ADOCACHI2CUT(30, ''))",
            MotherCut = "(ADMASS('Xi-')<35*MeV) & (VFASPF(VCHI2)<30) & {0}".format(LLLFilter),
        )

        _XimDDD = CombineParticles(
            DecayDescriptors=decDescriptors,
            DaughtersCuts = {'pi+': '(P>2*GeV) & (MIPCHI2DV(PRIMARY)>4)'},
            CombinationCut = "(ADAMASS('Xi-')<80*MeV) & (ADOCACHI2CUT(25, ''))",
            MotherCut = "(ADMASS('Xi-')<64*MeV) & (VFASPF(VCHI2)<25) & {0}".format(DDDFilter),
        )

        _XimDDL = CombineParticles(
            DecayDescriptors=decDescriptors,
            DaughtersCuts = {'pi+': '(P>2*GeV) & (MIPCHI2DV(PRIMARY)>4)'},
            CombinationCut = "(ADAMASS('Xi-')<80*MeV) & (ADOCACHI2CUT(25, ''))",
            MotherCut = "(ADMASS('Xi-')<64*MeV) & (VFASPF(VCHI2)<25) & {0}".format(DDLFilter),
        )

        selXimLLL = Selection(
            'XimLLLFor{0}'.format(name),
            Algorithm=_XimLLL,
            RequiredSelections=inputSelLLL
        )
        selXimDDD = Selection(
            'XimDDDFor{0}'.format(name),
            Algorithm=_XimDDD,
            RequiredSelections=inputSelDDD
        )
        selXimDDL = Selection(
            'XimDDLFor{0}'.format(name),
            Algorithm=_XimDDL,
            RequiredSelections=inputSelDDL
        )

        
        return {'LLL':selXimLLL,'DDD':selXimDDD,'DDL':selXimDDL}

    def makeLambdac2VHH(self, name, inputSelLLL, inputSelDDD, inputSelDDL, decDescriptors):
        """Return two Selection instances for a Lambda_c+ -> V- h+ h+ decay.

        The return value is a dictionary of Selection instances as
            {'LLL': LLL Selection, 'DDD': DDD Selection, 'DDL': DDL Selection}
        depending on how the V has been reconstructed.
        Keyword arguments:
        name -- Name to give the Selection instance
        inputSelLLL -- List of inputs passed to Selection.RequiredSelections
                       for the LLL Selection
        inputSelDDD -- List of inputs passed to Selection.RequiredSelections
                       for the DDD Selection
        inputSelDDL -- List of inputs passed to Selection.RequiredSelections
                       for the DDL Selection
        decDescriptors -- List of decay descriptors for CombineParticles
        """
        lclPreambulo = [
            'from math import cos'
        ]

        combCuts = (
            "(ADAMASS('Lambda_c+') < {0[Comb_ADAMASS_WIN]})"
            "& (ADOCA(1,2) < {0[Comb_ADOCAMAX_MAX]})"
            "& (ADOCA(1,3) < {0[Comb_ADOCAMAX_MAX]})"
        ).format(self.config)

        lambdacCuts = (
            "(VFASPF(VCHI2/VDOF) < {0[Lambdac_VCHI2VDOF_MAX]})"
            "& ({0[Lambdac_PVDispCut]})"
            "& (BPVDIRA > cos({0[Lambdac_acosBPVDIRA_MAX]}))"
            "& (ADMASS('Lambda_c+') < {0[Lambdac_ADMASS_WIN]})"
        ).format(self.config)

        comb12Cuts = (
            "(DAMASS('Lambda_c+') < {0[Comb_ADAMASS_WIN]})"
            "& (ADOCA(1,2) < {0[Comb_ADOCAMAX_MAX]})"
            ).format(self.config)

        _Lambdac = DaVinci__N3BodyDecays(
            DecayDescriptors=decDescriptors,
            Preambulo=lclPreambulo,
            CombinationCut=combCuts,
            MotherCut=lambdacCuts,
            Combination12Cut=comb12Cuts,
        )

        selLLL = Selection(
            '{0}LLL'.format(name),
            Algorithm=_Lambdac,
            RequiredSelections=inputSelLLL
        )
        selDDD = Selection(
            '{0}DDD'.format(name),
            Algorithm=_Lambdac,
            RequiredSelections=inputSelDDD
        )
        selDDL = Selection(
            '{0}DDL'.format(name),
            Algorithm=_Lambdac,
            RequiredSelections=inputSelDDL
        )
        
        return {'LLL': selLLL, 'DDD': selDDD, 'DDL': selDDL}

'''
D0/D*+ cross-section lines

Adapted to current stripping framework by P. Spradlin.
'''

__author__ = ['Marco Gersabeck', 'Patrick Spradlin']
__date__ = '03/09/2010'
__version__ = '$Revision: 1.4 $'

__all__ = ( 'StrippingD02HHForXSecConf',
            'makeD02HH',
            'makeDstar2D0Pi',
            'default_config' )


from Gaudi.Configuration import *
from StrippingConf.StrippingLine import StrippingLine
from GaudiKernel.SystemOfUnits import MeV
from LHCbKernel.Configuration import *
#from Configurables import FilterDesktop, CombineParticles
from GaudiConfUtils.ConfigurableGenerators import FilterDesktop, CombineParticles
from PhysSelPython.Wrappers import Selection, SelectionSequence, DataOnDemand
from StrippingUtils.Utils import LineBuilder
from StandardParticles import StdNoPIDsPions, StdNoPIDsKaons

class StrippingD02HHForXSecConf(LineBuilder): # {

    __configuration_keys__ = (   'Daug_PT_MIN'
                               , 'Daug_TRCHI2DOF_MAX'
                               , 'Daug_MIPCHI2DV_MIN'
                               , 'D0_BPVVDCHI2_MIN'
                               , 'D0_BPVDIRA_MIN'
                               , 'D0_BPVIPCHI2_MAX'
                               , 'D0_ADAMASS_WIN'
                               , 'D0_ADMASS_WIN'
                               , 'Dstar_AMDiff_MAX'
                               , 'Dstar_MDiff_MAX'
                               , 'Dstar_VCHI2VDOF_MAX'
                               , 'HltFilter'
                               , 'PrescaleD02HH'
                               , 'PrescaleDstar2D0Pi_D02HH'
                               , 'PostscaleD02HH'
                               , 'PostscaleDstar2D0Pi_D02HH'
                             )



    def __init__(self, name, config) : # {

        LineBuilder.__init__(self, name, config)

        d02HH_name = name + 'D02HH'
        dstar_name  = name + 'Dstar2D0Pi_D02HH'

        self.inPions = StdNoPIDsPions
        self.inKaons = StdNoPIDsKaons

        self.selD02HH = makeD02HH( d02HH_name
                                   , inputSel = [ self.inPions, self.inKaons ]
                                   , Daug_PT_MIN        = config['Daug_PT_MIN']
                                   , Daug_TRCHI2DOF_MAX = config['Daug_TRCHI2DOF_MAX']
                                   , Daug_MIPCHI2DV_MIN = config['Daug_MIPCHI2DV_MIN']
                                   , D0_ADAMASS_WIN     = config['D0_ADAMASS_WIN']
                                   , D0_ADMASS_WIN      = config['D0_ADMASS_WIN']
                                   , D0_BPVVDCHI2_MIN   = config['D0_BPVVDCHI2_MIN']
                                   , D0_BPVDIRA_MIN     = config['D0_BPVDIRA_MIN']
                                   , D0_BPVIPCHI2_MAX   = config['D0_BPVIPCHI2_MAX']
                                 )


        self.line_D02HH = StrippingLine( d02HH_name + 'Line',
                                         HLT = config['HltFilter'],
                                         prescale  = config['PrescaleD02HH'],
                                         postscale = config['PostscaleD02HH'],
                                         algos = [ self.selD02HH ]
                                       )
        self.registerLine(self.line_D02HH)


        self.selDstar2D0Pi_D02HH = makeDstar2D0Pi( dstar_name
                    , inputSel = [ self.inPions, self.selD02HH ]
                    , Daug_TRCHI2DOF_MAX  = config['Daug_TRCHI2DOF_MAX']
                    , Dstar_AMDiff_MAX    = config['Dstar_AMDiff_MAX']
                    , Dstar_VCHI2VDOF_MAX = config['Dstar_VCHI2VDOF_MAX']
                    , Dstar_MDiff_MAX     = config['Dstar_MDiff_MAX']
        )

        self.line_Dstar2D0Pi_D02HH = StrippingLine( dstar_name + 'Line',
                                         HLT = config['HltFilter'],
                                         prescale   = config['PrescaleDstar2D0Pi_D02HH'],
                                         postscale = config['PostscaleDstar2D0Pi_D02HH'],
                                         algos = [ self.selDstar2D0Pi_D02HH ]
                                        )
        self.registerLine(self.line_Dstar2D0Pi_D02HH)

    # }

# }


def makeD02HH( name
               , inputSel
               , Daug_PT_MIN
               , Daug_TRCHI2DOF_MAX
               , Daug_MIPCHI2DV_MIN
               , D0_ADAMASS_WIN
               , D0_ADMASS_WIN
               , D0_BPVVDCHI2_MIN
               , D0_BPVDIRA_MIN
               , D0_BPVIPCHI2_MAX
               , decDescriptors = [ "D0 -> pi+ pi-",
                                    "D0 -> K- pi+",
                                    "D0 -> K+ pi-",
                                    "D0 -> K+ K-" ]
             ) : # {

    daugCuts = "(PT > %(Daug_PT_MIN)s)" \
               "& (TRCHI2DOF < %(Daug_TRCHI2DOF_MAX)s)" \
               "& (MIPCHI2DV(PRIMARY) > %(Daug_MIPCHI2DV_MIN)s)" % locals()

    combCuts = "(ADAMASS('D0') < %(D0_ADAMASS_WIN)s)" % locals()

    d0Cuts = "(ADMASS('D0') < %(D0_ADMASS_WIN)s)" \
             "& (BPVVDCHI2 > %(D0_BPVVDCHI2_MIN)s)" \
             "& (BPVDIRA > %(D0_BPVDIRA_MIN)s)" \
             "& (BPVIPCHI2()<%(D0_BPVIPCHI2_MAX)s)" % locals()


    _D0 = CombineParticles(
        DecayDescriptors = decDescriptors
        , DaughtersCuts = { "pi+" : daugCuts, "K+" : daugCuts }
        , CombinationCut = combCuts
        , MotherCut = d0Cuts
    )



    return Selection( name,
                      Algorithm = _D0,
                      RequiredSelections = inputSel
                    )

# }



def makeDstar2D0Pi( name
                    , inputSel
                    , Daug_TRCHI2DOF_MAX
                    , Dstar_AMDiff_MAX
                    , Dstar_VCHI2VDOF_MAX
                    , Dstar_MDiff_MAX
                    , decDescriptors= [ "D*(2010)+ -> D0 pi+",
                                        "D*(2010)- -> D0 pi-" ]
                  ) : # {

    daugCuts = "(TRCHI2DOF < %(Daug_TRCHI2DOF_MAX)s)" % locals()

    combCuts = "((AM - AM1) < %(Dstar_AMDiff_MAX)s)" % locals()

    dstarCuts = "(VFASPF(VCHI2/VDOF) < %(Dstar_VCHI2VDOF_MAX)s)" \
                "& ((M - M1) < %(Dstar_MDiff_MAX)s)" % locals()

    _Dstar = CombineParticles(
        DecayDescriptors = decDescriptors
        , DaughtersCuts = { "pi+" : daugCuts }
        , CombinationCut = combCuts
        , MotherCut = dstarCuts
    )

    return Selection( name,
                      Algorithm = _Dstar,
                      RequiredSelections = inputSel
                    )

# }




default_config = {  'Daug_PT_MIN'               : 250.0*MeV
                  , 'Daug_TRCHI2DOF_MAX'        :   9.0
                  , 'Daug_MIPCHI2DV_MIN'        :   9.0
                  #
                  , 'D0_BPVVDCHI2_MIN'          :  16.0
                  , 'D0_BPVDIRA_MIN'            :   0.9999
                  , 'D0_BPVIPCHI2_MAX'          : 100.0
                  , 'D0_ADAMASS_WIN'            :  80.0*MeV
                  , 'D0_ADMASS_WIN'             :  75.0*MeV
                  #
                  , 'Dstar_AMDiff_MAX'          : 160.0*MeV
                  , 'Dstar_MDiff_MAX'           : 155.0*MeV
                  , 'Dstar_VCHI2VDOF_MAX'       : 100.0
                  , 'HltFilter'          : "HLT_PASS_RE('Hlt1MB.*')"
                  #
                  , 'PrescaleD02HH'             :   1.0
                  , 'PrescaleDstar2D0Pi_D02HH'  :   1.0
                  , 'PostscaleD02HH'            :   1.0
                  , 'PostscaleDstar2D0Pi_D02HH' :   1.0
                 }



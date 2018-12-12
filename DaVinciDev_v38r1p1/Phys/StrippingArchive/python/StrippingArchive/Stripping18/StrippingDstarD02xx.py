#
__author__ = ['Francesco Dettori', 'Walter Bonivento']
__date__ = '2010/04/23'
__version__ = '$Revision: 1.5 $'

'''
  Stripping for D*(2010)+ -> pi+ (D0->xx) selection:
            where xx = {mu mu, pi pi, pi mu, k mu, ... }
            
'''
from Gaudi.Configuration import *
from LHCbKernel.Configuration import *
from Configurables import FilterDesktop, CombineParticles
from PhysSelPython.Wrappers import Selection, DataOnDemand
from StrippingConf.StrippingLine import StrippingLine
from StrippingUtils.Utils import LineBuilder, checkConfig

# Default values

config_default ={'PrescalepipiBox'     : 0.5
                 , 'PrescalemumuBox'     : 1.
                 , 'PrescaleKpiBox'    : 0.3
                 , 'PrescaleemuBox'    : 1.
                 , 'PrescaleeKBox'    : 1.
                 , 'PrescaleepiBox'    : 1.
                 , 'PrescalepimuBox'    : 1.
                 , 'PrescaleKmuBox'    : 1.
                 , 'Prescalepipi_untagged_Box'     : 0.2
                 , 'Prescalemumu_untagged_Box'     : 1.
                 , 'PrescaleKpi_untagged_Box'    : 0.2
                 , 'Prescalepimu_untagged_Box'    : 1.
                 , 'PrescaleKmu_untagged_Box'    : 0.2
                 , 'PrescaleKpi_untagged_BoxMB' : 1
                 , 'Prescalepipi_untagged_BoxMB':1
                 , 'PrescaleKpi_untagged_BoxMBTrEff' : 1
                 ,'DMassWin'           : 70.       # MeV
                 ,'DMassWinMuMuLow'    : -150.       #MeV
                 ,'DMassWinMuMuHigh'   : 300       #MeV
                 ,'DMassWinEMu'        : 300
                 ,'doca'               : 0.1        # mm
                 ,'XminPT'             : 750.       # MeV
                 ,'XmaxPT'             : 1100.      # MeV
                 ,'XminP'              : 4000.      # MeV
                 ,'XTrackChi2'         : 5.        # adimensional
                 ,'XTrackChi2Pi'         : 7.        # adimensional
                 ,'XminIPChi2'         : 3        # adimensional
                 ,'XmaxIPChi2'         : 8        # adimensional
                 ,'DMinFlightChi2'    :  20.
                 ,'DDira'              : 0.9997     # adimensional
                 ,'D0MinPT'            : 1800.      # MeV
                 ,'DMaxIPChi2'        :15.
                 ,'DVChi2'            :10. 
                 ,'PiMinPT'            : 110.       # MeV
                 ,'PiMaxIPCHI2'        : 10.         # adimensional
                 ,'DstMassWin'         : 300.       # MeV
                 ,'DstD0DMWin'         : 10.        # MeV
                 ,'DstD0DMWinMuMu'      : 30.        # MeV  
                 ,'RequireHlt'         : 1          # 
                 ,'prefix'         : '' 
                 }


default_name = "DstarD02xx"

class StrippingDstarD02xxConf(LineBuilder):
    """
    Builder for  D*(2010)+ -> pi+ (D0->xx) stripping lines
    """
    __configuration_keys__ = (   'PrescalepipiBox' 
                                 , 'PrescalemumuBox'
                                 , 'PrescaleKpiBox'
                                 , 'PrescaleemuBox'
                                 , 'PrescaleeKBox'
                                 , 'PrescaleepiBox'
                                 , 'PrescalepimuBox'
                                 , 'PrescaleKmuBox'
                                 , 'Prescalepipi_untagged_Box'
                                 , 'Prescalemumu_untagged_Box'
                                 , 'PrescaleKpi_untagged_Box'
                                 , 'Prescalepimu_untagged_Box'
                                 , 'PrescaleKmu_untagged_Box'
                                 , 'PrescaleKpi_untagged_BoxMB'
                                 , 'Prescalepipi_untagged_BoxMB'
                                 , 'PrescaleKpi_untagged_BoxMBTrEff' 
                                 ,'DMassWin'
                                 ,'DMassWinMuMuLow'
                                 ,'DMassWinMuMuHigh'
                                 ,'DMassWinEMu' 
                                 ,'doca'
                                 ,'XminPT'
                                 ,'XmaxPT'
                                 ,'XminP'
                                 ,'XTrackChi2'
                                 ,'XTrackChi2Pi'
                                 ,'XminIPChi2'
                                 ,'XmaxIPChi2'
                                 ,'DMinFlightChi2'
                                 ,'DDira'
                                 ,'D0MinPT'
                                 ,'DMaxIPChi2'
                                 ,'DVChi2'
                                 ,'PiMinPT'
                                 ,'PiMaxIPCHI2'
                                 ,'DstMassWin'
                                 ,'DstD0DMWin'
                                 ,'DstD0DMWinMuMu'
                                 ,'RequireHlt'
                                 ,'prefix'
                                 )
    
    
    def __init__(self, name, config) :
        LineBuilder.__init__(self, name, config)
        
        lines_to_be = self.my_lines(name, config)
        for i in lines_to_be:
            self.registerLine(i)
            
 
            
    ####### Template for combine particles for D0 -> x+ y-  ######
    def combinetwobody(self, name, config, xplus, xminus, postfix="") :
        from Configurables import CombineParticles
        if(xplus == "mu") and (xminus == "mu") :                                     
            d0comb_combcut =       "(AMAXDOCA('')< %(doca)s *mm) & (DAMASS('D0')< %(DMassWinMuMuHigh)s *MeV) & (DAMASS('D0')> %(DMassWinMuMuLow)s *MeV) & (AMAXCHILD(PT)>%(XmaxPT)s *MeV) & (APT> %(D0MinPT)s)"
        elif (((xplus == "mu") and (xminus == "e")) or ((xplus == "e") and (xminus == "mu"))) :
            d0comb_combcut =       "(AMAXDOCA('')< %(doca)s *mm) & (ADAMASS('D0')< %(DMassWinEMu)s *MeV) & (AMAXCHILD(PT)>%(XmaxPT)s *MeV) & (APT> %(D0MinPT)s)"
        else :
            d0comb_combcut =       "(AMAXDOCA('')< %(doca)s *mm) & (ADAMASS('D0')< %(DMassWin)s *MeV) & (AMAXCHILD(PT)>%(XmaxPT)s *MeV) & (APT> %(D0MinPT)s)"
            
        d0comb_childcut = "(PT> %(XminPT)s *MeV) & (P>%(XminP)s *MeV) & (TRCHI2DOF<%(XTrackChi2)s) & (MIPCHI2DV(PRIMARY)> %(XminIPChi2)s) " 
        d0comb_d0cut = "(BPVDIRA> %(DDira)s) & (INGENERATION( (MIPCHI2DV(PRIMARY)>%(XmaxIPChi2)s),1 ) ) & (BPVVDCHI2> %(DMinFlightChi2)s) & (MIPCHI2DV(PRIMARY)< %(DMaxIPChi2)s) & (VFASPF(VCHI2/VDOF)< %(DVChi2)s)"
        xx_name = "D02"+xplus+xminus+postfix
        xx_comb = CombineParticles( config['prefix']+xx_name )

        inputLoc = {
             "pi" : "Phys/StdAllNoPIDsPions/Particles"
            ,"mu" : "Phys/StdAllLooseMuons/Particles"
            ,"K" : "Phys/StdAllLooseKaons/Particles"
            ,"e" : "Phys/StdAllLooseElectrons/Particles"
            }
        req_sel = []
        if xplus != xminus :
            decays = ["D0 -> "+ xplus + "+ " + xminus + "- ", "D0 -> "+ xplus + "- " + xminus + "+ " ]
            xx_comb.DecayDescriptors =  decays
            xx_comb.DaughtersCuts = { xplus+"+" : d0comb_childcut % config
                                     , xminus+"-" : d0comb_childcut % config }
            req_sel.append(DataOnDemand(Location = inputLoc[xplus]))
            req_sel.append(DataOnDemand(Location = inputLoc[xminus]))
        else:
            decay = "D0 -> "+ xplus + "+ " + xminus + "- "
            xx_comb.DecayDescriptor =  decay
            xx_comb.DaughtersCuts = { xplus+"+" : d0comb_childcut % config }
            req_sel.append(DataOnDemand(Location = inputLoc[xplus]))
        xx_comb.MotherCut = d0comb_d0cut  % config
        xx_comb.CombinationCut = d0comb_combcut % config

        _untag_sel = Selection (name+"seq_"+xx_name+"_selection", Algorithm = xx_comb, RequiredSelections = req_sel)
        
        
        return _untag_sel
    
    ####### Template for combine particles for D* -> D0 pi
    def combineDstar(self, name, config) :
        from Configurables import CombineParticles
        dstcomb_dstcut       =  "(abs(M-MAXTREE('D0'==ABSID,M)-145.42) < %(DstD0DMWin)s ) & (VFASPF(VCHI2/VDOF)< %(DVChi2)s)"
        dstcomb_combcut =  "(ADAMASS('D*(2010)+')<%(DstMassWin)s * MeV)"
        dstcomb_picut = "(PT> %(PiMinPT)s * MeV) &  ( MIPCHI2DV(PRIMARY)< %(PiMaxIPCHI2)s) & (TRCHI2DOF<%(XTrackChi2Pi)s) "
        dstcomb_d0cut = "PT>0"
        
        dstar = CombineParticles( config['prefix']+"combine" )
        #dstar.DecayDescriptors = ['[D*(2010)+ -> D0 pi+]cc']
        dstar.DecayDescriptors = ['D*(2010)+ -> D0 pi+', 'D*(2010)- -> D0 pi-']
        dstar.DaughtersCuts = {    "pi+" : dstcomb_picut % config ,
                                   "D0"    : dstcomb_d0cut % config
                                   }
        dstar.CombinationCut = dstcomb_combcut % config
        dstar.MotherCut =  dstcomb_dstcut % config
    
        return dstar

    ###### Full line
    def baseLine(self, name, config,  xplus, xminus) :
        """
        Returns the stripping line for the tagged decay
        D* -> D0(-> xx) pi
        """
        from StrippingConf.StrippingLine import StrippingLine
        xxCombSel = self.combinetwobody(name, config,xplus, xminus,"forTag")
        dstar = self.combineDstar(name, config)
        combname = xplus+xminus
        dstar_box = dstar.clone(name+config['prefix']+"Dst2PiD02"+combname+"D0PiComb" )
        dst_req_sel = [DataOnDemand( "Phys/StdAllNoPIDsPions/Particles" ) ,
                       DataOnDemand( "Phys/StdNoPIDsUpPions/Particles"),
                       xxCombSel]
        
        pres = "Prescale"+combname+"Box"
        _tag_sel = Selection (name+"_seq_"+combname+"_box",
                              Algorithm = dstar_box,
                              RequiredSelections = dst_req_sel)####
        
        # Capitalize particle names to match Hlt2 D*->pi D0-> xx lines
        Xplus  = xplus[0].upper() + xplus[1:]    
        Xminus = xminus[0].upper() + xminus[1:]
        hltname = "Hlt2Dst2PiD02"+Xplus+Xminus+"*Decision"  # * matches Signal, Sidebands and Box lines
        line_box = StrippingLine(name+config['prefix']+"Dst2PiD02"+combname+"Box",
                                 HLT = "HLT_PASS_RE('"+hltname+"')",
                                 algos = [ _tag_sel ], prescale = config[ pres ])
        
        return line_box
    
    def baseLine_untagged(self, name, config, xplus, xminus, minbias) :
        """
        Returns the stripping line for the untagged decay
        D0->xx
        """
        from StrippingConf.StrippingLine import bindMembers
        from StrippingConf.StrippingLine import StrippingLine
        suffix = ""
        if minbias == 1 :
            suffix = "MB"
        elif minbias ==2 :
            suffix = "MBTrEff"
            
        xxCombSel= self.combinetwobody(name+suffix, config,xplus, xminus)
        combname = xplus+xminus
        pres = "Prescale"+combname+"_untagged_Box"
        # Capitalize particle names to match Hlt2 D*->pi D0-> xx lines
        Xplus  = xplus[0].upper() + xplus[1:]    
        Xminus = xminus[0].upper() + xminus[1:]
        hltname = "Hlt2Dst2PiD02"+Xplus+Xminus+"*Decision"  # * matches Signal, Sidebands and Box lines
        
        if(minbias==1):
            line_untagged_box = StrippingLine(name+config['prefix']+"Dst2PiD02"+combname+"_untagged_BoxMB",
                                              HLT = "HLT_PASS_RE('Hlt1(MB|L0).*Decision')",
                                              algos = [ xxCombSel ], prescale = config[ pres+"MB" ])
        elif(minbias==2):
            line_untagged_box = StrippingLine(name+config['prefix']+"Dst2PiD02"+combname+"_untagged_BoxMBTrEff",
                                              HLT = "HLT_PASS_RE('Hlt2CharmHadMinBiasD02KPiDecision')",
                                              algos = [ xxCombSel ], prescale = config[ pres+"MBTrEff" ])
        else :
            line_untagged_box = StrippingLine(name+config['prefix']+"Dst2PiD02"+combname+"_untagged_Box",
                                              HLT = "HLT_PASS_RE('"+hltname+"')",
                                              algos = [ xxCombSel ], prescale = config[ pres ])

        return line_untagged_box    
    
    def my_lines ( self , name, config) :
        """
        Builds all of the lines
        """

        # Untagged lines
       
        line_pipi_box = self.baseLine(name,config,"pi", "pi")
        line_mumu_box = self.baseLine(name,config,"mu", "mu")
        line_Kpi_box  = self.baseLine(name,config,"K",  "pi")
        #line_eK_box   = self.baseLine(name,config,"e",   "K")
        #line_epi_box  = self.baseLine(name,config,"e",   "pi")
        line_mue_box  = self.baseLine(name,config,"e",  "mu")
        #line_pimu_box = self.baseLine(name,config,"pi", "mu")
        line_Kmu_box  = self.baseLine(name,config,"K",  "mu")


        # Tagged lines
        
        line_mumu_untagged_box  = self.baseLine_untagged(name,config,"mu",  "mu", 0)
        line_Kmu_untagged_box  = self.baseLine_untagged(name,config,"K",  "mu" ,  0)
        line_pipi_untagged_box  = self.baseLine_untagged(name,config,"pi",  "pi", 0)
        line_Kpi_untagged_box  = self.baseLine_untagged(name,config,"K",  "pi",   0)
        #line_pimu_untagged_box = self.baseLine_untagged(name,config,"pi", "mu")


        # Untagged minimum bias lines for trigger efficiency estimate
        
        line_Kpi_minbias =  self.baseLine_untagged(name,config,"K",  "pi",   1)
        line_pipi_minbias =  self.baseLine_untagged(name,config,"pi",  "pi", 1)
        
        line_Kpi_minbias_treff =  self.baseLine_untagged(name,config,"K",  "pi",   2)
        
        lines = [line_pipi_box,  line_mumu_box, line_Kpi_box, line_mue_box, line_Kmu_box,line_mumu_untagged_box ,line_Kmu_untagged_box, line_pipi_untagged_box,line_Kpi_untagged_box, line_Kpi_minbias, line_pipi_minbias,  line_Kpi_minbias_treff]
        
        return lines
    







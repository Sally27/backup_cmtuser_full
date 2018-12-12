import sys,os

logfile =  os.path.dirname(os.path.abspath(sys.argv[0]))+"/decparse.log"
enable_colours = True
overwrite = True
dkfilespath =  os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../dkfiles/"
obsoletepath =  os.path.dirname(os.path.abspath(sys.argv[0]))+"/../../doc/"
partdictpath =  os.path.dirname(os.path.abspath(sys.argv[0]))+"/particle_dictionary"


use_url  = True
dec_url  = "http://lhcb-release-area.web.cern.ch/LHCb-release-area/DOC/decfiles/"
obs_url  = "https://svnweb.cern.ch/trac/lhcb/browser/DBASE/trunk/Gen/DecFiles/doc/table_obsolete.sql?format=txt"
cuts_url = "https://svnweb.cern.ch/trac/lhcb/browser/Gauss/trunk/Gen/GenCuts/src"
#table_url= "http://svn.cern.ch/guest/evtgen/tags/R01-01-00/evt.pdl"
table_url= "http://www2.warwick.ac.uk/fac/sci/physics/staff/academic/kreps/tmp/evt.pdl"

groups = ["Charm",
          "RD",
          "Exotica",
          "Onia",
          "QCD",
          "B2HQ",
          "B2Ch",
          "B2OC",
          "BnoC",
          "B2SL",
          "Calo",
          "PID",
          "Alignment",
          "Tagging",
          "Sim"]

groups_obsolete = ["Charm",
          "Exotics",
          "All",
          "EW",
          "GWT",
          "P&S",
          "RD",
          "GWL",
          "Semileptonics",
          "Calo",
          "BetaS",
          "BnoC",
          ]

terminators = ["VSS",
               "VSS_BMIX",
               "PHOTOS",
               "VLL",
               "VVPIPI",
               "PARTWAVE",
               "HELAMP",
               "PYTHIA",
               "HQET",
               "ISGW2",
               "GOITY_ROBERTS",
               "VUB",
               "PHSP",
               "SVS",
               "SVV_HELAMP",
               "BTOXSGAMMA",
               "BTOSLLBALL",
               "BTOXSLL",
               "BTO3PI_CP",
               "STS",
               "SLN",
               "CB3PI-P00",
               "CB3PI-MPP",
               "VSP_PWAVE",
               "SVP_HELAMP",
               "BTOSLLALI",
               "TAULNUNU",
               "TAUSCALARNU",
               "TAUHADNU",
               "TAUVECTORNU",
               "D_DALITZ",
               "VVS_PWAVE",
               "TVS_PWAVE",
               "TSS",
               "PI0_DALITZ",
               "ETA_DALITZ",
               "OMEGA_DALITZ",
               "VVP",
               "BTOSLLMS",
               "BC_VHAD",
               ]

longlived = ["pi+",
             "pi-",
             "K+",
             "K-",
             "K_L0",
             "p+",
             "anti-p-",
             "n0",
             "anti-n0",
             "e+",
             "e-",
             "mu+",
             "mu-",
             ]

nickslation = { "B0" : "Bd",
                "B+" : "Bu",
                "D*+" : "Dst"
                }

#Obsolete
descripslation = { "D*+" : "D*(2010)+",
                   #"K_S0" : "KS0"
                   }

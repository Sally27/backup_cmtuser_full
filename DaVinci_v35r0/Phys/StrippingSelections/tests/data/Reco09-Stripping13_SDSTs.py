from Gaudi.Configuration import *

EventSelector().Input = [ 
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002581_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'", 
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002595_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'", 
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002662_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002665_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002785_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002930_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002935_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002938_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002942_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002943_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002944_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002945_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",        
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002946_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'", 
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002952_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002953_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002957_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002959_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00002962_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00003005_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00003043_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00003044_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00003045_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'",
    "DATAFILE='LFN:/lhcb/LHCb/Collision11/SDST/00010035/0000/00010035_00003110_1.sdst' TYP='POOL_ROOTTREE' OPT='READ'" 
    ]

FileCatalog().Catalogs = [ 'xmlcatalog_file:out.xml',
                           'xmlcatalog_file:$STRIPPINGSELECTIONSROOT/tests/data/pool_xml_catalog_reco09_stripping13.xml' ]

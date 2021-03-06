##  -*- python -*-  
# db file automatically generated by genconf on: Sun Mar 13 16:12:57 2016## insulates outside world against anything bad that could happen
## also prevents global scope pollution
def _fillCfgDb():
    from GaudiKernel.Proxy.ConfigurableDb import CfgDb

    # get a handle on the repository of Configurables
    cfgDb = CfgDb()

    # populate the repository with informations on Configurables 

    cfgDb.add( configurable = 'TupleToolAngles',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolApplyPiMuIsolation',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolApplypMuIsolation',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolBremInfo',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolCaloHypo',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolDecayTreeFitter',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolDira',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolGeometry',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolIsolationTwoBody',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolKinematic',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolMassHypo',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolNeutrinoReco',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolP2VV',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolParticleReFit',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolParticleStats',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolPhotonInfo',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolPi0Info',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolPid',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolPropertime',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolSallyvs3',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolSelResults',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolSubMass',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolSwimmingInfo',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolTagging',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexMisIDmu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexMisMuMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexMismpMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexMispmMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexMisppMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexMuMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexPions',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexXmu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexXmutrial',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexmpMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexpmMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVertexppMuMu',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVeto',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    cfgDb.add( configurable = 'TupleToolVtxIsoln',
               package = 'DecayTreeTuple',
               module  = 'DecayTreeTuple.DecayTreeTupleConf',
               lib     = 'DecayTreeTuple' )
    return #_fillCfgDb
# fill cfgDb at module import...
try:
    _fillCfgDb()
    #house cleaning...
    del _fillCfgDb
except Exception,err:
    print "Py:ConfigurableDb   ERROR Problem with [%s] content!" % __name__
    print "Py:ConfigurableDb   ERROR",err
    print "Py:ConfigurableDb   ERROR   ==> culprit is package [DecayTreeTuple] !"

import PartProp.PartPropSvc
 
from GaudiPython.Bindings import AppMgr 

gaudi = AppMgr()

# get the service from Gaudi:
ppSvc = gaudi.ppSvc() 

p1 = ppSvc.find( 'B+' ) 
# find particle property by PID
#pid = LHCb.ParticleID( 511 )
#p2  = ppsvc.find ( pid ) 

print p1

# loop over all particle properties:
#for pp in ppSvc :  print pp.particle()
  
# print them as table:
print ppSvc.all() 


# 
#
# EventType: 12513060
#
# Descriptor: [B+ -> mu+ mu- (W+ -> mu+ nu_mu)]cc
#
# NickName: Bu_Kstmumu,munu=DecProdCut
#
# Cuts: DaughtersInLHCb
#
#
#
#
#
# Documentation: Kst+ forced to mu+ nu_mu
# EndDocumentation
#
# PhysicsWG: RD
# Tested: Yes
# Responsible: Slavomira Stefkova
# Email: s.stefkova14@imperial.ac.uk
# Date: 20150408
#
Alias      MyW+    W+
Alias      MyW-    W-
ChargeConj MyW+    MyW-
#
Decay B+
  1.000        MyW+     mu+     mu-     BTOSLLBALL;
Enddecay
CDecay B-
#
Decay MyW+
  1.000        mu+      nu_mu             PHSP;
Enddecay
CDecay MyW-
#
End
#

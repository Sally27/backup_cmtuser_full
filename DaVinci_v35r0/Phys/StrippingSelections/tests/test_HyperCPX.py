#!/usr/bin/env python
# =============================================================================
# $Id: test_HyperCPX.py 122310 2011-04-20 18:57:46Z ibelyaev $
# =============================================================================
## @file test_HyperCPX.py
#  helper script to test HyperCPXConf-configurabloid
#  @author Vanya BELYAEV Ivan.Belyaev@cern.ch
#  @date 2011-04-20
#
#                    $Revision: 122310 $
#  Last modification $Date: 2011-04-20 19:57:46 +0100 (Wed, 20 Apr 2011) $
#                 by $Author: ibelyaev $
# =============================================================================
"""
Helper script to test HyperCPXConf-configurabloid
"""
# =============================================================================
__author__  = 'Vanya BELYAEV Ivan.Belyaev@cern.ch'
__date__    = '2011-04-20'
__version__ = '$Revision: 122310 $'
# =============================================================================

from StrippingUtils import LineBuilderTests

from StrippingSelections.StrippingHyperCPX import HyperCPXConf as builder

# =============================================================================
## the actual function to test stripping configurabloid 
def test_line_builder() :
    """
    The actual function to test stripping configurabloid 
    """
    LineBuilderTests.test_line_builder(builder, builder.defaultConfiguration() )
    
# =============================================================================
if __name__ == '__main__' :
    
    test_line_builder()
    
# =============================================================================
# The END 
# =============================================================================


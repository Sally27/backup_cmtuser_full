#!/usr/bin/env python

from StrippingUtils import LineBuilderTests
from StrippingSelections.StrippingInclPhi import InclPhiConf as builder

config_params = builder.config_default

def test_line_builder() :
    LineBuilderTests.test_line_builder(builder, config_params)

if __name__ == '__main__' :
    
    test_line_builder()

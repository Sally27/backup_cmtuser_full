#!/usr/bin/env python

from StrippingSelections.StrippingB0q2DplusMuX import B0q2DplusMuXAllLinesConf as builder

from StrippingSelections.StrippingB0q2DplusMuX import confdict as config_params

from StrippingUtils import LineBuilderTests

def test_line_builder() :
    LineBuilderTests.test_line_builder(builder, config_params)

if __name__ == '__main__' :
    
    test_line_builder()

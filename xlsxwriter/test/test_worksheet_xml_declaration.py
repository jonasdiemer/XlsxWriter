###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013, John McNamara, jmcnamara@cpan.org
#

import unittest
from StringIO  import StringIO
from ..worksheet import Worksheet

class TestWorksheetXmlDeclaration(unittest.TestCase):
    """Test initialisation of the Worksheet class and call a method."""


    def setUp(self):
        self.fh       = StringIO()
        self.instance = Worksheet(self.fh)


    def test_xml_declaration(self):
        """Test Worksheet xml_declaration()"""

        self.instance.xml_declaration()

        expected = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n"""
        got      = self.fh.getvalue()

        self.assertEqual(got, expected)


if __name__ == '__main__':
    unittest.main()
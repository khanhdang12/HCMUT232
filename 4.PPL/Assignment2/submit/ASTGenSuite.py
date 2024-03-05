
import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test(self):
        input = """
            number ck12
        """
        expect = str(Program([
                VarDecl(Id("ck12"), NumberType())
            ]))
        self.assertTrue(TestAST.test(input, expect, 301))
from ..service.criador import Criador
import unittest

class TestaCriador(unittest.TestCase):
    def testCriadorShouldReturnInstanceOfBuilderUm(self):
        builder = Criador()
        builder.build('builderum')
        self.assertEquals(builder.getInstance(),'builderUm')
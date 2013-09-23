import ipdb; ipdb.set_trace()

class Criador:
    instance = None

    def build(self,builderName):
        modulo = __import__('service.builderum',level=-1)
        class_ = getattr(modulo, class_name)
        self.instance = class_()

    def getInstance():
        return getattr(self.instance, class_name)
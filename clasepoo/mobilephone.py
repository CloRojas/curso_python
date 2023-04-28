class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = False
        self.apps = []

    def power_on(self):
        self.status  = True
        print('Celular encendido')
    
    def power_off(self):
        self.status = False
        print('Celular apagado')
    
    # def install_app(self,app):
        
    
    # def uninstall_app(self,app):

 

miphone = MobilePhone('China', 6.7, 8)
print('Celular:', miphone, ': Fabricado en', miphone.manufacturer , ', tamaño pantalla:', miphone.screen_size , 'pulgadas, procesador:', miphone.num_cores , 'nucleos')
miphone.power_on()
miphone.power_off()

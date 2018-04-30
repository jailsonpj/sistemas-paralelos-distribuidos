import Pyro4

@Pyro4.expose
class Hello(object):
	def say_hello(self):
		return 'Hello Word!'

daemon = Pyro4.Daemon()			#cria um daemon do Pyro
ns = Pyro4.locateNS()			#Procura o servidor DNS
uri = daemon.register(Hello)	#registra Hello no Pyro
ns.register("example.hello",uri)#registra Hello no servidor DNS

print("Servidor Pronto.")
daemon.requestLoop()			#inicia e espera por chamadas

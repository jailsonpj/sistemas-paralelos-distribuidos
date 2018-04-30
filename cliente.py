import Pyro4

#localiza o objeto no servidor DNS
Hello = Pyro4.Proxy("PYRONAME:example.hello")

#executa o metodo do objeto Distribuido
print(Hello.say_hello())
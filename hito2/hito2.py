from mininet.topo import Topo

class Hito2( Topo ):
    def __init__( self ):
        # Inicializar topologia
        Topo.__init__( self )
        # Agregar hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        # Agregar switches
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        # Agregar enlaces
        # Subarbol izquierdo
        self.addLink(s1,h1)
        self.addLink(s1,h2)
        # Subarbol central
        self.addLink(s2,s4)
        self.addLink(s2,s5)
        self.addLink(s4,h3)
        self.addLink(s5,h4)
        #Subarbol derecho
        self.addLink(s3,s6)
        self.addLink(s6,h5)
        self.addLink(s6,h6)
        self.addLink(s3,h7)
       

topos = { 'hito2': ( lambda: Hito2() )} 

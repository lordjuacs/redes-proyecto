py "Arbol izquierdo"
py "h1 --> h2"
h1 ping -c 4 h2
py "h2 --> h1"
h2 ping -c 4 h1

py "Arbol central"
py "h3 --> h4"
h3 ping -c 4 h4
py "h4 --> h3"
h4 ping -c 4 h3

py "Arbol derecho"
py "h5 --> h6"
h5 ping -c 4 h6
py "h5 --> h7"
h5 ping -c 4 h7
py "h6 --> h5"
h6 ping -c 4 h5
py "h6 --> h7"
h6 ping -c 4 h7
py "h7 --> h5"
h7 ping -c 4 h5
py "h7 --> h6"
h7 ping -c 4 h6

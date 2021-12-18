py "Hosts imposibles de conectar"
py "h1 --> h3"
h1 ping -c 4 h3
py "h3 --> h1"
h3 ping -c 4 h1

py "h4 --> h5"
h4 ping -c 4 h5
py "h5 --> h4"
h5 ping -c 4 h4

py "h7 --> h2"
h7 ping -c 4 h2
py "h2 --> h7"
h2 ping -c 4 h7

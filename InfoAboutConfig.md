<- Pc , Switch , Router

- Pc , Switch , Router
  -> Pc , Switch , Router
  <- ((serial0/0/0)1.1.1.2|1.1.1.1(serial0/0/0)) \*
  <- enable , configure terminal , int serial0/0/0 , ip address 1.1.1.2 255.255.255.0 , no shutdown
- enable, configure terminal, int serial0/0/0, ip address 1.1.1.1 255.255.255.0, no shutdown
- ((serial0/0/1)2.2.2.1|2.2.2.2(serial0/0/1)) ->
  -> enable, configure terminal, int serial0/0/1, ip address 2.2.2.2 255.255.255.0, no shutdown
- enable, configure terminal, int serial0/0/1, ip address 2.2.2.1 255.255.255.0 , no shutdown
  <- Pc : 192.168.10.10, 255.255.255.0, 192.168.10.1
  \*^ Pc : 192.168.20.20, 255.255.255.0, 192.168.20.1
  -> Pc : 192.168.30.30, 255.255.255.0, 192.168.30.1
  <- Router : enable, configure terminal, int gi0/0, ip address 192.168.10.1 255.255.255.0, no sh
- Router : enable, configure terminal, int gi0/0, ip address 192.168.20.1 255.255.255.0, no sh
  -> Router : enable, configure terminal, int gi0/0, ip address 192.168.30.1 255.255.255.0, no sh
  <- Router : enable, configure terminal, router rip, version 2, network 1.1.1.0, network 192.168.10.0
- Router : enable, configure terminal, router rip, version 2, network 1.1.1.0, network 2.2.2.0, network 192.168.20.0
  -> Router : enable, configure terminal, router rip, version 2, network 2.2.2.0, network 192.168.30.0
  All : wr
  Switchlere rip 2 paket gönderimini engelleme :
  All : en, conf t, router rip, ver 2, passive-interface gi0/0
  Default rota oluşturma (küçük rip 2 yapılandırmasında geçerli) :
- : en, conf t, ip route 0.0.0.0 0.0.0.0 244.132.211.24
- : router rip, ver 2, default-information originate

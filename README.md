## io-manager 

馃敆 https://github.com/Lebackrobot/io-manager

Com o intuito de integrar o sheduler com a probabilidade de processos de requisitar entrata e sa铆da, foi desenvolvido 
um pequeno "escalonador" no qual processos, agora, tem a probabilidade de requisitar opera莽玫es de entrada e sa铆da.

## Arquitetura do C贸digo
O c贸digo foi organizado seguindo a seguinte arquitetura

 馃搧 models /cpu.py         <br>
  &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /device.py      <br>
  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /sheduler.py    <br>
  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /process.py     <br>
   
 馃搧 view / view.py     <br>
 馃摑 main.py
 
## Entendendo um pouco mais dos m贸dulos
<h3>Devices</h3>
Classe que representa dos dispositivos 

<h3>Process</h3>
Classe dos Processos
 

<h3>Sheduler</h3>
Classe do escalonador



## Depend锚ncias
Antes de executar o c贸digo, 茅 necess谩rio instalar a biblioteca <strong>Prettytable</strong>, utilizada para printar tabelas. Para isso, basta:
```console
fulano@pc:~$ python3 -m pip install -U prettytable
```

## Executando o c贸digo
Para executar o c贸digo, n茫o tem segredo. 脡 mandar no terminal (estando no diret贸rio do projeto):

```console
fulano@pc:~$ python3 main.py
```

## Saidas 

![Screenshot from 2022-12-08 02-21-59](https://user-images.githubusercontent.com/49316490/206363351-2b76ae7f-b643-462e-9bd2-7aab14068480.png)

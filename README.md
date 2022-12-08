## io-manager 

🔗 https://github.com/Lebackrobot/io-manager

Com o intuito de integrar o sheduler com a probabilidade de processos de requisitar entrata e saída, foi desenvolvido 
um pequeno "escalonador" no qual processos, agora, tem a probabilidade de requisitar operações de entrada e saída.

## Arquitetura do Código
O código foi organizado seguindo a seguinte arquitetura

 📁 models /cpu.py         <br>
  &nbsp;&nbsp; &nbsp; &nbsp;&nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /device.py      <br>
  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /sheduler.py    <br>
  &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; /process.py     <br>
   
 📁 view / view.py     <br>
 📝 main.py
 
## Entendendo um pouco mais dos módulos
<h3>Devices</h3>
Classe que representa dos dispositivos 

<h3>Process</h3>
Classe dos Processos
 

<h3>Sheduler</h3>
Classe do escalonador



## Dependências
Antes de executar o código, é necessário instalar a biblioteca <strong>Prettytable</strong>, utilizada para printar tabelas. Para isso, basta:
```console
fulano@pc:~$ python3 -m pip install -U prettytable
```

## Executando o código
Para executar o código, não tem segredo. É mandar no terminal (estando no diretório do projeto):

```console
fulano@pc:~$ python3 main.py
```

## Saidas 

![Screenshot from 2022-12-08 02-21-59](https://user-images.githubusercontent.com/49316490/206363351-2b76ae7f-b643-462e-9bd2-7aab14068480.png)

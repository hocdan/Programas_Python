from Objetos import *

#simulando a utilizaca do modulo Objetos

jogador = Heroi('Israel', 1, 0, 10, 3, 5)

jogador.verPerfil()
jogador.verTitulos()
jogador.verEquipamento()
jogador.verInventario()

jogador.adicionarTitulo("Menino do Codo")
jogador.mudarTitulo("Menino do Codo")

jogador.ganharXp(110)
jogador.adicionarMoedas(64)
jogador.removerMoedas(10)

jogador.perderVida()
print("Ocorreu um ataque de {} DMG".format(jogador.atacar()))

jogador.verPerfil()

item1 = Item('Pocao de Vida', 'Um líquido vermelho de sabor amargo.', 'Curar')
item2 = Item('Pocao de Ataque', 'Um líquido amarelo de sabor apimentado.', 'Buff')
item3 = Item('Antidoto', 'Um composto de ervas aromatico.', 'Reparar')
item4 = Item('Veneno', 'Basta um frasco para fazer efeito.', 'Debuff')

elmo = Equipamento('Cabeca', 'Elmo Sagrado', 'Um artefato dado pelos deuses ao humanos mais fieis.', 3, 6, 'Divino')
peitoral = Equipamento('Peito', 'Cota de Malha', ' Uma dupla camada de ferro entrelacado. Muito usado por gladiadores nas arenas...', 1, 0, 'Comum')
luvas = Equipamento('Maos', 'Luvas do Surrupiador', 'Pertenciam ao grande heroi ladino Esfisus.', 1, 5, 'Heroico')
calcas = Equipamento('Pernas', 'Saia grega', 'Estilosa e perfeita para os dias quentes!', 0, 1, 'Comum')
botas = Equipamento('Pes', 'Botas Saltitantes', 'Com um mecanismo revolucionario de molas ao seu favor!\nCriador desconhecido', 0, 2, 'Incomum')
espada = Equipamento('Arma', 'Katana Yin Yun', 'Fabricada pelo melhores ferreiros do Leste, digna de lendas.', 2, 4, 'Epico')
amuleto = Equipamento('Amuleto', 'Joia da Coroa', 'De valor inestimavel e brilho hipnotizante...', 2, 2, 'Raro')
anel1 = Equipamento('Anel', 'Dedo do Necromante', 'Muitos ja ousaram utilizar, poucos conseguiram manter no dedo...', 0, 4, 'Sobrenatural')
anel2 = Equipamento('Anel', 'Alianca de Casamento', 'Dado na tradicao dos humanos, sinal de fidelidade e comprometimento.', 2, 1, 'Comum')

jogador.adicionarItem(item1)
jogador.adicionarItem(item2)
jogador.adicionarItem(elmo)
jogador.adicionarItem(peitoral)
jogador.adicionarItem(luvas)
jogador.adicionarItem(calcas)
jogador.adicionarItem(botas)
jogador.adicionarItem(espada)
jogador.adicionarItem(amuleto)
jogador.adicionarItem(anel1)
jogador.adicionarItem(anel2)

jogador.verEquipamento()
jogador.verInventario()

jogador.equiparArmamento(0, elmo)
jogador.equiparArmamento(1, peitoral)
jogador.equiparArmamento(2, luvas)
jogador.equiparArmamento(3, calcas)
jogador.equiparArmamento(4, botas)
jogador.equiparArmamento(5, espada)
jogador.equiparArmamento(6, amuleto)
jogador.equiparArmamento(7, anel1)

jogador.verPerfil()
jogador.verEquipamento()
jogador.verInventario()

jogador.retirarArmamento(2)
jogador.retirarArmamento(7)
jogador.equiparArmamento(7, anel2)
jogador.adicionarTitulo("O terror das novinhas")
jogador.mudarTitulo("O terror das novinhas")
jogador.adicionarItem(item3)
jogador.adicionarItem(item4)

jogador.verPerfil()
jogador.verTitulos()
jogador.verEquipamento()
jogador.verInventario()


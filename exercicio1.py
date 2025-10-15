from typing import Dict
aluno0 = str(input("Digite o nome do primeiro aluno:"))
nota0 = float(input("Digite a nota do primeiro aluno:"))

aluno1 = str(input("Digite o nome do segundo aluno:"))
nota1 = float(input("Digite a nota do segundo aluno:"))

aluno2 = str(input("Digite o nome do terceiro aluno:"))
nota2 = float(input("Digite a nota do terceiro aluno:"))

aluno3 = str(input("Digite o nome do quarto aluno:"))
nota3 = float(input("Digite a nota do quarto aluno:"))

aluno4 = str(input("Digite o nome do quinto aluno:"))
nota4 = float(input("Digite a nota do quinto aluno:"))

aluno5 = str(input("Digite o nome do sexto aluno:"))
nota5 = float(input("Digite a nota do sexto aluno:"))

aluno6 = str(input("Digite o nome do sétimo aluno:"))
nota6 = float(input("Digite a nota do sétimo aluno:"))

aluno7= str(input("Digite o nome do oitavo aluno:"))
nota7= float(input("Digite a nota do oitavo aluno:"))

aluno8 = str(input("Digite o nome do nono aluno:"))
nota8= float(input("Digite a nota do nono aluno:"))

aluno9 = str(input("Digite o nome do décimo aluno:"))
nota9 = float(input("Digite a nota do décimo aluno:"))

nota = dict ([(1,nota0),(2, nota1),(3, nota2),(4,nota3),(5,nota4),(6,nota5),(7,nota6),(8,nota7),(9,nota8),(10,nota9)])
alunos = dict ([(1,aluno0),(2, aluno1),(3, aluno2),(4,aluno3),(5,aluno4),(6,aluno5),(7,aluno6),(8,aluno7),(9,aluno8),(10,aluno9)])
notas = [nota0, nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9]
aluno = [aluno0, aluno1, aluno2, aluno3, aluno4, aluno5, aluno6, aluno7, aluno8, aluno9]

mediacrua =(nota0 + nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9)/10
media = round(mediacrua,2)
print("a média é: ", media)

maxima = max(notas)
minima = min(notas)

if maxima == nota0:
  print("a nota máxima e o aluno são respectivamente:",nota.get(1), alunos.get(1))
if maxima == nota1:
  print("a nota máxima e o aluno são respectivamente:",nota.get(2), alunos.get(2))
if maxima == nota2:
  print("a nota máxima e o aluno são respectivamente:", nota.get(3), alunos.get(3))
if maxima == nota3:
  print("a nota máxima e o aluno são respectivamente:", nota.get(4), alunos.get(4))
if maxima == nota4:
  print("a nota máxima e o aluno são respectivamente:", nota.get(5), alunos.get(5))
if maxima == nota5:
  print("a nota máxima e o aluno são respectivamente:", nota.get(6), alunos.get(6))
if maxima == nota6:
  print("a nota máxima e o aluno são respectivamente:", nota.get(7), alunos.get(7))
if maxima == nota7:
  print("a nota máxima e o aluno são respectivamente:", nota.get(8), alunos.get(8))
if maxima == nota8:
  print("a nota máxima e o aluno são respectivamente:", nota.get(9), alunos.get(9))
if maxima == nota9:
  print("a nota máxima e o aluno são respectivamente:", nota.get(10), alunos.get(10))

if minima == nota0:
  print("a menor nota e o aluno são respectivamente:", nota.get(1), alunos.get(1))
if minima == nota1:
  print("a menor nota e o aluno são respectivamente:", nota.get(2), alunos.get(2))
if minima == nota2:
  print("a menor nota e o aluno são respectivamente:", nota.get(3), alunos.get(3))
if minima == nota3:
  print("a menor nota e o aluno são respectivamente:", nota.get(4), alunos.get(4))
if minima == nota4:
  print("a menor nota e o aluno são respectivamente:", nota.get(5), alunos.get(5))
if minima == nota5:
  print("a menor nota e o aluno são respectivamente:", nota.get(6), alunos.get(6))
if minima == nota6:
  print("a menor nota e o aluno são respectivamente:", nota.get(7), alunos.get(7))
if minima == nota7:
  print("a menor nota e o aluno são respectivamente:", nota.get(8), alunos.get(8))
if minima == nota8:
  print("a menor nota e o aluno são respectivamente:", nota.get(9), alunos.get(9))
if minima == nota9:
  print("a menor nota e o aluno são respectivamente:", nota.get(10), alunos.get(10))

abaixo = []
acima = []

if nota0 >= media:
  acima.append(aluno0)
if nota0 < media:
  abaixo.append(aluno0)
if nota1 >= media:
  acima.append(aluno1)
if nota1 < media:
  abaixo.append(aluno1)
if nota2 >= media:
  acima.append(aluno2)
if nota2 < media:
  abaixo.append(aluno2)
if nota3 >= media:
  acima.append(aluno3)
if nota3 < media:
  abaixo.append(aluno3)
if nota4 >= media:
  acima.append(aluno4)
if nota4 < media:
  abaixo.append(aluno4)
if nota5 >= media:
  acima.append(aluno5)
if nota5 < media:
  abaixo.append(aluno5)
if nota6 >= media:
  acima.append(aluno6)
if nota6 < media:
  abaixo.append(aluno6)
if nota7 >= media:
  acima.append(aluno7)
if nota7 < media:
  abaixo.append(aluno7)
if nota8 >= media:
  acima.append(aluno8)
if nota8 < media:
  abaixo.append(aluno8)
if nota9 >= media:
  acima.append(aluno9)
if nota9 < media:
  abaixo.append(aluno9)

print("notas abaixo da media", abaixo)
print("notas acima da media", acima)

# Organização do Projeto
## Organização das Tarefas

### Programas
#### Main
1. readPWF - run the base case
2. readREL - read the report created
3. cpflowGen - generated cpflow with varied growth factors
4. cpflowSimulation - run all the cpflows
5. readPV - read all plots created
6. write all data in a csv (or another option)
7. create training data and test data

#### readPWF
1. Ler um arquivo PWF
  1. ~~Encontra nome dos arquivos .his e .rel gerados~~
  2. ~~Encontra número de barras~~
  3. ~~Pega dados de cada barra~~
  3. ~~Roda simulação no ANAREDE~~
  2. ~~Move arquivos para pasta de trabalho~~

#### readREL
0. ~~Executar o pwf para gerar REL~~
1. ~~Ler o arquivo REL e pegar dados~~
  1. Modulo tensão
  2. Angulo da barra
  3. Dados de geração
  4. Dados de carga

#### cpflowGen
1. ~~Generate files variying PF~~
  1. Change PF

#### readPV
1. ~~Ler o arquivo plt~~
2. ~~Descartar barras de geração~~
3. ~~Pegar margem de carregamento~~
  1. Achar ponto de máximo ou minímo no eixo y
4. ~~Pegar tensao crítica~~

#### cpflowSimulation
1. Get all folders generated in cpflowGen
2. Simulate the cases in each folder
3. Move the created files to each folder
4. Run readPV inside each folder

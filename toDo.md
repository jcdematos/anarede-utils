# Organização do Projeto
## Organização das Tarefas

### Python Programs
#### pvPlot
* Descartar barras de geração
#### readREL
* Find type of the bars
* Read voltage of each bar
* Read the angle of each bar
* Read the generation for PQ e V0 bars
* Read the load for each bar
* Read the shunt of each bar

# Ideia do Algoritmo
0. Executar o pwf para gerar REL
1. Ler o arquivo REL e pegar dados das barras
2. Executar o pwf de CPFLOW
3. Ler o arquivo plt
  1. Descartar barras de geração
  2. Pegar margem de carregamento
  3. Pegar tensao crítica

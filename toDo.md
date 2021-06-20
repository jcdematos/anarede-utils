# Organização do Projeto
## Organização das Tarefas

### Programas
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
1. Generate files variying PF
  1. Change PF
2. Executar o pwf de CPFLOW
3. Ler o arquivo plt
  1. Descartar barras de geração
  2. Pegar margem de carregamento
  3. Pegar tensao crítica

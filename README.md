# Análise de Dados de COVID-19

## Descrição

Este projeto tem como objetivo analisar os dados globais e regionais relacionados à pandemia de COVID-19. A análise inclui visualizações e insights sobre a evolução da pandemia, como o número de casos confirmados, recuperados, óbitos e taxa de vacinação. O projeto visa fornecer uma visão abrangente e acessível para compreender o impacto do COVID-19 em diferentes locais e ao longo do tempo.

## Funcionalidades

- Importação de dados de COVID-19 em formato CSV ou de APIs públicas.
- Cálculo de métricas como total de casos, número de óbitos, taxa de recuperação e vacinas administradas.
- Análise temporal para ver a evolução dos dados ao longo dos dias.
- Comparação entre diferentes países ou estados.
- Geração de gráficos interativos e visualizações sobre a propagação do vírus, vacinação e taxas de mortalidade.

## Pré-requisitos

1. Certifique-se de ter os seguintes requisitos instalados no seu ambiente:

    - Python 3.7 ou superior.
    - Bibliotecas necessárias:
        - pandas
        - matplotlib
        - seaborn
        - requests (caso queira obter dados da API)

2. Você pode instalar as dependências utilizando o comando:

```bash
    pip install pandas matplotlib seaborn requests
```


## Como Usar

1. Clone este repositório:

```bash
    git clone https://github.com/LuiSilvak/COVID-19_Data_Analysis.git
    cd COVID-19_Data_Analysis
```

2. Certifique-se de ter um arquivo CSV ou link para a API contendo os dados de COVID-19. O arquivo ou API deve conter, no mínimo, as seguintes colunas:

    - Data
    - País
    - Casos_Confirmados
    - Óbitos
    - Recuperados
    - Vacinas_Administradas

3. Exemplo de formato do arquivo:

```bash
    Data,País,Casos_Confirmados,Óbitos,Recuperados,Vacinas_Administradas
    2025-01-01,Brasil,1000000,30000,950000,2000000
    2025-01-01,Estados Unidos,1500000,50000,1400000,5000000
    2025-01-01,Índia,1200000,40000,1100000,3000000
```

4. Execute o script principal:

```bash
    python COVID-19_Data_Analysis.py
```

5. Visualize as saídas no console e nos gráficos gerados.

## Exemplo de Saída

1. Estatísticas Sumarizadas:

```bash
    Total de Casos Confirmados: 3700000
    Total de Óbitos: 120000
    Total de Recuperados: 3550000
    Total de Vacinas Administradas: 10000000
```

2. Gráficos Gerados:
    - Gráfico de linha mostrando a evolução diária de casos confirmados, óbitos e recuperados.
    - Gráfico de barras comparando o número de casos por país.
    - Gráfico de pizza com a distribuição de vacinas administradas entre os países.
    - Gráfico de barras mostrando a taxa de mortalidade por país.

## Estrutura do Projeto

```bash
    COVID-19_Data_Analysis/
    │
    ├── COVID-19_Data_Analysis.py      # Script principal
    ├── exemplos/
        └── exemplo_covid19.csv        # Exemplo de arquivo de dados (Caso queira usar um arquivo de dados csv)
        └── gerar_arquivo.py           # Programa gerador de arquivo de dados
    └── README.md                      # Documentação do projeto
```

## Expansões Futuras

- Análise de impacto de variantes do vírus em diferentes regiões.
- Previsão de futuros casos e óbitos com base em modelos de aprendizado de máquina.
- Análise de dados de vacinação e a relação com a diminuição de novos casos e óbitos.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e novas funcionalidades.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo LICENSE para mais informações.


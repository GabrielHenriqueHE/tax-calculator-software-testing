# TaxCalculator


# Fórmulas

## Base de cálculo do ICMS

- Valor do produto
- Valor do IPI
- Valor do frete
- Valor de outras despesas acessórias
- Valor do seguro
- Valor do desconto

- **Fórmula:** `Base de cálculo = Valor do produto + Valor do IPI (se incluído) + Valor do frete (se por conta) + Valor outras desp. acessórias + Seguro - Desconto`

## Valor do ICMS

### Base de cálculo normal

- **Fórmula:** `Base de cálculo * (Alíquota / 100)`

```
Valor do ICMS: 100 * (18/100) = R$18,00
```

### Base de cálculo reduzida

- **Fórmula:** `Base de cálculo * (1 - Red. BC / 100)) * (Alíquota / 100)`

```
Valor do ICMS: 100 * (1 - 20/100) * (18/100) = 100 * 0.8 * 0.18
Valor do ICMS: 80 * 0.18 = R$14,40
```

## Base de cálculo do ICMS-ST

- Valor do IPI
- Valor do frete
- Valor de outras despesas acessórias
- Valor do seguro
- Valor do desconto
- **Valor do produto:** refere-se ao preço de venda do produto pelo fabricante ou distribuidor, excluindo o imposto;
- **MVA (Margem de valor agregado):** é um percentual definido pela legislação para cada tipo de produto. Seu objetivo é estimar o incremento de valor que o produto experimentará até a venda ao consumidor final;
- **Base de cálculo do ICMS-ST:** resulta da soma do valor do produto e os outros valores, com o acréscimo calculado pela aplicação do MVA;
- **Fórmula:** `Base de cálculo do ICMS-ST = Valor do produto * (1 + MVA/100)`

## Exemplo

#### Tabela de produtos (alíquota base interna e MVA)

| Código do produto | Descrição | Alíquota interna | MVA |
| :------------ | :------------ | :------------ | :------------ |
| 001 | Fertilizante A | 12% | 40% |
| 002 | Defensivo B | 12% | 30% |

#### Tabela de lançamento de saída de produtos (com base nos estados)

| Código do produto | Estado de destino | Alíquota interestedual | Valor do produto |
| :------------ | :------------ | :------------ | :------------ |
| 001 | SP | 7% | R$10.000 |
| 002 | MG | 12% | R$20.000 |

```
Para o Fertilizante A: R$ 10.000,00 * (1 + 40/100)
= R$ 10.000,00 * 1.40 = R$ 14.000,00.
```

[Fonte: Dattos](https://www.dattos.com.br/blog/calculo-de-icms-st/)

## Valor do ICMS-ST

### ICMS-ST a ser pago ao estado de origem

- **Fórmula:** `ICMS Origem = Valor do produto * Alíquota interestadual`

#### Exemplo

```
Para o Fertilizante A: R$ 10.000,00 * 7% = R$ 700,00.
```

### ICMS-ST a ser pago ao estado de destino

- **Fórmula:** `Base de cálculo * Alíquota interna - ICMS origem`

#### Exemplo
```
Para o Fertilizante A: R$ 14.000,00 * 12% – R$ 700,00

= R$ 1.680 – R$ 700,00 = R$ 980,00.
```

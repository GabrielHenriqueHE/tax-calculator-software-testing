from tax_calculator import TaxCalculator
from utils import read_float, read_int

def run():
    while True:
        __print_menu__()
        while True:
            opt = read_int("Escolha uma opção: ")
        
            match opt:
                case 1:
                    valor_icms = calcular_icms_normal()
                    print(f"Valor ICMS: R${valor_icms}")
                case 2:
                    valor_icms_st = calcular_icms_st()
                    print(f"Valor ICMS-ST: R${valor_icms_st}")
                case 0:
                    return
                case _:
                    print("Opção inválida.")
                    break


def calcular_icms_normal():
    try:
        valor_produto: float = read_float("Insira o valor do produto: R$")
        valor_ipi: float = read_float("Insira o valor do IPI: R$")
        valor_frete: float = read_float("Insira o valor do frete: R$")
        valor_out_desp: float = read_float("Insira o valor das outras despesas acessórias: R$")
        valor_seguro: float = read_float("Insira o valor do seguro: R$")
        valor_desconto: float = read_float("Insira o valor do desconto: R$")
        valor_red_bc: float = read_float("Insira o percentual da redução de base de cálculo: ")
        aliq_icms: float = read_float("Insira o percentual da alíquota de ICMS: ")

        valor_icms = TaxCalculator().calcular_valor_icms(
            valor_produto,
            valor_ipi,
            valor_frete,
            valor_out_desp,
            valor_seguro,
            valor_desconto,
            valor_red_bc,
            aliq_icms
        )

        return valor_icms
    except:
        return 0

def calcular_icms_st():
    try:
        valor_produto: float = read_float("Insira o valor do produto: R$")
        valor_mva: float = read_float("Insira o percentual do MVA: ")
        aliq_interna: float = read_float("Insira o percentual da alíquota interna de ICMS: ")
        aliq_interestadual: float = read_float("Insira o percentual da alíquota interestadual de ICMS: ")
        valor_red_bc: float = read_float("Insira o percentual da redução de base de cálculo: ")
        valor_ipi: float = read_float("Insira o valor do IPI: R$")
        valor_frete: float = read_float("Insira o valor do frete: R$")
        valor_out_desp: float = read_float("Insira o valor das outras despesas acessórias: R$")
        valor_seguro: float = read_float("Insira o valor do seguro: R$")
        valor_desconto: float = read_float("Insira o valor do desconto: R$")

        valor_icms_st = TaxCalculator().calcular_valor_icms_st(
            valor_produto,
            valor_mva,
            aliq_interna,
            aliq_interestadual,
            valor_red_bc,
            valor_ipi,
            valor_frete,
            valor_out_desp,
            valor_seguro,
            valor_desconto
        )

        return valor_icms_st
    except:
        return 0


def __print_menu__():
    menu: str = """
    ======= Calculadora de impostos =======
    [1] Calcular ICMS normal
    [2] Calucular ICMS-ST
    [0] Finalizar programa
    """

    print(menu)

if __name__ == '__main__':
    run()
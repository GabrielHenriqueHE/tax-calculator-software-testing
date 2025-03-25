from tax_calculator import TaxCalculator


def test_calcular_bc_icms():
    tax_calculator = TaxCalculator()

    bc_icms_reduzido = tax_calculator.__calcular_bc_icms__(
        160.0, 0, 0, 0, 0, 0, 20
    )

    assert bc_icms_reduzido == 128.0

def test_calcular_valor_icms():
    
    tax_calculator = TaxCalculator()

    valor_icms_1 = tax_calculator.calcular_valor_icms(
        200, 50, 30, 20, 10, 15, 0, 17
    ) 
    assert valor_icms_1 == 50.15

    valor_icms_2 = tax_calculator.calcular_valor_icms(
        500, 100, 50, 30, 20, 50, 10, 12
    ) 
    assert valor_icms_2 == 70.20

    valor_icms_3 = tax_calculator.calcular_valor_icms(
        750, 150, 100, 50, 25, 75, 20, 18
    ) 
    assert valor_icms_3 == 144.00

    valor_icms_4 = tax_calculator.calcular_valor_icms(
        1000, 200, 150, 80, 40, 100, 25, 15
    ) 
    assert valor_icms_4 == 154.12

    valor_icms_5 = tax_calculator.calcular_valor_icms(
        300, 70, 40, 25, 15, 20, 30, 16
    )
    assert valor_icms_5 == 48.16

def test_calcular_bc_icms_st():
    tax_calculator = TaxCalculator()
    
    bc_icms_st_1 = tax_calculator.__calcular_bc_icms_st__(1000, 50, 0, 100, 25, 30, 10, 0)
    assert bc_icms_st_1 == 1747.50

def test_calcular_valor_icms_st():
    tax_calculator = TaxCalculator()

    valor_icms_st_1 = tax_calculator.calcular_valor_icms_st(1000, 50, 18, 12, 0, 100, 25, 30, 10, 0)
    assert valor_icms_st_1 == 174.75
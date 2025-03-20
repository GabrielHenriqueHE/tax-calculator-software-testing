class TaxCalculator:
    
    def __calcular_bc_icms_normal__(
            valor_produto: float,
            valor_ipi: float,
            valor_frete: float,
            valor_out_desp: float,
            valor_seguro: float,
            valor_desconto: float
    ) -> float:
        
        """
            Calcula a base de cálculo do ICMS normal.
        """

        bc_icms: float = valor_produto + valor_ipi + valor_frete + valor_out_desp + valor_seguro - valor_desconto
        return bc_icms
   
    def __calcular_bc_icms_reduzido__(
            self,
            valor_produto: float,
            valor_ipi: float,
            valor_frete: float,
            valor_out_desp: float,
            valor_seguro: float,
            valor_desconto: float,
            valor_red_bc: float
    ) -> float:
        bc_icms: float = self.__calcular_bc_icms_normal__(
            valor_produto,
            valor_ipi,
            valor_frete,
            valor_out_desp,
            valor_seguro,
            valor_desconto
        )

        return bc_icms * (1 - (valor_red_bc / 100))

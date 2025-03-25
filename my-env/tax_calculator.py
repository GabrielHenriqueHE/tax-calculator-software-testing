class TaxCalculator:
       
    def __calcular_bc_icms__(
        self,
        valor_produto: float,
        valor_ipi: float = 0,
        valor_frete: float = 0,
        valor_out_desp: float = 0,
        valor_seguro: float = 0,
        valor_desconto: float = 0,
        valor_red_bc: float = 0
    ) -> float:
        
        """
            Calcula o valor da base de cálculo do valor de ICMS.
        """
        
        if valor_produto <= 0:
            raise ValueError("Valor inválido para o produto.")
        
        if valor_red_bc < 0:
            raise ValueError("Valor inválido para o percentual de redução de base de cálculo.")
        
        if valor_ipi < 0:
            raise ValueError("Valor inválido para o IPI.")
        
        if valor_frete < 0:
            raise ValueError("Valor inválido para o frete.")
        
        if valor_out_desp < 0:
            raise ValueError("Valor inválido para outras despesas acessórias.")
        
        if valor_desconto < 0:
            raise ValueError("Valor inválido para o desconto.")
   
        bc_icms: float = valor_produto + valor_ipi + valor_frete + valor_out_desp + valor_seguro - valor_desconto
        
        return round(bc_icms, 2) if valor_red_bc == 0 else round(bc_icms * (1 - (valor_red_bc / 100)), 2)
    
    def calcular_valor_icms(
        self,
        valor_produto: float,
        valor_ipi: float,
        valor_frete: float,
        valor_out_desp: float,
        valor_seguro: float,
        valor_desconto: float,
        valor_red_bc: float,
        aliq_icms: float
    ) -> float:
        """
            Calcula o valor do ICMS.
        """

        bc_icms = self.__calcular_bc_icms__(
            valor_produto, 
            valor_ipi, 
            valor_frete, 
            valor_out_desp, 
            valor_seguro, 
            valor_desconto, 
            valor_red_bc
        )

        return round(bc_icms * (aliq_icms / 100), 2)

    def __calcular_bc_icms_st__(
        self,
        valor_produto: float,
        mva: float,
        valor_red_bc: float = 0,
        valor_ipi: float = 0,
        valor_frete: float = 0,
        valor_out_desp: float = 0,
        valor_seguro: float = 0,
        valor_desconto: float = 0,
    ) -> float:
        
        """
            Calcula o valor da base de cálculo do ICMS-ST.
        """

        if mva < 0:
            raise ValueError("Valor inválido para o MVA")
        
        if valor_produto <= 0:
            raise ValueError("Valor inválido para o produto.")
        
        if valor_red_bc < 0:
            raise ValueError("Valor inválido para o percentual de redução de base de cálculo.")
        
        if valor_ipi < 0:
            raise ValueError("Valor inválido para o IPI.")
        
        if valor_frete < 0:
            raise ValueError("Valor inválido para o frete.")
        
        if valor_out_desp < 0:
            raise ValueError("Valor inválido para outras despesas acessórias.")
        
        if valor_desconto < 0:
            raise ValueError("Valor inválido para o desconto.")

        bc_icms_st: float = (valor_produto + valor_ipi + valor_frete + valor_out_desp + valor_seguro - valor_desconto) * (1 + (mva / 100))

        return round(bc_icms_st, 2) if valor_red_bc == 0 else round(bc_icms_st * (1 - (valor_red_bc / 100)), 2)
        
    def calcular_valor_icms_st(
        self,
        valor_produto: float,
        mva: float,
        aliq_interna: float,
        aliq_interestadual: float,
        valor_red_bc: float = 0,
        valor_ipi: float = 0,
        valor_frete: float = 0,
        valor_out_desp: float = 0,
        valor_seguro: float = 0,
        valor_desconto: float = 0,
    ) -> float:
        
        """
            Calcula o valor do ICMS-ST.
        """

        valor_icms = self.calcular_valor_icms(valor_produto, valor_ipi, valor_frete, valor_out_desp, valor_seguro, valor_desconto, valor_red_bc, aliq_interestadual)
        
        bc_icms_st = self.__calcular_bc_icms_st__(valor_produto, mva, valor_red_bc, valor_ipi, valor_frete, valor_out_desp, valor_seguro, valor_desconto)

        valor_icms_st = (bc_icms_st * (aliq_interna / 100)) - valor_icms

        return round(valor_icms_st, 2)

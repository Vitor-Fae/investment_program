#Lista de inputs
ROE = input("Entre com o valor de ROE: ")
PL = input("Entre com o valor de P/L: ")
PVP = input("Entre com o valor de P/VP: ")
PSR = input("Entre com o valor do PSR(Lucro liquido/ação): ")
Div_Yield = input("Entre com o valor do Dividend Yield: ")
Crescimento_recorente = input("Entre com o valor do Crescimento Recorente (5a): ")
VPA = input("Entre com o valor do VPA: ")

#calcular conforme as métricas o valuation da empresa analisada. Para isso é preciso escolher um 
#método para definir as fórmulas utilziadas.
# Usando o Fluxo de Caixa Descontado temos a seguinte fórmula:
# WACC = E/V * Re + D/V * Rd * (1-Tc)
class Calculadora:
    """
    Classe que implementa operações básicas de uma calculadora.
    """
    
    def somar(self, a: float, b: float) -> float:
        """Retorna a soma de dois números."""
        return a + b
    
    def subtrair(self, a: float, b: float) -> float:
        """Retorna a diferença entre dois números."""
        return a - b
    
    def multiplicar(self, a: float, b: float) -> float:
        """Retorna o produto de dois números."""
        return a * b
    
    def dividir(self, a: float, b: float) -> float:
        """
        Retorna a divisão de a por b.
        Levanta ValueError se b for zero.
        """
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        return a / b
    
    def potencia(self, base: float, expoente: float) -> float:
        """Retorna a base elevada ao expoente."""
        return base ** expoente
    
    def raiz_quadrada(self, num: float) -> float:
        """
        Retorna a raiz quadrada de um número.
        Levanta ValueError se o número for negativo.
        """
        if num < 0:
            raise ValueError("Raiz quadrada de número negativo não é real")
        return num ** 0.5
    
    def fatorial(self, n: int) -> int:
        """
        Retorna o fatorial de um número inteiro não negativo.
        Levanta ValueError se n for negativo.
        """
        if n < 0:
            raise ValueError("Fatorial de número negativo não existe")
        return 1 if n <= 1 else n * self.fatorial(n - 1)
    
    def eh_par(self, num: int) -> bool:
        """Verifica se um número é par."""
        return num % 2 == 0
    
    def eh_primo(self, num: int) -> bool:
        """
        Verifica se um número é primo.
        Levanta ValueError se num for menor que 2.
        """
        if num < 2:
            raise ValueError("Números primos são maiores ou iguais a 2")
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def porcentagem(self, valor: float, percentual: float) -> float:
        """Calcula x% de um valor."""
        return valor * (percentual / 100)
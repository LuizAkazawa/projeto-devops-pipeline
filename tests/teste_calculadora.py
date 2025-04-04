#python -m pytest teste_calculadora.py --html=report.html
import sys
import pytest
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.calculadora import Calculadora

@pytest.fixture
def calc():
    """Fixture que fornece uma instância da calculadora para todos os testes."""
    return Calculadora()

class TestCalculadora:
    """Classe de testes para a calculadora."""
    
    # Testes básicos
    def test_somar(self, calc):
        assert calc.somar(2, 3) == 5
        assert calc.somar(-1, 1) == 0
        assert calc.somar(0, 0) == 0
    
    def test_subtrair(self, calc):
        assert calc.subtrair(5, 3) == 2
        assert calc.subtrair(3, 5) == -2
        assert calc.subtrair(0, 0) == 0
    
    # Testes com tratamento de erro
    def test_dividir(self, calc):
        assert calc.dividir(10, 2) == 5
        assert calc.dividir(1, 2) == 0.5
        
        with pytest.raises(ValueError, match="Divisão por zero"):
            calc.dividir(10, 0)
    
    # Testes com valores limite
    def test_potencia(self, calc):
        assert calc.potencia(2, 3) == 8
        assert calc.potencia(5, 0) == 1
        assert calc.potencia(0, 5) == 0
        assert calc.potencia(4, -1) == 0.25
    
    # Testes com exceções
    def test_raiz_quadrada(self, calc):
        assert calc.raiz_quadrada(9) == 3
        assert calc.raiz_quadrada(0) == 0
        
        with pytest.raises(ValueError, match="Raiz quadrada de número negativo"):
            calc.raiz_quadrada(-1)
    
    # Testes com recursão
    def test_fatorial(self, calc):
        assert calc.fatorial(0) == 1
        assert calc.fatorial(1) == 1
        assert calc.fatorial(5) == 120
        
        with pytest.raises(ValueError, match="Fatorial de número negativo"):
            calc.fatorial(-1)
    
    # Testes booleanos
    def test_eh_par(self, calc):
        assert calc.eh_par(2) is True
        assert calc.eh_par(3) is False
        assert calc.eh_par(0) is True
    
    # Testes com números primos
    def test_eh_primo(self, calc):
        assert calc.eh_primo(2) is True
        assert calc.eh_primo(7) is True
        assert calc.eh_primo(4) is False
        
        with pytest.raises(ValueError, match="Números primos são maiores ou iguais a 2"):
            calc.eh_primo(1)
    
    # Testes com porcentagem
    def test_porcentagem(self, calc):
        assert calc.porcentagem(100, 50) == 50
        assert calc.porcentagem(200, 10) == 20
        assert calc.porcentagem(0, 50) == 0
    
    # Teste combinando operações
    def test_operacoes_combinadas(self, calc):
        resultado = calc.dividir(
            calc.somar(10, calc.multiplicar(2, 3)),
            4
        )
        assert resultado == 4
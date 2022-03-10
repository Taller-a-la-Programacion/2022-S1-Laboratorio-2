#NO MODIFICAR ESTE ARCHIVO

import Laboratorio02;
import pytest;

    
def test_lab_1():
    assert Laboratorio02.elevarPotencia(2, 3) == 8
    
def test_lab_2():
    assert Laboratorio02.elevarPotencia(12, 2) == 144
    
def test_lab_3():
    assert Laboratorio02.calculadora(1, 4, 8) == 12
    
def test_lab_4():
    assert Laboratorio02.calculadora(2, 4, 8) == -4

def test_lab_5():
    assert Laboratorio02.calculadora(4, 4, 8) == 0.5
    

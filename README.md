# MTUniversal
Trabalho prático da disciplina Teoria da Computação

Foi implementado uma máquina de turing universal com heurística para detecção de loop.

A entrada é um arquivo txt contendo as transições δ(qi, x) = (qj, y, d) encodificadas da seguinte maneira:
en(qi)0en(x)0en(qj)0en(y)0en(d).

A Heurística implementada consiste monitorar o número de vezes as transições foram realizadas, se esse número utrapassar um trashhold definido como 
len(fita de entrada) * número de estados.

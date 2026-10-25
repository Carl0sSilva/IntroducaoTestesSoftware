import unittest;
import aluno as a;
import turma as t;

class turmaTest(unittest.TestCase):

  def setUp(self):
    print('Teste', self._testMethodName, 'sendo executado...');
    self.alunos = [];

    def lancarNota (nome, sobrenome, nota):
      try:
          self.alunos.append(a.Aluno(nome, sobrenome, nota));
      except ValueError:
          print(f"Falha ao cadastrar {nome}"); 

    lancarNota('Fabio', 'Teixeira', 10);
    lancarNota('Fabiano', 'Teixeira', 8);
    lancarNota('Melissa', 'Teixeira', -1);    
    lancarNota('Angela', 'Teixeira', 7);
    lancarNota('Carlos', 'Silva', 11);
    lancarNota('Neymar', 'Júnior', 5.5);
    lancarNota('Cristiano', 'Ronaldo', -3);
    lancarNota('Sabrina', 'Carpenter', 9);   

    self.turmaObject = t.Turma();
    self.turmaObject.cadastrarAlunos(self.alunos);
  
  def tearDown(self):
    print('Teste', self._testMethodName, 'finalizado.'); 
  
  def testMaior(self):      
    self.assertEqual(10, self.turmaObject.maiorNota.nota, 'Erro ao encontrar maior nota');

  def testMenor(self):    
    self.assertEqual(5.5, self.turmaObject.menorNota.nota, 'Erro ao encontrar menor nota');

  def testIntervalo(self):
    print('Testar se o intervalo de notas está correto.')
    #Escreva o seu código aqui
    #Testar se o intervalo de notas está entre 0 e 10.
    for nota in self.turmaObject.notas:
      self.assertGreaterEqual(nota, 0, 'A nota é menor que zero');
      self.assertLessEqual(nota, 10, 'A nota é maior que 10');


if __name__ == "__main__":
  unittest.main()
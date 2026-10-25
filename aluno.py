class Aluno:
  def __init__(self, nome, sobrenome, nota):
    self.nome = nome;
    self.sobrenome = sobrenome;

    if nota >= 0 and nota <= 10:
      self.nota = nota;
    else:
      raise ValueError("A nota deve estar entre 0 e 10.");

  def mostrarAluno(self):
    return 'Aluno: ' + self.nome + ' ' + self.sobrenome + ' - Nota: ' + str(self.nota);
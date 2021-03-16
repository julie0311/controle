## Question 4 

note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]

print(notes)

#a/ moyenne de eleve 1
noteseleve1=0
l1=0

for x in notes :
  if x[0] == 'eleve1':
    noteseleve1 = noteseleve1 + x[2]
    l1=l1+1
  moyeleve1 = noteseleve1/l1
print('moyenne de eleve 1 : ',moyeleve1)

#b/ moyenne de eleve 1 en maths

noteseleve1mat=0
l2=0

for x in notes :
  if x[0] == 'eleve1':
    if x[1] == 'math':
      noteseleve1mat = noteseleve1mat + x[2]
      l2 = l2+1
    moyeleve1mat = noteseleve1mat/l2
print('moyenne de eleve 1 en maths :', moyeleve1mat)

#c/ 

def moyenne_tuples(notes, eleve=None, matiere=None):
  l = 0
  noteseleve = 0
  moyeleve = 0
  for x in notes:
    if x[0] == eleve or eleve==None:
      if x[1] == matiere or matiere==None:
        noteseleve = noteseleve + x[2]
        l = l+1
      moyeleve = noteseleve/(l)
  return(moyeleve)

print('moyenne eleve 1 en maths : ',moyenne_tuples(notes,'eleve1','math'))

print('moyenne eleve 2 en maths : ',moyenne_tuples(notes,'eleve2','math'))

print('moyennes des notes de tous les eleves dans toutes les matieres :',moyenne_tuples(notes))

#print(moyenne_tuples(notes,'eleve1', 'maths'))
# si on écrit mal la matière, la fonction ne peut pas fonctionner 
# de meme si on entre une chaine de caractère au lieu d'un nomvre puisque les calculs ne pourront pas se faire 


# Pour ajouter des coefficients aux notes et aux matières il faudrait rajouter des paramètres dans la fonction.



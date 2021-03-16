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
moyeleve1=0

for x in notes :
  if x[0] == 'eleve1':
    moyeleve1 = moyeleve1 + x[2]
print(moyeleve1)

#b/ moyenne de eleve 1 en maths
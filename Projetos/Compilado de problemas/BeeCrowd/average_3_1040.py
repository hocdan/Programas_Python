'''
Read four numbers (N1, N2, N3, N4), which one with 1 digit after the decimal point, corresponding to 
4 scores obtained by a student. Calculate the average with weights 2, 3, 4 e 1 respectively, for these
4 scores and print the message "Media: " (Average), followed by the calculated result. If the average 
was 7.0 or more, print the message "Aluno aprovado." (Approved Student). If the average was less than 
5.0, print the message: "Aluno reprovado." (Reproved Student). If the average was between 5.0 and 6.9,
including these, the program must print the message "Aluno em exame." (In exam student).

In case of exam, read one more score. Print the message "Nota do exame: " (Exam score) followed by 
the typed score. Recalculate the average (sum the exam score with the previous calculated average and 
divide by 2) and print the message “Aluno aprovado.” (Approved student) in case of average 5.0 or more)
or "Aluno reprovado." (Reproved student) in case of average 4.9 or less. For these 2 cases (approved 
or reproved after the exam) print the message "Media final: " (Final average) followed by the final 
average for this student in the last line.

Input

The input contains four floating point numbers that represent the students' grades.

Output

Print all the answers with one digit after the decimal point.

'''
notas = input().split()
nota1 = float(notas[0])
nota2 = float(notas[1])
nota3 = float(notas[2])
nota4 = float(notas[3])

media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4) / 10

print("Media: {0:.1f}".format(media))
if ( media >= 7.0 ):
    print("Aluno aprovado.")
elif ( media <= 6.9 and media >= 5.0):
    print("Aluno em exame.")
    nota5 = float(input())
    print("Nota do exame: {}".format(nota5))
    mediaFinal = (media + nota5) / 2
    if (mediaFinal > 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {0:.1f}".format(mediaFinal))
else:
    print("Aluno reprovado.")

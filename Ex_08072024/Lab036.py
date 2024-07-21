# write a porggram to calculate and displays the letters
# numericAl score (e.g A,B,C,D,F)
# based on following grading
# inpit score -89
# utput -B
# A : 90-100
# B: 80-89
# C: 70-79
# D:60-69
# F:0-59


# multiple conditon if , elif.else
# step 1=== logic buildeing
# input ?
# score== int
score = int(input("enter the score\n"))
# output =string =A,B,C,D,F

# step-2
# write thr rough logic

# score >=90 and score<=100---A
# score >=80 and score<=89---B
# score >=70 and score<=79---C
# score >=60 and score<=69---D
# score >=0 and score<=59---F

if score >= 90 and score <= 100:
 print("grading is A")

elif score >= 80 and score <= 89:
 print("grading is B")
elif score >= 70 and score <= 79:
 print("grading is c")
elif score >= 60 and score <= 69:

 print("grading is D")
elif score >=0 and score<=59:
    print("invalid data")

def letter_grade(grade):
    if grade < 0 or grade > 100:
        return "Invalid grade"

    elif grade >= 94:
        return "A", 4.0
    elif grade >= 90:
        return "A-", 3.7
    elif grade >= 87:
        return "B+", 3.3
    elif grade >= 83:
        return "B", 3.0
    elif grade >= 80:
        return "B-", 2.7
    elif grade >= 77:
        return "C+", 2.3
    elif grade >= 73:
        return "C", 2.0
    elif grade >= 70:
        return "C-", 1.7
    elif grade >= 67:
        return "D+", 1.3
    elif grade >= 60:
        return "D", 1.0
    else:
        return "F", 0.0


print(letter_grade(95))  
print(letter_grade(88))  
print(letter_grade(75))  
print(letter_grade(55))  
print(letter_grade(101))
print(letter_grade(-1))


def grading_system(score,total):
    if(score > total):
        return f"That's not a valid score and total score, {score} is greater than {total}"
    elif(score < 0 or total < 0):
        return f"Those are negative values, Invalid values"
    elif(total == 0):
        return f"You can not divide by 0"
    else:
        grade_score = score / total * 100    
        if(grade_score <= 37):
            return f"You score {grade_score} which is grade F"
        elif(grade_score <=44):
            return f"You score {grade_score} which is grade E"
        elif(grade_score <=49):
            return f"You score {grade_score} which is grade D"
        elif(grade_score <=59):
            return f"You score {grade_score} which is grade C"
        elif(grade_score <=69):
            return f"You score {grade_score} which is grade B"
        elif(grade_score <=100):
            return f"You score {grade_score} which is grade A"
        else:
            return f"Invalid"


    
print(grading_system(69,100))



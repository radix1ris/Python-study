def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total/len(scores)

def is_passed(score):
    if score >= 60:
        return True
    else:
        return False
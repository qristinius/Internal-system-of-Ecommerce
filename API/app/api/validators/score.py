def validate_score_range(score):
    if not score in range(0,6,1):
        return "Bad request"



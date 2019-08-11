from datetime import datetime


def get_time_passed(date_posted):
    current_time = datetime.utcnow()
    delta = current_time - date_posted
    tot_sec = delta.total_seconds()
    if tot_sec < 60:
        return f"{int(tot_sec)} sec"
    elif tot_sec < 60 * 60:
        tot_min = tot_sec / 60
        return f"{int(tot_min)} min"
    elif tot_sec < 24 * 60 * 60:
        tot_hrs = tot_sec / 60 / 60
        return f"{int(tot_hrs)} hrs"
    elif tot_sec < 30 * 24 * 60 * 60:
        tot_days = tot_sec / 60 / 60 / 24
        return f"{int(tot_days)} days"
    elif tot_sec < 365 * 24 * 60 * 60:
        tot_months = tot_sec / 60 / 60 / 24 / 30
        return f"{int(tot_months)} months"
    else:
        tot_yrs = tot_sec / 60 / 60 / 24 / 30 / 365
        return f"{int(tot_yrs)} years"


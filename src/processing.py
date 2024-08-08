def filter_by_state(filt, state="EXECUTED"):
    filtered_date = []
    for item in filt:
        if item.get("state") == state:
            filtered_date.append(item)
    return filtered_date

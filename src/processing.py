def filter_by_state(filter, state="EXECUTED"):
    filtered_date = []
    for item in filter:
        if item.get("state") == state:
            filtered_date.append(item)
    return filtered_date

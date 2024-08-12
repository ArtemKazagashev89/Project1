eature/homework_10_
def filter_by_state(date: list, state="EXECUTED") -> list:

    """Функция фильтрует данные по указоннаму состоянию"""
    filtered_date = []
    for item in date:
        if item.get("state") == state:
            filtered_date.append(item)
    return filtered_date


      
      
   
       
def sort_by_date(date_list: list, reverse_list: bool = True) -> list:
    """Функция сортирует список по дате"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list


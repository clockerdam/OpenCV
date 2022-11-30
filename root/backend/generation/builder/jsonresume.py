import datetime


def parse_common(names, data):
    return {f: data.get(f, "") for f in names.split()}


def format_date(date, fmt="%m/%Y"):
    try:
        date = datetime.datetime.fromisoformat(date).date()
        fmt = "{:" + fmt + "}"
        date = fmt.format(date)
    except ValueError:
        date = date.capitalize()
    return date


def add_section_items(obj, item_processor):
    if isinstance(obj, (list, tuple)):
        return [item_processor(i) for i in obj]
    elif isinstance(obj, dict):
        return item_processor(obj)


def parse_year(date):
    date = datetime.datetime.fromisoformat(date).date()
    return str(date.year)


def stringify_sequence(sequence):
    if not sequence:
        return ""
    if isinstance(sequence, str):
        return sequence
    elif isinstance(sequence, (list, tuple, set)):
        return ", ".join(sequence)


def format_date_range(start, end, fmt="%m/%Y"):
    if not start or not end:
        return ""
    start = format_date(start, fmt)
    end = format_date(end, fmt)
    if start == end:
        return start
    return f"{start} -- {end}"


def add_items(obj, items):
    if not items:
        return obj
    if isinstance(items, str):
        obj.add_item(items)
    if isinstance(items, (tuple, list)):
        for item in items:
            obj.add_item(item)
    return obj

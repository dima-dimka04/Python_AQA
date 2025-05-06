import json


def parse_multiplicity(mult_str):
    if not mult_str:
        return None, None
    if '..' in mult_str:
        min_val, max_val = mult_str.split('..')
    else:
        min_val = max_val = mult_str
    return min_val, max_val


def generate_meta_json(classes, filepath):
    meta = []

    for cls in classes.values():
        entry = {
            "class": cls.name,
            "documentation": cls.documentation,
            "isRoot": cls.is_root
        }

        if cls.multiplicity:
            min_val, max_val = parse_multiplicity(cls.multiplicity)
            entry["min"] = min_val
            entry["max"] = max_val

        params = [{"name": n, "type": t} for n, t in cls.attributes]
        params += [{"name": c, "type": "class"} for c in cls.children]
        entry["parameters"] = params

        meta.append(entry)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=4)

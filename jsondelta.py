def compare(left, right, path='$'):
    """Yield (path, kind, old, new) for meaningful JSON differences."""
    changes = []
    if type(left) is not type(right):
        return [(path,'type',left,right)]
    if isinstance(left, dict):
        for key in sorted(set(left) | set(right)):
            key_path = path + '[' + repr(key) + ']'
            if key not in left: changes.append((key_path,'added',None,right[key]))
            elif key not in right: changes.append((key_path,'removed',left[key],None))
            else: changes.extend(compare(left[key],right[key],key_path))
    elif isinstance(left, list):
        for i in range(max(len(left),len(right))):
            child = path + '[' + str(i) + ']'
            if i >= len(left): changes.append((child,'added',None,right[i]))
            elif i >= len(right): changes.append((child,'removed',left[i],None))
            else: changes.extend(compare(left[i],right[i],child))
    elif left != right:
        changes.append((path,'changed',left,right))
    return changes

def is_ignored(path, ignored):
    # Ignore exactly the configured JSON path or its descendants.
    for prefix in ignored:
        if path == prefix or path.startswith(prefix + '['):
            return True
    return False


def without_paths(changes, ignored):
    return [change for change in changes if not is_ignored(change[0], ignored)]

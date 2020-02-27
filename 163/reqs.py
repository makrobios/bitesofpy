def _make_version_dict(reqs):
    reqs_dict = {}
    for line in reqs.strip().splitlines():
        name, version= line.split('==')
        version = tuple([int(num) for num in version.split('.')])
        reqs_dict[name] = version 
    return reqs_dict

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    upgraded = []
    old_dict = _make_version_dict(old_reqs)
    new_dict = _make_version_dict(new_reqs)
    for package, version in new_dict.items():
        if version > old_dict[package]:
            upgraded.append(package)
    return upgraded

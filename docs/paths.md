# Change paths

Object keys are shown in bracket notation using Python's `repr` so keys
containing periods or spaces stay distinguishable. Arrays use zero-based
numeric indices. For example, `$['server']['ports'][0]`.

To ignore a subtree, pass its exact path:
`--ignore "$['metadata']"` (quote it to prevent shell substitution).

from logicProblem import yes
"""bottom-up procedure is forward chaining on the definite clauses, in the sense of going forward from what is known rather than going backward from the query"""

def fixed_point(kb):
    """Returns the fixed point of knowledge base kb."""
    fp = ask_askables(kb)
    added = True
    while added:
        added = False  # added is true when an atom was added to fp this iteration
        for c in kb.clauses:
            if c.head not in fp and all(b in fp for b in c.body):
                fp.add(c.head)
                added = True
    return fp
"""The final fp generated in the algorithm is called a fixed point because any further application of the rule of derivation does not change C. 
fp is the least fixed point because there is no smaller fixed point."""

def ask_askables(kb):
    return {at for at in kb.askables if yes(input("Is " + at + " true? "))}
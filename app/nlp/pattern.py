

rules = {
    "rule_one_neg" : [
        # anchor token: founded
        {
            "RIGHT_ID": "aux",
            "RIGHT_ATTRS": {"POS": "AUX"}
        },
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "expression",
            "RIGHT_ATTRS": {"DEP": "nsubj", "POS" : "NOUN"}
        },
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "neg",
            "RIGHT_ATTRS": {"DEP": "neg"}
        },
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "subject",
            "RIGHT_ATTRS": {"DEP": "acomp"}
        }
    ],
    "rule_one" : [
        {
            "RIGHT_ID": "aux",
            "RIGHT_ATTRS": {"POS": "AUX"}
        },
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "expression",
            "RIGHT_ATTRS": {"DEP": "nsubj", "POS" : "NOUN"}
        },
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "subject",
            "RIGHT_ATTRS": {"DEP": "acomp"}
        }
    ],
    "rule_conj" : [
        {
            "RIGHT_ID": "aux",
            "RIGHT_ATTRS": {"POS": "AUX"}
        },
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "expression",
            "RIGHT_ATTRS": {"DEP": "nsubj", "POS" : "NOUN"}
        },
        {
            "LEFT_ID": "aux",
            "REL_OP": ">",
            "RIGHT_ID": "subject",
            "RIGHT_ATTRS": {"DEP": "acomp"}
        },
        {
            "LEFT_ID": "subject",
            "REL_OP": ">",
            "RIGHT_ID": "conj",
            "RIGHT_ATTRS": {"DEP": "conj"}
        }
    ],
}

def init_patterns (dep_patcher) :
    """
    Add all the above patterns
    """
    global rules

    for key in rules :
        dep_patcher.add(key,[rules[key]])
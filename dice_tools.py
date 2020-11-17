import lea
from lea import leaf


def re_rolling(die=leaf.die(), on=1):
    first_roll = die.new()
    second_roll = die.new()

    def re_roll_func(a, b, val):
        if not isinstance(val, list):
            val = [val]
        if a in val:
            return b
        return a
    return first_roll.map(re_roll_func, second_roll, on)


def variable_shots(shots, success_probability):
    if not isinstance(shots, lea.Lea):
        shots = lea.vals(shots)
    distribution = dict()
    for (n, p) in shots.pmf_tuple:
        single_distribution = lea.binom(n, success_probability)
        for (n_p, p_p) in single_distribution.pmf_tuple:
            distribution[n_p] = distribution.setdefault(n_p, 0.0)+(p*p_p)
    return lea.pmf(distribution)


def add_pmf_to_result(single_tuple, tuple_set):
    result_dict = dict()
    for (n_2, p_2) in tuple_set:
        result = (single_tuple[0]+n_2, single_tuple[1]*p_2)
        result_dict[result[0]] = result_dict.setdefault(result[0], 0.0) + result[1]
    return result_dict


def merge_pmf_dicts(a, b):
    for n in a.keys():
        if b.__contains__(n):
            b[n] = b[n] + a[n]
        else:
            b[n] = a[n]
    return b


def variable_damage_table(max_wounds, damage_die, wounds_per_model):
    result_dict = dict()
    if not isinstance(damage_die, lea.Lea):
        damage_die = lea.vals(damage_die)
    for i in range(0, max_wounds+1):
        for j in range(wounds_per_model):
            if i > 0:
                damage_spread = lea.min_of(wounds_per_model - j, damage_die)
                temp_dict = dict()
                for (n, p) in damage_spread.pmf_tuple:
                    temp_dict = merge_pmf_dicts(
                        add_pmf_to_result(
                            (n, p),
                            result_dict[(i-1, (j-n)%wounds_per_model)].pmf_tuple
                        ),
                        temp_dict
                    )
                result_dict[(i, j)] = lea.pmf(temp_dict)
            else:
                result_dict[(i, j)] = lea.vals(i)
    return result_dict


def merge_distributions(parent_distribution, child_dictionary):
    result_dict = dict()
    for (key, key_prob) in parent_distribution.pmf_tuple:
        for (value, value_prob) in child_dictionary[key].pmf_tuple:
            result_dict[value] = result_dict.setdefault(value, 0.0) + key_prob * value_prob
    return lea.pmf(result_dict)


def flatten_damage_dictionary(damage_dictionary):
    new_dictionary = dict()
    for (wounds, remainder) in damage_dictionary.keys():
        if remainder == 0:
            new_dictionary[wounds] = damage_dictionary[(wounds, remainder)]
    return new_dictionary


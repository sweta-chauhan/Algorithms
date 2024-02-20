def recursive_01_knap_sack(capacity, weights, profits, number_of_weights):
    if number_of_weights == 0 or capacity == 0:
        return 0

    if weights[number_of_weights-1] > capacity:
        return recursive_01_knap_sack(capacity, weights, profits, number_of_weights-1)

    return max(
        profits[number_of_weights-1] + recursive_01_knap_sack(
            capacity-weights[number_of_weights-1],
            weights,
            profits, number_of_weights-1
        ),
        recursive_01_knap_sack(
            capacity,
            weights,
            profits,
            number_of_weights-1
        )

    )


def memoized_01_knap_sack(capacity, weights, profits, number_of_weights, table):
    if capacity == 0 or number_of_weights == 0:
        return 0

    if table[number_of_weights][capacity] != -1:
        return table[number_of_weights][capacity]

    if capacity < weights[number_of_weights-1]:
        table[number_of_weights][capacity] = memoized_01_knap_sack(
            capacity, weights, profits, number_of_weights-1, table
        )
    elif weights[number_of_weights-1] <= capacity:
        table[number_of_weights][capacity] = max(
            profits[number_of_weights-1] + memoized_01_knap_sack(
                capacity-weights[number_of_weights-1],
                weights,
                profits,
                number_of_weights-1,
                table
            ),
            memoized_01_knap_sack(
                capacity,
                weights,
                profits,
                number_of_weights-1,
                table
            )
        )

    return table[number_of_weights][capacity]


def memoized_01_knap_sack_helper(capacity, weights, profits, number_of_weights):
    table = [[-1] * (capacity+1) for _ in range(number_of_weights+1)]
    return memoized_01_knap_sack(capacity, weights, profits, number_of_weights, table)


def tabulated_01_knap_sack(capacity, weights, profits, number_of_weights):
    table = [[0] * (capacity+1) for _ in range(number_of_weights+1)]

    for weight_index in range(1, number_of_weights+1):
        for local_capacity in range(1, capacity+1):
            if table[weight_index][local_capacity] > capacity:
                table[weight_index][local_capacity] = table[weight_index-1][local_capacity]
            else:
                table[weight_index][local_capacity] = max(
                    profits[weight_index-1] + table[weight_index-1][local_capacity-weights[weight_index-1]],
                    table[weight_index-1][local_capacity]
                )

    return table[number_of_weights][capacity]

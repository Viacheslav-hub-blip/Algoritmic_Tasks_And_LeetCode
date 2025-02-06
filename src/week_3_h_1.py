def calculate_cost(*args, discount=0, delivery_type = 'стандартная'):
    total_cost = sum(list(args))

    if delivery_type == 'стандартная':
        if total_cost < 5000:
            total_cost += 1000
        else:
            total_cost += 0
    elif delivery_type == 'экспресс':
        total_cost += 1500

    cost_with_discount  = total_cost - total_cost * (discount/100)
    return int(cost_with_discount)

print(calculate_cost(4500))
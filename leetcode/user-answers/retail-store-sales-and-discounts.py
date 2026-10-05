def solution(priceList, logs):
    prices = {}

    for entry in priceList:
        item, price = entry.split(": ")
        prices[item] = int(price)

    # item -> [discount_amount, remaining_discount_count]
    discounts = {}

    revenue = 0

    for log in logs:
        if log.startswith("sell "):
            data = log[len("sell "):]
            item, count = data.split(", ")
            count = int(count)

            price = prices[item]

            if item in discounts:
                discount_amount, remaining = discounts[item]

                discounted_count = min(count, remaining)
                normal_count = count - discounted_count

                revenue += discounted_count * (price - discount_amount)
                revenue += normal_count * price

                discounts[item][1] -= discounted_count
            else:
                revenue += count * price

        elif log.startswith("discount_start "):
            data = log[len("discount_start "):]
            item, discount_amount, max_count = data.split(", ")

            discounts[item] = [
                int(discount_amount),
                int(max_count)
            ]

        elif log.startswith("discount_end "):
            item = log[len("discount_end "):]
            del discounts[item]

    return revenue

def can_ship(weights, capacity, days):
    current_weight = 0
    day_count = 1

    for weight in weights:
        if current_weight + weight > capacity:
            print("Current weight ",current_weight)
            print("Capacity ", capacity)
            print("day", day_count)
            day_count += 1
            current_weight = 0
        current_weight += weight

        if day_count > days:
            return False
    return True

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)

    while left < right:
        mid = (left + right) // 2
        if can_ship(weights, mid, days):
            right = mid
        else:
            left = mid + 1

    return left

my_list= [1,2,3,4,5,6,7,8,9,10]
#my_list = [1,2,3,1,1]
days = 5

print(shipWithinDays(my_list, days))
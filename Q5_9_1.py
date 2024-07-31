mountain_in_japan = {'fuli': 3776, 'kitadake': 3193, 'okuhodakadake': 3190, 'dummy': 0}

sorted_mountains = dict(sorted(mountain_in_japan.items(), key=lambda x: x[1], reverse=True))

print(sorted_mountains)


num = 63302
guests = ""
guest_list = [int(i) for i in guests.split()]

indexed_guests = list(enumerate(guest_list))
sorted_guests = sorted(indexed_guests, key=lambda x: x[1])
result = {original_index: value for original_index, value in sorted_guests}

trimmed_result = {index : value for index, value in list(result.items())[:num]}
trimmed_index = list(trimmed_result.keys())

new_list = [0] * len(guest_list)

for i in trimmed_index:
    new_list[i] = 1

d = open("output.txt", "w")
d.write(" ".join(map(str, new_list)))

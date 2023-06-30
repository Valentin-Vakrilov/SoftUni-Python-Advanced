reservation_codes = int(input())

guest_list = set()

for guest in range(reservation_codes):
    current_guest = input()
    guest_list.add(current_guest)

arrived_guest = input()

while arrived_guest != "END":
    guest_list.remove(arrived_guest)
    arrived_guest = input()

print(len(guest_list))

sorted_guest_list = sorted(guest_list)

print("\n".join(sorted_guest_list))

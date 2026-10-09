snack_box1 = {"chips", "juicce", "cookies", "chips", "apple"}
snack_box2 = {"cookies", "sandwich", "juice", "sandwich"}
snack_box1.add("banana")
print("Updated Snack Box 1:", snack_box1)
common_snacks = snack_box1.intersection(snack_box2)
print("Common Snacks:", common_snacks)
import array
snack_counts = array.array('i', [5, 3, 7, 2, 4])
snack_counts.insert(0, 10)
snack_counts.append(6)
print("Snack counts:", snack_counts)
print("Number of times 3 appears:", snack_counts.count(3))
snack_counts.reverse()
print("Reversed snack counts:", snack_counts)
print("School Snack Summary")
print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)
print("Shared Snacks:", common_snacks)
print("Final Snack Counts:", snack_counts)
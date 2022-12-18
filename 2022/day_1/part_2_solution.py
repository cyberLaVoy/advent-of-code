# Read the input list of calorie counts
calorie_counts = []
while True:
  try:
    line = input()
    calorie_counts.append(line)
  except EOFError:
    break

# Split the input list into sublists, each representing the calorie counts for a single Elf
elves = []
current_elf = []
for calorie_count in calorie_counts:
  if calorie_count == "":
    elves.append(current_elf)
    current_elf = []
  else:
    current_elf.append(calorie_count)

# Calculate the total number of calories for each Elf
calorie_totals = []
for elf in elves:
  calorie_total = 0
  for calorie_count in elf:
    # Convert calorie_count to an integer before adding it to calorie_total
    calorie_total += int(calorie_count)
  calorie_totals.append(calorie_total)

# Sort the calorie totals in descending order
calorie_totals.sort(reverse=True)

# Select the top three Elves with the highest number of calories
top_three_elves = calorie_totals[:3]

# Calculate the total number of calories carried by the top three Elves
total_calories = 0
for calorie_total in top_three_elves:
  total_calories += calorie_total

# Print the total number of calories carried by the top three Elves
print("The top three Elves carry a total of", total_calories, "calories")
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

# Find the Elf with the highest number of calories
max_calories = 0
max_elf = 0
for i in range(len(calorie_totals)):
  if calorie_totals[i] > max_calories:
    max_calories = calorie_totals[i]
    max_elf = i

# Print the total number of calories carried by the Elf with the highest number of calories
print("Elf", max_elf, "carries the most calories with a total of", max_calories)

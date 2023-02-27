import pigAge

# Accept an integer input representing the age of a pig
pig_age = int(input())

# Calculate the human-equivalent age of the pig using the pigAge_converter() function
human_age = pigAge.pigAge_converter(pig_age)

# Output the human-equivalent age of the pig
print(f"{pig_age} is {human_age} in human years")

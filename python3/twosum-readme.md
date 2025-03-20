# The Two Sum problem is a common coding challenge where we need to find two numbers in an array that add up to a given target.

# The function returns the indices of these two numbers.

# How the Code Works:

# 1️⃣ Using a Dictionary (HashMap):

# We use a dictionary (hash table) called MyDict to store numbers as keys and their indices as values.

# This allows for quick lookups to check if a required number exists in the array.

# 2️⃣ Iterating Through the Array:

# We loop through each element in the array while keeping track of its index.

# 3️⃣ Calculating the Difference:

# For each number, we calculate diff = target - nums[i].

# This tells us the number we need to find in order to get the sum equal to the target.

# 4️⃣ Checking if the Difference Exists:

# We check if diff is already present in MyDict.

# If found, it means we have found the required pair, and we return the indices.

# 5️⃣ Storing the Current Number:

# If the diff is not found, we store the current number in MyDict with its index.

# This ensures that any future elements can find this number when needed.

# 6️⃣ Returning an Empty List if No Pair is Found:

# If no valid pair is found, the function returns an empty list.

# 🚀 Time Complexity:

# O(n) → Each element is checked once, making the solution very efficient.

# 🛠 Space Complexity:

# O(n) → In the worst case, we store all elements in the dictionary.

# 🔥 This approach is efficient, beginner-friendly, and widely used in coding interviews!

# Global variable (string)
global_var = "Hello, "
def add_variables():
    # Local variable (initial string value)
    local_var = "World"
    # First combination of global and local variables
    first_result = global_var + local_var
    # Change the local variable for the second combination
    local_var = "Python"
    # Second combination of global and local variables
    second_result = global_var + local_var
    # Return a string that includes both combinations
    return(f"First result: {first_result}. Second result: {second_result}")
# Print the combined string
print(add_variables())
def is_palindrome_string(s):
  """Checks if a string is a palindrome."""
  return s == s[::-1]

# Example usage
word1 = "madam"
word2 = "hello"
print(f"'{word1}' is a palindrome: {is_palindrome_string(word1)}")
print(f"'{word2}' is a palindrome: {is_palindrome_string(word2)}")
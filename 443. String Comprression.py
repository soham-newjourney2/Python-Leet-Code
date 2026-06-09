# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.

# Note: The characters in the array beyond the returned length do not matter and should be ignored.



# Try 1

class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0

        l = [chars[0]]
        tag = chars[0]
        count = 1

        for i in chars[1:]:
            if tag != i:
                if count > 1:
                    for digit in str(count):
                        l.append(digit)
                tag = i
                l.append(tag)
                count = 1
            else:
                count += 1

        if count > 1:
            for digit in str(count):
                l.append(digit)

        chars[:] = l
        return len(chars)
    
# Try 2

class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            cur_char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == cur_char:
                read += 1
                count += 1

            chars[write] = cur_char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        chars = chars[:write]
        return write
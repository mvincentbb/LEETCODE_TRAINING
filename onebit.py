def hammingWeight(n: int) -> int:
        # Initialize a count variable to keep track of the number of '1' bits
            count = 0
                
                    # Iterate through all the bits in the integer
                        while n > 0:
                                # If the rightmost bit is 1, increment the count
                                        if n & 1 == 1:
                                                    count += 1
                                                            # Right shift the integer by 1 bit to move to the next bit
                                                                    n >>= 1
                                                                        
                                                                            # Return the final count
                                                                                return count
                                                                                
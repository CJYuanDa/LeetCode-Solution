class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]: # type: ignore
        ans = []
         
        # Iterate over all possible hour values (0-11) and minute values (0-59)
        for h in range(12): # hour
            for m in range(60): # minutes
                # A 1 in the binary representation means that the corresponding LED is on.
                # Count the number of 1-bits in both hour and minute
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        
        return ans
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += f"{i}:,"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = s.split(":,")

        return decoded[:-1]
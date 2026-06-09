class Solution:

    def encode(self, strs: List[str]) -> str:
        return "👽".join(["🫦"] + strs + ["🫦"])

    def decode(self, s: str) -> List[str]:

        res = s.split("👽")[1:-1] # skipping the first and last 🫦
        return res

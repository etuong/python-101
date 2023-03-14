class LFSR:
    # Create an LFSR with initial state ‘seed’ and tap ‘tap’
    def __init__(self, seed: str, tap: int):
        self.seed = seed
        self.tap = tap

    # Return the bit at index ‘i’
    def bit(self, i: int):
        return self.seed[i]

    # Execute one LFSR iteration and return new (rightmost) bit as an int
    def step(self):
        bit = int(self.seed[0])
        tap = int(self.seed[-self.tap])
        bit ^= tap
        self.seed = self.seed[1:] + str(bit)
        return bit

    # Get seed
    def get_seed(self):
        return self.seed

    # Return string representation of the LFSR, ex: 01001010
    def __str__(self):
        return self.seed


# Executable code that invokes LFSR
def main():
    seed1 = LFSR("0110100111", 2)
    seed2 = LFSR("0100110010", 8)
    seed3 = LFSR("1001011101", 5)
    seed4 = LFSR("0001001100", 1)
    seed5 = LFSR("1010011101", 7)

    for seed in [seed1, seed2, seed3, seed4, seed5]:
        new_bit = seed.step()
        print(f"{seed} {new_bit}")


if __name__ == "__main__":
    main()

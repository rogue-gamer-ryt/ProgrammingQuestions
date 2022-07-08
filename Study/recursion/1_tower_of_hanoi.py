"""
A peg contains rings in sorted orde1, with the largest ring being the lowest. You are to transfer these
rings to another peg, which is initially empty

Write a program which prints a sequence of operations that transfers n rings from one peg to
another. You have a third peg, which is initially empty. The only operation you can perform is
taking a single ring from the top of one peg and placing it on the top of another peg. You must
never place a larger ring above a smaller ring.
"""
NUM_PEGS = 3

# Time - O(2**n)
def compute_tower_hanoi(num_rings):
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)
    
    result = []
    pegs = [
        list(reversed(range(1, num_rings + 1)))
    ] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result

print(compute_tower_hanoi(6))

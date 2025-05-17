def count_legal_climbs(ladder: int) -> int:
    # two steps or a single step at a time
    if ladder <= 2:
        return ladder
    
    return count_legal_climbs(ladder-1) + count_legal_climbs(ladder-2)

print(count_legal_climbs(int(input())))
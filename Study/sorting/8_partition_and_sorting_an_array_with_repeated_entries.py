"""
You are given an array of student objects. Each student has an integer-valued age field that is to be
treated as a key. Rearrange the elements of the array so that students of equal age appear together.
The order in which diffurent ages appear is not important. How would your solution change if ages
have to appear in sorted order?
"""

Person = collections.namedtuple('Person', ('age', 'name'))

# Time - O(n)
def group_by_age(people):
    age_to_count = collections.Counter([person.age for person in people])
    age_to_offset, offset = {}, 0
    for age, count in age_to_count.items():
        age_to_offset[age] = offset
        offset += count
    
    while age_to_offset:
        from_age = next(iter(age_to_offset))
        from_idx = age_to_offset[from_age]
        to_age = people[from_idx].age
        to_idx = age_to_offset[people[from_idx].age]
        people[from_idx], people[to_idx] = people[to_idx], people[from_idx]
        age_to_count[to_age] -= 1
        if age_to_count[to_age]:
            age_to_offset[to_age] = to_idx + 1
        else:
            del age_to_offset[to_age]

"""
The Intemational Standard Book Number (ISBN) is a unique commercial book identifier. It is a
string of length 10. The first 9 characters are digits; the last character is a check character. The check
character is the sum of the first 9 digits, mod 11, with 10 represented by 'X'.(Modem ISBNs use
13 digits, and the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs.)

Create a cache for looking up prices of books identified by their ISBN. You implement lookup,
insert, and remove methods. Use the Least Recently Used (LRU) policy for cache eviction. If an
ISBN is already present, insert should not change the price, but it should update that entry tobe the
most recently used entry. Lookup should also update that entry to be the most recently used entry.
"""

class LRUCache:
    def __init__(self, capacity):
        self._isbin_price_table = collections.OrderedDict()
        self._capacity = capacity
    
    def lookup(self, isbin):
        if isbin not in self._isbin_price_table:
            return -1
        price = self._isbin_price_table[isbin]
        self._isbin_price_table[isbin] = price
        return price

    def insert(self, isbin, price):
        if isbin in self._isbin_price_table:
            price = self._isbin_price_table.pop(isbin)
        elif self._capacity <= len(self._isbin_price_table):
            self._isbin_price_table.popitem(last=False)
        self._isbin_price_table[isbin] = price

    def erase(self, isbin):
        return self._isbin_price_table.pop(isbin, None) is not None


# Sorting and Caching Notes

## Sorting
Sorting is REALLY important to get right because it's very hard and takes a lot of energy, storage, and time

Can be used to find
Largest or smallest
Most common or rarest
Tallies
Indexes
Find duplicates
ANYTHING
But it's really to make things easier for us as humans to view

Sorted lists are everywhere and we don't even notice

### Sorting theory
The bigger it is, the worse it is

Minimize number to sort, minimize pain and agony and suffering

### BIG-O ! ! ! ! ! ! 
An algorithms worst case scenario

Measures inexactly, because it measures the relationships between the size and the time rather than the time it takes to do something

Big O of 1 is written as O(1) and is called constant time, because no matter what a number (n) is, it stays the same.

For some thing that directly changes with n, it is linear time and is written as O(n)

Quadratic time, is logically, O(n2), where for each one it takes exponentially longer

O(n + 1), O(2n2), and O(n2 + n) are all still quadratic time

Exponential time is O(2n) where each additional one doubles

The worst way is factorial time, or O(n!), like trying to get the right option by just trying things randomly until one option works

### Bubble Sort

Simple, intuitive, but really inefficient

Falls under quadratic time, so still not the best

You look through, flipping every out of order pair, and repeating until it works

It adds up FAST

### Insertion Sort

Like bubble sort but more intuitive

Putting one thing at a time into a new set, and then looking through to see where it goes between what's already put in

It's not really that much better than bubble sort

Again, still quadratic time so still not great

### Non-quadratic sorting, so in theory better

Linear time is practically impossible, however, we can get between linear and quadratic time

### Mergesort

The holy grail of sorting, you take two sorted stacks and you can combine them in linear time

It uses linearithmic time, or O(n log n)

Leaps and bounds better than quadratic time, so its used for most industrial sorting operations

Like breaking up piles of books into smaller piles, sorting them, and then combining two of them, repeating until it's all sorted

### waaaay better than logarithmic time. Bucket sorting

If you don't have to be exact, we can sort in linear time.

Instead of perfect sorting, which is perfected in linearithmic time, we can group them in linear time

It's really O(nm), but if you don't have 300 million groups you want it sorted into, it's basically O(n)

Properly defined buckets sort a larger, extremely hard to sort list, into smaller more manageable lists

A good strategy is to bucket sort, and then insertion sort once you have a smaller set to work with

### Trade Offs
Is it really worth sorting? If it takes less energy to just search, what's the point in sorting?

You need to see if the time it takes to sort it now will pay off in the saved time when you search later

## Caching

What to keep and how to arrange it are the challenges of big data

Putting data in nested folders is called caching

Tradeoffs of size and speed

Have a hierarchy where each level has greater storage but is harder to access

Like taking a bunch of books from the library and storing them on your desk to access them faster

It needs to predict what you will need, like picking out books for the next week so that you only have to go to the library once

Cache replacement of cache eviction means you ran out of storage and need to remove something old to make room for something new

Caching algorithms figure out what to evict

The goal of caching algorithms is to minimize the number of times you can't find what you're looking for

Get as close to clairvoyant as we can get, a completely clairvoyant algorithm is called Bélády’s algorithm

A good way is to remove the least recently used

Libraries have a hierarchy, the books at the front, books on shelves, books in the back, and books that are stored off-site

The ideal cache is shown when a library takes the books that were just returned and puts them in the lobby. 
This means that the books people want are easily accessible and time does not have to be wasted by putting them back on the shelves and then located again to be checked out.

 Content Distribution Centers are located around the world as closer caches for people to access webpages, as further storage means a longer time for it to get to you

Caching is just as good with proximity as it is with performance

### Filing and Piling

Once we know what to keep and where to put it, we need to organize it

Noguchi's system: If you always reinsert values after you use them on the left side, this causes a cache to be made without any additional effort, if anything it takes less effort than putting it back where it was

Noguchi's system perfects the LRU principle

You don't need to sort because it sorts itself!

### The Mind

The mind is really good at remembering, but it takes longer to recall.

We have an infinite storage for memories, but a limited amount of time to remember them, so we forget.

Like a single, very long bookshelf. You can add as many books as you want, and it's faster to find a book closer to the front


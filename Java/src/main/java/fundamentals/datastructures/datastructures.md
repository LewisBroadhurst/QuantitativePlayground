# Data Structures
Used for organising, processing, retrieving, and storing data.

## Iterable
An iterable is the base of Lists, Queues, and Sets in Java.
A collection extends an iterable.
List Queue Set extend from a collection.

Implements: e.g. A class can implement an interface, which will define a set of variables 
and methods that the class must implement.
Extends: e.g. A class that extends a class gains all the methods and variables from 
the parent class. These can then be overridden or have new classes added.

## Lists
ArrayList - LinkedList - Vector.
All implement the List Collection.

##### ArrayList
- Dynamically resizable. Don't need to specify size during initialisation. This is relatively
memory efficient.
- Accepts a generic that defines the data type of the elements stored in the ArrayList
- Order of elements is maintained from the order they are added in.
- Allows for null elements.
- Implements List interface methods like add, remove, get, indexOf, and more.
- ArrayList is not synchronized, meaning it is not thread-safe.

```java
ArrayList<int> cryptocurrencies = new ArrayList<>();
```

##### LinkedList
- Dynamic sizing, can grow or shrink on demand. Memory efficient.
- Each element in a list contains data and a reference to the previous/next node.
- Faster insertion/deletion vs. ArrayList as only one element and references to that
element need to be replaced, rather than shifting multiple elements.
- Higher memory overhead vs. ArrayList as need to store the references.
- Not synchronized, meaning it is not thread-safe.

```java
LinkedList<int> cryptocurrencies = new LinkedList<>();
```

##### Vector
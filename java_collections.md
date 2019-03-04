# sources:
- https://www.baeldung.com/java-collections-interview-questions
- https://howtodoinjava.com/interview-questions/useful-java-collection-interview-questions/
- https://javahungry.blogspot.com/2015/05/50-java-collections-interview-questions-and-answers.html (contiune from question 18)
- http://commons.apache.org/proper/commons-collections/javadocs/api-4.3/index.html (read all the collections from here)


# notes:
- Root Interface is Collection -> Iterable (java.lang).
- Collection is an Interface while Collections is a Class.
- Thread-safe: Stack, Properties, Vector, Hashtable
- Implementation of List Interface: ArrayList, LinkedList, Vector
- Implementation of Set Interface: HashSet, TreeSet
- Iterator(element removal allowed) and Enumeration(read-only) are both interfaces.
- Methods needed to override to be used as HashMap's Key: equals() and hashCode()
- ArrayList(non-sync, capacity increment 50%), Vector(sync, capacity increment 100%).
- HashMap(allows one null key and multiple null values, non-sync), Hashtable(no null key/value, sync)
- hashCode: default is address converted to number, can be overriden without overriding equals
- equals: default is implementation of the parent class, need to override hashCode if it is overriden
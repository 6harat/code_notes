- biased locking:
    https://blogs.oracle.com/dave/biased-locking-in-hotspot

- fast i/o:
    https://www.geeksforgeeks.org/fast-io-in-java-in-competitive-programming/

- spring/rest:
    implementation used in previous projects: jersey (because it is JAX-RS compliant)
    JAX-RS: Java API for restful web services
    JAX-WS: Java API for XML-based web services

- weak vs soft references:
    weak: gc is allowed to recover the object as long as the object is only weakly referenced and no other reference to the object exists.
    soft: gc tries not to recover the object until and unless there is a memory pressure. for client jre - expanding the heap size qualifies as memory pressure. for server jre - the heap is expanded until no longer possible after which the recovery happens.
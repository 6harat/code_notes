# osi model:
* aka: open systems interconnection (osi)
* ref: 
    + https://www.geeksforgeeks.org/layers-osi-model/
    + https://en.wikipedia.org/wiki/List_of_network_protocols_(OSI_model)
* Different Layers:
    + Application:
        - e.g. HTTP, FTP, SOAP, SMTP
    + Presentation:
        - e.g. TLS, SSL
    + Session:
        - e.g. RPC
    + Transport:
        - e.g. TCP, UDP
    + Lower/Hardware Layers:
        - Network: responsible for transmission of data amongst host of different networks
            + e.g. IP
            + routing: determining which route is suitable from source to destination
            + logical addressing: attaching ip addresses of each device to the header to help distinguish one device from another
        - Data Link: responsible for node-to-node delivery of the message
            + e.g. Ethernet
            + Logical Link Control
            + Media Access Control
            + Functions:
                - Framing: attach special bit patterns at begin/end to create a frame
                - Physical Addressing: adding physical (MAC) addresses of sender/receiver in the header of the frame
                - Error Control: detecting and retransmitting damaged/lost frames
                - Flow Control: coordinating the amound of data that can be sent before receiving acknowledgement to maintain constant data rate
                - Access Control: manage controls amongst devices sharing the same channel for a single communication
        - Phsyical: responsible for actual physical connection between devices
            + e.g. USB, Infrared
            + bit synchronization by providing a clock
            + bit rate control
            + identifies the topology as well - star, bus, mesh, etc.
            + transmission mode  simplex, half-duplex, full-duplex
        __Note__: mnemonic for remembering the above order is AP-ST-ND-P 
        {Arunachal Pradhesh StaTe New Delhi Punjab}



# architecture:
- https://www.geeksforgeeks.org/cache-memory/
- https://www.geeksforgeeks.org/2d-and-2-5d-memory-organization/
- https://www.geeksforgeeks.org/computer-organization-von-neumann-architecture/
- https://www.geeksforgeeks.org/computer-architecture-flynns-taxonomy/
- https://www.geeksforgeeks.org/multilevel-cache-organisation/


# operating_system:
    - https://www.geeksforgeeks.org/operating-system-introduction-operating-system-set-1/
    - https://www.geeksforgeeks.org/operating-system-types-operating-systems-awaiting-author/
    - https://www.geeksforgeeks.org/functions-of-operating-system/
    - https://www.geeksforgeeks.org/operating-systems-need-and-functions/
    - https://www.geeksforgeeks.org/operating-system-requirements-of-memory-management-system/
    - https://www.geeksforgeeks.org/semaphores-operating-system/
    - https://www.geeksforgeeks.org/operating-system-kernel-i-o-subsystem-i-o-system/

    - https://www.geeksforgeeks.org/operating-system-allocating-kernel-memory-buddy-system-slab-system/
    - https://www.geeksforgeeks.org/operating-system-introduction-system-call/
    - https://www.geeksforgeeks.org/operating-system-unix-file-system/
    - https://www.geeksforgeeks.org/operating-system-paging/
    - https://www.geeksforgeeks.org/operating-system-microkernel/
    - https://www.geeksforgeeks.org/operarting-system-thread/
    - https://www.geeksforgeeks.org/operating-system-multithreading/
    - https://www.geeksforgeeks.org/operating-systems-segmentation/
    - https://www.geeksforgeeks.org/operating-system-deadlock-detection-algorithm/
    - https://www.geeksforgeeks.org/operating-system-page-fault-handling/
    - https://www.geeksforgeeks.org/deadlock-detection-recovery/
    - https://www.geeksforgeeks.org/operating-system-deadlock-detection-in-distributed-systems/
    - https://www.geeksforgeeks.org/deadlock-prevention/
    - https://www.geeksforgeeks.org/deadlock-starvation-and-livelock/
    - https://www.geeksforgeeks.org/operating-system-resource-allocation-graph-rag/
    - https://www.geeksforgeeks.org/operating-system-allocation-frames/
    - https://www.geeksforgeeks.org/non-contiguous-allocation-in-operating-system/
    - https://www.geeksforgeeks.org/methods-of-resource-allocation-to-processes-by-operating-system/
    - https://www.geeksforgeeks.org/operating-system-page-table-entries/
    - https://www.geeksforgeeks.org/operating-system-inverted-page-table/

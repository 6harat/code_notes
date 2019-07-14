# sources:
* throttling:
    - https://compiletoi.net/fast-scraping-in-python-with-asyncio/
    - https://stackoverflow.com/a/35198369/6687477
    - https://stackoverflow.com/questions/20247354/limiting-throttling-the-rate-of-http-requests-in-grequests

* others:
    - https://docs.python.org/3/library/asyncio.html
    - https://www.pythonsheets.com/notes/python-asyncio.html
    - https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/
    - https://realpython.com/async-io-python/
    - http://lucumr.pocoo.org/2016/10/30/i-dont-understand-asyncio/

    - https://github.com/ReactiveX/RxPY

    - https://github.com/syrusakbary/promise

    - https://github.com/AndreLouisCaron/a-tale-of-event-loops

    - https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures

* sharing event loop in asyncio:
    - https://github.com/aio-libs/aiohttp/issues/2619

* coroutines:
    - http://dabeaz.com/coroutines/

* multiprocessing:
    - http://effbot.org/pyfaq/what-kinds-of-global-value-mutation-are-thread-safe.htm
    - https://gist.github.com/mangecoeur/9540178

* async library list:
    - https://github.com/timofurrer/awesome-asyncio

* graceful shutdown:
- https://groups.google.com/forum/#!topic/python-tulip/91NCCqV4SFs
- https://www.roguelynn.com/words/asyncio-we-did-it-wrong-pt-2/
- http://allyouneedisbackend.com/blog/2017/09/15/how-backend-software-should-retry-on-failures/
- https://asyncio.readthedocs.io/en/latest/hello_world.html#stopping-the-loop

* multiprocessing vs multithreading vs async:
- http://masnun.rocks/2016/10/06/async-python-the-different-forms-of-concurrency/

* threadpool vs processpool:
- https://giuseppeciotta.net/threadpoolexecutor-and-processpoolexecutor-modern-python-idioms.html

* scaling:
- https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html
- https://forum.dabeaz.com/t/thats-a-nice-event-loop-itd-be-a-shame/118
- https://www.bettercodebytes.com/theadpoolexecutor-with-a-bounded-queue-in-python/

* asyncio tutorial:
- https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/
- https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

* asyncio shield:
- https://stackoverflow.com/a/52511210/6687477

* asyncio semaphore:
- https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore

* asyncio discussions:
- https://github.com/python/asyncio/issues/208


# todo:
- [ ] experiment with multithreading, multiprocessing, ThreadPoolExecutor and ProcessPoolExecutor to better understand the difference in performance during application
    + https://stackoverflow.com/questions/3044580/multiprocessing-vs-threading-python
    + https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
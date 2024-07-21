def caching_fibonacci():
    """
    Returns the fibonacci function that had internal cache to improve performance.
    :return:
    """
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0

        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n-1) + fibonacci(n-2)

        return cache[n]

    return fibonacci

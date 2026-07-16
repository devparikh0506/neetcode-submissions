class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)

        # Negative values simulate a max heap
        max_heap = [-count for count in frequencies.values()]
        heapq.heapify(max_heap)

        # Each item: (available_time, remaining_count)
        cooldown = deque()

        time = 0

        while max_heap or cooldown:
            time += 1

            if cooldown and cooldown[0][0] == time:
                available_time, count = cooldown.popleft()
                heapq.heappush(max_heap, count)

            # Execute the most frequent available task
            if max_heap:
                count = heapq.heappop(max_heap)

                count += 1

                if count < 0:
                    cooldown.append((time + n + 1, count))

        return time
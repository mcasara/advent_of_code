import asyncio
import time


async def read_input(file, file_type=""):
    content = []
    with open(file, "r") as f:
        if file_type == "float":
            for line in f:
                try:
                    content.append(float(line.strip("\n")))
                except:
                    content.append("null")
        elif file_type == "int":
            for line in f:
                try:
                    content.append(int(line.strip("\n")))
                except:
                    content.append("null")
        else:
            for line in f:
                if line != "\n":
                    content.append(line.strip("\n"))
    return content


maps = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]


async def get_seeds(input_5):
    return input_5[0].split(":")[1].split()


async def get_maps(input_5):
    indexes = [input_5.index(k) for k in maps]
    indexes.append(len(input_5))
    list_of_maps = []
    for _ in range(len(indexes) - 1):
        line = [line.split() for line in input_5[indexes[_] + 1: indexes[_ + 1]]]
        list_of_maps.append([list(map(int, xs)) for xs in line])

    return list_of_maps


async def seed_to_location(seed, list_of_maps):
    new_seed = seed
    for _ in range(len(list_of_maps)):
        for a, b, c in list_of_maps[_]:
            innit = b + c > seed >= b
            if innit:
                new_seed = a + seed - b
                break
        seed = new_seed
    return seed


# def seed_range_to_location(seeds, list_of_maps):
#     min_seed = 3075226163
#     seed = seeds[::2]
#     seed_range = seeds[1::2]
#     seed_range_zip = list(zip(seed, seed_range))
#     for i, j in seed_range_zip:
#         k = int(j)
#         for x in range(k):
#             new_seed = seed_to_location(int(i) + int(x), list_of_maps)
#             if new_seed < min_seed:
#                 min_seed = new_seed
#         break
#     return min_seed


async def main():
    start_time = time.time()
    input_5 = await read_input("input_5.txt")
    seeds = await get_seeds(input_5)
    list_of_maps = await get_maps(input_5)
    # results = await asyncio.gather(*[seed_to_location(int(seed), list_of_maps) for seed in seeds])
    i = seeds[0]
    j = seeds[1]
    k = int(j)
    results = await asyncio.gather(
        *[seed_to_location(int(i) + int(x), list_of_maps) for x in range(k)])
    print(min(results))
    print("--- %s seconds ---" % (time.time() - start_time))
    ##0.0006968975067138672s
    ##0.0008490085601806641


if __name__ == "__main__":
    asyncio.run(main())

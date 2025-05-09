def self_num(input):
    result = int(input)
    for num in input:
        result += int(num)
    return result


def main(results):
    prev = [2]
    for i in range(2, 10001):
        if not i in prev:
            results.append(i)
        prev.append(int(self_num(str(i))))
    return results

results = [1]
results = main(results)


for i in results:
    print(i)
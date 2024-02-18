from heapq import heappush, heappop, heapify
from os.path import isfile


class HuffmanEncoding:
    def __init__(self, input):
        self.content_type = None
        self.content = input
        if isinstance(input, str):
            if isfile(input):
                self.frequency_table = {}
                with open(input, "r") as fp:
                    lines = fp.readlines()
                    for line in lines:
                        line = line.strip("\n")
                        for character in line:
                            if character in self.frequency_table:
                                self.frequency_table[character] += 1
                            else:
                                self.frequency_table[character] = 1
                self.content_type = "file"
            else:
                self.frequency_table = {}
                for character in input:
                    if character in self.frequency_table:
                        self.frequency_table[character] += 1
                    else:
                        self.frequency_table[character] = 1
                self.content_type = "text"
                print(self.frequency_table)
        elif isinstance(input, dict):
            if all(isinstance(k, str) and isinstance(v, int) for k, v in input.items()):
                self.frequency_table = input
                self.content_type = "table"
            else:
                raise ("Invalid input is provided")
        elif isinstance(input, list):
            if all(isinstance(k, str) and isinstance(v, int) for d in input for k, v in d.items()):
                self.frequency_table = {k:v for d in input for k, v in d.items()}
                self.content_type = "list"
            else:
                raise ("Invalid input is provided")
        else:
            raise ("Invalid input is provided")

    def __build_encoding_table(self):
        heap = [[frequency, [character, ""]] for character, frequency in self.frequency_table.items()]
        heapify(heap)

        while len(heap) > 1:
            first_low_frequent_data = heappop(heap)
            second_low_frequent_data = heappop(heap)

            for low_frequent in first_low_frequent_data[1:]:
                low_frequent[1] = "0" + low_frequent[1]

            for low_frequent in second_low_frequent_data[1:]:
                low_frequent[1] = "1" + low_frequent[1]

            heappush(
                heap,
                [
                    first_low_frequent_data[0] + second_low_frequent_data[0]
                ] +
                first_low_frequent_data[1:] + second_low_frequent_data[1:]

            )
        return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    def encode(self):
        encoding_table = self.__build_encoding_table()
        character_code_map = {enconding[0]: enconding[1] for enconding in encoding_table}
        if self.content_type == "list":
            return "done", character_code_map
        elif self.content_type == "table":
            return "done", {enconding[0]: enconding[1] for enconding in encoding_table}
        elif self.content_type == "text":
            result = []
            for character in self.content:
                result.append(character_code_map[character])
            return "".join(result), character_code_map

        elif self.content_type == "file":
            with open(f"{self.content}_encoded", "w") as writer_fp:
                with open(self.content, "r") as reader_fp:
                    lines = reader_fp.readlines()
                    for line in lines:
                        write_line = []
                        for character in line.strip("\n"):
                            write_line.append(character_code_map[character])
                        line = "".join(write_line)
                        writer_fp.write(line)
            return "done", character_code_map

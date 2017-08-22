import json
from pprint import pprint
from collections import Counter
import os

input_filename = 'meeting.txt'
output_filename1 = 'output1.txt'
output_filename2 = 'output2.txt'


class ZoomChallenge():

    def __init__(self, input_filename, output_filename1, output_filename2):
        self.input_filename = input_filename
        self.output_filename1 = output_filename1
        self.output_filename2 = output_filename2

    def read_json_file(self):
        if os.path.isfile(self.input_filename) is None:
            return "File NOT found"
        else:
            with open(self.input_filename) as json_data:
                json_dict = json.load(json_data)
                return json_dict

    def write_output1(self):

        import collections
        import json

        with open(self.input_filename) as infile:
            data = json.load(infile)

        answer = collections.defaultdict()
        for comp in data:
            answer[comp["Company"]] = comp["Company"]

            answer[comp["country"]] = comp["country"]

        answer = answer.values()
        print answer


def main():
    zoom_obj = ZoomChallenge(input_filename, output_filename1, output_filename2)
    res = zoom_obj.read_json_file()
    zoom_obj.write_output1()
    # print res


if __name__ == "__main__":
    main()

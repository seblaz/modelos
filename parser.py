class Parser:

    def __init__(self, file_path):
        self.nodes = []
        self.edges = []
        with open(file_path) as file:
            header = file.readline()
            self._process_header(header)

            for line in file:
                if line and not line.isspace():
                    self._process_line(line)

    def _process_header(self, header):
        self.nodes = [int(node) for node in header.split()]

    def _process_line(self, line):
        node, *row = line.split()
        node = int(node)
        for index, value in enumerate(row[node + 1:]):
            if value == '1':
                self.edges.append([node, index + node + 1])

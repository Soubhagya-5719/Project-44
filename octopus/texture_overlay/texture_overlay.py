mtl = "mtllib ./Dwarf_Low.obj.mtl\n"

def overlay(path):
    lines = []
    lines.append(mtl)

    with open(path, 'rt') as f:
        for index, line in enumerate(f):
            lines.append(line)
            if index == 6889:
                break

    with open('smpl_faces.txt', 'rt') as f:
        for index, line in enumerate(f):
            lines.append(line)

    with open('SMPL_texture', 'rt') as f:
        for index, line in enumerate(f):
            lines.append(line)

    with open(path, 'w') as f:
        for item in lines:
            f.write(item)

overlay('../data/sample/out/sample.obj')
overlay('../data/sample/out/sample_tposed.obj')

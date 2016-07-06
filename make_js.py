import glob

names = {
    'ear': 'earth',
    'emb': 'earthandmoon',
    'jup': 'jupiter',
    'mar': 'mars',
    'mer': 'mercury',
    'nep': 'neptune',
    'sat': 'saturn',
    'ura': 'uranus',
    'ven': 'venus',
}

for f in glob.glob("vsop87/VSOP87A.*"):
    function_name = names[f.split(".")[-1]]
    with open("%s.js" % function_name, "w") as out:
        out.write("function %s(t) {\n" % function_name)
        with open(f) as data:
            lines = data.read().strip().split('\n')[1:]
            out.write("var X0 = 0.0;\n")
            out.write("var X1 = 0.0;\n")
            out.write("var X2 = 0.0;\n")
            out.write("var X3 = 0.0;\n")
            out.write("var X4 = 0.0;\n")
            out.write("var X5 = 0.0;\n")
            out.write("var Y0 = 0.0;\n")
            out.write("var Y1 = 0.0;\n")
            out.write("var Y2 = 0.0;\n")
            out.write("var Y3 = 0.0;\n")
            out.write("var Y4 = 0.0;\n")
            out.write("var Y5 = 0.0;\n")
            out.write("var Z0 = 0.0;\n")
            out.write("var Z1 = 0.0;\n")
            out.write("var Z2 = 0.0;\n")
            out.write("var Z3 = 0.0;\n")
            out.write("var Z4 = 0.0;\n")
            out.write("var Z4 = 0.0;\n")
            out.write("var Z5 = 0.0;\n")
            for line in lines:
                if line[1] == 'V':
                    continue
                iv = int(line[1])
                ib = int(line[2])
                ic = int(line[3])
                it = int(line[4])
                n = int(line[5:10])
                a = []
                for i in xrange(10, 46, 3):
                    a.append(int(line[i:i+3]))
                S = float(line[46:61])
                K = float(line[61:79])
                A = float(line[79:97])
                B = float(line[97:111])
                C = float(line[111:131])

                out.write("%s%d+=%.11f*Math.cos(%.11f+%.11f*t);\n" % (
                    " XYZ"[ic],
                    it,
                    A,
                    B,
                    C))
            out.write("var t2 = t * t;\n")
            out.write("var t3 = t2 * t;\n")
            out.write("var t4 = t2 * t2;\n")
            out.write("var t5 = t3 * t2;\n")
            out.write("var X = X0 + X1 * t + X2 * t2 + X3 * t3 + X4 * t4 + X5 * t5;\n")
            out.write("var Y = Y0 + Y1 * t + Y2 * t2 + Y3 * t3 + Y4 * t4 + Y5 * t5;\n")
            out.write("var Z = Z0 + Z1 * t + Z2 * t2 + Z3 * t3 + Z4 * t4 + Z5 * t5;\n")
            out.write("return [X, Y, Z];\n")
            out.write("}\n")

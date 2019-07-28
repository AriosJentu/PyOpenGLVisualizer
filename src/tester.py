from os import path, remove
import sys

from visualizer_glfw import load
from comparator import compare

TESTS_FOLDER = "tests/"

def readHeader():
	with open(TESTS_FOLDER+"header.txt") as header:
		objname = header.readline().split()[0]
		return objname

def readTest(index):
	with open(TESTS_FOLDER+"test"+str(index)+".txt") as testinfo:
		line = testinfo.readline().split()
		size = tuple(map(int, line[:2]))
		campos = [tuple(map(float, line[2:5]))]
		camlook = [tuple(map(float, line[5:8]))]
		withtexture = (bool(int(line[8])), )
		floats = tuple(map(float, line[9:]))
		return size + tuple(campos) + tuple(camlook) + withtexture + floats

def executeTests(userobjdir, rmafter=True, testexec=lambda dif: print(dif)):

	testobjdir = readHeader()

	testindex = "1"
	difs = []
	while path.isfile(TESTS_FOLDER+"test"+testindex+".txt"):
		testvals = readTest(testindex)

		imgorig = "renders/imgorig"+testindex+".png"
		imguser = "renders/imguser"+testindex+".png"

		load(testobjdir, imgorig, *testvals)
		load(userobjdir, imguser, *testvals)

		dif = compare(imgorig, imguser)
		difs.append(dif)
		testexec(dif)

		if rmafter:
			remove(imgorig)
			remove(imguser)

		testindex = str(int(testindex)+1)

	return difs

def main(args):
	return executeTests(args[1], bool(int(args[2])) if len(args) > 2 else True)

if __name__ == "__main__":
	main(sys.argv)


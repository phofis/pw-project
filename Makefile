# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++17 -O3
CXXFLAGS_THREADS = -std=c++17 -pthread -O3
CXXFLAGS_OPENMP = -std=c++17 -fopenmp -DNTHREADS=16 -O3

# Time measurement
TIME = time -p

# Directories
BIN_DIR = ./bin
SRC_DIR = ./src
GEN_DIR = ./tests/gen
INPUT_DIR = ./tests/input
OUTPUT_DIR = ./tests/output

.SILENT:

# Targets
all: z5 z5single z5threaded z5openmp

# Compile gen.cpp, run it, and save output to /tests/input
gen: $(SRC_DIR)/gen.cpp
	$(CXX) $(CXXFLAGS) $(SRC_DIR)/gen.cpp -o $(BIN_DIR)/gen
	echo "Generating tests - small..."
	$(BIN_DIR)/gen < $(GEN_DIR)/small.txt > $(INPUT_DIR)/small.in
	echo "Generating tests - medium..."
	$(BIN_DIR)/gen < $(GEN_DIR)/medium.txt > $(INPUT_DIR)/medium.in
	echo "Generating tests - big..."
	$(BIN_DIR)/gen < $(GEN_DIR)/big.txt > $(INPUT_DIR)/big.in

# Compile orginal z5og.cpp, run it with tests, measure the time, and save output to /tests/output
z5: $(SRC_DIR)/z5og.cpp $(INPUT_DIR)/small.in $(INPUT_DIR)/medium.in $(INPUT_DIR)/big.in
	$(CXX) $(CXXFLAGS) $(SRC_DIR)/z5og.cpp -o $(BIN_DIR)/z5og
	echo "Running orginal z5..."
	echo "Running test - small..."
	$(TIME) $(BIN_DIR)/z5og < $(INPUT_DIR)/small.in > $(OUTPUT_DIR)/z5ogsmall.out
	echo "Running test - medium..."
	$(TIME) $(BIN_DIR)/z5og < $(INPUT_DIR)/medium.in > $(OUTPUT_DIR)/z5ogmedium.out
	echo "Running test - big..."
	$(TIME) $(BIN_DIR)/z5og < $(INPUT_DIR)/big.in > $(OUTPUT_DIR)/z5ogbig.out

# Compile optimized, single-threaded z5single.cpp, run it with tests, measure the time, and save output to /tests/output
z5single: $(SRC_DIR)/z5single.cpp $(INPUT_DIR)/small.in $(INPUT_DIR)/medium.in $(INPUT_DIR)/big.in
	$(CXX) $(CXXFLAGS) $(SRC_DIR)/z5single.cpp -o $(BIN_DIR)/z5single
	echo "Running optimized, single-threaded z5..."
	echo "Running test - small..."
	$(TIME) $(BIN_DIR)/z5single < $(INPUT_DIR)/small.in > $(OUTPUT_DIR)/z5singlesmall.out
	echo "Running test - medium..."
	$(TIME) $(BIN_DIR)/z5single < $(INPUT_DIR)/medium.in > $(OUTPUT_DIR)/z5singlemedium.out
	echo "Running test - big..."
	$(TIME) $(BIN_DIR)/z5single < $(INPUT_DIR)/big.in > $(OUTPUT_DIR)/z5singlebig.out


# Compile multi-threaded z5thread.cpp which uses C++ thread library for parallel operations
# Run it with tests, measure the time, and save output to /tests/output
# Number of threads used can be changed ath the start of z5thread.cpp
z5threaded: $(SRC_DIR)/z5thread.cpp $(INPUT_DIR)/small.in $(INPUT_DIR)/medium.in $(INPUT_DIR)/big.in
	$(CXX) $(CXXFLAGS_THREADS) $(SRC_DIR)/z5thread.cpp -o $(BIN_DIR)/z5thread
	echo "Running multi-threaded z5 with C++ Threads..."
	echo "Running test - small..."
	$(TIME) $(BIN_DIR)/z5thread < $(INPUT_DIR)/small.in > $(OUTPUT_DIR)/z5threadsmall.out
	echo "Running test - medium..."
	$(TIME) $(BIN_DIR)/z5thread < $(INPUT_DIR)/medium.in > $(OUTPUT_DIR)/z5threademedium.out
	echo "Running test - big..."
	$(TIME) $(BIN_DIR)/z5thread < $(INPUT_DIR)/big.in > $(OUTPUT_DIR)/z5threadbig.out

# Compile multi-threaded z5openmp.cpp which uses OpenMP compiler extension for parallel operations
# Run it with tests, measure the time, and save output to /tests/output
# Number of threads used can be changed in CXXFLAGS_OPENMP at the start of Makefile
z5openmp: $(SRC_DIR)/z5openmp.cpp $(INPUT_DIR)/small.in $(INPUT_DIR)/medium.in $(INPUT_DIR)/big.in
	$(CXX) $(CXXFLAGS_OPENMP) $(SRC_DIR)/z5openmp.cpp -o $(BIN_DIR)/z5openmp
	echo "Running multi-threaded z5 with OpenMP..."
	echo "Running test - small..."
	$(TIME) $(BIN_DIR)/z5openmp < $(INPUT_DIR)/small.in > $(OUTPUT_DIR)/z5openmpsmall.out
	echo "Running test - medium..."
	$(TIME) $(BIN_DIR)/z5openmp < $(INPUT_DIR)/medium.in > $(OUTPUT_DIR)/z5openmpmedium.out
	echo "Running test - big..."
	$(TIME) $(BIN_DIR)/z5openmp < $(INPUT_DIR)/big.in > $(OUTPUT_DIR)/z5openmpbig.out

# Clean up binaries and tests
clean:
	rm -rf $(BIN_DIR)/* $(OUTPUT_DIR)/* $(INPUT_DIR)/*